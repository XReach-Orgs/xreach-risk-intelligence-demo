from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "XReach Risk Intelligence API"
    environment: str = "dev"
    api_prefix: str = "/api/v1"
    log_level: str = "INFO"

    postgres_user: str = "xreach"
    postgres_password: str = "xreach_dev_password"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "xreach_risk"

    model_path: str = "app/ml/artifacts/risk_model.joblib"
    model_version: str = "v1.0.0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()