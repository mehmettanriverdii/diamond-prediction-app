from pydantic import BaseModel, Field
from typing import Literal

class DiamondFeatures(BaseModel):
    carat: float = Field(..., gt=0, description="Diamond weight in carats")
    cut: Literal["Fair", "Good", "Very Good", "Premium", "Ideal"]
    color: Literal["J", "I", "H", "G", "F", "E", "D"]
    clarity: Literal["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
    depth: float = Field(..., gt=0, description="Depth percentage", )
    table: float = Field(..., gt=0, description="Table percentage")
    x: float = Field(..., gt=0, description="Length in mm")
    y: float = Field(..., gt=0, description="Width in mm")
    z: float = Field(..., gt=0, description="Depth in mm")

class PredictionResponse(BaseModel):
    predicted_price: float
    currency: str = "USD"