from pathlib import Path

from fastapi.testclient import TestClient
from app.main import app
from app.ml.training.train import main as train_model

client = TestClient(app)


def test_predict():
    model_path = Path("app/ml/artifacts/risk_model.joblib")
    if not model_path.exists():
        train_model()

    payload = {
        "transaction_amount": 8000,
        "account_age_days": 30,
        "device_trust_score": 0.2,
        "vendor_risk_score": 0.9,
        "unusual_access_hour": 1,
        "prior_incidents": 4,
    }

    response = client.post("/api/v1/predict", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "risk_score" in body
    assert "risk_band" in body
    assert "model_version" in body