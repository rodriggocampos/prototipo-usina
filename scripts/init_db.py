from app.database import SessionLocal
from app.models.usina import Usina
from app.models.inversor import Inversor

def main():
    db = SessionLocal()

    usina1 = Usina(id=1, nome="Usina Solar 1")
    usina2 = Usina(id=2, nome="Usina Solar 2")
    db.add_all([usina1, usina2])
    db.commit()

    inversores = [
        Inversor(id=i, nome=f"Inversor {i}", usina_id=1 if i <= 4 else 2)
        for i in range(1, 9)
    ]
    db.add_all(inversores)
    db.commit()
    print("Usinas e inversores inseridos com sucesso.")

if __name__ == "__main__":
    main()
