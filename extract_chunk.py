import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pickle

# Load and extract text from PDF
def extract_text(path):
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

# Split into chunks
def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50
    )
    return splitter.split_text(text)

if __name__ == "__main__":
    text = extract_text("fjwu_prospectus.pdf")
    chunks = chunk_text(text)

    # Save chunks for later
    with open("fjwu_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print(f"✅ Extracted and saved {len(chunks)} chunks.")
