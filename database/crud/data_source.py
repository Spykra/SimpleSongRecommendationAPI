from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import models
from sqlalchemy import or_

async def create_data_source(db: AsyncSession, source_type: str, source_data: str):
    data_source = models.DataSource(source_type=source_type, source_data=source_data)
    db.add(data_source)
    await db.commit()
    await db.refresh(data_source)
    return data_source

async def get_data_source(db: AsyncSession, data_source_id: int):
    result = await db.execute(select(models.DataSource).where(models.DataSource.id == data_source_id))
    return result.scalar()

async def update_data_source(db: AsyncSession, data_source_id: int, updated_data: str):
    data_source = await db.execute(select(models.DataSource).where(models.DataSource.id == data_source_id))
    data_source = data_source.scalar()
    if data_source:
        data_source.source_data = updated_data
        await db.commit()
        await db.refresh(data_source)
        return data_source
    return None

async def delete_data_source(db: AsyncSession, data_source_id: int):
    data_source = await db.execute(select(models.DataSource).where(models.DataSource.id == data_source_id))
    data_source = data_source.scalar()
    if data_source:
        await db.delete(data_source)
        await db.commit()
    return data_source

async def list_data_sources(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.DataSource).offset(skip).limit(limit))
    return [row.DataSource for row in result.fetchall()]

async def search_data_sources(db: AsyncSession, query: str):
    result = await db.execute(
        select(models.DataSource).filter(
            or_(
                models.DataSource.source_type.ilike(f"%{query}%"),
                models.DataSource.source_data.ilike(f"%{query}%")
            )
        )
    )
    # return result.fetchall()
    return [row.DataSource for row in result.fetchall()]


