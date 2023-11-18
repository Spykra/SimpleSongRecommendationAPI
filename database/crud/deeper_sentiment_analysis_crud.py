# DeepSentimentAnalysisCRUD.py
from sqlalchemy.ext.asyncio import AsyncSession
from database.models.deeper_sentiment_analysis_model import DeepSentimentAnalysis
from database.schemas.deeper_sentiment_analysis_schema import DeepSentimentAnalysisCreate

async def create_deep_sentiment_analysis(db: AsyncSession, create_data: DeepSentimentAnalysisCreate):
    db_obj = DeepSentimentAnalysis(
        text_id=create_data.text_id,
        **create_data.deep_sentiment_scores.dict(exclude_unset=True)
    )   
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj
