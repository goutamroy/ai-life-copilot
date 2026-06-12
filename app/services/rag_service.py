from app.agents.graph import build_graph


class RAGService:

    @staticmethod
    def answer_question(
        db,
        question: str,
        user_id: int,
        conversation_id: int
    ):

        graph = build_graph()

        result = graph.invoke(
            {
                "question": question,
                "route": "",
                "context": "",
                "memory": "",
                "chunk_ids": [],
                "answer": "",
                "user_id": user_id,
                "conversation_id": conversation_id,
                "db": db
            }
        )

        return {
            "answer": result["answer"],
            "sources": result["chunk_ids"]
        }