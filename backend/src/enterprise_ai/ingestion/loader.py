from pathlib import Path
from langchain_core.documents import Document 
from langchain_community.document_loaders import (PyPDFLoader,
Docx2txtLoader,TextLoader)

class DocumentLoader:
    """ loads all supported documents from a directory"""
    supported_extension=[".pdf",".docx",".txt"]


    def load_document(self, file_path: Path) -> list[Document]:
        sufix=file_path.suffix.lower()

        if sufix == ".pdf":
            loader=PyPDFLoader(str(file_path))
        elif sufix == ".docx":
            loader=Docx2txtLoader(str(file_path))
        elif sufix == ".txt":
            loader=TextLoader(str(file_path))
        else:
            raise ValueError(f"Unsupported file type: {sufix}")

        documents= loader.load()

        for doc in documents:
            doc.metadata["filename"]=file_path.name

        return documents

    def load_directory(self,directory:Path)->list[Document]:
        directory=Path(directory)
        all_documents=[]

        for file_path in directory.iterdir():
            if file_path.suffix .lower() not in self.supported_extension:
                continue

            print(f"Loading:{file_path.name}")

            docs=self.load_document(file_path)
            all_documents.extend(docs)

        return all_documents   





