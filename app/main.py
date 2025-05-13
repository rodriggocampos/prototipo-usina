from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.models import usina, inversor, metrica
from app.routers import usinas, inversores, metricas

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./monitoring.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criação das tabelas
Base.metadata.create_all(bind=engine)

# Inicialização do FastAPI
app = FastAPI(
    title="Monitoramento de Usinas Fotovoltaicas",
    description="API para gestão e monitoramento de usinas de energia solar",
    version="1.0.0"
)

# Registrar rotas
app.include_router(usinas.router, prefix="/api/v1/usinas", tags=["Usinas"])
app.include_router(inversores.router, prefix="/api/v1/inversores", tags=["Inversores"])
app.include_router(metricas.router, prefix="/api/v1/metricas", tags=["Metricas"])

@app.get("/")
def root():
    return {"message": "API Operacional"}
