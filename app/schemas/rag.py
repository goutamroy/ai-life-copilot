from pydantic import BaseModel


class RAGQuestionRequest(
    BaseModel
):
    question: str


class RAGAnswerResponse(
    BaseModel
):
    answer: str
    sources: list[int]