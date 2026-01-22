# Pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    TITLE: str = Field(default="🐰 Pxxguin's GUESTBOOK", description="App main title")
    TAGS_METADATA: list = [
        {
            'name':'Auth',
            'description':'This is login & subscribe page.'
        }
    ]
    DATABASE_URL: str
    
    model_config = SettingsConfigDict(env_file='.env')

# First define
settings = Settings()