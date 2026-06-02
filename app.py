import streamlit as st
from assistant import get_response
from utils import save_chat
import json
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Student Assistant", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
.stChatMessage {
    border-radius: 12px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🤖 AI Student Assistant")
st.caption("Your Smart Companion for Learning & Career 🚀")

# ---------------- INIT ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Controls")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    if st.session_state.messages:
        st.download_button(
            "📥 Download Chat",
            json.dumps(st.session_state.messages, indent=2),
            "chat_history.json"
        )

    st.markdown("---")
    st.subheader("📊 Stats")
    st.write(f"Total Messages: {len(st.session_state.messages)}")

# ---------------- WELCOME SCREEN ----------------
if len(st.session_state.messages) == 0:
    st.markdown("""
    ### 👋 Welcome!
    
    I can help you with:
    - 💻 Programming  
    - 🤖 AI & Machine Learning  
    - 🎯 Career Guidance  
    - 🎤 Interview Preparation  
    
    👉 Try asking something below!
    """)

# ---------------- SUGGESTIONS ----------------
st.markdown("### 💡 Quick Suggestions")
col1, col2, col3 = st.columns(3)

if col1.button("What is Machine Learning?"):
    st.session_state.auto_query = "What is machine learning?"

if col2.button("How to become Data Analyst?"):
    st.session_state.auto_query = "How to become a data analyst?"

if col3.button("Interview tips for freshers"):
    st.session_state.auto_query = "Interview tips for freshers"

# ---------------- CATEGORY BUTTONS ----------------
st.markdown("### 🎯 Categories")
c1, c2, c3, c4 = st.columns(4)

if c1.button("💻 Programming"):
    st.session_state.auto_query = "Explain Python basics"

if c2.button("🤖 AI/ML"):
    st.session_state.auto_query = "What is machine learning?"

if c3.button("🎯 Career"):
    st.session_state.auto_query = "How to become data analyst?"

if c4.button("🎤 Interview"):
    st.session_state.auto_query = "Interview tips for freshers"

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🤖" if msg["role"]=="assistant" else "🧑"):
        st.write(msg["content"])

# ---------------- CATEGORY DETECTION ----------------
def detect_category(query):
    q = query.lower()
    if "python" in q or "java" in q:
        return "💻 Programming"
    elif "machine learning" in q or "ai" in q:
        return "🤖 AI/ML"
    elif "career" in q:
        return "🎯 Career"
    elif "interview" in q:
        return "🎤 Interview"
    return "📌 General"

# ---------------- INPUT ----------------
user_input = st.chat_input("Ask me anything...")

if "auto_query" in st.session_state:
    user_input = st.session_state.auto_query
    del st.session_state.auto_query

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🧑"):
        st.write(user_input)

    # Category display
    category = detect_category(user_input)
    st.caption(f"Category: {category}")

    # Bot response with typing effect
    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        full_response = ""

        response = get_response(user_input)

        for char in response:
            full_response += char
            placeholder.markdown(full_response + "▌")
            time.sleep(0.005)

        placeholder.markdown(full_response)

    # Save chat
    save_chat(user_input, response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # ---------------- FEEDBACK ----------------
    col1, col2 = st.columns(2)
    if col1.button("👍 Helpful"):
        st.success("Glad it helped!")

    if col2.button("👎 Improve"):
        st.warning("Thanks! We'll improve.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with ❤️ by Saumya Bhagat | AI Student Assistant")