from pydantic import BaseSettings, BaseModel


class PostgresSettings(BaseModel):
    host: str
    port: int
    user: str
    password: str
    db: str

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class Settings(BaseSettings):
    bot_token: str
    postgres: PostgresSettings

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


config = Settings()
