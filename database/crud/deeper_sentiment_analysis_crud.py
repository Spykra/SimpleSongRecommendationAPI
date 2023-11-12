from sqlalchemy.ext.asyncio import AsyncSession
from database.models.deeper_sentiment_analysis_model import DeepSentimentAnalysis
from database.schemas.deeper_sentiment_analysis_schema import DeepSentimentScores

async def create_deep_sentiment_analysis(db: AsyncSession, text: str, deep_sentiment_scores: DeepSentimentScores):
    db_obj = DeepSentimentAnalysis(
        text=text,
        **deep_sentiment_scores.dict()
    )
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj
