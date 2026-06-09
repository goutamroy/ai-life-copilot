from typing import TypedDict


class RAGState(TypedDict):
    question: str
    context: str
    chunk_ids: list[int]
    answer: str