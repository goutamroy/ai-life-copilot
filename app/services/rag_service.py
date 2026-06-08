from app.services.retrieval_service import (
    RetrievalService
)

from app.services.llm_service import (
    AzureOpenAIProvider
)


class RAGService:

    @staticmethod
    def answer_question(
        db,
        question: str,
        user_id: int
    ):
        retrieval_result = (
            RetrievalService.retrieve_context(
                db=db,
                question=question,
                user_id=user_id
            )
        )

        context = retrieval_result["context"]

        chunk_ids = retrieval_result["chunk_ids"]

        prompt = f"""
You are a Retrieval-Augmented Generation assistant.

Rules:
1. Use only the supplied context.
2. If the answer is not present in the context, respond:
   "I could not find that information in the uploaded documents."
3. Do not invent facts.
4. Be concise and accurate.

Context:
{context}

Question:
{question}

Answer using only the context above.
"""

        llm = AzureOpenAIProvider()

        answer = llm.generate_response(
            prompt
        )

        return {
            "answer": answer,
            "sources": chunk_ids
        }