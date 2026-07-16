from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from enterprise_ai.config.settings import settings
from uuid import uuid4
from qdrant_client.models import PointStruct

class QdrantService:

    def __init__(self):

        self.client = QdrantClient(
            path=settings.qdrant_path
        )

        self.collection_name = settings.qdrant_collection

        self._create_collection()

    def _create_collection(self):

        collections = self.client.get_collections().collections

        names = [c.name for c in collections]

        if self.collection_name not in names:

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE,
                ),
            )

            print(f"Created collection: {self.collection_name}")

        else:

            print(f"Collection already exists.")
    def index_documents(self, chunks, embeddings):

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            points.append(
                PointStruct(
                    id=str(uuid4()),
                    vector=embedding.tolist(),
                    payload={
                        "text": chunk.page_content,
                        "metadata": chunk.metadata,
                    },
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

        print(f"Indexed {len(points)} chunks into Qdrant.")