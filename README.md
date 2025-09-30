# AI Document Question Answering System

This project implements a simple **Question Answering (QA) system** that allows users to query their own documents and receive direct answers. It combines **document retrieval** with **language generation**.

---

## Features
- Reads user documents (e.g., `.txt`).
- Splits into manageable chunks.
- Uses embeddings + cosine similarity for retrieval.
- Generates concise answers with a text generation model.
- Provides fallback if no answer is found.

---

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/AI-Document-QA.git
cd AI-Document-QA
pip install -r requirements.txt
```

## Usage
1. Upload your document (e.g., my_notes.txt) in Colab or local environment.

2. Open and run the notebook.ipynb.

3. Ask questions like:

print(ask_ai("What is artificial intelligence?"))
print(ask_ai("Explain gradient descent."))

## Repository Structure:
AI-Document-QA/
│
├── notebook.ipynb          # Main notebook with code
├── my_notes.txt            # Sample input document
├── problem-analysis.md     # Problem statement and analysis
├── architecture.md         # System design and architecture
├── README.md               # Project documentation
└── requirements.txt        # Dependencies

## Example
- **Question:** What is artificial intelligence?
**Answer:** Artificial intelligence is the field of computer science that focuses on creating systems capable of performing tasks that typically require human intelligence.
## Limitations
- Works best with medium-sized text files.
- Model may produce generic answers if context is weak.
- Currently supports English documents.

## Future Improvements
- Multi-document support.
- Better summarization techniques.
- Integration with advanced LLMs.
