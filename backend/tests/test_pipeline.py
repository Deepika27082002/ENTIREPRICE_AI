from enterprise_ai.ingestion.pipeline import IngestionPipeline

pipeline = IngestionPipeline()

pipeline.index_file(
    "uploads/1115378eadad4b2ca06a18db20f8607f_Medical_book.pdf"
)