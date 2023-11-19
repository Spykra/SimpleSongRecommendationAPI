from fastapi import FastAPI
from app.api.endpoints import sound

app = FastAPI()

app.include_router(sound.router, prefix="/api", tags=["Sound"])


