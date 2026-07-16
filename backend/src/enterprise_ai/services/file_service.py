import shutil
import uuid
from pathlib import Path

from fastapi import UploadFile

from enterprise_ai.config.settings import settings


def save_file(file: UploadFile):
    """
    Save an uploaded file to the upload directory.
    """

    # Create upload directory if it doesn't exist
    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Generate unique filename
    unique_filename = f"{uuid.uuid4().hex}_{file.filename}"

    # Full path where the file will be stored
    file_path = upload_dir / unique_filename

    # Save file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get file size
    file_size = file_path.stat().st_size

    return {
        "filename": file.filename,
        "saved_filename": unique_filename,
        "saved_path": str(file_path),
        "content_type": file.content_type,
        "size": file_size,
        "status": "uploaded",
    }