from typing import TypedDict


class RAGState(TypedDict):
    question: str
    chat_history: str
    context: str
    chunk_ids: list[int]
    answer: str