# src/agent.py
import os
import glob
import docx
from sentence_transformers import SentenceTransformer, util
import torch
from transformers import pipeline
import ast

# ---------- Load documents ----------
def read_file(path):
    if path.lower().endswith(".docx"):
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def load_documents(data_folder="data"):
    all_texts = []
    for p in glob.glob(f"{data_folder}/*"):
        all_texts.append(read_file(p))
    return "\n\n".join(all_texts)

# ---------- Chunking ----------
def split_into_chunks(text, chunk_size=250):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

# ---------- Embeddings ----------
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ---------- Load generator ----------
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device_map="auto" if torch.cuda.is_available() else None
)

# ---------- Core AI function ----------
def ask_ai(query, chunks, top_k=3, max_context_len=400):
    q_emb = embedder.encode(query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(q_emb, embedder.encode(chunks, convert_to_tensor=True))[0]
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

    prompt = f"""You are an assistant. Use the following CONTEXT from the documents to answer the question simply.

CONTEXT:
{context}

QUESTION:
{query}

Answer concisely (1-4 sentences). If the answer is not in the context, say "I could not find this in the documents."
"""
    out = generator(prompt, max_new_tokens=256)
    return out[0]['generated_text'].strip()

# ---------- Calculator tool ----------
def calculate_expr(expr):
    node = ast.parse(expr, mode='eval')
    def eval_node(n):
        if isinstance(n, ast.Constant):
            return n.value
        if isinstance(n, ast.BinOp):
            left = eval_node(n.left)
            right = eval_node(n.right)
            if isinstance(n.op, ast.Add): return left + right
            if isinstance(n.op, ast.Sub): return left - right
            if isinstance(n.op, ast.Mult): return left * right
            if isinstance(n.op, ast.Div): return left / right
            if isinstance(n.op, ast.Pow): return left ** right
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -eval_node(n.operand)
        raise ValueError("Unsupported expression")
    return eval_node(node.body)

def process_query(query, chunks):
    if any(op in query for op in ["+", "-", "*", "/", "^", "calculate", "times", "divide"]):
        try:
            expr = "".join(ch for ch in query if ch.isdigit() or ch in "+-*/^.() ")
            return f"Calculator: {calculate_expr(expr)}"
        except Exception as e:
            return f"Calculator Error: {e}"
    else:
        return ask_ai(query, chunks)
