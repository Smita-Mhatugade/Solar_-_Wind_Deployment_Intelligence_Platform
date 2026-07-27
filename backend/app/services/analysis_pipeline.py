from app.services.feature_engineering.feature_builder import FeatureBuilder
from app.evaluation.evaluator import run_evaluation
from app.services.deployment_strategy import recommend_deployment

class AnalysisPipeline:
    """
    A unified service that executes the complete analysis workflow for a given site.
    """
    
    def __init__(self):
        self.feature_builder = FeatureBuilder()
        
    def execute_pipeline(self, latitude: float, longitude: float, site_name: str = None) -> dict:
        """
        Executes the full pipeline:
        1. Retrieve features
        2. Evaluate the site (score and constraints)
        3. Determine deployment recommendation
        4. Return consolidated response
        """
        
        # 1. Retrieve all features
        features = self.feature_builder.build_features(latitude, longitude)
        
        # Ensure 'wind_speed_ms' is present for the evaluator (use 50m as standard hub height)
        if "wind_speed_50m_ms" in features and features["wind_speed_50m_ms"] is not None:
            features["wind_speed_ms"] = features["wind_speed_50m_ms"]
        else:
            features["wind_speed_ms"] = 0.0

        # Also provide defaults if data sources fail
        if features.get("solar_irradiance_kwh") is None:
            features["solar_irradiance_kwh"] = 0.0
            
        if features.get("slope_deg") is None:
            features["slope_deg"] = 0.0
            
        if features.get("dist_grid_km") is None:
            features["dist_grid_km"] = 0.0
            
        if features.get("dist_road_km") is None:
            features["dist_road_km"] = 0.0

        # 2. Evaluate the site
        evaluation_result = run_evaluation(features)
        
        # 3. Generate deployment recommendation
        deployment_rec = recommend_deployment(
            solar_irradiance=features["solar_irradiance_kwh"],
            wind_speed=features["wind_speed_ms"]
        )
        
        # 4. Consolidate response
        return {
            "site_name": site_name,
            "latitude": latitude,
            "longitude": longitude,
            "features": features,
            "evaluation": {
                "overall_score": evaluation_result["overall_score"],
                "criteria_evaluation": evaluation_result["criteria_evaluation"],
                "constraints": evaluation_result["constraints"],
                "failed_constraints": evaluation_result["failed_constraints"]
            },
            "deployment": {
                "recommended_technology": deployment_rec["deployment"],
                "confidence": deployment_rec["confidence"],
                "reason": deployment_rec["reason"],
                "solar_class": deployment_rec["solar_class"],
                "wind_class": deployment_rec["wind_class"]
            }
        }
