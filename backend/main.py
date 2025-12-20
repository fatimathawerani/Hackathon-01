from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents import Agent, Runner
import os
from dotenv import load_dotenv
from typing import List, Literal
from my_config import openrouter_key, open_router_config

load_dotenv()

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
    user_profile: dict = None

class TranslateRequest(BaseModel):
    content: str

# Setup OpenRouter client - USE ONLY OPENROUTER_API_KEY


@app.post("/ask")
async def chat(request: ChatRequest):
    
    print("📥 Received messages:", request.messages)
    
    instructions = get_prompt_instructions(request.user_profile)

    agent = Agent(
        name="Physical AI & Humanoid Robotics Agent",
        instructions=instructions,
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

@app.post("/translate")
async def translate(request: TranslateRequest):
    translated_content = services.translate(request.content, "Urdu")
    return {"translated_content": translated_content}

@app.get("/")
async def health():
    return {
        "status": "healthy",
        "response": "api set" if openrouter_key else "API key missing",
        "api_key_set": bool(openrouter_key),
        "web_url": os.getenv("WEB_URL", "not set"),
    }