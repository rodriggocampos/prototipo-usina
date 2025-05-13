from .usinas import router as usinas_router
from .inversores import router as inversores_router
from .metricas import router as metricas_router

__all__ = ["usinas_router", "inversores_router", "metricas_router"]