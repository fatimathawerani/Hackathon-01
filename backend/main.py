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
    try:
        print("📥 Received messages:", request.messages)

        conversation_input = "\n".join(
            [f"{msg.role}: {msg.text}" for msg in request.messages]
        )
        print("📝 Conversation input:", conversation_input)

        agent = Agent(
            name="Physical AI & Humanoid Robotics Agent",
            instructions="...",
            tools=[retrieve]
        )

        result = await Runner.run(
            agent,
            input=conversation_input,
            run_config=groq_key,
        )

        print("✅ Response generated successfully")
        return {"role": "bot", "text": result.final_output}

    except Exception as e:
        print("❌ /ask endpoint error:", e)
        return {"role": "bot", "text": "Sorry, something went wrong internally."}

    
@app.get("/")
async def health():
    return {
        "status": "healthy",
        "response": "api set" if groq_key else "API key missing",
        "api_key_set": bool(groq_key),
        "web_url": os.getenv("WEB_URL", "not configured"),
    }