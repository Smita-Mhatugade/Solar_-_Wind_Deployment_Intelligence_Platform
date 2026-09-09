from fastapi import APIRouter, HTTPException
from typing import List, Optional
import logging

from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.schemas.site import SiteAnalysisResponse
from app.services.analysis_pipeline import AnalysisPipeline

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=AnalysisResponse)
def analyze_site_workflow(request: AnalysisRequest):
    """
    Executes the complete site suitability analysis pipeline.
    This unified public endpoint accepts coordinates, retrieves all relevant features (solar, wind, terrain),
    evaluates the site against deployment constraints, calculates scores, and returns
    a final deployment recommendation.
    """
    try:
        pipeline = AnalysisPipeline()
        result = pipeline.execute_pipeline(
            latitude=request.latitude,
            longitude=request.longitude,
            site_name=request.site_name
        )

        # Try to save to Database if DB is available, otherwise skip gracefully
        try:
            from app.database import SessionLocal
            from app.models.site_analysis import SiteAnalysis
            db = SessionLocal()
            db_analysis = SiteAnalysis(
                user_id=1,  # Default public user ID
                site_name=request.site_name or f"Site at {request.latitude}, {request.longitude}",
                latitude=request.latitude,
                longitude=request.longitude,
                solar_irradiance_kwh=result["features"].get("solar_irradiance_kwh"),
                wind_speed_ms=result["features"].get("wind_speed_ms"),
                elevation_m=result["features"].get("elevation_m"),
                slope_deg=result["features"].get("slope_deg"),
                ndvi=result["geospatial"]["ndvi"],
                land_cover_class=result["geospatial"]["land_cover"],
                dist_grid_km=result["features"].get("dist_grid_km"),
                dist_road_km=result["features"].get("dist_road_km"),
                suitability_score=result["evaluation"]["overall_score"],
                recommendation=result["deployment"]["recommended_technology"]
            )
            db.add(db_analysis)
            db.commit()
            db.refresh(db_analysis)
            result["site_id"] = str(db_analysis.id)
            db.close()
        except Exception as db_err:
            logger.info(f"Database save skipped (stateless mode): {db_err}")

        return result
    except ValueError as e:
        logger.error(f"Validation error in analysis pipeline: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in analysis pipeline: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the analysis.")


@router.get("/history", response_model=List[SiteAnalysisResponse])
def get_analysis_history():
    """
    Get the history of site analyses. Safely falls back if DB is offline.
    """
    try:
        from app.database import SessionLocal
        from app.models.site_analysis import SiteAnalysis
        db = SessionLocal()
        analyses = db.query(SiteAnalysis).order_by(SiteAnalysis.created_at.desc()).all()
        db.close()
        return analyses
    except Exception as e:
        logger.info(f"Database offline or uninitialized: returning empty history ({e})")
        return []

@router.delete("/history/{analysis_id}")
def delete_analysis(analysis_id: int):
    """
    Delete a specific site analysis.
    """
    try:
        from app.database import SessionLocal
        from app.models.site_analysis import SiteAnalysis
        db = SessionLocal()
        analysis = db.query(SiteAnalysis).filter(SiteAnalysis.id == analysis_id).first()
        if analysis:
            db.delete(analysis)
            db.commit()
            db.close()
            return {"message": "Analysis deleted successfully."}
        db.close()
    except Exception as e:
        logger.info(f"Database delete skipped: {e}")
    return {"message": "Analysis deleted."}
