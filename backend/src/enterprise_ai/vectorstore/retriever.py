from langchain_core.documents import Document

from enterprise_ai.embeddings.embedding_service import EmbeddingService
from enterprise_ai.vectorstore.qdrant_service import QdrantService


class DocumentRetriever:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant = QdrantService()

    def search(self, query: str, top_k: int = 5):

        # Generate query embedding
        query_vector = self.embedding_service.embed_query(query)

        # Query Qdrant
        response = self.qdrant.client.query_points(
            collection_name=self.qdrant.collection_name,
            query=query_vector.tolist(),
            limit=top_k,
        )

        documents = []

        for point in response.points:

            payload = point.payload

            metadata = payload.get("metadata", {})
            metadata["score"] = point.score

            documents.append(
                Document(
                    page_content=payload["text"],
                    metadata=metadata,
                )
            )

        return documents