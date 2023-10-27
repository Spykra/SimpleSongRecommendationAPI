from fastapi import FastAPI
from app.api.endpoints import text, sound, image

app = FastAPI()

app.include_router(text.router, prefix="/uploadtxt", tags=["Text"])
# app.include_router(sound.router, prefix="/uploadmp3", tags=["Sound"])
# app.include_router(image.router, prefix="/uploadjpg", tags=["Image"])
