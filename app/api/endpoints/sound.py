from fastapi import FastAPI, APIRouter, UploadFile, Depends, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import logging

from database import connection, crud
from database.schemas import DataSourceResponse
from processes.audio_processing import sound_to_text

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

@router.post("/upload_sound", response_model=DataSourceResponse)
async def upload_sound(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    sound_data = await file.read()
    logger.info("Processing sound for transcription generation")
    # Process the sound bytes and generate a transcription
    transcription = await sound_to_text(sound_data)
    logger.info(f"Transcription generated: {transcription}")
    # Store the transcription in the database
    return await crud.create_data_source(db=db, source_type="audio", source_data=transcription)

@router.get("/get_sound/{sound_id}", response_model=DataSourceResponse)
async def get_sound(sound_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_data_source(db, sound_id)
    if not result:
        raise HTTPException(status_code=404, detail="Sound not found")
    return result

@router.put("/update_sound/{sound_id}", response_model=DataSourceResponse)
async def update_sound(sound_id: int, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    sound_data = await file.read()
    logger.info("Processing sound for transcription update")
    new_transcription = await sound_to_text(sound_data)
    return await crud.update_data_source(db, sound_id, new_transcription)

@router.delete("/delete_sound/{sound_id}", response_model=DataSourceResponse)
async def delete_sound(sound_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_data_source(db, sound_id)

@router.get("/list_sounds", response_model=List[DataSourceResponse])
async def list_sounds(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.list_data_sources(db, skip=skip, limit=limit)

@router.get("/search_sounds", response_model=List[DataSourceResponse])
async def search_sounds(query: str, db: AsyncSession = Depends(get_db)):
    return await crud.search_data_sources(db, query)

@router.get("/health", response_model=str)
async def health_check():
    return "Healthy"

# Include the router with all the endpoints
app.include_router(router)
