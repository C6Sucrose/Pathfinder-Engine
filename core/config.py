from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    GENAI_API_KEY: str = ""
    API_PREFIX: str = "/api"
    DATABASE_URL: str = ""
    DEBUG_MODE: bool = False
    ALLOWED_ORIGINS: str = ""
    
    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, value: str) -> List[str]:
        """Parse the allowed origins from a comma-separated string."""
        return value.split(",") if value else []
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        

settings = Settings()