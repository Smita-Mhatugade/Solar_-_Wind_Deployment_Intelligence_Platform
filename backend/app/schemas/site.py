"""
app/schemas/site.py – Pydantic schemas for Site Suitability validation.

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class SiteAnalysisRequest(BaseModel):
    site_name: str = Field(..., min_length=1, max_length=200)
    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)


class SiteAnalysisResponse(BaseModel):
    id: int
    user_id: int
    site_name: Optional[str]
    latitude: float
    longitude: float
    
    # Inputs
    solar_irradiance_kwh: Optional[float]
    wind_speed_50m_ms: Optional[float]
    elevation_m: Optional[float]
    slope_deg: Optional[float]
    ndvi: Optional[float]
    dist_grid_km: Optional[float]
    
    # Sub-scores
    solar_score: Optional[float]
    wind_score: Optional[float]
    terrain_score: Optional[float]
    land_use_score: Optional[float]
    infrastructure_score: Optional[float]
    
    # Final
    suitability_score: Optional[float]
    recommendation: Optional[str]
    notes: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
