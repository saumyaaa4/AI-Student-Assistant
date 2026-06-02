# 🤖 AI Student Assistant

An intelligent AI-powered assistant built using Python and Streamlit that helps students with queries related to Programming, AI/ML, Career Guidance, and Interview Preparation.

---

## 📌 Overview

The AI Student Assistant is designed to simulate a smart chatbot experience for students. It can answer academic and career-related questions while maintaining chat history and providing a modern interactive UI.

The system integrates AI capabilities (via API) along with a fallback mechanism to ensure uninterrupted responses even when API limits are reached.

---

## 🚀 Features

### 🧠 Core Features

* Accepts user queries in real-time
* Generates intelligent responses
* Covers:

  * 💻 Programming
  * 🤖 AI/ML
  * 🎯 Career Guidance
  * 🎤 Interview Preparation

---

### 💬 Chat Features

* ChatGPT-style interface
* Chat history persistence (session-based)
* Download chat history as JSON
* Clear chat functionality

---

### 🎨 UI Enhancements

* Modern dark-themed UI
* Chat bubbles with avatars
* Typing animation effect
* Smart suggestion buttons
* Category tagging system

---

### ⚙️ Advanced Features

* Fallback response system (works without API)
* Response feedback (👍 / 👎)
* Sidebar controls
* Message statistics dashboard

---

## 🧠 Tech Stack

* **Python** – Core programming language
* **Streamlit** – Web app framework
* **OpenAI API** – AI response generation
* **JSON** – Chat history storage

---

## 📂 Project Structure

```
student_ai_assistant/
│── app.py                # Main Streamlit application
│── assistant.py         # AI logic (API + fallback)
│── utils.py             # Chat storage functions
│── chat_history.json    # Stored conversations
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR-USERNAME/AI-Student-Assistant.git
cd AI-Student-Assistant
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```
streamlit run app.py
```

---

## 🔑 API Setup (Optional)

To enable real AI responses:

1. Get API key from OpenAI
2. Add it in `assistant.py`:

```
client = OpenAI(api_key="YOUR_API_KEY")
```

⚠️ Do NOT upload your API key to GitHub.

---

## 💡 How It Works

1. User enters a query via the UI
2. Query is sent to `assistant.py`
3. If API is available → AI generates response
4. If API fails → fallback logic handles query
5. Response is displayed with typing animation
6. Chat is stored in JSON file

---

## 🎯 Future Enhancements

* 🎤 Voice input support
* 🔐 User authentication system
* 🌐 Deployment (Streamlit Cloud)
* 📊 Analytics dashboard
* 🧠 Advanced caching system

---

## 🎥 Live Link

https://ai-student-assistant-xgggejhqswziacycxghgej.streamlit.app/
---

## 🏆 Key Highlights

* Robust design with fallback mechanism
* Clean and modern UI/UX
* Modular and scalable architecture
* Handles errors gracefully
* Designed with real-world usability in mind

---

## 👩‍💻 Author

**Saumya Bhagat**
B.Tech Student | AI/ML Enthusiast

---

## 📜 License

This project is for educational purposes.
