from fastapi import APIRouter

from app.api.routes.audit import router as audit_router
from app.api.routes.explanations import router as explanations_router
from app.api.routes.health import router as health_router
from app.api.routes.history import router as history_router
from app.api.routes.model import router as model_router
from app.api.routes.predict import router as predict_router

api_router = APIRouter()

api_router.include_router(health_router, tags=["health"])
api_router.include_router(model_router, tags=["model"])
api_router.include_router(predict_router, tags=["predict"])
api_router.include_router(history_router, tags=["history"])
api_router.include_router(audit_router, tags=["audit"])
api_router.include_router(explanations_router, tags=["explanations"])