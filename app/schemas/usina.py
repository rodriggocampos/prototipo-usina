from pydantic import BaseModel
from datetime import datetime

class UsinaBase(BaseModel):
    nome: str

class UsinaCreate(UsinaBase):
    pass

class Usina(UsinaBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UsinaUpdate(UsinaBase):
    pass