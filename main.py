from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from webhooks.whatsapp import router as whatsapp_router
import uvicorn
import os

app = FastAPI(title="BaatAI - WhatsApp AI Chatbot")

# Setup Templates
templates = Jinja2Templates(directory="templates")

# Include WhatsApp Webhook Router
app.include_router(whatsapp_router, prefix="/api")

@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.get("/")
def home():
    return {
        "message": "BaatAI is running 🔥",
        "status": "active",
        "version": "1.0",
        "author": "Antigravity AI"
    }

if __name__ == "__main__":
    # Start server
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
