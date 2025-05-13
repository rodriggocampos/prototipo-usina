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

@router.post("/importar")
async def importar_metricas(
    raw_metricas: list[dict],
    db: Session = Depends(get_db),
):
    try:
        mappings = []
        for m in raw_metricas:
            dt = m.get("datetime")
            if isinstance(dt, dict) and "$date" in dt:
                iso_str = dt["$date"]
            else:
                iso_str = dt
            parsed_dt = isoparse(iso_str) if isinstance(iso_str, str) else iso_str

            potencia = m.get("potencia_ativa_watt")
            temperatura = m.get("temperatura_celsius")

            potencia = float(potencia) if potencia is not None else 0.0
            temperatura = float(temperatura) if temperatura is not None else 0.0

            mappings.append({
                "datetime": parsed_dt,
                "inversor_id": m["inversor_id"],
                "potencia_ativa_watt": potencia,
                "temperatura_celsius": temperatura,
            })

        stmt = insert(Metrica)
        db.execute(stmt, mappings)
        db.commit()
        return {"mensagem": f"{len(mappings)} métricas importadas com sucesso"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
