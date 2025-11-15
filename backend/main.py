import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import re


def strip_markdown(text):
    text = re.sub(r"\*", "", text)          # remove all *
    text = re.sub(r"[_`#~]", "", text)      # remove _, `, #, ~
    return text.strip()

# FORCE load env
load_dotenv("/home/akshansh/Projects/rights-chatbot/backend/.env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

app = FastAPI()

print("Loaded GROQ Key:", GROQ_API_KEY)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

SYSTEM_PROMPT = """
You are a Rights & Resources Chatbot.
Explain gender rights, domestic violence laws, protection laws, and support services in simple, empathetic language.
You DO NOT give legal advice.
"""

def safety_filter(text: str):
    danger = ["kill", "hurt", "danger", "violence happening", "emergency"]
    for w in danger:
        if w in text.lower():
            return {"flag": True, "response": "Sir, if this is an emergency, please call a local helpline or emergency services immediately."}
    return {"flag": False}

@app.post("/chat")
async def chat(data: ChatRequest):
    user_message = data.message.lower()
    print("User message:", user_message)

    # ==========================================
    # 1️⃣ INDIA HELPLINE TRIGGER BLOCK — SHOULD RUN FIRST
    # ==========================================
    india_triggers = [
        "india helpline", "emergency number india", "women helpline india",
        "show india helplines", "indian helpline", "helpline india",
        "show india emergency helplines"
    ]

    if any(t in user_message for t in india_triggers):
        return {
            "reply": """
🇮🇳 INDIA EMERGENCY HELPLINES

🚨 112 — All-in-One Emergency  
👮 100 — Police  
👩‍🦰 1091 — Women’s Helpline  
⚠️ 181 — Women Distress Helpline  
🧒 1098 — Child Helpline  
🚑 108 — Govt Ambulance  
🚑 1298 — Private Ambulance  
📞 1090 — Women Power Line (UP)

Sir, if anyone is in danger, please call 112 or 100 immediately.
"""
        }

    # ==========================================
    # 2️⃣ SAFETY FILTER (APPLIES ONLY IF NOT HELPLINE REQUEST)
    # ==========================================
    safe = safety_filter(user_message)
    if safe["flag"]:
        return {"reply": safe["response"]}

    # ==========================================
    # 3️⃣ GROQ MODEL CALL
    # ==========================================
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    response = requests.post(GROQ_URL, json=payload, headers=headers)
    result = response.json()

    # Extract reply
    try:
        reply_text = result["choices"][0]["message"]["content"]
    except:
        reply_text = "I couldn't process that, Sir. Please try again."
    
    return {"reply": strip_markdown(reply_text)}

