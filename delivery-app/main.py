from fastapi import FastAPI
import uvicorn

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run("delivery-app:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)