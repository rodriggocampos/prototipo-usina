from datetime import datetime
from pydantic import BaseModel

class MetricaBase(BaseModel):
    datetime: datetime
    inversor_id: int
    potencia_ativa_watt: float
    temperatura_celsius: float

class MetricaCreate(MetricaBase):
    pass

class Metrica(MetricaBase):
    id: int

    class Config:
        from_attributes = True