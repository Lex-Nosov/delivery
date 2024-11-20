from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/parcel"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api_prefix: ApiPrefix = ApiPrefix()


settings = Settings()
