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

from app.api.routes.users import (
    get_current_user
)

from app.models.user import User

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
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    result = (
        RAGService.answer_question(
            db=db,
            question=request.question,
            user_id=current_user.id,
            conversation_id=request.conversation_id
        )
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"]
    }