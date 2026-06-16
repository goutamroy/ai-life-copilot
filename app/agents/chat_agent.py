from app.agents.graph import (
    build_graph
)


class ChatAgent:

    def __init__(self):

        self.graph = build_graph()

    def run(
        self,
        db,
        user_id: int,
        conversation_id: int,
        context: str,
        message: str
    ):

        result = self.graph.invoke(
            {
                "conversation_id": conversation_id,
                "user_id": user_id,
                "db": db,
                "question": message,
                "context": context,   
                "response": "",
                "route": "",
                "memory": "",
                "chunk_ids": []
            }
        )

        return result["response"]