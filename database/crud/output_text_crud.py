from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.models.output_text_model import TextGeneration
from database.schemas.output_text_schema import TextGenerationUpdate


async def create_text_record(db: AsyncSession, original_text: str, generated_text: str) -> TextGeneration:
    """
    Create a record in the TextGeneration table with both original and generated text.

    Args:
        db (AsyncSession): The database session.
        original_text (str): The original text to store.
        generated_text (str): The generated text to store.

    Returns:
        TextGeneration: The created TextGeneration record.
    """
    db_obj = TextGeneration(original_text=original_text, generated_text=generated_text)
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj


async def read_text_record(db: AsyncSession, text_id: int):
    result = await db.get(TextGeneration, text_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Text record not found")


async def delete_text_record_by_id(db: AsyncSession, text_id: int):
    obj = await db.get(TextGeneration, text_id)
    if obj:
        await db.delete(obj)
        await db.commit()
        return {"message": "Record deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Text record not found")
