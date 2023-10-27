from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import connection, crud
from database.models import User
from database.schemas import User as UserSchema, UserCreate as UserCreateSchema

router = APIRouter()

# Dependency
def get_db():
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
