from sqlalchemy.ext.declarative import declarative_base
from database.connection import engine

Base = declarative_base(bind=engine)
