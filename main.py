from fastapi import FastAPI
from app.api.endpoints import text, sound, image, user

app = FastAPI()

app.include_router(text.router, prefix="/api", tags=["Text"])
app.include_router(sound.router, prefix="/api", tags=["Sound"])
app.include_router(image.router, prefix="/api", tags=["Image"])
app.include_router(user.router, prefix="/api", tags=["User"])


