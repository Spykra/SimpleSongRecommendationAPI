from fastapi import FastAPI, APIRouter, UploadFile, Depends, File, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import logging

from database import connection, crud
from database.schemas import SentimentAnalysisResponse
from database.crud.deeper_sentiment_analysis_crud import create_deep_sentiment_analysis
from database.crud.sentiment_analysis_crud import create_sentiment_analysis
from database.schemas.deeper_sentiment_analysis_schema import DeepSentimentAnalysisResponse
from processes.deeper_sentiment_processing import analyze_deep_sentiment
from processes.audio_processing import sound_to_text
from processes.sentiment_processing import analyze_sentiment

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()
router = APIRouter()

# Dependency to get the database session
async def get_db():
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        await db.close()


@router.post("/sentiment_analysis", response_model=SentimentAnalysisResponse)
async def sentiment_analysis(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    sound_data = await file.read()

    # Process the sound bytes and generate a transcription
    logger.info("Processing sound for transcription generation...")
    transcription = await sound_to_text(sound_data)

    # Perform sentiment analysis
    logger.info("Processing sentiment analysis...")
    sentiment_scores = await analyze_sentiment(transcription)

    # Create the DeepSentiment record in the database
    sentiment_data = await create_sentiment_analysis(db, transcription, sentiment_scores)

    # Construct and return the response
    response_data = {
        "id": sentiment_data.id,
        "text": sentiment_data.text,
        "sentiment_scores": sentiment_scores
    }
    return SentimentAnalysisResponse(**response_data)


@router.post("/deeper_sentiment_analysis", response_model=DeepSentimentAnalysisResponse)
async def deeper_sentiment_analysis(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    sound_data = await file.read()

    # Process the sound bytes and generate a transcription
    logger.info("Processing sound for transcription generation...")
    transcription = await sound_to_text(sound_data)

    # Perform deeper sentiment analysis
    logger.info("Processing deeper sentiment analysis...")
    deep_sentiment_scores = await analyze_deep_sentiment(transcription)

    # Create the DeepSentiment record in the database
    deep_sentiment_data = await create_deep_sentiment_analysis(db, transcription, deep_sentiment_scores)

    # Construct and return the response
    response_data = {
        "id": deep_sentiment_data.id,
        "text": deep_sentiment_data.text,
        "deep_sentiment_scores": deep_sentiment_scores
    }
    return DeepSentimentAnalysisResponse(**response_data)

# Include the router with all the endpoints
app.include_router(router)
