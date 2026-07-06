"""
app/models/site_analysis.py – SQLAlchemy ORM model for site suitability analysis.

SQL Concept: COMPOSITE SCORE & NORMALISED DATA
  - This table stores results of the multi-factor site suitability algorithm.
  - The suitability_score (0–100) is a weighted composite of 5 sub-scores:
      Solar score (30%) + Wind score (25%) + Terrain score (20%)
      + Land use score (15%) + Infrastructure score (10%)
  - Storing sub-scores separately allows analysts to understand WHY a site
    scored high or low — important for stakeholder reporting.

Table: site_analyses
  id                    SERIAL PRIMARY KEY
  user_id               INTEGER FK → users.id
  site_name             VARCHAR(200)
  latitude              FLOAT NOT NULL
  longitude             FLOAT NOT NULL
  -- Input Features from all 5 datasets --
  solar_irradiance_kwh  FLOAT    -- from NASA POWER
  wind_speed_50m_ms     FLOAT    -- from Global Wind Atlas
  elevation_m           FLOAT    -- from SRTM
  slope_deg             FLOAT    -- from SRTM
  ndvi                  FLOAT    -- from Sentinel-2
  land_cover_class      VARCHAR  -- from Sentinel-2
  dist_grid_km          FLOAT    -- from OpenStreetMap
  dist_road_km          FLOAT    -- from OpenStreetMap
  -- Composite Scores --
  solar_score           FLOAT    -- 0–100
  wind_score            FLOAT    -- 0–100
  terrain_score         FLOAT    -- 0–100
  land_use_score        FLOAT    -- 0–100
  infrastructure_score  FLOAT    -- 0–100
  suitability_score     FLOAT    -- 0–100 weighted composite
  recommendation        VARCHAR  -- "Highly Suitable" | "Suitable" | "Marginal" | "Unsuitable"
  created_at            TIMESTAMP DEFAULT NOW()

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, func
from sqlalchemy.orm import relationship
from app.database.connection import Base


class SiteAnalysis(Base):
    """
    ORM model mapped to the 'site_analyses' table.

    Integrates data from all five datasets to produce a 0–100 suitability score.
    Both raw input values and computed sub-scores are stored for full traceability.
    """

    __tablename__ = "site_analyses"

    # ── Primary Key ───────────────────────────────────────────────────────
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # ── Foreign Key → users.id ────────────────────────────────────────────
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ── Site Identification ───────────────────────────────────────────────
    site_name = Column(String(200), nullable=True)      # user-given name
    city_name = Column(String(100), nullable=True)       # nearest city
    latitude = Column(Float, nullable=False, index=True)
    longitude = Column(Float, nullable=False, index=True)
    country = Column(String(100), nullable=True)
    continent = Column(String(100), nullable=True)

    # ── NASA POWER Features ───────────────────────────────────────────────
    solar_irradiance_kwh = Column(Float, nullable=True)  # annual kWh/m²
    clearness_index = Column(Float, nullable=True)        # 0–1
    wind_speed_ms = Column(Float, nullable=True)          # m/s at 10m
    temp_mean_c = Column(Float, nullable=True)
    precip_total_mm = Column(Float, nullable=True)

    # ── Global Wind Atlas Features ────────────────────────────────────────
    wind_speed_50m_ms = Column(Float, nullable=True)     # m/s at 50m AGL
    wind_speed_100m_ms = Column(Float, nullable=True)    # m/s at 100m AGL

    # ── SRTM Features ─────────────────────────────────────────────────────
    elevation_m = Column(Float, nullable=True)           # metres above sea level
    slope_deg = Column(Float, nullable=True)             # terrain slope angle

    # ── Sentinel-2 Features ───────────────────────────────────────────────
    ndvi = Column(Float, nullable=True)                  # vegetation index -1 to 1
    ndwi = Column(Float, nullable=True)                  # water index
    land_cover_class = Column(String(100), nullable=True) # e.g. "Barren / Desert"

    # ── OpenStreetMap Features ────────────────────────────────────────────
    dist_grid_km = Column(Float, nullable=True)          # km to nearest grid
    dist_road_km = Column(Float, nullable=True)          # km to nearest road

    # ── Sub-Scores (0–100) ────────────────────────────────────────────────
    solar_score = Column(Float, nullable=True)           # weight: 30%
    wind_score = Column(Float, nullable=True)            # weight: 25%
    terrain_score = Column(Float, nullable=True)         # weight: 20%
    land_use_score = Column(Float, nullable=True)        # weight: 15%
    infrastructure_score = Column(Float, nullable=True)  # weight: 10%

    # ── Final Composite Score ─────────────────────────────────────────────
    suitability_score = Column(Float, nullable=True)     # 0–100 weighted composite
    recommendation = Column(String(50), nullable=True)   # text label

    # ── Analysis Notes ────────────────────────────────────────────────────
    notes = Column(Text, nullable=True)                  # analyst comments

    # ── Model Metadata ────────────────────────────────────────────────────
    model_version = Column(String(50), default="v1.0")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # ── Relationship back to User ─────────────────────────────────────────
    user = relationship("User", back_populates="site_analyses")

    @property
    def recommendation_label(self) -> str:
        """Derive recommendation text from composite score."""
        if self.suitability_score is None:
            return "Unknown"
        if self.suitability_score >= 75:
            return "Highly Suitable"
        elif self.suitability_score >= 55:
            return "Suitable"
        elif self.suitability_score >= 35:
            return "Marginal"
        else:
            return "Unsuitable"

    def __repr__(self) -> str:
        return (
            f"<SiteAnalysis id={self.id} site={self.site_name} "
            f"score={self.suitability_score} ({self.recommendation})>"
        )
