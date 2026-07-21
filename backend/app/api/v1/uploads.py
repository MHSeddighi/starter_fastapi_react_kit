"""File upload endpoints."""

from __future__ import annotations

from typing import List, Optional

from fastapi import APIRouter, Depends, UploadFile, File, Form
from loguru import logger

from app.models.user import User
from app.schemas.common import APIResponse
from app.services.auth import get_current_user
from app.services.file_upload import FileUploadService

router = APIRouter(prefix="/upload", tags=["File Upload"])


@router.post("", response_model=APIResponse)
async def upload_file(
    file: UploadFile = File(...),
    subdir: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
) -> APIResponse:
    """Upload a single file."""
    logger.info(f"Uploading file: {file.filename} by user {current_user.id}")
    path = await FileUploadService.save_file(file, subdir)
    return APIResponse(
        success=True,
        message="File uploaded successfully",
        data={"filename": file.filename, "path": path},
    )


@router.post("/multiple", response_model=APIResponse)
async def upload_multiple_files(
    files: List[UploadFile] = File(...),
    subdir: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
) -> APIResponse:
    """Upload multiple files."""
    logger.info(f"Uploading {len(files)} files by user {current_user.id}")
    paths = await FileUploadService.save_multiple_files(files, subdir)
    return APIResponse(
        success=True,
        message=f"{len(files)} files uploaded successfully",
        data=[{"filename": file.filename, "path": path} for file, path in zip(files, paths)],
    )
