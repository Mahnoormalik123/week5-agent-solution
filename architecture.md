# Technical Architecture

## Overview
The system is designed as a lightweight, retrieval-based assistant that works fully on Google Colab without requiring paid APIs. It integrates:
- Document retrieval (vector embeddings + similarity search)
- Local text generation model
- A simple calculator tool
- Clear documentation for easy reproducibility

## Components

### 1. Document Processing
- Input: `.txt` or `.docx` file uploaded by the user.
- Tool: `SentenceTransformers (all-MiniLM-L6-v2)` for embedding text.
- Step: File split into chunks → embeddings stored → vector search applied.

### 2. Retrieval System
- Uses cosine similarity to match user query with the most relevant chunk.
- Returns top-k context to feed into the language model.

### 3. Language Model
- Model: `google/flan-t5-base` from HuggingFace.
- Task: Generates concise answers using context + query.
- Runs on CPU in Colab (works offline with HuggingFace hub).

### 4. Tool Integration (Calculator)
- Built using Python `ast` for safe math evaluation.
- Example:
  - Input: `23*45`
  - Output: `1035`

### 5. User Interaction
- Functions:
  - `calculate(expression)` → math results
  - `ask_ai(query)` → answers from uploaded document
- Output shown with `print()` in Colab.

## Flow Diagram (Textual)
1. User uploads notes →  
2. Notes chunked + embedded →  
3. User asks query →  
4. Retriever finds best chunk →  
5. HuggingFace model generates answer →  
6. Answer displayed →  
7. If query is math → calculator handles.

## Error Handling
- Invalid math expression → returns `"Error: Invalid expression"`
- Missing file → shows `"Please upload a document"`
- Model loading errors → fallback to smaller model.

## Future Improvements
- Add web-based UI (Gradio/Streamlit).
- Multi-file indexing.
- Integration with APIs like web search.
