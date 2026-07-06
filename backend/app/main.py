"""
app/main.py – FastAPI Application Entrypoint.

This is the main application file that:
  1. Initializes the FastAPI app
  2. Sets up CORS (Cross-Origin Resource Sharing)
  3. Tests the database connection on startup
  4. Includes all the API routers from the app.api package

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.database import test_db_connection, engine, Base
from app.api import (
    auth_router,
    solar_router,
    wind_router,
    site_router,
    reports_router,
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan events: Code to run before the app starts accepting requests,
    and code to run after it stops.
    """
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    
    # Test DB Connection
    db_ok = test_db_connection()
    if not db_ok:
        logger.warning("Database is not reachable. App is starting, but DB endpoints will fail.")
    else:
        # For development only: Auto-create tables (in production use Alembic migrations)
        # Base.metadata.create_all(bind=engine)
        logger.info("Database connection verified.")
    
    yield  # App runs here
    
    logger.info("Shutting down application...")


# Initialize FastAPI Application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API for predicting solar/wind energy output and analyzing site suitability.",
    lifespan=lifespan,
)

# Configure CORS (Allows frontend on localhost:3000 to call backend on localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc)
    allow_headers=["*"],  # Allow all headers
)

# ── Include API Routers ───────────────────────────────────────────────────────
api_prefix = settings.API_V1_STR

app.include_router(auth_router, prefix=f"{api_prefix}/auth", tags=["Authentication"])
app.include_router(solar_router, prefix=f"{api_prefix}/solar", tags=["Solar Prediction"])
app.include_router(wind_router, prefix=f"{api_prefix}/wind", tags=["Wind Prediction"])
app.include_router(site_router, prefix=f"{api_prefix}/site", tags=["Site Suitability Analysis"])
app.include_router(reports_router, prefix=f"{api_prefix}/reports", tags=["Report Generation"])


# ── Root Endpoint ─────────────────────────────────────────────────────────────
@app.get("/", tags=["Health Check"])
def read_root():
    """Health check endpoint to verify API is running."""
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "online",
        "message": "Welcome to the Solar & Wind Deployment Intelligence API. Visit /docs for the interactive API documentation."
    }
