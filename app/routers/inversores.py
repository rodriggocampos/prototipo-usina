from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.inversor import Inversor, InversorCreate, InversorUpdate
from app.crud.inversor import (
    create_inversor,
    get_inversor,
    get_inversores,
    update_inversor,
    delete_inversor
)

router = APIRouter( tags=["inversores"])

@router.post("/", response_model=Inversor)
def criar_inversor(inversor: InversorCreate, db: Session = Depends(get_db)):
    return create_inversor(db=db, inversor=inversor)

@router.get("/", response_model=List[Inversor])
def listar_inversores(
    skip: int = 0,
    limit: int = 100,
    usina_id: int = None,
    db: Session = Depends(get_db)
):
    return get_inversores(db, skip=skip, limit=limit, usina_id=usina_id)

@router.get("/{inversor_id}", response_model=Inversor)
def buscar_inversor(inversor_id: int, db: Session = Depends(get_db)):
    db_inversor = get_inversor(db, inversor_id=inversor_id)
    if not db_inversor:
        raise HTTPException(status_code=404, detail="Inversor não encontrado")
    return db_inversor

@router.put("/{inversor_id}", response_model=Inversor)
def atualizar_inversor(
    inversor_id: int,
    inversor: InversorUpdate,
    db: Session = Depends(get_db)
):
    return update_inversor(db=db, inversor_id=inversor_id, inversor=inversor)

@router.delete("/{inversor_id}")
def remover_inversor(inversor_id: int, db: Session = Depends(get_db)):
    success = delete_inversor(db=db, inversor_id=inversor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Inversor não encontrado")
    return {"mensagem": "Inversor removido com sucesso"}