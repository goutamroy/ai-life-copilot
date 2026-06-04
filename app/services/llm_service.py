from abc import ABC
from abc import abstractmethod

from openai import AzureOpenAI

from app.core.config import settings


class LLMProvider(ABC):

    @abstractmethod
    def generate_response(
        self,
        prompt: str
    ) -> str:
        pass


class MockLLMProvider(
    LLMProvider
):

    def generate_response(
        self,
        prompt: str
    ) -> str:

        return (
            "This is a mock AI response generated "
            "using conversation memory."
        )


class AzureOpenAIProvider(
    LLMProvider
):

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version="2024-02-15-preview",
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
        )

    def generate_response(
        self,
        prompt: str
    ) -> str:

        response = (
            self.client.chat.completions.create(
                model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
                messages=[
                    {
                        "role": "system",
                        "content":
                        (
                            "You are AI Life Copilot, "
                            "an intelligent personal assistant."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=300
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )


class LLMService:

    def __init__(
        self,
        provider: LLMProvider
    ):

        self.provider = provider

    def chat(
        self,
        prompt: str
    ) -> str:

        return self.provider.generate_response(
            prompt
        )