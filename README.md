# AI Document Question Answering System

This project implements a simple **Question Answering (QA) system** that allows users to query their own documents and receive direct answers. It combines **document retrieval** with **language generation**.

---

## Features
- Reads user documents (e.g., `.txt`).
- Splits into manageable chunks.
- Uses embeddings + cosine similarity for retrieval.
- Generates concise answers with a text generation model.
- Provides fallback if no answer is found.
- Modular calculator tool via `custom_tool.py`.
- Supports `.txt` and `.docx` documents.

---

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/AI-Document-QA.git
cd AI-Document-QA
pip install -r requirements.txt
```

## Usage
## Usage
1. Put your documents (e.g., my_notes.txt, my_doc.docx) in the `data/` folder.
2. Run the system locally:

```bash
python src/main.py
3. Ask questions or perform calculations:

print(ask_ai("What is artificial intelligence?"))
print(ask_ai("Explain gradient descent."))

Ask your question: 23*45
Answer: Calculator: 1035

## Repository Structure
week5-agent-solution/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── main.py
│   ├── agent.py
│   └── tools/
│       └── custom_tool.py
├── data/                  # Put your documents here
├── docs/
│   ├── problem-analysis.md
│   ├── architecture.md
├── tests/
└── screenshots/


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
