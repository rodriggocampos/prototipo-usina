# Exportação dos schemas Pydantic
from .usina import Usina, UsinaCreate
from .inversor import Inversor, InversorCreate
from .metrica import Metrica, MetricaCreate

__all__ = [
    "Usina", "UsinaCreate",
    "Inversor", "InversorCreate",
    "Metrica", "MetricaCreate"
]