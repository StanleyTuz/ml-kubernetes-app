import fastapi
from pydantic import BaseModel
import random

app = fastapi.FastAPI()


class PredictionRequest(BaseModel):
    prediction_request: str

@app.post("/predict")
def make_prediction(prediction_request: PredictionRequest):
    # Return a dummy prediction response
    return {"prediction": random.random()}