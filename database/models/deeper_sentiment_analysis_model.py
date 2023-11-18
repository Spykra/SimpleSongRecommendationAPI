from sqlalchemy import Column, Integer, ForeignKey, Float
from .base import Base
from sqlalchemy.orm import relationship

class DeepSentimentAnalysis(Base):
    __tablename__ = "deep_sentiment_analysis"
    
    id = Column(Integer, primary_key=True, index=True)
    text_id = Column(Integer, ForeignKey('text_generation.id'), nullable=False)
    admiration = Column(Float)
    amusement = Column(Float)
    anger = Column(Float)
    annoyance = Column(Float)
    approval = Column(Float)
    caring = Column(Float)
    confusion = Column(Float)
    curiosity = Column(Float)
    desire = Column(Float)
    disappointment = Column(Float)
    disapproval = Column(Float)
    disgust = Column(Float)
    embarrassment = Column(Float)
    excitement = Column(Float)
    fear = Column(Float)
    gratitude = Column(Float)
    grief = Column(Float)
    joy = Column(Float)
    love = Column(Float)
    nervousness = Column(Float)
    optimism = Column(Float)
    pride = Column(Float)
    realization = Column(Float)
    relief = Column(Float)
    remorse = Column(Float)
    sadness = Column(Float)
    surprise = Column(Float)
    neutral = Column(Float)

    text_generations = relationship("TextGeneration", backref="deep_sentiment_analysis")
