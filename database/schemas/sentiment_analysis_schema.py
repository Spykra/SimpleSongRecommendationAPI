from pydantic import BaseModel
from typing import Optional

class SentimentScores(BaseModel):
    negative_score: Optional[float] = None
    neutral_score: Optional[float] = None
    positive_score: Optional[float] = None


class SentimentAnalysisBase(BaseModel):
    text: str

class SentimentAnalysisCreate(SentimentAnalysisBase):
    pass

class SentimentAnalysisResponse(SentimentAnalysisBase):
    id: Optional[int]
    sentiment_scores: SentimentScores

    class Config:
        orm_mode = True
