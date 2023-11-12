from sqlalchemy import Column, Integer, String, Float
from .base import Base

class SentimentAnalysis(Base):
    __tablename__ = "sentiment_analysis"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    negative_score = Column(Float)
    neutral_score = Column(Float)
    positive_score = Column(Float)

