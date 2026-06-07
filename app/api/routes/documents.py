from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException
)

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.routes.users import get_current_user
from app.models.user import User
from app.models.document import Document
from app.schemas.document import (
    DocumentResponse,
    UploadResponse
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/health")
def document_health():
    return {
        "status": "documents route working"
    }


@router.post(
    "/upload",
    response_model=UploadResponse
)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files allowed"
        )

    document = Document(
        filename=file.filename,
        content_type=file.content_type,
        user_id=current_user.id
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "message": "Document uploaded successfully",
        "document": document
    }