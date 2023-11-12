from sqlalchemy.ext.asyncio import AsyncSession
from database.models.sentiment_analysis_model import SentimentAnalysis
from database.schemas.sentiment_analysis_schema import SentimentScores 
import json
import numpy as np

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.float32):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

async def create_sentiment_analysis(db: AsyncSession, text: str, emotion_scores: SentimentScores):
    db_obj = SentimentAnalysis(
        text=text,
        **emotion_scores.dict()
    )
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj
