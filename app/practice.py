from dataclasses import dataclass

@dataclass
class CodeChunk:
    content: str
    file_path: str
    language: str
    start_line: int

    def token_estimate(self) -> int:
        """Rough estimate: 1 token ≈ 4 characters."""
        return len(self.content) // 4
    
    def __str__(self) -> str:
        return f"[{self.language}] {self.file_path}:{self.start_line} ({self.token_estimate()} tokens.)"
    
    def to_dict(self) -> dict:
        return {
            "content": self.content,
            "file_path": self.file_path,
            "language": self.language,
            "start_line": self.start_line,
            "token_estimate": self.token_estimate()
        }   

def load_chunks(file_paths: list[str]) -> list[CodeChunk]:
    chunks = []
    for path in file_paths:
        ext = path.split(".")[-1]
        language = {
            "py": "python",
            "cs": "csharp",
            "md": "markdown"
        }.get(ext, "unknown")
        chunk = CodeChunk(
            content=f"Sample content from {path}",
            file_path=path,
            language=language,
            start_line=1
        )
        chunks.append(chunk)
    return chunks



def main():
    files = ["app/main.py", "Program.cs", "README.md", "config.yaml"]
    chunks = load_chunks(files)

    # Print all chunks
    for chunk in chunks:
        print(chunk)

    # Filter only Python chunks (like LINQ Where in C#)
    python_chunks = [c for c in chunks if c.language == "python"]
    print(f"\nPython files: {len(python_chunks)}")

    # Get total token estimate (like LINQ Sum in C#)
    total_tokens = sum(c.token_estimate() for c in chunks)
    print(f"Total estimate tokens: {total_tokens}")

    # Print dictionary representation all chunks (like LINQ Select in C#)
    chunk_dicts = [chunk.to_dict() for chunk in chunks]
    print("\nChunk dictionaries:")
    for cd in chunk_dicts:
        print(cd)

if __name__ == "__main__":    
    main()