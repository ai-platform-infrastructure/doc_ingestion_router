from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import urlparse, urlunparse
from loguru import logger


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    APP_NAME: str = "Document Ingestion Router"

    API_KEY: str

    TIKA_BASE_URL: str
    TIKA_USER: str
    TIKA_PASSWORD: str

    # HTTP Client connection pool settings
    HTTP_MAX_CONNECTIONS: int = 100
    HTTP_MAX_KEEPALIVE_CONNECTIONS: int = 20
    HTTP_KEEPALIVE_EXPIRY: float = 30.0
    HTTP_ENABLE_HTTP2: bool = True

    # HTTP Client timeout settings (in seconds)
    HTTP_TIMEOUT_CONNECT: float = 10.0
    HTTP_TIMEOUT_READ: float = 600.0
    HTTP_TIMEOUT_WRITE: float = 60.0
    HTTP_TIMEOUT_POOL: float = 10.0

    @property
    def tika_url_with_auth(self) -> str:
        """Constructs Tika URL with authentication credentials"""
        parsed = urlparse(self.TIKA_BASE_URL)
        netloc = f"{self.TIKA_USER}:{self.TIKA_PASSWORD}@{parsed.netloc}"
        return urlunparse(
            (
                parsed.scheme,
                netloc,
                parsed.path,
                parsed.params,
                parsed.query,
                parsed.fragment,
            )
        )


settings = Settings()
logger.info(
    f"Loaded settings: {settings.model_dump(exclude=['API_KEY', 'TIKA_PASSWORD'])}"
)
