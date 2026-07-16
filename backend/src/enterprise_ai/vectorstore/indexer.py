import uuid

from qdrant_client.models import PointStruct

from enterprise_ai.embeddings.embedding_service import EmbeddingService
from enterprise_ai.vectorstore.qdrant_service import QdrantService


class DocumentIndexer:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.qdrant = QdrantService()

    def index_documents(self, chunks):

        print(f"Generating embeddings for {len(chunks)} chunks...")

        texts = [chunk.page_content for chunk in chunks]

        embeddings = self.embedding_service.embed_documents(texts)

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            points.append(

                PointStruct(

                    id=str(uuid.uuid4()),

                    vector=embedding.tolist(),

                    payload = {
                            "text": chunk.page_content,
                            "document_name": "Medical_book.pdf",
                            "document_hash": "...",
                            "page": 12,
                            "chunk_id": 45,
                        },
                )

            )

        self.qdrant.client.upsert(

            collection_name=self.qdrant.collection_name,

            points=points,

        )

        print(f"Stored {len(points)} chunks in Qdrant.")