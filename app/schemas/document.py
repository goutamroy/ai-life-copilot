from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    filename: str
    content_type: str
    uploaded_at: datetime

    class Config:
        from_attributes = True


class UploadResponse(BaseModel):
    message: str
    document: DocumentResponse

class UploadDocumentResponse(BaseModel):
    message: str
    filename: str
    pages: int
    characters: int
    chunks: int