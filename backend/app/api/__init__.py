"""
app/api/__init__.py – API route handlers.

Exports all the individual feature routers so they can be easily included
in the main FastAPI application (main.py).

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from app.api.auth import router as auth_router
from app.api.solar import router as solar_router
from app.api.wind import router as wind_router
from app.api.site import router as site_router
from app.api.reports import router as reports_router

__all__ = [
    "auth_router",
    "solar_router",
    "wind_router",
    "site_router",
    "reports_router",
]
