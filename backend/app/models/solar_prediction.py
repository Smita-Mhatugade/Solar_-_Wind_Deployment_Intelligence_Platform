"""
app/models/solar_prediction.py – SQLAlchemy ORM model for solar predictions.

SQL Concept: FOREIGN KEY relationship
  - user_id (FK): Links every prediction to the user who requested it.
    If a user is deleted → their predictions are deleted too (CASCADE).
  - Referential Integrity: The DB guarantees user_id always points to a
    valid user — you cannot insert a prediction with a non-existent user_id.

Table: solar_predictions
  id                   SERIAL PRIMARY KEY
  user_id              INTEGER FK → users.id
  city_name            VARCHAR(100)
  latitude             FLOAT NOT NULL
  longitude            FLOAT NOT NULL
  input_year           INTEGER
  solar_irradiance_kwh FLOAT           -- Input feature: annual kWh/m²
  clearness_index      FLOAT           -- Input feature: cloud clearness ratio
  temp_mean_c          FLOAT           -- Input feature: mean temperature
  predicted_output_kwh FLOAT           -- Model output: predicted yield
  panel_efficiency_pct FLOAT           -- Panel efficiency used
  system_capacity_kw   FLOAT           -- System size in kilowatts
  annual_generation_kwh FLOAT          -- Total predicted annual generation
  confidence_score     FLOAT           -- Model confidence (0–1)
  model_version        VARCHAR(50)     -- ML model version used
  status               VARCHAR(50)     -- pending | completed | failed
  created_at           TIMESTAMP DEFAULT NOW()

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database.connection import Base


class SolarPrediction(Base):
    """
    ORM model mapped to the 'solar_predictions' table.

    Stores all inputs used for the solar prediction and the ML model output.
    Each record is linked to the requesting user via user_id (Foreign Key).
    """

    __tablename__ = "solar_predictions"

    # ── Primary Key ───────────────────────────────────────────────────────
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # ── Foreign Key → users.id ────────────────────────────────────────────
    # ondelete="CASCADE": if the user is deleted, their predictions are too
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ── Location Info ─────────────────────────────────────────────────────
    city_name = Column(String(100), nullable=True)       # e.g. "Abu Dhabi"
    latitude = Column(Float, nullable=False)             # e.g. 24.47
    longitude = Column(Float, nullable=False)            # e.g. 54.37
    input_year = Column(Integer, nullable=True)          # e.g. 2024

    # ── Input Features (from NASA POWER dataset) ──────────────────────────
    solar_irradiance_kwh = Column(Float, nullable=True)  # annual kWh/m²
    clearness_index = Column(Float, nullable=True)       # 0–1 solar clearness
    temp_mean_c = Column(Float, nullable=True)           # mean temperature °C
    humidity_pct = Column(Float, nullable=True)          # relative humidity %
    days_above_35c = Column(Integer, nullable=True)      # extreme heat days

    # ── Prediction Outputs ────────────────────────────────────────────────
    predicted_output_kwh = Column(Float, nullable=True)  # predicted daily kWh/m²
    annual_generation_kwh = Column(Float, nullable=True) # total annual generation
    panel_efficiency_pct = Column(Float, default=20.0)   # standard panel: 20%
    system_capacity_kw = Column(Float, nullable=True)    # system size kW
    capacity_factor = Column(Float, nullable=True)        # 0–1 efficiency ratio

    # ── Model Metadata ────────────────────────────────────────────────────
    confidence_score = Column(Float, nullable=True)      # model confidence 0–1
    model_version = Column(String(50), default="v1.0")
    status = Column(String(50), default="completed")     # completed | failed

    # ── Timestamps ────────────────────────────────────────────────────────
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # ── Relationship back to User ─────────────────────────────────────────
    user = relationship("User", back_populates="solar_predictions")

    def __repr__(self) -> str:
        return (
            f"<SolarPrediction id={self.id} city={self.city_name} "
            f"output={self.predicted_output_kwh} kWh/m²>"
        )
