##An APIRouter in FastAPI is a tool used to split a large web application into smaller, manageable, and organized files.

from fastapi.openapi.utils import status_code_ranges
from fastapi import APIRouter,File,HTTPException,UploadFile
from enterprise_ai.services.file_service import save_file

router = APIRouter(
    tags=["Documents"]
)

@router.post("/")
async def upload_documents(file:UploadFile=File(...)):
    """ upload a documents to a server"""
    try:
     result=save_file(file)
     return result

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


