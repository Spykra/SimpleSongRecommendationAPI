from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .base import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class ResponseData(Base):
    __tablename__ = "response_data"

    id = Column(Integer, primary_key=True, index=True)
    response_data = Column(String)
    response_timestamp = Column(DateTime(timezone=True), default=func.now())

    owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="responses")

    processed_data_id = Column(Integer, ForeignKey("processed_data.id"))
    # processed_data = relationship("ProcessedData", back_populates="responses")
