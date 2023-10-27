from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class DataSource(Base):
    __tablename__ = "data_sources"

    id = Column(Integer, primary_key=True, index=True)
    source_type = Column(String)
    source_data = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="data_sources")
    # processed_data = relationship("ProcessedData", back_populates="data_source")
