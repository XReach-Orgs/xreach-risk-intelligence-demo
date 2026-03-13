from pydantic import BaseModel, Field


class RiskPredictionRequest(BaseModel):
    transaction_amount: float = Field(..., ge=0)
    account_age_days: int = Field(..., ge=0)
    device_trust_score: float = Field(..., ge=0, le=1)
    vendor_risk_score: float = Field(..., ge=0, le=1)
    unusual_access_hour: int = Field(..., ge=0, le=1)
    prior_incidents: int = Field(..., ge=0)


class RiskPredictionResponse(BaseModel):
    risk_score: float
    risk_band: str
    model_version: str