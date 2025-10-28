"""
Configuration centralisée pour Torah AI
"""

from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache


class Settings(BaseSettings):
    """Configuration de l'application"""

    # Application
    app_name: str = "Torah AI - Rav Virtuel"
    app_version: str = "1.0.0"
    debug: bool = True

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_reload: bool = True

    # Base de données
    database_url: str = "postgresql://postgres:postgres@localhost:5432/torah_ai"
    db_echo: bool = False

    # IA et Modèles
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    embedding_model: str = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    llm_model: str = "gpt-4-turbo-preview"

    # Langues
    supported_languages: List[str] = ["he", "fr", "en", "es", "ru"]
    default_language: str = "fr"

    # Cache
    redis_url: str = "redis://localhost:6379/0"
    cache_ttl: int = 3600

    # Sécurité
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Rate Limiting
    rate_limit_per_minute: int = 60

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"

    # Monitoring
    enable_metrics: bool = True
    metrics_port: int = 9090

    # Sources externes
    sefaria_api_url: str = "https://www.sefaria.org/api"
    enable_sefaria_import: bool = True

    # Configuration du Rav
    rav_personality: List[str] = ["wise", "compassionate", "patient"]
    max_context_length: int = 4000
    temperature: float = 0.7
    top_k_results: int = 5

    # Éthique
    enable_content_filter: bool = True
    response_validation: bool = True

    # Multilingue
    enable_auto_translation: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """
    Retourne les settings (cached)

    Usage:
        from config import get_settings
        settings = get_settings()
        print(settings.database_url)
    """
    return Settings()


# Instance globale pour import direct
settings = get_settings()
