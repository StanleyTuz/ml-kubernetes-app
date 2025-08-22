
import fastapi
import json
from pydantic import BaseModel
import random
from utils import configure_logging
from time import time, sleep
app = fastapi.FastAPI()

# configure logging
logger = configure_logging()

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

    # Structured log
    log = {
        "timestamp": time(),
        "endpoint": "/predict",
        "input": prediction_request.dict(),
        "prediction": pred,
        "latency_ms": (time() - start) * 1000,
    }
    log_event(log)  # emit
    
    # Return a dummy prediction response
    return {"prediction": pred}
