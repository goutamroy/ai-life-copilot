from langchain_openai import AzureChatOpenAI

from app.core.config import settings


class LangChainLLMService:

    @staticmethod
    def get_llm():

        return AzureChatOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            azure_deployment=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
            api_version="2024-02-01",
            temperature=0
        )