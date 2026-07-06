"""
app/models/wind_prediction.py – SQLAlchemy ORM model for wind predictions.

SQL Concept: FOREIGN KEY + INDEX
  - user_id (FK): Every wind prediction belongs to a user.
  - index=True on user_id and latitude/longitude: Creates a B-Tree index
    so queries like "get all predictions for user 5" or "find predictions
    near latitude 24.47" are fast (O(log n) instead of O(n) full table scan).

Table: wind_predictions
  id                    SERIAL PRIMARY KEY
  user_id               INTEGER FK → users.id
  city_name             VARCHAR(100)
  latitude              FLOAT NOT NULL
  longitude             FLOAT NOT NULL
  wind_speed_10m_ms     FLOAT           -- Station-level wind (10m AGL)
  wind_speed_50m_ms     FLOAT           -- Hub-height proxy (GWA data)
  wind_power_density    FLOAT           -- W/m² at site
  wind_consistency      FLOAT           -- mean/std deviation ratio
  elevation_m           FLOAT           -- Site elevation in metres
  turbine_capacity_kw   FLOAT           -- Turbine rated capacity
  predicted_output_kwh  FLOAT           -- Annual energy output prediction
  capacity_factor       FLOAT           -- Turbine capacity factor 0–1
  wind_class            INTEGER         -- NREL wind class 1–7
  confidence_score      FLOAT
  model_version         VARCHAR(50)
  status                VARCHAR(50)
  created_at            TIMESTAMP DEFAULT NOW()

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database.connection import Base


class WindPrediction(Base):
    """
    ORM model mapped to the 'wind_predictions' table.

    Wind turbine energy output is primarily driven by wind speed at hub height
    (50m–150m AGL). The model stores both station-level (10m) and hub-height
    (50m from Global Wind Atlas) wind speeds for comparison.
    """

    __tablename__ = "wind_predictions"

    # ── Primary Key ───────────────────────────────────────────────────────
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # ── Foreign Key → users.id ────────────────────────────────────────────
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ── Location Info ─────────────────────────────────────────────────────
    city_name = Column(String(100), nullable=True)
    latitude = Column(Float, nullable=False, index=True)
    longitude = Column(Float, nullable=False, index=True)
    input_year = Column(Integer, nullable=True)

    # ── Input Features (NASA POWER + Global Wind Atlas) ───────────────────
    wind_speed_10m_ms = Column(Float, nullable=True)    # m/s at 10m AGL (NASA POWER)
    wind_speed_50m_ms = Column(Float, nullable=True)    # m/s at 50m AGL (GWA)
    wind_speed_100m_ms = Column(Float, nullable=True)   # m/s at 100m AGL (GWA)
    wind_power_density = Column(Float, nullable=True)   # W/m²
    wind_consistency = Column(Float, nullable=True)     # mean/std ratio
    high_wind_days = Column(Integer, nullable=True)     # days with high wind

    # ── Site Characteristics ──────────────────────────────────────────────
    elevation_m = Column(Float, nullable=True)          # from SRTM dataset
    roughness_length = Column(Float, default=0.03)      # terrain roughness

    # ── Turbine Configuration ─────────────────────────────────────────────
    turbine_capacity_kw = Column(Float, default=2000.0) # 2 MW standard turbine
    hub_height_m = Column(Float, default=100.0)         # 100m hub height

    # ── Prediction Outputs ────────────────────────────────────────────────
    predicted_output_kwh = Column(Float, nullable=True)  # annual kWh per turbine
    capacity_factor = Column(Float, nullable=True)        # 0–1 (>0.35 is good)
    wind_class = Column(Integer, nullable=True)           # NREL 1–7 (7=best)

    # ── Model Metadata ────────────────────────────────────────────────────
    confidence_score = Column(Float, nullable=True)
    model_version = Column(String(50), default="v1.0")
    status = Column(String(50), default="completed")

    # ── Timestamps ────────────────────────────────────────────────────────
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # ── Relationship back to User ─────────────────────────────────────────
    user = relationship("User", back_populates="wind_predictions")

    def __repr__(self) -> str:
        return (
            f"<WindPrediction id={self.id} city={self.city_name} "
            f"wind_50m={self.wind_speed_50m_ms} m/s class={self.wind_class}>"
        )
