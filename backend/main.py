from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents import Agent, Runner
from retrieval import retrieve
import os
from dotenv import load_dotenv
from typing import List, Literal
from my_config import config ,gemini_key

load_dotenv()

open_router_config = config
translate_config = config
retrieve = {}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        run_config=open_router_config,
    )

    print("✅ Response generated successfully")
    
    return {"role": "bot", "text": result.final_output}


class TranslateRequest(BaseModel):
    text: str
    target_language: str = "Urdu"  # Default to Urdu, can be extended

@app.post("/translate")
async def translate_text(
    request_data: TranslateRequest,
):
    """
    Translates the provided text to the target language using an LLM agent.
    """
    print(f"   Text (first 100 chars): {request_data.text[:100]}...")

    try:
        # Define the Agent specifically for translation
        translation_agent = Agent(
            name="Translation AI",
            instructions=f"""
            You are a specialized AI assistant for translating technical content about Physical AI and Humanoid Robotics.
            Your task is to translate the provided text to '{request_data.target_language}' language.

            ### TRANSLATION GUIDELINES:
            - **Target Language:** Translate to {request_data.target_language} (e.g., 'ur' for Urdu, 'es' for Spanish, etc.)
            - **Technical Accuracy:** Maintain all technical terms, jargon, and concepts accurately
            - **Context Preservation:** Keep the meaning, tone, and technical context intact
            - **Cultural Adaptation:** Adapt examples and references appropriately for the target language if needed
            - **Formatting:** Preserve markdown formatting, code snippets, and technical notations

            ### PROCESS:
            1. Read the provided text carefully.
            2. Translate the entire text to {request_data.target_language}.
            3. Ensure technical terms are translated appropriately or kept in English if standard.
            4. Output only the translated text, do not add conversational remarks.
            """,
        )

        messages_for_llm = [
            ChatMessage(role="user", text=f"Please translate the following text to {request_data.target_language}:\n\n{request_data.text}")
        ]

        translation_result = await Runner.run(
            translation_agent,
            input="\n".join([f"{m.role}: {m.text}" for m in messages_for_llm]),
            run_config=translate_config,
        )

        print("✅ Translation completed successfully")
        return {"translated_text": translation_result.final_output}

    except Exception as e:
        print("❌ Translation Error:", str(e))
        raise HTTPException(status_code=500, detail=f"Failed to translate text: {str(e)}")

@app.get("/")
async def health():
    return {
        "status": "healthy",
        "response": "api set" if gemini_key else "API key missing",
        "api_key_set": bool(gemini_key),
        "web_url": os.getenv("WEB_URL", "not set"),
    }