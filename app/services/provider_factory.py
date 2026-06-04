from app.core.config import settings

from app.services.llm_service import (
    MockLLMProvider,
    AzureOpenAIProvider
)


class ProviderFactory:

    @staticmethod
    def get_provider():

        if settings.LLM_PROVIDER == "azure":

            return AzureOpenAIProvider()

        return MockLLMProvider()