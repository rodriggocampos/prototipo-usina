from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.usina import UsinaCreate, Usina
from app.crud.usina import get_usinas, create_usina, get_usina
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=Usina)
def create_usina(usina: UsinaCreate, db: Session = Depends(get_db)):
    return create_usina(db=db, usina=usina)