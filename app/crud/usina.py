from sqlalchemy.orm import Session
from app.models.usina import Usina
from app.schemas.usina import UsinaUpdate
from app.schemas.usina import UsinaCreate

def update_usina(db: Session, usina_id: int, usina: UsinaUpdate):
    db_usina = db.query(Usina).filter(Usina.id == usina_id).first()
    if db_usina:
        for key, value in usina.dict().items():
            setattr(db_usina, key, value)
        db.commit()
        db.refresh(db_usina)
    return db_usina

def get_usina(db: Session, usina_id: int):
    return db.query(Usina).filter(Usina.id == usina_id).first()

def get_usinas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usina).offset(skip).limit(limit).all()

def create_usina(db: Session, usina: UsinaCreate):
    db_usina = Usina(nome=usina.nome)
    db.add(db_usina)
    db.commit()
    db.refresh(db_usina)
    return db_usina

def delete_usina(db: Session, usina_id: int):
    db_usina = db.query(Usina).filter(Usina.id == usina_id).first()
    if db_usina:
        db.delete(db_usina)
        db.commit()
        return True
    return False