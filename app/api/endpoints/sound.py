# from fastapi import APIRouter, UploadFile, Depends
# from sqlalchemy.orm import Session
# from database import crud, session
# from database.models import DataSource
# from database.schemas import DataSource as DataSourceSchema

# router = APIRouter()

# def get_db():
#     db = session.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/upload_sound", response_model=DataSourceSchema)
# async def upload_mp3(file: UploadFile, db: Session = Depends(get_db)):
#     content = await file.read()

#     # Directly assign without processing for now. Implement sound processing if needed.
#     processed_data = content

#     owner_id_placeholder = 1  # TODO: Replace this with actual owner/user ID once authentication is implemented.
#     return crud.create_data_source(db=db, source_type="sound", source_data=processed_data, owner_id=owner_id_placeholder)
