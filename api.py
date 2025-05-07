from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model
with open("compost_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class InputData(BaseModel):
    moisture: float
    ph: float
    ec: float

@app.post("/predict")
def predict(data: InputData):
    inputs = np.array([[data.moisture, data.ph, data.ec]])
    prediction = model.predict(inputs)[0]
    return {"result": prediction}
