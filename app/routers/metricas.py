from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import insert
from dateutil.parser import isoparse
from datetime import datetime
from app.database import get_db
from app.models.metrica import Metrica
from app.models.inversor import Inversor
from app.crud.metrica import (
    get_max_power,
    get_avg_temperature,
    calculate_generation,
    get_metrics_by_inversor,
    get_metrics_by_usina
)
from app.schemas.metrica import MetricaCreate

router = APIRouter(tags=["Metricas"])

@router.get("/potencia-maxima")
async def potencia_maxima(
    inversor_id: int = Query(...),
    data_inicio: datetime = Query(...),
    data_fim: datetime = Query(...),
    db: Session = Depends(get_db)
):
    if data_inicio > data_fim:
        raise HTTPException(status_code=400, detail="Data inicial maior que data final")
    return {
        "inversor_id": inversor_id,
        "potencia_maxima": get_max_power(db, inversor_id, data_inicio, data_fim)
    }

@router.get("/temperatura-media")
async def temperatura_media(
    inversor_id: int = Query(...),
    data_inicio: datetime = Query(...),
    data_fim: datetime = Query(...),
    db: Session = Depends(get_db)
):
    if data_inicio > data_fim:
        raise HTTPException(status_code=400, detail="Data inicial maior que data final")
    return {
        "inversor_id": inversor_id,
        "temperatura_media": get_avg_temperature(db, inversor_id, data_inicio, data_fim)
    }

@router.get("/geracao-usina")
async def geracao_usina(
    usina_id: int = Query(...),
    data_inicio: datetime = Query(...),
    data_fim: datetime = Query(...),
    db: Session = Depends(get_db)
):
    if data_inicio > data_fim:
        raise HTTPException(status_code=400, detail="Data inicial maior que data final")
    metrics = get_metrics_by_usina(db, usina_id, data_inicio, data_fim)
    total = calculate_generation(db, metrics)
    return {
        "usina_id": usina_id,
        "geracao_total": total
    }

@router.get("/geracao-inversor")
async def geracao_inversor(
    inversor_id: int = Query(...),
    data_inicio: datetime = Query(...),
    data_fim: datetime = Query(...),
    db: Session = Depends(get_db)
):
    if data_inicio > data_fim:
        raise HTTPException(status_code=400, detail="Data inicial maior que data final")
    metrics = get_metrics_by_inversor(db, inversor_id, data_inicio, data_fim)
    total = calculate_generation(db, metrics)
    return {
        "inversor_id": inversor_id,
        "geracao_total": total
    }