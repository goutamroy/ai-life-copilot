from sqlalchemy import text


class VectorSearchService:

    @staticmethod
    def search(
        db,
        query_embedding,
        user_id,
        limit=5
    ):
        sql = text("""
            SELECT
                dc.id,
                dc.chunk_text,
                de.embedding <=> CAST(:embedding AS vector) AS distance
            FROM document_embeddings de
            JOIN document_chunks dc
                ON de.document_chunk_id = dc.id
            JOIN documents d
                ON dc.document_id = d.id
            WHERE d.user_id = :user_id
            ORDER BY de.embedding <=> CAST(:embedding AS vector)
            LIMIT :limit
        """)

        result = db.execute(
            sql,
            {
                "embedding": str(query_embedding),
                "user_id": user_id,
                "limit": limit
            }
        )

        return result.fetchall()