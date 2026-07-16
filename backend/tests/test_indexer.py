from enterprise_ai.ingestion.loader import DocumentLoader
from enterprise_ai.ingestion.cleaner import DocumentCleaner
from enterprise_ai.ingestion.chunker import DocumentChunker

from enterprise_ai.vectorstore.indexer import DocumentIndexer


loader = DocumentLoader()
cleaner = DocumentCleaner()
chunker = DocumentChunker()

documents = loader.load_directory("uploads")

documents = cleaner.clean_documents(documents)

chunks = chunker.chunk_documents(documents)

indexer = DocumentIndexer()

indexer.index_documents(chunks)