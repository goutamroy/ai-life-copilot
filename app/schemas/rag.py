from pydantic import BaseModel


class RAGQuestionRequest(
    BaseModel
):
    question: str
    conversation_id: int


class RAGAnswerResponse(
    BaseModel
):
    answer: str
    sources: list[int]