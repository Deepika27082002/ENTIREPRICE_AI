from enterprise_ai.vectorstore.qdrant_service import QdrantService

service = QdrantService()

count = service.client.count(
    collection_name=service.collection_name,
    exact=True,
)

print(count.count)