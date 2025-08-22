
import fastapi
import json
from pydantic import BaseModel
import random
from utils import configure_logging
from time import time, sleep

from prometheus_client import Counter, Histogram, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST


app = fastapi.FastAPI()

# configure logging
logger = configure_logging()

# --- Prometheus metrics ---
REQUEST_COUNT = Counter(name="predictions_total", documentation="Total number of predictions")
REQUEST_LATENCY = Histogram(name="prediction_latency_seconds", documentation="Latency of prediction requests")

def log_event(event: dict):
    """Write structured log as JSON"""
    logger.info(json.dumps(event))

class PredictionRequest(BaseModel):
    prediction_request: str

@app.post("/predict")
async def make_prediction(prediction_request: PredictionRequest):
    
    start = time()
    # Make dummy prediction
    pred = random.random()
    # Fake latency
    sleep(random.random())
    end = time()
    latency_ms = (end - start) * 1000

    # Create and emit structured log
    log = {
        "timestamp": time(),
        "endpoint": "/predict",
        "input": prediction_request.model_dump(),
        "prediction": pred,
        "latency_ms": latency_ms,
    }
    log_event(log)  # emit
    
    # Update metrics
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time() - start) # total latency

    # Return the response
    return {"prediction": pred}


# --- Expose a metrics endpoint ---
@app.get("/metrics")
def metrics():
    """This is what Prometheus will scrape."""
    return fastapi.Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)