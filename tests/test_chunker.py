from app.rag.loader import load_directory
from app.rag.chunker import chunk_documents

def main():
    docs = load_directory(".")
    chunks = chunk_documents(docs, chunk_size=30, chunk_overlap=5)

    print(f"\nTotal chunks: {len(chunks)}")

    print(f"\nFirst 5 chunks:")
    for chunk in chunks[:5]:
        print(f"  [{chunk.language}] {chunk.file_name} "
              f"(chunk {chunk.chunk_index + 1}/{chunk.total_chunks}, "
              f"line {chunk.start_line})")
        print(f"    {chunk.content[:100]}...")
        print()

if __name__ == "__main__":
    main();