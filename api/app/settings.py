from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PDF Form API"
    app_description: str = "API for filling PDF forms"
    app_version: str = "0.0.1"
    USERNAME: str
    PASSWORD: str


settings = Settings()
