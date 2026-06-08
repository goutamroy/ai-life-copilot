from app.models.document_embedding import (
    DocumentEmbedding
)


class DocumentEmbeddingService:

    @staticmethod
    def save_embedding(
        db,
        document_chunk_id,
        embedding
    ):
        embedding_record = DocumentEmbedding(
            document_chunk_id=document_chunk_id,
            embedding=embedding
        )

        db.add(embedding_record)
        db.commit()

        return embedding_record