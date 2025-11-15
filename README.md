# 🛡 Rights & Resources Chatbot  
A privacy-focused chatbot designed to provide clear and accessible information about **gender rights**, **domestic violence laws**, and **emergency support services**.  
Built with a safety-first approach, this chatbot ensures confidentiality, accurate legal awareness (not advice), and quick access to verified helplines in India.

---

## 🚀 Features

### 🔹 Legal Awareness & Rights Information
- Explains domestic violence laws in simple everyday language  
- Helps users understand restraining orders, filing complaints, and rights under Indian law  
- *Does not give legal advice* — only provides factual, safe guidance

### 🔹 India-Specific Emergency Helplines Built-In
Instant responses for:
- **112** – All-in-one emergency  
- **1091** – National Women Helpline  
- **181** – Women Distress Helpline  
- **100** – Police  
- **1098** – Child Helpline  
- **108 / 1298** – Ambulance services  

Activated when the user asks:
> “Show India emergency helplines”

### 🔹 Safety Detection
If users express danger (“hurt me”, “kill myself”, “immediate danger”), the bot provides:
- Emergency instructions  
- Immediate helpline recommendation  
- Non-judgmental, empathetic language  

### 🔹 Beautiful Animated Frontend
- Modern UI  
- Smooth chat bubble animations  
- Typing indicator  
- Quick helpline buttons  

### 🔹 No Data Stored
- No logs  
- No personal information stored  
- Excellent for real-world safety and privacy

---

## 🧠 Tech Stack

### **Frontend**
- HTML5  
- CSS3 (advanced animations, responsive UI)  
- Vanilla JavaScript  

### **Backend**
- FastAPI (Python)  
- Requests (HTTPS API calls)  
- Pydantic  
- CORS enabled  

### **AI Model (via Groq)**
- **LLaMA 3.1 - 8B Instant**  
Fast, accurate, and ideal for conversational legal information.

---

## 📁 Project Structure

```
rights-chatbot/
│
├── backend/
│   ├── main.py
│   ├── .gitignore (contains .env)
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/akshansh-thakur/rights-chatbot.git
cd rights-chatbot
```

---

## 🛠 Backend Setup (FastAPI)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### Run Backend Server

```bash
uvicorn main:app --reload --port 8000
```

Backend will run at:  
👉 http://127.0.0.1:8000/chat

---

## 🎨 Frontend Setup

Just open:

```
frontend/index.html
```

No server required — runs instantly.

---

## 📨 API Usage

### POST `/chat`

#### Request
```json
{
  "message": "What are my rights?"
}
```

#### Response
```json
{
  "reply": "Here is a simple explanation of your rights..."
}
```

---

## 🧩 Future Enhancements

- Multi-language support (Hindi, Tamil, Marathi, Bengali)  
- WhatsApp-style UI redesign  
- Panic Exit Button  
- State-wise helpline directories  
- NGO search by city  
- Deploy frontend + backend  
- Mobile version  
- AI-powered risk level detection  

---

## 📸 Screenshots (Add yours here)

```
<img width="2560" height="1070" alt="image" src="https://github.com/user-attachments/assets/05ef53b4-5718-4c46-8ea8-6f9490c202a1" />

```

---

## 🤝 Contributing

Contributions are welcome!  
Please open an issue before major changes.

---

## 📜 License

MIT License

---

## 👨‍💻 Developed By  
**Akshansh Thakur**  
Built with ❤️ using FastAPI, Groq, HTML, CSS, and JavaScript.
