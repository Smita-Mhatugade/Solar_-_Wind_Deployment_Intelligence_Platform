from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from app.database import get_db
from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.services.analysis_pipeline import AnalysisPipeline

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=AnalysisResponse)
def analyze_site_workflow(
    request: AnalysisRequest,
    db: Session = Depends(get_db),
):
    """
    Executes the complete site suitability analysis pipeline.
    This unified endpoint accepts coordinates, retrieves all relevant features (solar, wind, terrain),
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
        return result
    except ValueError as e:
        logger.error(f"Validation error in analysis pipeline: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in analysis pipeline: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the analysis.")
