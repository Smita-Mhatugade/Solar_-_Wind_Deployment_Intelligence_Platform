"""
Solar & Wind Deployment Intelligence Platform – Backend Entry Point
===================================================================
Run with:
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# ── Application Factory ──────────────────────────────────────────────────────

app = FastAPI(
    title="Solar & Wind Deployment Intelligence Platform API",
    description=(
        "AI-powered platform for predicting solar/wind energy potential "
        "and assessing renewable energy deployment sites."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS Middleware ──────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Database Initialization ──────────────────────────────────────────────────
from app.database.connection import engine, Base
from app.models.project import Project

# Create all tables in the database (this includes the new Project model)
Base.metadata.create_all(bind=engine)

# ── Root Endpoints ───────────────────────────────────────────────────────────


@app.get("/ping", tags=["Health"])
def ping():
    """Health check endpoint."""
    return {"status": "ok", "service": "solar-wind-api"}


@app.get("/health", tags=["Health"])
def health():
    """Returns the current health status of the application."""
    return {"status": "Running"}


@app.get("/about", tags=["Info"])
def about():
    """Returns information about the project."""
    return {"project": "Solar & Wind Deployment Intelligence Platform"}


# ── Register API routers ─────────────────────────────────────────────────────
from app.api import home, projects, sites, predictions
# from app.api import solar, wind, site, auth, reports

app.include_router(home.router)
app.include_router(projects.router)
app.include_router(sites.router)
app.include_router(predictions.router)

# app.include_router(auth.router,   prefix="/api/v1/auth",    tags=["Auth"])
# app.include_router(solar.router,  prefix="/api/v1/solar",   tags=["Solar"])
# app.include_router(wind.router,   prefix="/api/v1/wind",    tags=["Wind"])
# app.include_router(site.router,   prefix="/api/v1/site",    tags=["Site"])
# app.include_router(reports.router,prefix="/api/v1/reports", tags=["Reports"])
