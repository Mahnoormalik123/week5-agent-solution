# System Architecture

The system is designed in **modular steps** so that each component handles a specific function in the Question Answering pipeline.

## Components

1. **Data Ingestion**
   - Reads text from `my_notes.txt` or other documents.
   - Splits into chunks (e.g., 200–300 words each) for efficient retrieval.

2. **Text Embedding**
   - Uses `sentence-transformers` to convert each chunk into vector embeddings.
   - Also encodes the user query into a vector representation.

3. **Similarity Search**
   - Computes cosine similarity between query embedding and document embeddings.
   - Selects the top-k most relevant chunks.

4. **Answer Generation**
   - Uses a pre-trained text generation model (`transformers` pipeline) to process the retrieved context.
   - Combines the relevant chunks with the user query into a prompt.
   - Produces a short, focused answer.

5. **Fallback Handling**
   - If no relevant context is found, the system replies:
     > "I could not find this in the documents."

## Data Flow Diagram

User Query
↓
Embedding Model (query vector)
↓
Cosine Similarity with document vectors
↓
Top-k Relevant Chunks
↓
Language Model (Generator)
↓
Final Answer

## Technology Stack
- **Python** (Google Colab environment)
- **Libraries:**
  - `sentence-transformers`
  - `transformers`
  - `torch`
  - `docx` (for document reading)
  - `faiss` (optional for fast vector search)

---

The architecture ensures modularity, so each block (data, embeddings, search, generation) can be improved or replaced independently.
