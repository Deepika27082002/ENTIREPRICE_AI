import re
from langchain_core.documents import Document


class DocumentCleaner:
    """
    Cleans extracted document text before chunking.
    """

    def clean_documents(self, documents: list[Document]) -> list[Document]:
        cleaned_documents = []

        for doc in documents:
            text = doc.page_content

            # Remove extra spaces
            text = re.sub(r"\s+", " ", text)

            # Remove extra blank lines
            text = re.sub(r"\n\s*\n", "\n", text)

            # Remove leading/trailing whitespace
            text = text.strip()

            cleaned_documents.append(
                Document(
                    page_content=text,
                    metadata=doc.metadata
                )
            )

        return cleaned_documents