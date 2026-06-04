from app.models.message import Message


class MemoryService:

    @staticmethod
    def build_context(
        db,
        conversation_id: int
    ):

        messages = (
            db.query(Message)
            .filter(
                Message.conversation_id
                == conversation_id
            )
            .order_by(
                Message.created_at.asc()
            )
            .all()
        )

        context = []

        for message in messages:

            context.append(
                f"{message.role}: {message.content}"
            )

        return "\n".join(context)