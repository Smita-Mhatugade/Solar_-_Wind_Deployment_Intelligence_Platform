"""
app/api/site.py – Site Suitability Analysis endpoints.

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import SiteAnalysisRequest, SiteAnalysisResponse

router = APIRouter()

@router.post("/analyze", response_model=SiteAnalysisResponse)
def analyze_site_suitability(request: SiteAnalysisRequest, db: Session = Depends(get_db)):
    """
    Run site suitability analysis combining 5 datasets.
    Requires authenticated user (mocked for now).
    """
    # TODO: Fetch data from NASA POWER, GWA, SRTM, Sentinel, OSM
    # TODO: Calculate sub-scores and composite score, save to DB, return result
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("/history", response_model=List[SiteAnalysisResponse])
def get_site_history(db: Session = Depends(get_db)):
    """Get the authenticated user's site analysis history."""
    # TODO: Fetch analyses for current user from DB
    raise HTTPException(status_code=501, detail="Not implemented yet")
