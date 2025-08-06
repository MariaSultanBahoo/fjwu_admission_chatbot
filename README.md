# 🎓 FJWU Admission Chatbot

An intelligent chatbot built for **Fatima Jinnah Women University (FJWU)** that provides instant answers about admissions, departments, programs, fee structures, hostels, and more — all based on the official university prospectus.

---

## 🚀 Features

- 💬 **Chat-based UI** built with Streamlit
- 📄 Uses official **FJWU Prospectus (2025–2026)** as the knowledge base
- ⚡ Powered by **Groq's LLaMA3-8B** via Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using **FAISS** and **Sentence Transformers**
- 🎨 Clean UI with:
  - Welcome message
  - Suggested question buttons
  - Background image of the university
  - Auto-updating chat history

---

## 🧠 Tech Stack

- **LLM:** Groq (LLaMA3-8B)
- **Framework:** Streamlit
- **RAG Stack:**
  - FAISS (vector similarity)
  - SentenceTransformers (MiniLM)
- **Data Source:** FJWU Prospectus PDF (2025–2026)
- **Styling:** Custom CSS + Background image

---

## 📦 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/fjwu_admission_chatbot.git
   cd fjwu_admission_chatbot
   
2.Install dependencies:
pip install -r requirements.txt

3.Add your Groq API key:
Set it as an environment variable OPENAI_API_KEY
Or directly edit the key in ask_groq.py

4.Prepare FAISS index:
Make sure you have fjwu_index.faiss and fjwu_chunks.pkl (already generated)

5.Run the chatbot:
streamlit run streamlit_app.py

🖼️ Preview
📚 Data Source
This chatbot is based on the FJWU Prospectus (2025–2026) and answers are generated using RAG from its content.

🙋‍♀️ Developed By
Maria Sultan – Software Engineering student with interests in AI, LLMs, and educational automation tools.

📝 License
MIT License. You are free to use and adapt with credit.
