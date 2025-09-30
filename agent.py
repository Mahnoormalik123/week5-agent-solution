# src/agent.py
"""
Handles:
- Document loading and chunking
- Embeddings
- LLM-based query answering
- Calculator tool integration
"""

import os
import glob
import docx
from sentence_transformers import SentenceTransformer, util
import torch
from transformers import pipeline
from tools.custom_tool import calculate_expression  # custom calculator

# ---------------------------
# Document Handling
# ---------------------------
def read_file(path):
    """Read a .txt or .docx file and return text."""
    if path.lower().endswith(".docx"):
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def load_documents(data_folder="data"):
    """Load and concatenate all documents in a folder."""
    all_texts = []
    for p in glob.glob(f"{data_folder}/*"):
        all_texts.append(read_file(p))
    full_text = "\n\n".join(all_texts)
    return full_text

# ---------------------------
# Chunking
# ---------------------------
def split_into_chunks(text, chunk_size=250):
    """Split text into chunks of roughly `chunk_size` words."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

# ---------------------------
# Embeddings
# ---------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------------------
# LLM Generator
# ---------------------------
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device_map="auto" if torch.cuda.is_available() else None
)

# ---------------------------
# Core AI function
# ---------------------------
def ask_ai(query, chunks, top_k=3, max_context_len=400):
    """Answer a query using top-k similar document chunks."""
    # Embed query
    q_emb = embedder.encode(query, convert_to_tensor=True)
    chunk_emb = embedder.encode(chunks, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(q_emb, chunk_emb)[0]

    # Top-k chunks
    topk = torch.topk(scores, k=min(top_k, len(chunks)))
    indices = topk.indices.tolist()
    sims = topk.values.tolist()

    selected_chunks = []
    for i, (idx, s) in enumerate(zip(indices, sims)):
        chunk_text = chunks[idx]
        if len(chunk_text) > max_context_len:
            chunk_text = chunk_text[:max_context_len] + "..."
        selected_chunks.append(f"Source {i+1} (score={s:.3f}):\n{chunk_text}")

    context = "\n\n".join(selected_chunks)

    # Prompt for LLM
    prompt = f"""You are an assistant. Use the following CONTEXT from the documents to answer the question simply.

CONTEXT:
{context}

QUESTION:
{query}

Answer concisely (1-4 sentences). If the answer is not in the context, say "I could not find this in the documents."
"""
    out = generator(prompt, max_new_tokens=256)
    return out[0]['generated_text'].strip()

# ---------------------------
# Combined Query Processor
# ---------------------------
def process_query(query, chunks):
    """
    Decide whether to use calculator or AI to answer the query.
    """
    if any(op in query for op in ["+", "-", "*", "/", "^", "calculate", "times", "divide"]):
        try:
            # Extract simple arithmetic expression
            expr = "".join(ch for ch in query if ch.isdigit() or ch in "+-*/^.() ")
            return f"Calculator: {calculate_expression(expr)}"
        except Exception as e:
            return f"Calculator Error: {e}"
    else:
        return ask_ai(query, chunks)

# ---------------------------
# Optional: Return Answer + Sources
# ---------------------------
def ask_with_sources(query, chunks, top_k=3):
    """
    Returns AI answer along with the top-k source chunks.
    """
    # Embed query
    q_emb = embedder.encode(query, convert_to_tensor=True)
    chunk_emb = embedder.encode(chunks, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(q_emb, chunk_emb)[0]

    topk = torch.topk(scores, k=min(top_k, len(chunks)))
    indices = topk.indices.tolist()
    sims = topk.values.tolist()

    selected_chunks = [chunks[i] for i in indices]
    answer = ask_ai(query, chunks, top_k=top_k)

    sources = []
    for idx, s in zip(indices, sims):
        sources.append({
            "index": idx,
            "score": float(s),
            "text": chunks[idx][:400]  # preview first 400 chars
        })

    return {"answer": answer, "sources": sources}
