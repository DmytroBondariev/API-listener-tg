from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "API Listener Telegram"
    DATABASE_URL: str | None = "sqlite+aiosqlite:///./message_catalog.db"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
