from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str

    DATABASE_URL: str

    OPENAI_API_KEY: str = ""

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    LLM_PROVIDER: str = "mock"

    AZURE_OPENAI_ENDPOINT: str = ""

    AZURE_OPENAI_API_KEY: str = ""

    AZURE_OPENAI_DEPLOYMENT_NAME: str = ""

    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str = ""

    # AWS Bedrock
    AWS_REGION: str | None = None
    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None
    BEDROCK_MODEL_ID: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()