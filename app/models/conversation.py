from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(
        "User",
        backref="conversations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )