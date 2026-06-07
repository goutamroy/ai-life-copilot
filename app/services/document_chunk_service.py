from app.models.document_chunk import (
    DocumentChunk
)


class DocumentChunkService:

    @staticmethod
    def save_chunks(
        db,
        document_id,
        chunks
    ):
        for index, chunk in enumerate(chunks):

            document_chunk = DocumentChunk(
                document_id=document_id,
                chunk_index=index,
                chunk_text=chunk
            )

            db.add(document_chunk)

        db.commit()