# Study Buddy - LLM Agent & Retrieval (Week 5 Assignment)

## Problem Statement
Students often have long lecture notes and struggle to quickly find answers. This project builds a local Document Q&A assistant that reads your notes and answers questions. It also includes a simple calculator tool.

## Solution Architecture
- **Retrieval**: SentenceTransformers (all-MiniLM-L6-v2) to embed chunks and retrieve most relevant chunk.
- **Generation**: HuggingFace `google/flan-t5-base` or local text-generation (fallback: `gpt2`) for answer generation.
- **Tool integration**: Local safe calculator using Python `ast`.
- Implemented as a Colab notebook and packaged for GitHub.

## Setup Instructions (Colab)
1. Open Google Colab and upload `src/notebook.ipynb`.
2. Upload `data/report_ai_project.txt` using the upload cell.
3. Run cells top-to-bottom. (All required installs are in Cell 1.)
4. Example queries:
   ```python
   calculate("23*45")
   ask_ai("Explain gradient descent")
