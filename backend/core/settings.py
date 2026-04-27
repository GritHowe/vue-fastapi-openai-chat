from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    OPENAI_API_KEY: str
    OPENAI_BASE_URL: str
    MODEL_NAME: str = "qwen-turbo"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()