from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from datetime import datetime
from app.models.metrica import Metrica
from app.models.inversor import Inversor
from app.utils.calculations import TimeSeriesValue, calc_inverters_generation

class EntityWithPowerWrapper:
    def __init__(self, power_data):
        self.power = [
            TimeSeriesValue(value=metric.potencia_ativa_watt, date=metric.datetime)
            for metric in power_data
        ]

def get_metrics_by_inversor(db: Session, inversor_id: int, start: datetime, end: datetime):
    return db.query(Metrica).filter(
        and_(
            Metrica.inversor_id == inversor_id,
            Metrica.datetime >= start,
            Metrica.datetime <= end
        )
    ).order_by(Metrica.datetime).all()

def get_metrics_by_usina(db: Session, usina_id: int, start: datetime, end: datetime):
    inversores = db.query(Inversor).filter(Inversor.usina_id == usina_id).all()
    metrics = []
    for inversor in inversores:
        metrics.extend(get_metrics_by_inversor(db, inversor.id, start, end))
    return metrics

def get_max_power(db: Session, inversor_id: int, start: datetime, end: datetime):
    max_power = db.query(func.max(Metrica.potencia_ativa_watt)).filter(
        and_(
            Metrica.inversor_id == inversor_id,
            Metrica.datetime >= start,
            Metrica.datetime <= end
        )
    ).scalar()
    return max_power or 0.0

def get_avg_temperature(db: Session, inversor_id: int, start: datetime, end: datetime):
    avg_temp = db.query(func.avg(Metrica.temperatura_celsius)).filter(
        and_(
            Metrica.inversor_id == inversor_id,
            Metrica.datetime >= start,
            Metrica.datetime <= end
        )
    ).scalar()
    return round(avg_temp, 2) if avg_temp else 0.0

def calculate_generation(db: Session, metrics: list):
    if not metrics:
        return 0.0
    
    entities = []
    current_inversor = None
    power_data = []
    
    for metric in sorted(metrics, key=lambda x: x.inversor_id):
        if metric.inversor_id != current_inversor:
            if power_data:
                entities.append(EntityWithPowerWrapper(power_data))
                power_data = []
            current_inversor = metric.inversor_id
        power_data.append(metric)
    
    if power_data:
        entities.append(EntityWithPowerWrapper(power_data))
    
    return calc_inverters_generation(entities)