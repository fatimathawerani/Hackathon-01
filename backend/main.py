from contextlib import asynccontextmanager
from sqlmodel import select
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from agents import Agent, Runner
from retrieval import retrieve
import os
from dotenv import load_dotenv
from typing import List, Literal
from sqlalchemy.ext.asyncio.session import AsyncSession 
from my_config import open_router_config, gemini_key, groq_key

# --- AUTH & DB IMPORTS ---
from auth.models import User # Assuming User model has software_experience and hardware_experience
from auth.schemas import UserCreate, UserRead, Token
from auth.db import init_db, get_session
from auth.auth import (
    get_password_hash, 
    verify_password, 
    create_access_token, 
    create_refresh_token, 
    get_current_user,
    decode_token
)


# --- STARTUP EVENT ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

load_dotenv()

# --- CORS SETUP ---
# Combine your WEB_URL with localhost for flexibility
origins = ["*"]  # Allow all origins (for testing only)



print("🌐 CORS allowed origins:", origins)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# ==========================================
# AUTHENTICATION ENDPOINTS
# ==========================================

@app.post("/register", response_model=UserRead)
async def register(user: UserCreate, session: AsyncSession = Depends(get_session)):
    statement = select(User).where(User.email == user.email)
    result = await session.exec(statement)
    existing_user = result.first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pwd = get_password_hash(user.password)
    
    new_user = User(
        email=user.email, 
        name=user.name,
        software_experience=user.software_experience,
        hardware_experience=user.hardware_experience,
        hashed_password=hashed_pwd
    )
    
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    """
    Login to get Access Token and Refresh Token.
    """
    statement = select(User).where(User.email == form_data.username)
    result = await session.exec(statement)
    user = result.first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})
    
    return {
        "access_token": access_token, 
        "refresh_token": refresh_token, 
        "token_type": "bearer"
    }

@app.post("/refresh", response_model=Token)
async def refresh_token(token_data: dict, session: AsyncSession = Depends(get_session)):
    """
    Use a long-lived refresh token to get a new access token.
    """
    refresh_token_str = token_data.get("refresh_token")
    if not refresh_token_str:
        raise HTTPException(status_code=400, detail="Refresh token missing")

    payload = decode_token(refresh_token_str)
    
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    email = payload.get("sub")
    statement = select(User).where(User.email == email)
    result = await session.exec(statement)
    user = result.first()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
        
    return {
        "access_token": create_access_token(data={"sub": user.email}),
        "refresh_token": create_refresh_token(data={"sub": user.email}),
        "token_type": "bearer"
    }

