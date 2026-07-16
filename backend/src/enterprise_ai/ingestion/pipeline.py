from pathlib import Path

from enterprise_ai.ingestion.loader import DocumentLoader
from enterprise_ai.ingestion.cleaner import DocumentCleaner
from enterprise_ai.ingestion.chunker import DocumentChunker

from enterprise_ai.embeddings.embedding_service import EmbeddingService

from enterprise_ai.vectorstore.qdrant_service import QdrantService

from enterprise_ai.storage.hash_service import HashService
from enterprise_ai.storage.registry import DocumentRegistry


class IngestionPipeline:
    """
    Complete ingestion pipeline:
    Upload → Hash → Registry → Load → Clean → Chunk → Embed → Index
    """

    def __init__(self):

        self.loader = DocumentLoader()
        self.cleaner = DocumentCleaner()
        self.chunker = DocumentChunker()

        self.embedder = EmbeddingService()

        self.qdrant = QdrantService()

        self.registry = DocumentRegistry()

    def index_file(self, file_path: str):

        print("=" * 70)
        print(f"Processing: {file_path}")
        print("=" * 70)

        # Step 1 : Calculate Hash
        file_hash = HashService.calculate_hash(file_path)

        print("SHA256:", file_hash)

        # Step 2 : Check Registry
        if self.registry.document_exists(file_hash):
            print("Document already indexed.")
            return

        # Step 3 : Load Document
        documents = self.loader.load_document(file_path)

        print(f"Loaded {len(documents)} pages")

        # Step 4 : Clean
        documents = self.cleaner.clean_documents(documents)

        # Step 5 : Chunk
        chunks = self.chunker.chunk_documents(documents)

        print(f"Created {len(chunks)} chunks")

        # Step 6 : Generate Embeddings
        embeddings = self.embedder.embed_documents(chunks)

        print(f"Generated {len(embeddings)} embeddings")

        # ===================================================
        # STEP 7
        # Replace this line with YOUR qdrant method
        # ===================================================

        # self.qdrant.index_documents(chunks, embeddings)
        self.qdrant.index_documents(
            chunks,
            embeddings,
        )

        # ===================================================

        # Step 8 : Register Hash
        self.registry.register_document(
            file_hash=file_hash,
            filename=Path(file_path).name,
        )

        print("Document indexed successfully.")
        print("=" * 70)