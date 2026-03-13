from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "xreach_api_requests_total",
    "Total API requests",
    ["method", "path", "status_code"],
)

REQUEST_LATENCY = Histogram(
    "xreach_api_request_latency_seconds",
    "API request latency",
    ["method", "path"],
)

PREDICTION_COUNT = Counter(
    "xreach_predictions_total",
    "Total predictions",
    ["risk_band", "model_version"],
)