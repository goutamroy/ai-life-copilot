from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from pgvector.sqlalchemy import Vector

from app.core.database import Base


class DocumentEmbedding(Base):
    __tablename__ = "document_embeddings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    document_chunk_id = Column(
        Integer,
        ForeignKey("document_chunks.id"),
        nullable=False
    )

    embedding = Column(
        Vector(1536)
    )