from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
import uvicorn

# load model
model = joblib.load("boston_model.pkl")

# Build the API
app = FastAPI(title="Boston Housing Price Predictor")

# input schema
class HouseFeatures(BaseModel):
    crim: float
    zn: float
    indus: float
    chas: int
    nox: float
    rm: float
    age: float
    dis: float
    rad: int
    tax: float
    ptratio: float
    b: float
    lstat: float

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def prediction_price(features: HouseFeatures):
    data = np.array([[
        features.crim,
        features.zn,
        features.indus,
        features.chas,
        features.nox,
        features.rm,
        features.age,
        features.dis,
        features.rad,
        features.tax,
        features.ptratio,
        features.b,
        features.lstat
    ]])

    prediction = model.predict(data)
    return {"predicted_price": float(prediction[0])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# run the code uvicorn app:app --reload