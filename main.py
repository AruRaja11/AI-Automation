from fastapi import FastAPI
from api.routes.health import router as health_router
from api.routes.chat import router as chat_router
import os 


app = FastAPI()

app.include_router(
    health_router
)

app.include_router(
    chat_router
)


