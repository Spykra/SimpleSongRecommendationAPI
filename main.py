from fastapi import FastAPI
import os
from app.api.endpoints import sound

from sqladmin import Admin
from sqlalchemy.ext.asyncio import create_async_engine
from database.models.admin_user import DeepSentimentAnalysisAdmin, TextGenerationAdmin

DATABASE_URL = os.getenv("DATABASE_URL")
async_engine = create_async_engine(DATABASE_URL)

app = FastAPI()

admin = Admin(app, async_engine)
admin.add_view(DeepSentimentAnalysisAdmin)
admin.add_view(TextGenerationAdmin)

app.include_router(sound.router, prefix="/api", tags=["Sound"])


