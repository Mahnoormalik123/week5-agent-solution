# Study Buddy - LLM Agent & Retrieval (Week 5 Assignment)

## Problem Statement
Students often have long lecture notes and struggle to quickly find answers. This project builds a local Document Q&A assistant that reads your notes and answers questions. It also includes a simple calculator tool.

## Solution Architecture
- Retrieval: SentenceTransformers (all-MiniLM-L6-v2)
- Generation: HuggingFace flan-t5-base
- Tool integration: Local safe calculator
- Implemented in Colab notebook

## Setup Instructions
1. Upload notebook into Colab
2. Upload `report_ai_project.txt` file
3. Run cells top-to-bottom
4. Example queries:
   calculate("23*45")
   ask_ai("Explain gradient descent")

## Future Improvements
- Stronger models
- Web UI
- Multi-document indexing
