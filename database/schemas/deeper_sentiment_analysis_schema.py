from pydantic import BaseModel
from typing import Optional


class DeepSentimentScores(BaseModel):
    admiration: Optional[float] = None
    amusement: Optional[float] = None
    anger: Optional[float] = None
    annoyance: Optional[float] = None
    approval: Optional[float] = None
    caring: Optional[float] = None
    confusion: Optional[float] = None
    curiosity: Optional[float] = None
    desire: Optional[float] = None
    disappointment: Optional[float] = None
    disapproval: Optional[float] = None
    disgust: Optional[float] = None
    embarrassment: Optional[float] = None
    excitement: Optional[float] = None
    fear: Optional[float] = None
    gratitude: Optional[float] = None
    grief: Optional[float] = None
    joy: Optional[float] = None
    love: Optional[float] = None
    nervousness: Optional[float] = None
    optimism: Optional[float] = None
    pride: Optional[float] = None
    realization: Optional[float] = None
    relief: Optional[float] = None
    remorse: Optional[float] = None
    sadness: Optional[float] = None
    surprise: Optional[float] = None
    neutral: Optional[float] = None


class DeepSentimentAnalysisBase(BaseModel):
    text: str

class DeepSentimentAnalysisCreate(DeepSentimentAnalysisBase):
    pass

class DeepSentimentAnalysisResponse(DeepSentimentAnalysisBase):
    id: Optional[int]
    deep_sentiment_scores: DeepSentimentScores

    class Config:
        orm_mode = True
