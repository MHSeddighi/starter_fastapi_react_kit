"""File upload service with local storage support."""

from __future__ import annotations

import uuid
from pathlib import Path
from typing import List, Optional

from fastapi import HTTPException, UploadFile, status
from loguru import logger

from app.core.config import settings

ALLOWED_EXTENSIONS = settings.upload_allowed_extensions
MAX_SIZE = settings.UPLOAD_MAX_SIZE
UPLOAD_DIR = settings.upload_path


class FileUploadService:
    """Service for handling file uploads."""

    @staticmethod
    def validate_file(file: UploadFile) -> None:
        """Validate file type and size."""
        # Check extension
        ext = Path(file.filename or "").suffix.lower().lstrip(".")
        if ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File type '.{ext}' is not allowed. Allowed: {', '.join(ALLOWED_EXTENSIONS)}",
            )

    @staticmethod
    async def save_file(file: UploadFile, subdir: Optional[str] = None) -> str:
        """Save an uploaded file and return the relative path."""
        FileUploadService.validate_file(file)

        # Determine upload path
        upload_path = UPLOAD_DIR
        if subdir:
            upload_path = upload_path / subdir
            upload_path.mkdir(parents=True, exist_ok=True)

        # Generate unique filename
        ext = Path(file.filename or "file").suffix
        unique_name = f"{uuid.uuid4().hex}{ext}"
        file_path = upload_path / unique_name

        # Save file
        content = await file.read()
        if len(content) > MAX_SIZE:
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail=f"File too large. Maximum size is {MAX_SIZE // (1024*1024)}MB",
            )

        file_path.write_bytes(content)
        logger.info(f"File saved: {file_path}")

        return str(file_path.relative_to(UPLOAD_DIR.parent if subdir else Path(".")))

    @staticmethod
    async def save_multiple_files(
        files: List[UploadFile], subdir: Optional[str] = None
    ) -> List[str]:
        """Save multiple uploaded files."""
        paths = []
        for file in files:
            path = await FileUploadService.save_file(file, subdir)
            paths.append(path)
        return paths

    @staticmethod
    def delete_file(relative_path: str) -> bool:
        """Delete a file by its relative path."""
        file_path = UPLOAD_DIR.parent / relative_path
        if file_path.exists() and file_path.is_file():
            file_path.unlink()
            logger.info(f"File deleted: {file_path}")
            return True
        return False
