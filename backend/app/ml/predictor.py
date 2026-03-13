import numpy as np

from app.core.config import get_settings
from app.ml.model_loader import ModelLoader
from app.ml.schemas import RiskPredictionRequest, RiskPredictionResponse


class Predictor:
    def __init__(self) -> None:
        self.settings = get_settings()
        self.loader = ModelLoader()

    def predict(self, payload: RiskPredictionRequest) -> RiskPredictionResponse:
        model = self.loader.load()
        features = np.array(
            [[
                payload.transaction_amount,
                payload.account_age_days,
                payload.device_trust_score,
                payload.vendor_risk_score,
                payload.unusual_access_hour,
                payload.prior_incidents,
            ]]
        )

        proba = float(model.predict_proba(features)[0][1])

        if proba >= 0.75:
            band = "high"
        elif proba >= 0.40:
            band = "medium"
        else:
            band = "low"

        return RiskPredictionResponse(
            risk_score=round(proba, 4),
            risk_band=band,
            model_version=self.settings.model_version,
        )