import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")      # AiSensy / Wati / Official
WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")

BUSINESS_NAME = "BaatAI"
DEFAULT_MODEL = "llama-3.1-70b-versatile"   # High speed on Groq
