from pydantic import BaseModel
from typing import List, Optional

# The BaseModel from Pydantic is used for data validation and serialization/deserialization.
# For each model, we generally have three schema classes:
# A base schema defining shared attributes.
# A creation schema for creating new instances (might include fields like passwords).
# A full schema used for reading instances, often with the database ID included.
class DataSourceBase(BaseModel):
    source_type: str
    source_data: str

class DataSourceCreate(DataSourceBase):
    pass

class DataSourceResponse(DataSourceBase):
    source_type: Optional[str]
    source_data: Optional[str]
    id: Optional[int]
# The Config class ensures that the schemas can be used with ORM objects (like those from SQLAlchemy).
    class Config:
        orm_mode = True
