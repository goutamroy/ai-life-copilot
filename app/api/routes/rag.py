from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.rag import (
    RAGQuestionRequest,
    RAGAnswerResponse
)

from app.services.rag_service import (
    RAGService
)

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@router.post(
    "/ask",
    response_model=RAGAnswerResponse
)
def ask_question(
    request: RAGQuestionRequest,
    db: Session = Depends(get_db)
):
    result = (
        RAGService.answer_question(
            db=db,
            question=request.question
        )
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"]
    }