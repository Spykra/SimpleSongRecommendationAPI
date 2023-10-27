from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.sql import func

class ProcessedData(Base):
    __tablename__ = "processed_data"

    id = Column(Integer, primary_key=True, index=True)
    processed_data = Column(String)
    processing_timestamp = Column(DateTime(timezone=True), default=func.now())

    owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="processed_data")

    data_source_id = Column(Integer, ForeignKey("data_sources.id"))
    # data_source = relationship("DataSource", back_populates="processed_data")

    # responses = relationship("ResponseData", back_populates="processed_data")
