from app.rag.loader import load_directory

def main():
    # Load your own project as a test
    docs = load_directory(".")

    print(f"\nTotal documents: {len(docs)}")
    print(f"\nBy language: ")

    # Group by language
    languages = {}
    for doc in docs:
        languages[doc.language] = languages.get(doc.language, 0) + 1
    for lang, count in sorted(languages.items()):
        print(f"    {lang}: {count}")

    print(f"\nFirst 3 documents:")
    for doc in docs[:3]:
        print(f"    {doc.file_name} ({doc.language}, {doc.line_count} lines)")
        print(f"    > Preview: {doc.content[:80]} ...")
        print()

if __name__ == "__main__":
    main();