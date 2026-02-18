from dataclasses import dataclass
from app.rag.loader import Document

@dataclass
class Chunk:
    """A chunk of text read for embedding."""
    content:str
    file_path:str
    file_name:str
    language:str
    chunk_index:int
    start_line=int
    total_chunks:int

    def to_metadata(self) -> dict:
        """Convert to metada dic for ChromaDB."""
        return {
            "file_path": self.file_path,
            "file_name": self.file_name,
            "language": self.language,
            "chunk_index": self.chunk_index,
            "start_line": self.start_line,
            "total_chunks": self.total_chunks,
        }
    
def chunk_document(
        document: Document,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
) -> list[Chunk]:
    """Split a document into overlapping chunks by line count."""
    lines = document.content.split("\n")
    chunks = []
    start = 0
    chunk_index = 0

    while start < len(lines):
        end = min(start + chunk_size, len(lines))
        chunk_lines = lines[start:end]
        content = "\n".join(chunk_lines).strip()

        if content:
            chunks.append(Chunk(
                content=content,
                file_path=document.file_path,
                file_name=document.file_name,
                language=document.language,
                chunk_index=chunk_index,
                start_line=start + 1,
                total_chunks=0,
            ))
            chunk_index += 1
        start += chunk_size - chunk_overlap

    # Update total_chunks count
    for chunk in chunks:
        chunk.total_chunks = len(chunks)

    return chunks
    
def chunk_documents(
    documents: list[Document],
    chunk_size: int = 512,
    chunk_overlap: int = 50,
) -> list[Chunk]:
    """"Chunk multiple documents."""
    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc, chunk_size, chunk_overlap)
        all_chunks.extend(chunks)

    print(f"Created: {len(all_chunks)} chunks from {len(documents)} documents")
    return all_chunks