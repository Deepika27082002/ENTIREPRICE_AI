from enterprise_ai.storage.hash_service import HashService
from enterprise_ai.storage.registry import DocumentRegistry

file_path = "uploads/1115378eadad4b2ca06a18db20f8607f_Medical_book.pdf"

registry = DocumentRegistry()

file_hash = HashService.calculate_hash(file_path)

print("Hash:", file_hash)

if registry.document_exists(file_hash):
    print("Document already indexed.")
else:
    print("New document.")

    registry.register_document(
        file_hash=file_hash,
        filename=file_path,
    )

    print("Document registered.")