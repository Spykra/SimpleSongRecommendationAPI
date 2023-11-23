from fastapi import FastAPI, APIRouter, UploadFile, Depends, File
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from database import connection
from database.crud.output_text_crud import create_text_record, read_text_record, delete_text_record_by_id
from database.crud.deeper_sentiment_analysis_crud import create_deep_sentiment_analysis, read_deep_sentiment_analysis
from database.crud.deeper_sentiment_analysis_crud import delete_deep_sentiment_analysis_by_id
from database.schemas.deeper_sentiment_analysis_schema import DeepSentimentAnalysisCreate, DeepSentimentScores
from processes.audio_transformation_processing import sound_to_text
from processes.deeper_sentiment_processing import analyze_deep_sentiment
from processes.output_generation import generate_text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
router = APIRouter()

async def get_db():
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        await db.close()

@router.post("/deeper_sentiment_analysis")
async def deeper_sentiment_analysis(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    sound_data = await file.read()

    logger.info("Converting sound to text...")
    transcription = await sound_to_text(sound_data)
    if not transcription:
        logger.error("Failed to transcribe sound data.")
        return {"error": "Failed to transcribe sound data."}
    logger.info("Transcription successful.")

    logger.info("Performing deep sentiment analysis...")
    sentiment_scores = await analyze_deep_sentiment(transcription)
    if not sentiment_scores:
        logger.error("Failed to perform deep sentiment analysis.")
        return {"error": "Failed to perform deep sentiment analysis."}
    logger.info("Deep sentiment analysis completed.")

    # Extracting top two emotions for the prompt
    logger.info("Extracting top two emotions from sentiment analysis...")
    top_emotions = sorted(sentiment_scores.dict().items(), key=lambda x: x[1], reverse=True)[:2]
    emotion_descriptions = [f"{emotion.replace('_', ' ').capitalize()} ({score:.2%})" for emotion, score in top_emotions]
    logger.info(f"Top two emotions identified: {emotion_descriptions}")

    # Generating new text based on the top emotions
    logger.info("Generating new text based on the top emotions...")
    emotion_text = ' and '.join(emotion_descriptions)
    sentiment_prompt = f"Based on the emotions of {emotion_text}, here are some song recommendations that encapsulate these feelings:"
    generated_texts = await generate_text(sentiment_prompt)
    if not generated_texts:
        logger.error("Failed to generate new text.")
        return {"error": "Failed to generate new text."}

    text_record = await create_text_record(db, original_text=transcription, generated_text=generated_texts[0])

    sentiment_analysis_data = DeepSentimentAnalysisCreate(
        text_id=text_record.id,
        deep_sentiment_scores=DeepSentimentScores(**sentiment_scores.dict())
    )

    sentiment_record = await create_deep_sentiment_analysis(db, sentiment_analysis_data)
    logger.info(generated_texts[0])

    return {
        "transcription": transcription,
        "sentiment_analysis": sentiment_scores.dict(),
        "generated_text": generated_texts[0]
    }


@router.get("/text_record/{text_id}")
async def get_text_record(text_id: int, db: AsyncSession = Depends(get_db)):
    return await read_text_record(db, text_id)


@router.get("/deep_sentiment/{sentiment_id}")
async def get_deep_sentiment_record(sentiment_id: int, db: AsyncSession = Depends(get_db)):
    return await read_deep_sentiment_analysis(db, sentiment_id)


@router.delete("/text_record/{text_id}")
async def delete_text_record(text_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_text_record_by_id(db, text_id)


@router.delete("/deep_sentiment/{sentiment_id}")
async def delete_deep_sentiment_record(sentiment_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_deep_sentiment_analysis_by_id(db, sentiment_id)
