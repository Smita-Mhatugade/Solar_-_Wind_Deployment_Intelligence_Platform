"""
app/api/solar.py – Solar Prediction endpoints.

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import SolarPredictionRequest, SolarPredictionResponse

router = APIRouter()

@router.post("/predict", response_model=SolarPredictionResponse)
def predict_solar_yield(request: SolarPredictionRequest, db: Session = Depends(get_db)):
    """
    Run solar prediction model for a given location.
    Requires authenticated user (mocked for now).
    """
    # TODO: Load ML model, run inference, save to DB, return result
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("/history", response_model=List[SolarPredictionResponse])
def get_solar_history(db: Session = Depends(get_db)):
    """Get the authenticated user's solar prediction history."""
    # TODO: Fetch predictions for current user from DB
    raise HTTPException(status_code=501, detail="Not implemented yet")
