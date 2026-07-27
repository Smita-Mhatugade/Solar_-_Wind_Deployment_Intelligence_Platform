from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict, Any, List

class AnalysisRequest(BaseModel):
    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)
    site_name: Optional[str] = Field(None, max_length=200)

class DeploymentRecommendation(BaseModel):
    recommended_technology: str
    confidence: int
    reason: str
    solar_class: str
    wind_class: str

class CriteriaEvaluationItem(BaseModel):
    value: float
    status: str

class CriteriaEvaluation(BaseModel):
    solar_irradiance: CriteriaEvaluationItem
    wind_speed: CriteriaEvaluationItem
    slope: CriteriaEvaluationItem
    distance_to_grid: CriteriaEvaluationItem
    distance_to_road: CriteriaEvaluationItem

class EvaluationSummary(BaseModel):
    overall_score: float
    criteria_evaluation: CriteriaEvaluation
    constraints: Dict[str, bool]
    failed_constraints: List[str]

class AnalysisResponse(BaseModel):
    site_name: Optional[str]
    latitude: float
    longitude: float
    features: Dict[str, Any]
    evaluation: EvaluationSummary
    deployment: DeploymentRecommendation

    model_config = ConfigDict(from_attributes=True)
