from fastapi import FastAPI, APIRouter, UploadFile, Depends, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import logging

from database import connection, crud
from database.schemas import DataSourceResponse
from processes.text_processing import enhance_text


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


@router.post("/upload_text", response_model=DataSourceResponse)
async def upload_txt(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    content = await file.read()
    content_str = content.decode('utf-8')
    processed_data = enhance_text(content_str)

    return await crud.create_data_source(db=db, source_type="text", source_data=processed_data)

@router.get("/get_text/{text_id}", response_model=DataSourceResponse)
async def get_text(text_id: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_data_source(db, text_id)
    if not result:
        raise HTTPException(status_code=404, detail="Text not found")
    return result

@router.put("/update_text/{text_id}", response_model=DataSourceResponse)
async def update_text(text_id: int, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    content = await file.read()
    content_str = content.decode('utf-8')
    return await crud.update_data_source(db, text_id, content_str)

@router.delete("/delete_text/{text_id}", response_model=DataSourceResponse)
async def delete_text(text_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_data_source(db, text_id)

@router.get("/list_texts", response_model=List[DataSourceResponse])
async def list_texts(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.list_data_sources(db, skip=skip, limit=limit)

@router.get("/search_texts", response_model=List[DataSourceResponse])
async def search_texts(query: str, db: AsyncSession = Depends(get_db)):
    return await crud.search_data_sources(db, query)

@router.get("/health", response_model=str)
async def health_check():
    return "Healthy"

# Include the router with all the endpoints
app.include_router(router)