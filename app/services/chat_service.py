from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message
from app.agents.chat_agent import (
    ChatAgent
)


class ChatService:

    @staticmethod
    def create_conversation(
        db: Session,
        user_id: int
    ):

        conversation = Conversation(
            user_id=user_id,
            title="New Conversation"
        )

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    @staticmethod
    def save_user_message(
        db: Session,
        conversation_id: int,
        content: str
    ):

        message = Message(
            conversation_id=conversation_id,
            role="user",
            content=content
        )

        db.add(message)
        db.commit()

        return message
    
    @staticmethod
    def update_conversation_title(
        db: Session,
        conversation_id: int,
        title: str
    ):

        conversation = (
            db.query(Conversation)
            .filter(
                Conversation.id == conversation_id
            )
            .first()
        )

        if (
            conversation and
            conversation.title == "New Conversation"
        ):

            conversation.title = title[:50]

            db.commit()

    @staticmethod
    def save_ai_message(
        db: Session,
        conversation_id: int,
        content: str
    ):

        message = Message(
            conversation_id=conversation_id,
            role="assistant",
            content=content
        )

        db.add(message)
        db.commit()

        return message

    @staticmethod
    def generate_ai_response(
    conversation_id: int,
    context: str,
    message: str
    ):

        agent = ChatAgent()

        return agent.run(
            conversation_id=
                conversation_id,

            context=context,

            message=message
        )
    
    @staticmethod
    def get_conversation(
        db: Session,
        conversation_id: int
    ):

        return (
            db.query(Conversation)
            .filter(
                Conversation.id == conversation_id
            )
            .first()
        )
    
    @staticmethod
    def get_messages(
        db: Session,
        conversation_id: int
    ):

        return (
            db.query(Message)
            .filter(
                Message.conversation_id == conversation_id
            )
            .order_by(
                Message.created_at.asc()
            )
            .all()
        )
    

    @staticmethod
    def build_context(
        db: Session,
        conversation_id: int
    ) -> str:

        messages = (
            ChatService.get_messages(
            db,
            conversation_id
            )
        )

        context = []

        for message in messages:

            context.append(
                f"{message.role}: {message.content}"
            )

        return "\n".join(context)
    
    @staticmethod
    def get_user_conversations(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Conversation)
            .filter(
                Conversation.user_id == user_id
            )
            .all()
        )
    
    @staticmethod
    def rename_conversation(
        db: Session,
        conversation_id: int,
        user_id: int,
        title: str
    ):

        conversation = (
            db.query(Conversation)
            .filter(
                Conversation.id == conversation_id,
                Conversation.user_id == user_id
            )
            .first()
        )

        if not conversation:
            return False

        conversation.title = title

        db.commit()

        return True
    
    @staticmethod
    def delete_conversation(
        db: Session,
        conversation_id: int,
        user_id: int
    ):

        conversation = (
            db.query(Conversation)
            .filter(
                Conversation.id == conversation_id,
                Conversation.user_id == user_id
            )
            .first()
        )

        if not conversation:
            return False

        db.delete(conversation)

        db.commit()

        return True