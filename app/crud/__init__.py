# Exportação das operações CRUD
from .usina import (
    create_usina,
    get_usina,
    get_usinas,
    update_usina,
    delete_usina
)
from .inversor import (
    create_inversor,
    get_inversor,
    get_inversores,
    update_inversor,
    delete_inversor
)
from .metrica import (
    get_max_power,
    get_avg_temperature,
    calculate_generation,
    get_metrics_by_inversor,
    get_metrics_by_usina
)

__all__ = [
    "create_usina", "get_usina", "get_usinas", "update_usina", "delete_usina",
    "create_inversor", "get_inversor", "get_inversores", "update_inversor", "delete_inversor",
    "get_max_power", "get_avg_temperature", "calculate_generation",
    "get_metrics_by_inversor", "get_metrics_by_usina"
]