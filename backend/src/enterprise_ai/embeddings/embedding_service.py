from sentence_transformers import SentenceTransformer
from enterprise_ai.config.settings import settings


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            settings.embedding_model,
            device=settings.embedding_device,
        )

    def embed_documents(self, texts: list[str]):

        embeddings = self.model.encode(
            texts,
            batch_size=settings.embedding_batch_size,
            normalize_embeddings=settings.normalize_embeddings,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        return embeddings

    def embed_query(self, query: str):

        embedding = self.model.encode(
            query,
            normalize_embeddings=settings.normalize_embeddings,
            convert_to_numpy=True,
        )

        return embedding