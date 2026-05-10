from fastapi import APIRouter, Request, HTTPException
import httpx
from groq import Groq
from rag.vector_store import get_vector_store
from utils.prompts import SYSTEM_PROMPT
from config import GROQ_API_KEY, WHATSAPP_PHONE_ID, WHATSAPP_TOKEN, DEFAULT_MODEL
import json

router = APIRouter()

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

async def send_whatsapp_message(to: str, text: str):
    """
    Sends a message back to the user via WhatsApp Cloud API.
    """
    url = f"https://graph.facebook.com/v20.0/{WHATSAPP_PHONE_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    async with httpx.AsyncClient() as http_client:
        await http_client.post(url, json=payload, headers=headers)

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    """
    Main webhook to handle incoming WhatsApp messages.
    """
    data = await request.json()
    
    try:
        # Incoming message structure parsing
        entry = data.get('entry', [{}])[0].get('changes', [{}])[0].get('value', {})
        messages = entry.get('messages', [])
        
        if not messages:
            return {"status": "ok"}
            
        msg = messages[0]
        from_number = msg['from']
        text = msg['text']['body']
        
        # Determine client (In production, lookup in DB via from_number or business ID)
        client_id = "demo_restaurant"   
        
        # 1. RAG Retrieval: Get relevant context from business docs
        vector_store = get_vector_store(client_id)
        docs = vector_store.similarity_search(text, k=4)
        context = "\n".join([doc.page_content for doc in docs])
        
        # 2. LLM Generation: Call Groq with System Prompt and Context
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT.format(
                    business_name="XYZ Restaurant",
                    location="Andheri West, Mumbai",
                    timings="11 AM - 11 PM"
                )},
                {"role": "user", "content": f"Context: {context}\n\nCustomer: {text}"}
            ],
            temperature=0.7,
            max_tokens=300
        )
        
        reply = response.choices[0].message.content
        
        # 3. Response: Send back to WhatsApp
        await send_whatsapp_message(from_number, reply)
        
        return {"status": "success"}
        
    except Exception as e:
        print(f"Error in Webhook: {e}")
        return {"status": "error", "message": str(e)}
