from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SPECTRUM_ANALYZER_MCP_", extra="ignore")
    backend: str = "simulator"
    port: int = 11007
    webapp_port: int = 11008
    work_dir: Path = Path("./data")

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
