from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    @property
    def URL(self):
        return f'postgresql+asyncpg://{self.DB_NAME}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='UTF-8',
    )

settings = Settings()