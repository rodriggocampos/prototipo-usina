from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Inversor(Base):
    __tablename__ = "inversores"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    usina_id = Column(Integer, ForeignKey("usinas.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    metricas = relationship("Metrica", back_populates="inversor")
    metricas = relationship(
        "Metrica",
        back_populates="inversor",
        cascade="all, delete-orphan"
    )