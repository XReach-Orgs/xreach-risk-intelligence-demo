import { useState } from "react";
import axios from "axios";

const API_BASE = "http://localhost:8000/api/v1";

export default function App() {
    const [form, setForm] = useState({
        transaction_amount: 2500,
        account_age_days: 120,
        device_trust_score: 0.82,
        vendor_risk_score: 0.30,
        unusual_access_hour: 0,
        prior_incidents: 1,
    });

    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const updateField = (key, value) => {
        setForm((prev) => ({ ...prev, [key]: Number(value) }));
    };

    const submitPrediction = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const response = await axios.post(`${API_BASE}/predict`, form);
            setResult(response.data);
        } catch (error) {
            console.error(error);
            alert("Prediction request failed.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="app-shell">
            <div className="card">
                <h1>XReach Risk Intelligence Demo</h1>
                <p>Production-style ML risk scoring platform targeting AKS.</p>

                <form onSubmit={submitPrediction} className="form">
                    <label>
                        Transaction Amount
                        <input
                            type="number"
                            value={form.transaction_amount}
                            onChange={(e) => updateField("transaction_amount", e.target.value)}
                        />
                    </label>

                    <label>
                        Account Age Days
                        <input
                            type="number"
                            value={form.account_age_days}
                            onChange={(e) => updateField("account_age_days", e.target.value)}
                        />
                    </label>

                    <label>
                        Device Trust Score
                        <input
                            type="number"
                            step="0.01"
                            value={form.device_trust_score}
                            onChange={(e) => updateField("device_trust_score", e.target.value)}
                        />
                    </label>

                    <label>
                        Vendor Risk Score
                        <input
                            type="number"
                            step="0.01"
                            value={form.vendor_risk_score}
                            onChange={(e) => updateField("vendor_risk_score", e.target.value)}
                        />
                    </label>

                    <label>
                        Unusual Access Hour
                        <input
                            type="number"
                            min="0"
                            max="1"
                            value={form.unusual_access_hour}
                            onChange={(e) => updateField("unusual_access_hour", e.target.value)}
                        />
                    </label>

                    <label>
                        Prior Incidents
                        <input
                            type="number"
                            value={form.prior_incidents}
                            onChange={(e) => updateField("prior_incidents", e.target.value)}
                        />
                    </label>

                    <button type="submit" disabled={loading}>
                        {loading ? "Scoring..." : "Run Risk Score"}
                    </button>
                </form>

                {result && (
                    <div className="result">
                        <h2>Prediction Result</h2>
                        <p><strong>Risk Score:</strong> {result.risk_score}</p>
                        <p><strong>Risk Band:</strong> {result.risk_band}</p>
                        <p><strong>Model Version:</strong> {result.model_version}</p>
                    </div>
                )}
            </div>
        </div>
    );
}