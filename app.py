from fastapi import FastAPI, Body
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline

text:str = "What is the Summarized Text?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        os.system("python main.py")
    except Exception as e:
        return Response(content=f"An error occurred: {e}", media_type="text/plain")
    
@app.post("/predict")
async def predict_route(text: str):
    try:
        pipeline = PredictionPipeline()
        predicted = pipeline.predict(text)
        return predicted
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)