from pathlib import Path
from dataclasses import dataclass

@dataclass
class Document:
    """A loaded document with metadata."""
    content: str
    file_path: str
    file_name: str
    language: str
    line_count: int

EXTENSION_MAP = {
    ".py": "python",
    ".cs": "csharp",
    ".md": "markdown",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".txt": "text",
    ".js": "javascript",
    ".ts": "typescript",
    ".html": "html",
    ".css": "css",
}

def detect_language(file_path: Path) -> str:
    """Detect programming language from file extension."""
    return EXTENSION_MAP.get(file_path.suffix.lower(), "unkown")

def load_file(file_path: Path) -> Document:
    """Load a single file into a Document. Returns None if unreadable."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError) as e:
        print(f"Skipping {file_path}: {e}")
        return None
    
    if not content.strip():
        return None
    
    return Document(
        content=content,
        file_path=str(file_path),
        file_name=file_path.name,
        language=detect_language(file_path),
        line_count=content.count("\n") + 1,
    )

def load_directory(
        directory: str,
        extensions: list[str] | None = None) -> list[Document]:
    """Load all matching files from a directory."""

    if extensions is None:
        extensions = list[EXTENSION_MAP.keys()]

    root = Path(directory)
    if not root.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    documents = []
    for ext in extensions:
        for file_path in root.rglob(f"*{ext}"):
            # Skip hidden folders and common noise
            parts = file_path.parts
            if any(p.startswith(".") or p in ("node_modules", "__pycache__", ".venv", "venv") for p in parts):
                continue

            doc = load_file(file_path)
            if doc:
                documents.append(doc)

    print(f"Loaded {len(documents)} files from {directory}")
    return documents