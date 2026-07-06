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

# ── Root Endpoints ───────────────────────────────────────────────────────────

@app.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint – confirms the API is running."""
    return {
        "message": "Welcome to the Solar & Wind Deployment Intelligence Platform API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/ping", tags=["Health"])
def ping():
    """Health check endpoint."""
    return {"status": "ok", "service": "solar-wind-api"}


# ── TODO: Register API routers below as modules are implemented ──────────────
# from app.api import solar, wind, site, auth, reports
# app.include_router(auth.router,   prefix="/api/v1/auth",    tags=["Auth"])
# app.include_router(solar.router,  prefix="/api/v1/solar",   tags=["Solar"])
# app.include_router(wind.router,   prefix="/api/v1/wind",    tags=["Wind"])
# app.include_router(site.router,   prefix="/api/v1/site",    tags=["Site"])
# app.include_router(reports.router,prefix="/api/v1/reports", tags=["Reports"])
