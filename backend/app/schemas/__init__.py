"""
app/schemas/__init__.py – Pydantic input/output validation schemas.

Schemas define what data the API accepts (request body) and returns
(response body). They are separate from ORM models intentionally:
  - Models  → what the DATABASE looks like
  - Schemas → what the API contract looks like

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from app.schemas.user import UserCreate, UserLogin, UserResponse, UserBase
from app.schemas.solar import SolarPredictionRequest, SolarPredictionResponse
from app.schemas.wind import WindPredictionRequest, WindPredictionResponse
from app.schemas.site import SiteAnalysisRequest, SiteAnalysisResponse
from app.schemas.report import ReportRequest, ReportResponse

__all__ = [
    "UserCreate",
    "UserLogin",
    "UserResponse",
    "UserBase",
    "SolarPredictionRequest",
    "SolarPredictionResponse",
    "WindPredictionRequest",
    "WindPredictionResponse",
    "SiteAnalysisRequest",
    "SiteAnalysisResponse",
    "ReportRequest",
    "ReportResponse",
]
