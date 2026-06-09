from app.agents.graph import build_graph


class RAGService:

    @staticmethod
    def answer_question(
        db,
        question: str,
        user_id: int
    ):

        graph = build_graph(
            db=db,
            user_id=user_id
        )

        result = graph.invoke(
            {
                "question": question,
                "context": "",
                "chunk_ids": [],
                "answer": ""
            }
        )

        return {
            "answer": result["answer"],
            "sources": result["chunk_ids"]
        }