from sqlalchemy.ext.asyncio import AsyncSession
from database import models

async def create_data_source(db: AsyncSession, source_type: str, source_data: str):
    data_source = models.DataSource(source_type=source_type, source_data=source_data)
    db.add(data_source)
    await db.commit()
    await db.refresh(data_source)
    return data_source

async def get_data_source_by_id(db: AsyncSession, data_source_id: int):
    return await db.query(models.DataSource).filter(models.DataSource.id == data_source_id).first()
