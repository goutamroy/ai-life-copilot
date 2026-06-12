from typing import TypedDict
from sqlalchemy.orm import Session


class AgentState(TypedDict):
    question: str
    route: str
    context: str
    memory: str
    chunk_ids: list[int]
    answer: str
    user_id: int
    conversation_id: int | None
    db: Session