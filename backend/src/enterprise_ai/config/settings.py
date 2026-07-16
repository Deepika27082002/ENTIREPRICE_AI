from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application Settings
    app_name: str = "Enterprise AI Engineering Assistant"
    app_version: str = "0.1.0"
    app_env: str = "development"

    # Server Settings
    host: str = "127.0.0.1"
    port: int = 8000

    # Logging
    log_level: str = "INFO"

    # File Uploads
    upload_dir: str = "uploads"

    # Tell Pydantic where to load environment variables from
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    # Embedding Settings

    embedding_model: str = "BAAI/bge-small-en-v1.5"

    embedding_device: str = "mps"

    embedding_batch_size: int = 32

    normalize_embeddings: bool = True
    # Qdrant Configuration
    qdrant_path: str = "./qdrant_data"
    qdrant_collection: str = "engineering_docs"


# Create one global settings object
settings = Settings()


