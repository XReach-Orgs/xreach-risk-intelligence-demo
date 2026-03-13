import json
from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.models import PredictionRecord
from app.db.session import get_db
from app.ml.predictor import Predictor
from app.ml.schemas import RiskPredictionRequest, RiskPredictionResponse
from app.observability.metrics import PREDICTION_COUNT
from fastapi import Depends

router = APIRouter()


@router.post("/predict", response_model=RiskPredictionResponse)
def predict(payload: RiskPredictionRequest, db: Session = Depends(get_db)):
    predictor = Predictor()
    result = predictor.predict(payload)

    db_record = PredictionRecord(
        risk_score=result.risk_score,
        risk_band=result.risk_band,
        model_version=result.model_version,
        request_payload=json.dumps(payload.model_dump()),
    )
    db.add(db_record)
    db.commit()

    PREDICTION_COUNT.labels(
        risk_band=result.risk_band,
        model_version=result.model_version,
    ).inc()

    return result