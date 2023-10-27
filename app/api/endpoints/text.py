from fastapi import APIRouter, UploadFile, Depends, File
from sqlalchemy.orm import Session
from database import connection, crud
from database.models import DataSource
from database.schemas import DataSourceResponse
from database.crud.data_source import create_data_source
from sqlalchemy.ext.asyncio import AsyncSession


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

    # Directly assign without processing for now. Implement processing if needed.
    processed_data = content_str

    # owner_id_placeholder = 1  # TODO: Implement authentication.
    return await create_data_source(db=db, source_type="text", source_data=processed_data)
