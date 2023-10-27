from sqlalchemy.orm import Session
from database import models

def create_processed_data(db: Session, processed_data: str, owner_id: int, data_source_id: int):
    data = models.ProcessedData(processed_data=processed_data, owner_id=owner_id, data_source_id=data_source_id)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_processed_data_by_id(db: Session, processed_data_id: int):
    return db.query(models.ProcessedData).filter(models.ProcessedData.id == processed_data_id).first()
