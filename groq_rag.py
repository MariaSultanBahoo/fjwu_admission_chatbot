import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


from fee_data_dict import fee_data

index = faiss.read_index("fjwu_index.faiss")
with open("fjwu_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)
sbert = SentenceTransformer("all-MiniLM-L6-v2")


def check_fee_question(query):
    q = query.lower()

    if "hostel" in q:
        return f"""
🏠 **Hostel Fees**:
- Without Security: PKR {fee_data['hostel']['without_security']}
- With Security: PKR {fee_data['hostel']['with_security']}
- Monthly Mess Dues: PKR {fee_data['hostel']['mess_per_month']}
"""
    elif "bscs" in q and "self" in q:
        return f"""
🎓 **BSCS (Self Support)**:
- Admission Fee: PKR {fee_data['undergraduate']['BSCS']['self_support']['admission']}
- Tuition Fee: PKR {fee_data['undergraduate']['BSCS']['self_support']['tuition']}
- Total: PKR {fee_data['undergraduate']['BSCS']['self_support']['total']}
"""
    elif "bscs" in q:
        return f"""
🎓 **BSCS (Regular)**:
- Admission Fee: PKR {fee_data['undergraduate']['BSCS']['regular']['admission']}
- Tuition Fee: PKR {fee_data['undergraduate']['BSCS']['regular']['tuition']}
- Total: PKR {fee_data['undergraduate']['BSCS']['regular']['total']}
"""
    elif "mphil" in q and "science" in q:
        return f"""
📘 **M.Phil (Sciences)**:
- Admission Fee: PKR {fee_data['postgraduate']['MPhil Sciences']['admission']}
- Tuition Fee: PKR {fee_data['postgraduate']['MPhil Sciences']['tuition']}
- Total: PKR {fee_data['postgraduate']['MPhil Sciences']['total']}
"""
    elif "phd" in q:
        return f"""
📘 **PhD (Sciences)**:
- Admission Fee: PKR {fee_data['postgraduate']['PhD Sciences']['admission']}
- Tuition Fee: PKR {fee_data['postgraduate']['PhD Sciences']['tuition']}
- Total: PKR {fee_data['postgraduate']['PhD Sciences']['total']}
"""
    return None

def ask_groq(query):
    fee_response = check_fee_question(query)
    if fee_response:
        return fee_response

    query_emb = sbert.encode([query])
    D, I = index.search(np.array(query_emb), k=5)
    context = "\n\n".join([chunks[i] for i in I[0]])

    prompt = f"""
You are an assistant for Fatima Jinnah Women University. Use the info below to answer the question.

Context:
{context}

Question: {query}

Answer:
"""
    response = llm([HumanMessage(content=prompt)])
    return response.content.strip()
