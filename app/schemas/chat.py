from pydantic import BaseModel


class CreateConversationResponse(BaseModel):
    conversation_id: int


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


class MessageResponse(BaseModel):
    role: str
    content: str


class ConversationResponse(BaseModel):
    id: int
    title: str
    messages: list[MessageResponse]