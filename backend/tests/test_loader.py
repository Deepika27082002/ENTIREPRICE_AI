from enterprise_ai.ingestion.loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load_directory("uploads")

print("=" * 50)
print(f"Total Documents Loaded: {len(documents)}")
print("=" * 50)

for i, doc in enumerate(documents[:5], start=1):
    print(f"\nDocument {i}")
    print("Metadata:", doc.metadata)
    print("Content Preview:")
    print(doc.page_content[:200])
    print("-" * 50)