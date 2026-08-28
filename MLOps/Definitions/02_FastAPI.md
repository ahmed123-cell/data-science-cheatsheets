# FastAPI Explained: A Complete Guide

## What is FastAPI?

**FastAPI** is a modern, high-performance Python web framework for building **APIs** (Application Programming Interfaces). 

It is one of the fastest web frameworks available (thanks to Starlette and Pydantic) and is extremely popular for building production-ready REST APIs, especially for **Machine Learning** and **Deep Learning** model deployment.

### Key Features
- **Very Fast**: One of the fastest Python frameworks (comparable to Node.js and Go)
- **Automatic Interactive Docs**: Swagger UI and ReDoc (accessible at `/docs` and `/redoc`)
- **Type Hints & Validation**: Uses Python type hints + Pydantic for automatic data validation
- **Async Support**: Built-in support for asynchronous code
- **Dependency Injection**: Clean and powerful dependency system
- **Easy to Learn**: Great developer experience

---

## Installation

```bash
pip install fastapi uvicorn
```

For Machine Learning projects, also install:
```bash
pip install pydantic numpy scikit-learn torch torchvision  # or tensorflow
```

---

## Basic FastAPI Example

```python
# main.py
from fastapi import FastAPI

app = FastAPI(title="My First API")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

**Run the app:**
```bash
uvicorn main:app --reload
```

Then visit: `http://127.0.0.1:8000/docs`

---

## FastAPI for Machine Learning (Practical Examples)

### 1. Simple ML Model Deployment (Scikit-learn)

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="ML Model API")

# Load your trained model
model = joblib.load("model.pkl")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
async def predict_iris(data: IrisInput):
    input_data = np.array([[data.sepal_length, data.sepal_width, 
                           data.petal_length, data.petal_width]])
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data).max()
    
    return {
        "prediction": prediction[0],
        "confidence": float(probability)
    }
```

### 2. Deep Learning Model Example (PyTorch)

```python
# main.py
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import torch
from torchvision import transforms
from PIL import Image
import io

app = FastAPI(title="Image Classification API")

# Load pre-trained model
model = torch.load("model.pth", map_location="cpu")
model.eval()

class PredictionResponse(BaseModel):
    class_name: str
    confidence: float

@app.post("/predict-image", response_model=PredictionResponse)
async def predict_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                           std=[0.229, 0.224, 0.225])
    ])
    
    input_tensor = transform(image).unsqueeze(0)
    
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
    
    confidence, predicted_class = torch.max(probabilities, 0)
    
    return {
        "class_name": f"class_{predicted_class.item()}",
        "confidence": float(confidence)
    }
```

---

## Running in Production

```bash
# Using Uvicorn (recommended)
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Or with Docker (recommended for production)
docker build -t my-ml-api .
docker run -p 8000:8000 my-ml-api
```

---

## Docker + FastAPI Best Practice (Dockerfile)

```dockerfile
# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Quick Tips for ML Engineers

- Use **Pydantic models** for input validation
- Always return clear JSON responses
- Add proper error handling
- Use dependency injection for model loading
- Monitor with Prometheus + Grafana in production
- Consider **FastAPI + Celery** for heavy inference tasks

---

Would you like me to add:
- Authentication (JWT)
- Batch prediction support
- Model versioning
- Health check endpoints?

Just say the word and I’ll expand this guide!