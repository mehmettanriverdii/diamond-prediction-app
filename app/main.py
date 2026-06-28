from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from loguru import logger
from pathlib import Path
import time
import uvicorn

from app.schemas import DiamondFeatures, PredictionResponse
from app.predictor import predict

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)
logger.add(
    log_dir / "app.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

app = FastAPI(
    title="Diamond Price Prediction API",
    description="Predicts diamond price based on features",
    version="1.0.0"
)

templates = Jinja2Templates(
    directory=str(Path(__file__).parent / "templates")
)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
async def predict_price(features: DiamondFeatures):
    start_time = time.time()

    logger.info(f"Prediction request: {features.model_dump()}")

    prediction = predict(features.model_dump())

    duration = time.time() - start_time
    logger.info(f"Prediction result: {prediction} | Duration: {duration:.3f}s")

    return PredictionResponse(predicted_price=prediction)