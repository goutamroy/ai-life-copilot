from sqlalchemy.orm import Session

from app.models.message import Message


class MemoryService:

    @staticmethod
    def get_recent_messages(
        db: Session,
        conversation_id: int,
        limit: int = 5
    ):

        messages = (
            db.query(Message)
            .filter(
                Message.conversation_id == conversation_id
            )
            .order_by(
                Message.created_at.desc()
            )
            .limit(limit)
            .all()
        )

        messages.reverse()

        history = []

        for message in messages:

            history.append(
                f"{message.role}: {message.content}"
            )

        return "\n".join(history)