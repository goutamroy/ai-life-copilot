from sqlalchemy import text


class VectorSearchService:

    @staticmethod
    def search(
        db,
        query_embedding,
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
            ORDER BY de.embedding <=> CAST(:embedding AS vector)
            LIMIT :limit
        """)

        result = db.execute(
            sql,
            {
                "embedding": str(query_embedding),
                "limit": limit
            }
        )

        return result.fetchall()