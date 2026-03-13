from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter()


@router.get("/model-info")
def model_info():
    settings = get_settings()
    return {
        "model_version": settings.model_version,
        "model_path": settings.model_path,
    }