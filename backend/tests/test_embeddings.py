from enterprise_ai.ingestion.loader import DocumentLoader
from enterprise_ai.ingestion.cleaner import DocumentCleaner
from enterprise_ai.ingestion.chunker import DocumentChunker

from enterprise_ai.embeddings.embedding_service import EmbeddingService

loader = DocumentLoader()
cleaner = DocumentCleaner()
chunker = DocumentChunker()

docs = loader.load_directory("uploads")

docs = cleaner.clean_documents(docs)

chunks = chunker.chunk_documents(docs)

texts = [chunk.page_content for chunk in chunks]

embedding_service = EmbeddingService()

embeddings = embedding_service.embed_documents(texts[:5])

print("Embedding Shape:", embeddings.shape)

print("First Vector Length:", len(embeddings[0]))