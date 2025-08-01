from typing import ClassVar, List, Union

from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings



class Settings(BaseSettings):


    # Segurança
    ALLOW_ORIGINS: List[Union[HttpUrl, str]] =Field(default=["*"])
    ALLOW_CREDENTIALS: bool =Field(default=True)
    ALLOW_METHODS: List[str] =Field(default=["*"])
    ALLOW_HEADERS: List[str] =Field(default=["*"])
    CORS_CONFIG: ClassVar[dict] = {
        "allow_origins": ALLOW_ORIGINS,
        "allow_credentials": ALLOW_CREDENTIALS,
        "allow_methods": ALLOW_METHODS,
        "allow_headers": ALLOW_HEADERS,
    }

    # Informações do Projeto
    PROJECT_NAME: str = Field(default="Desafio OP2B")
    PROJECT_VERSION: str = Field(default="1.0.0")
    DEBUG: bool = Field(default=False)


    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()