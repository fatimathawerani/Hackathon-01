---
title: "Conversational Robotics using LLMs"
---

# Conversational Robotics using LLMs


## Integrating LLMs with Hardware
How do we turn "Pick up the red apple" into a motor command? This chapter explores the pipeline of Voice-to-Action.

## The Pipeline
1.  **ASR (Automatic Speech Recognition):** Using OpenAI Whisper to convert audio to text.
2.  **LLM Processing:** Using Llama 3 or GPT-4o to interpret intent.
    *   *Prompt Engineering:* "You are a robot assistant. Output JSON only."
3.  **Function Calling:** The LLM triggers specific Python functions (e.g., `move_arm(x,y,z)`).
4.  **TTS (Text-to-Speech):** The robot confirms the action verbally.

## Vision-Language-Action (VLA) Models
Newer models (like Google's RT-2 or various Open Source alternatives) process video frames and text simultaneously to output robot actions directly, bypassing the coding step.

## Lab Exercise
Build a "Chat-with-your-Robot" interface where natural language commands trigger ROS 2 service calls. -->
