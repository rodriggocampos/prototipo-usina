from pydantic import BaseModel
from datetime import datetime

class InversorBase(BaseModel):
    nome: str
    usina_id: int

class InversorCreate(InversorBase):
    pass

class InversorUpdate(InversorBase):
    pass

class Inversor(InversorBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True