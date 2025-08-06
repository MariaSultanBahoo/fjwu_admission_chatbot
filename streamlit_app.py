import streamlit as st
import base64
from groq_rag import ask_groq

st.set_page_config(page_title="FJWU Chatbot", page_icon="🎓", layout="centered")

def set_bg_image(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_bg_image("fjwu_img.jpg")

st.markdown("""
<style>
    .main {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1rem;
        border-radius: 10px;
        max-width: 800px;
        margin: auto;
    }

    .message-user {
        background-color: #e6f0ff;
        color: #000;
        padding: 12px 18px;
        border-radius: 15px;
        margin: 10px 0;
        max-width: 80%;
        font-size: 1.1rem;
        align-self: flex-end;
    }

    .message-bot {
        background-color: #f0fff0;
        color: #111;
        padding: 12px 18px;
        border-radius: 15px;
        margin: 10px 0;
        max-width: 80%;
        font-size: 1.1rem;
        align-self: flex-start;
    }

    h2 {
        color: #ffffff;
        font-weight: 700;
        text-align: center;
        background-color: #228B22;
        padding: 10px;
        border-radius: 5px;
    }

    .stTextInput > div > input {
        background-color: #ffffff !important;
        border: 1px solid #006400 !important;
        color: #111 !important;
    }

    button[kind="primary"], .stButton > button {
    background-color: #228B22 !important;
    color: white !important;
    border: none !important;
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: bold;
    font-size: 0.9rem;
}

/* Optional: Hover effect */
button[kind="primary"]:hover, .stButton > button:hover {
    background-color: #1c6b1c !important;
}

    input[type="text"] {
    border: 2px solid #228B22 !important;
    background-color: #ffffff !important;
    color: #111 !important;
    border-radius: 8px;
    padding: 10px;
    font-size: 1rem;
    }
   

    .suggestion-container {
        background-color: #ffffffcc;
        padding: 10px;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("<h2>🎓 Welcome to FJWU Chatbot</h2>", unsafe_allow_html=True)
st.markdown('<strong>Ask me anything about <em>admissions, programs, fees, hostel, eligibility</em>, and more.</strong>', unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown('<div class="suggestion-container"><strong style="color:#228B22;"> Suggestions:</strong></div>', unsafe_allow_html=True)
suggestions = {
    "🎓\nBSCS Fee": "What is the BSCS fee?",
    "🏠 \nHostel": "What are hostel charges?",
    "🏛️ Departments": "List all departments",
    "📘\nMPhil": "What MPhil programs are offered?",
    "📅 Admissions": "When will admissions open?"
}
cols = st.columns(len(suggestions))
for i, (label, query_text) in enumerate(suggestions.items()):
    if cols[i].button(label):
        st.session_state.chat_history.append(("user", query_text))
        with st.spinner("Thinking..."):
            answer = ask_groq(query_text)
            st.session_state.chat_history.append(("bot", answer))
        st.rerun()


with st.form("chat_form", clear_on_submit=True):
    st.markdown('<label for="inputbox" style="font-weight:bold; font-style:italic;">Ask your question</label>', unsafe_allow_html=True)
    query = st.text_input(" ", key="inputbox")  
    submit = st.form_submit_button("Send")

if submit and query.strip():
    with st.spinner("Thinking..."):
        answer = ask_groq(query)
        st.session_state.chat_history.append(("user", query))
        st.session_state.chat_history.append(("bot", answer))
    st.rerun()

chat_box = st.container()
with chat_box:
    for sender, message in st.session_state.chat_history:
        css_class = "message-user" if sender == "user" else "message-bot"
        st.markdown(f'<div class="{css_class}">{message}</div>', unsafe_allow_html=True)

st.markdown("---")
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
