from app.services.retrieval_service import (
    RetrievalService
)

from app.services.langchain_llm_service import (
    LangChainLLMService
)

from app.services.rag_prompt_service import (
    RAG_PROMPT
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

        llm = LangChainLLMService.get_llm()

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        response = llm.invoke(prompt)

        answer = response.content

        return {
            "answer": answer,
            "sources": chunk_ids
        }