from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Metrica(Base):
    __tablename__ = "metricas"
    
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, nullable=False)
    inversor_id = Column(Integer, ForeignKey("inversores.id"), nullable=False)
    potencia_ativa_watt = Column(Float, nullable=False)
    temperatura_celsius = Column(Float, nullable=False)

    inversor = relationship(
       "Inversor",
       back_populates="metricas",
       lazy="joined",
   )