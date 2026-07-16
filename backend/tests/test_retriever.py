from enterprise_ai.vectorstore.retriever import DocumentRetriever

retriever = DocumentRetriever()

query = "Explain CAN Bus communication"

results = retriever.search(query)

print("=" * 80)
print(f"Retrieved {len(results)} Documents")
print("=" * 80)

for i, doc in enumerate(results, start=1):

    print(f"\nResult {i}")
    print(f"Score: {doc.metadata['score']:.4f}")
    print("-" * 80)

    print(doc.page_content[:700])