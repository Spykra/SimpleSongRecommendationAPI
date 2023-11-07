from fastapi import FastAPI, APIRouter, UploadFile, Depends, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import logging

from database import connection, crud
from database.schemas import DataSourceResponse
from processes.image_processing import image_to_text


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


@router.post("/upload_image", response_model=DataSourceResponse)
async def upload_image(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    image_data = await file.read()
    logger.info("Processing image for caption generation")
    # Process the image bytes and generate a caption
    image_caption = await image_to_text(image_data)
    logger.info("Caption generated, now storing to database")

    # Store the image caption in the database instead of an image path
    return await crud.create_data_source(db=db, source_type="image", source_data=image_caption)

@router.get("/get_image/{image_id}", response_model=DataSourceResponse)
async def get_image(image_id: int, db: AsyncSession = Depends(get_db)):
    # The get_data_source function must retrieve the path/URL
    result = await crud.get_data_source(db, image_id)
    if not result:
        raise HTTPException(status_code=404, detail="Image not found")
    return result

@router.put("/update_image/{image_id}", response_model=DataSourceResponse)
async def update_image(image_id: int, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    image_data = await file.read()
    logger.info("Processing image for caption update")
    # Update the image and return the new caption
    new_caption = await image_to_text(image_data)
    return await crud.update_data_source(db, image_id, new_caption)

@router.delete("/delete_image/{image_id}", response_model=DataSourceResponse)
async def delete_image(image_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_data_source(db, image_id)

@router.get("/list_images", response_model=List[DataSourceResponse])
async def list_images(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.list_data_sources(db, skip=skip, limit=limit)

@router.get("/search_images", response_model=List[DataSourceResponse])
async def search_images(query: str, db: AsyncSession = Depends(get_db)):
    return await crud.search_data_sources(db, query)

@router.get("/health", response_model=str)
async def health_check():
    return "Healthy"

# Include the router with all the endpoints
app.include_router(router)