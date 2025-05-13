from sqlalchemy.orm import Session
from app.models.inversor import Inversor
from app.schemas.inversor import InversorCreate, InversorUpdate

def create_inversor(db: Session, inversor: InversorCreate):
    db_inversor = Inversor(**inversor.dict())
    db.add(db_inversor)
    db.commit()
    db.refresh(db_inversor)
    return db_inversor

def get_inversor(db: Session, inversor_id: int):
    return db.query(Inversor).filter(Inversor.id == inversor_id).first()

def get_inversores(db: Session, skip: int = 0, limit: int = 100, usina_id: int = None):
    query = db.query(Inversor)
    if usina_id:
        query = query.filter(Inversor.usina_id == usina_id)
    return query.offset(skip).limit(limit).all()

def update_inversor(db: Session, inversor_id: int, inversor: InversorUpdate):
    db_inversor = get_inversor(db, inversor_id)
    if db_inversor:
        for key, value in inversor.dict().items():
            setattr(db_inversor, key, value)
        db.commit()
        db.refresh(db_inversor)
    return db_inversor

def delete_inversor(db: Session, inversor_id: int):
    db_inversor = get_inversor(db, inversor_id)
    if db_inversor:
        db.delete(db_inversor)
        db.commit()
        return True
    return False