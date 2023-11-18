# TextGenerationModel.py
from sqlalchemy import Column, Integer, String
from .base import Base

class TextGeneration(Base):
    __tablename__ = "text_generation"
    
    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(String, nullable=False)
    generated_text = Column(String, nullable=False)
