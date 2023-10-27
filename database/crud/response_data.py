from sqlalchemy.orm import Session
from database import models

def create_response_data(db: Session, response_data: str, owner_id: int, processed_data_id: int):
    data = models.ResponseData(response_data=response_data, owner_id=owner_id, processed_data_id=processed_data_id)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_response_by_id(db: Session, response_id: int):
    return db.query(models.ResponseData).filter(models.ResponseData.id == response_id).first()
