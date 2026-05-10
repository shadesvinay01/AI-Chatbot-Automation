# 🤖 BaatAI - WhatsApp AI Chatbot Automation

**BaatAI** is a high-performance, enterprise-ready WhatsApp chatbot automation platform. It leverages **Groq (Llama 3)** for lightning-fast AI responses and **ChromaDB** for Retrieval-Augmented Generation (RAG), allowing businesses to train the AI on their own custom data (PDFs, Menus, FAQs).

---

## ✨ Key Features
- ⚡ **Ultra-Fast Responses**: Powered by Groq Cloud for sub-second inference.
- 🧠 **Dynamic RAG**: Learns your business data instantly using Vector Embeddings.
- 📱 **WhatsApp Integration**: Built for WhatsApp Cloud API (Meta).
- 🛠️ **Admin Dashboard**: Sleek, dark-mode UI to manage clients and sync knowledge.
- 📄 **Bulk Ingestion**: Automatically process PDF and Text files into the AI's brain.
- 🇮🇳 **Hinglish Support**: Optimized for natural Indian conversational styles.

---

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python)
- **AI Model**: Llama 3.1-70B 
- **Vector Database**: ChromaDB
- **Embeddings**: HuggingFace (All-MiniLM-L6-v2)
- **Frontend**: Vanilla HTML5, CSS3 (Premium Aesthetics), JavaScript
- **Database**: SQLAlchemy + SQLite

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/shadesvinay01/AI-Chatbot-Automation.git
cd AI-Chatbot-Automation
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_key_here
WHATSAPP_TOKEN=your_whatsapp_token_here
WHATSAPP_PHONE_ID=your_phone_id_here
```

### 4. Run the Server
```bash
python main.py
```
Access the Dashboard at: `http://localhost:8000/admin`

---

## 📈 Testing
To test the AI logic without a live WhatsApp account, run the mock tester:
```bash
python scripts/test_mock_msg.py
```

## 🤝 Contributing
Feel free to fork this project and submit PRs! We are working on adding **Google Sheets** and **Stripe** integrations next.

---
*Built with ❤️ by [shadesvinay01](https://github.com/shadesvinay01)*
