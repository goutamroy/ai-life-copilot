from typing import TypedDict


class AgentState(TypedDict):
    conversation_id: int
    user_message: str
    context: str
    response: str