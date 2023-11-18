# TextGenerationSchema.py
from pydantic import BaseModel
from typing import Optional

class TextGenerationBase(BaseModel):
    original_text: str
    generated_text: str

class TextGenerationCreate(TextGenerationBase):
    pass

class TextGenerationResponse(TextGenerationBase):
    id: Optional[int]

    class Config:
        orm_mode = True
