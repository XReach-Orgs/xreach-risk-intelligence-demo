from pathlib import Path

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

ARTIFACT_DIR = Path("app/ml/artifacts")
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)


def generate_data(samples: int = 1000):
    rng = np.random.default_rng(42)

    transaction_amount = rng.uniform(1, 10000, samples)
    account_age_days = rng.integers(1, 3650, samples)
    device_trust_score = rng.uniform(0, 1, samples)
    vendor_risk_score = rng.uniform(0, 1, samples)
    unusual_access_hour = rng.integers(0, 2, samples)
    prior_incidents = rng.integers(0, 10, samples)

    X = np.column_stack([
        transaction_amount,
        account_age_days,
        device_trust_score,
        vendor_risk_score,
        unusual_access_hour,
        prior_incidents,
    ])

    y = (
        (transaction_amount > 5000).astype(int)
        + (device_trust_score < 0.3).astype(int)
        + (vendor_risk_score > 0.7).astype(int)
        + (unusual_access_hour == 1).astype(int)
        + (prior_incidents > 3).astype(int)
    ) >= 2

    return X, y.astype(int)


def main():
    X, y = generate_data()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, ARTIFACT_DIR / "risk_model.joblib")
    print("Model saved to app/ml/artifacts/risk_model.joblib")


if __name__ == "__main__":
    main()