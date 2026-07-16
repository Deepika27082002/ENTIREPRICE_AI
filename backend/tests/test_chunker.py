from enterprise_ai.ingestion.loader import DocumentLoader
from enterprise_ai.ingestion.chunker import DocumentChunker

loader = DocumentLoader()
documents = loader.load_directory("uploads")

chunker = DocumentChunker()

chunks = chunker.chunk_documents(documents)

print("=" * 60)
print("Total Pages :", len(documents))
print("Total Chunks:", len(chunks))
print("=" * 60)

first = chunks[0]

print(first.metadata)
print()
print(first.page_content[:500])