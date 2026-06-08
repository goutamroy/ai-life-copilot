from app.services.embedding_service import (
    EmbeddingService
)

from app.services.vector_search_service import (
    VectorSearchService
)


class RetrievalService:

    @staticmethod
    def retrieve_context(
        db,
        question: str,
        limit: int = 5
    ):
        query_embedding = (
            EmbeddingService()
            .generate_embedding(question)
        )

        results = (
            VectorSearchService.search(
                db=db,
                query_embedding=query_embedding,
                limit=limit
            )
        )

        context = "\n\n".join(
            [
                row.chunk_text
                for row in results
            ]
        )

        chunk_ids = [
            row.id
            for row in results
        ]

        return {
            "context": context,
            "chunk_ids": chunk_ids
        }