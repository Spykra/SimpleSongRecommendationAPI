from fastapi import HTTPException
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


async def read_deep_sentiment_analysis(db: AsyncSession, sentiment_id: int):
    result = await db.get(DeepSentimentAnalysis, sentiment_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Deep Sentiment Analysis record not found")


async def delete_deep_sentiment_analysis_by_id(db: AsyncSession, sentiment_id: int):
    obj = await db.get(DeepSentimentAnalysis, sentiment_id)
    if obj:
        await db.delete(obj)
        await db.commit()
        return {"message": "Record deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Deep Sentiment Analysis record not found")
