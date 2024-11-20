from fastapi import FastAPI
import uvicorn

from api import router as api_router
from core.config import settings

app = FastAPI()
app.include_router(api_router,
                   prefix=settings.api_prefix.prefix, )

if __name__ == '__main__':
    uvicorn.run("delivery-app:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)
