# Problem Analysis

## Problem Identification
Students often struggle with managing and retrieving information from large sets of lecture notes, assignments, and research materials. Searching manually consumes time and reduces productivity, especially when deadlines are close.

## Target Users
- University students preparing for exams or assignments
- Researchers who need quick fact-checking from long documents
- Professionals handling long technical documents

## Current Challenges
1. Manual searching is time-consuming and inefficient.
2. Existing solutions (like Ctrl+F) are limited and only match keywords, not context.
3. Lack of integration with productivity tools such as calculators or simple automation.
4. Students want user-friendly systems without paid APIs (like OpenAI).

## Proposed Solution
A **Document Q&A Assistant** built with LlamaIndex/HuggingFace:
- Reads uploaded `.txt` lecture notes or reports.
- Lets users ask questions in natural language.
- Retrieves the most relevant chunk of text using embeddings.
- Generates a simple, clear answer using a local HuggingFace model (no paid API).
- Provides an integrated calculator for quick math queries.

## Success Criteria
-  Accurate answers from lecture notes.
-  Safe local calculator tool for math.
-  Easy to run on Google Colab without paid APIs.
-  Structured repository with documentation and demo.
