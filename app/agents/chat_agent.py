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

        print("===== CHAT AGENT RESULT =====")
        print(result)
        print("=============================")

        if isinstance(result, dict):

            if "response" in result and result["response"]:
                return result["response"]

            if "answer" in result and result["answer"]:
                return result["answer"]

            if "error" in result:
                return f"Error: {result['error']}"

        return str(result)