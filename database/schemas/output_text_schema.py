# TextGenerationSchema.py
from pydantic import BaseModel
from typing import Optional

class TextGenerationBase(BaseModel):
    original_text: str
    generated_text: str

class TextGenerationCreate(TextGenerationBase):
    pass

class TextGenerationUpdate(BaseModel):
    original_text: Optional[str] = None
    generated_text: Optional[str] = None


class TextGenerationResponse(TextGenerationBase):
    id: Optional[int]

    class Config:
        orm_mode = True
