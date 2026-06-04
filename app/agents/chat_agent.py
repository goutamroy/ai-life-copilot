from app.agents.graph import (
    build_graph
)


class ChatAgent:

    def __init__(self):

        self.graph = build_graph()

    def run(
        self,
        conversation_id: int,
        context: str,
        message: str
    ):

        result = self.graph.invoke(
            {
                "conversation_id":
                    conversation_id,

                "user_message":
                    message,

                "context":
                    context,

                "response": ""
            }
        )

        return result["response"]