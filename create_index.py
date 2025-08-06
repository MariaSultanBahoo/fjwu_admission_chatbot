from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np

# Load chunks
with open("fjwu_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save FAISS index
faiss.write_index(index, "fjwu_index.faiss")
print("✅ FAISS index saved.")
