import os

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
    UploadDocumentResponse
)

from app.services.pdf_service import PDFService
from app.services.chunking_service import ChunkingService
from app.services.document_chunk_service import (
    DocumentChunkService
)
from app.services.embedding_service import (
    EmbeddingService
)
from app.services.document_embedding_service import (
    DocumentEmbeddingService
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
    response_model=UploadDocumentResponse
)
@router.post(
    "/upload",
    response_model=UploadDocumentResponse
)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Validate PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files allowed"
        )

    try:

        # Ensure uploads directory exists
        upload_dir = "uploads"

        os.makedirs(
            upload_dir,
            exist_ok=True
        )

        # Save file locally
        upload_path = os.path.join(
            upload_dir,
            file.filename
        )

        with open(upload_path, "wb") as buffer:
            buffer.write(
                file.file.read()
            )

        # Extract text
        text = PDFService.extract_text(
            upload_path
        )

        if not text or not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from PDF"
            )

        # Count pages
        pages = PDFService.get_page_count(
            upload_path
        )

        # Create chunks
        chunks = ChunkingService.chunk_text(
            text
        )

        # Save document metadata
        document = Document(
            filename=file.filename,
            content_type=file.content_type,
            user_id=current_user.id
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        # Save chunks
        saved_chunks = (
            DocumentChunkService.save_chunks(
                db=db,
                document_id=document.id,
                chunks=chunks
            )
        )

        embedding_service = EmbeddingService()

        for chunk in saved_chunks:

            embedding = (
                embedding_service.generate_embedding(
                    chunk.chunk_text
                )
            )

            DocumentEmbeddingService.save_embedding(
                db=db,
                document_chunk_id=chunk.id,
                embedding=embedding
            )

        return {
            "message": "Document uploaded successfully",
            "filename": file.filename,
            "pages": pages,
            "characters": len(text),
            "chunks": len(chunks)
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Document upload failed: {str(e)}"
        )