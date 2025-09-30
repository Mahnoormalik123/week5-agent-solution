# src/main.py
from agent import load_documents, split_into_chunks, process_query

def main():
    print("Loading documents from data/ ...")
    full_text = load_documents("data")
    chunks = split_into_chunks(full_text, chunk_size=250)
    print(f"Loaded {len(chunks)} chunks.\n")

    while True:
        query = input("Ask your question (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = process_query(query, chunks)
        print("Answer:", answer)
        print("-" * 50)

if __name__ == "__main__":
    main()
