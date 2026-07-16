from enterprise_ai.storage.hash_service import HashService

file_path = "uploads/1115378eadad4b2ca06a18db20f8607f_Medical_book.pdf"

file_hash = HashService.calculate_hash(file_path)

print(file_hash)