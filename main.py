from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import pickle
import pandas as pd

from utils import InputData

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Health check endpoint
@app.get("/")
def home():
    return {"message": "hello world!"}

# Prediction endpoint
@app.post("/predict")
def model_prediction(input: InputData):
    try:
        # Convert the input data to a DataFrame
        input_df = pd.DataFrame([input.model_dump()])
        # Make predictions using the loaded model
        predictions = model.predict(input_df)
        prediction = predictions.item()
        return JSONResponse(content=prediction, status_code=200)
    except Exception as e:
        # Handle exceptions and return an error message
        return JSONResponse(content={"error": str(e)}, status_code=422)


@app.get("/test")
def test_endpoint():
    content = "Test endpoint is working!"
    return JSONResponse(content=content, status_code=200)


# Only for local testing
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
