from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
    CreateConversationResponse,
    ConversationResponse,
    MessageResponse
)

from app.schemas.conversation import (
    UpdateConversationRequest
)

from app.services.chat_service import ChatService

from app.api.routes.users import (
    get_current_user
)

from app.models.user import User

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/conversations",
    response_model=CreateConversationResponse
)
def create_conversation(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    conversation = (
        ChatService.create_conversation(
            db,
            current_user.id
        )
    )

    return CreateConversationResponse(
        conversation_id=conversation.id
    )


@router.get("/conversations")
def get_conversations(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return (
        ChatService.get_user_conversations(
            db,
            current_user.id
        )
    )


@router.get(
    "/conversations/{conversation_id}",
    response_model=ConversationResponse
)
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    conversation = (
        ChatService.get_conversation(
            db,
            conversation_id
        )
    )

    if not conversation:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    messages = (
        ChatService.get_messages(
            db,
            conversation_id
        )
    )

    return ConversationResponse(
        id=conversation.id,
        title=conversation.title,
        messages=[
            MessageResponse(
                role=message.role,
                content=message.content
            )
            for message in messages
        ]
    )

@router.patch(
    "/conversations/{conversation_id}"
)
def rename_conversation(
    conversation_id: int,
    request: UpdateConversationRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    success = (
        ChatService.rename_conversation(
            db,
            conversation_id,
            current_user.id,
            request.title
        )
    )

    if not success:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return {
        "success": True
    }


@router.delete(
    "/conversations/{conversation_id}"
)
def delete_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    success = (
        ChatService.delete_conversation(
            db,
            conversation_id,
            current_user.id
        )
    )

    if not success:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return {
        "success": True
    }

@router.post(
    "/{conversation_id}",
    response_model=ChatResponse
)
def chat(
    conversation_id: int,
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    conversation = (
        ChatService.get_conversation(
            db,
            conversation_id
        )
    )

    if not conversation:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    ChatService.save_user_message(
        db,
        conversation_id,
        request.message
    )

    ChatService.update_conversation_title(
        db,
        conversation_id,
        request.message
    )

    context = (
        ChatService.build_context(
            db,
            conversation_id
        )
    )

    ai_response = (
        ChatService.generate_ai_response(
            db=db,
            user_id=current_user.id,
            conversation_id=
                conversation_id,
            context=context,
            message=request.message
        )
    )

    ChatService.save_ai_message(
        db,
        conversation_id,
        ai_response
    )

    return ChatResponse(
        response=ai_response
    )