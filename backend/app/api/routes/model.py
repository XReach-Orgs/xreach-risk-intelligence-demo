from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import get_settings


class ModelInfoResponse(BaseModel):
    model_version: str
    model_name: str
    environment: str


router = APIRouter()


@router.get("/model-info", response_model=ModelInfoResponse)
def model_info():
    settings = get_settings()

    return ModelInfoResponse(
        model_version=settings.model_version,
        model_name=settings.app_name,
        environment=settings.environment,
    )