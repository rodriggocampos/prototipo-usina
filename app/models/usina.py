from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Usina(Base):
    __tablename__ = "usinas"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())