@app.get("/users/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Get current logged-in user profile (includes Name, Software/Hardware Experience).
    """
    return current_user

# ==========================================
# USER PREFERENCE ENDPOINTS
# ==========================================

# NOTE: The UserRead model already contains software_experience and hardware_experience.
# So, GET /preference can just return the UserRead model.

@app.get("/preference", response_model=UserRead)
async def get_user_preference(current_user: User = Depends(get_current_user)):
    """
    Retrieves the current logged-in user's profile, which includes preference-like fields
    such as software_experience and hardware_experience.
    """
    return current_user

# If you wanted to allow users to update these fields *specifically* through a preference endpoint,
# you'd need a separate Pydantic model for update and a PUT/PATCH endpoint.
# For now, fetching the UserRead via /preference is sufficient as per the current flow.


class ChatMessage(BaseModel):
    role: Literal["user", "bot"]
    text: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]


@app.post("/ask")
async def chat(request: ChatRequest):
    
    print("📥 Received messages:", request.messages)
    
    agent = Agent(
        name="Physical AI & Humanoid Robotics Agent",
        instructions= """
You are the **Specialized AI Assistant** for the **Physical AI & Humanoid Robotics Capstone Course**.
Your primary function is to support students in understanding the curriculum, hardware prerequisites, system architectures, and foundational principles that connect a digital AI "brain" to a physical robotic body.

---

## **COURSE CONTEXT**

**Domain:** Embodied AI — the integration of machine intelligence with robots operating in simulated and real physical environments.
**Objective:** Guide students as they apply AI techniques to humanoid and quadruped robots using **ROS 2**, **Gazebo**, **Unity**, and **NVIDIA Isaac**.

---

## **CURRICULUM OVERVIEW**

### **1. The Robotic Nervous System (ROS 2)**
* Node graph architecture
* Topics, services, actions
* `rclpy` development
* URDF modeling and kinematics

### **2. The Digital Twin (Simulation Layer)**
* **Gazebo** physics-based simulation
* **Unity** for high-level visualization
* Collision dynamics, LiDAR, depth camera modeling

### **3. The AI–Robot Brain (NVIDIA Isaac)**
* Isaac Sim for photorealistic simulation
* Isaac ROS for perception (e.g., VSLAM)
* Nav2 for mapping, navigation, motion planning

### **4. Vision–Language–Action (VLA) Systems**
* Whisper for speech-to-text
* LLMs for goal decomposition
* Mapping natural-language commands to ROS 2 action graphs
* Example: "Clean the room" → perception → navigation → manipulation sequence

---

## **HARDWARE REQUIREMENTS (CRITICAL)**

### **Simulation Workstation**
* **GPU:** NVIDIA RTX 4070 Ti (12GB VRAM) minimum (Recommended: RTX 3090/4090)
* **CPU:** Intel i7 (13th Gen+) or equivalent
* **RAM:** 64GB DDR5
* **OS:** Ubuntu 22.04 LTS

### **Edge AI Deployment**
* NVIDIA Jetson Orin Nano (8GB) or Orin NX

### **Sensors**
* Intel RealSense D435i
* USB IMU (generic)
* ReSpeaker Microphone Array

### **Robotics Platforms**
* Unitree Go2 Edu (quadruped proxy)
* Unitree G1 (humanoid)
* Hiwonder TonyPi Pro (budget option for kinematics labs)

---

## **LAB SETUP OPTIONS**

### **On-Prem (High CapEx)**
Hardware-owned physical labs using local workstations and robots.

### **Cloud / Ether Lab (High OpEx)**
* AWS g5.2xlarge GPU instances (~$205/quarter)
* Jetson kit for local robotic deployment (~$700)

---

## **ANSWERING RULES**

### **1. Mandatory Tool Use**
Before answering **any question** related to:
* Humanoid robotics
* Physical AI
* ROS 2
* Isaac
* Sensors
* Simulation

You **must call the `retrieve_data` tool** to access relevant information from the course knowledge base.
Only respond after retrieving and summarizing the data.

### **2. Tone & Style**
* Technical, academic, and helpful
* Use Markdown formatting
* Highlight important terms in **bold**

### **3. Scope**
* Stick strictly to course material + retrieved knowledge base
* Avoid unsupported speculation
* Produce accurate, concise explanations

### **4. Refusals**
Politely decline unrelated questions (e.g., weather, humor, politics).

### **5. Hardware-Specific Answers**
* Always include precise specs (VRAM, OS version, CPU class)
* Identify performance bottlenecks where relevant

---

You operate strictly under these constraints and respond consistently according to them.
        """,
        tools = [retrieve]
    )

    print("⚙️ Running agent (Non-Streamed)...")
    

    conversation_input = "\n".join(
        [f"{msg.role}: {msg.text}" for msg in request.messages]
    )

    result = await Runner.run(
        agent,
        input=conversation_input,
        run_config=groq_key,
    )

    print("✅ Response generated successfully")
    
    return {"role": "bot", "text": result.final_output}

    
@app.get("/")
async def health():
    return {
        "status": "healthy",
        "response": "api set" if groq_key else "API key missing",
        "api_key_set": bool(groq_key),
        "web_url": os.getenv("WEB_URL", "not configured"),
    }