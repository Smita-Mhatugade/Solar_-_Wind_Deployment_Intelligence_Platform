"""
app/models/project.py – SQLAlchemy ORM model for the Projects table.

Table: projects
  id            SERIAL PRIMARY KEY
  project_name  VARCHAR NOT NULL
  description   TEXT
  state         VARCHAR NOT NULL
  latitude      FLOAT NOT NULL
  longitude     FLOAT NOT NULL
  created_at    TIMESTAMP DEFAULT NOW()

Day 6 – Infosys Virtual Internship | 10 July 2026
"""

from sqlalchemy import Column, Integer, String, Float, Text, DateTime, func
from app.database.database import Base


class Project(Base):
    """
    ORM model mapped to the 'projects' table in PostgreSQL.

    Fields:
      - id           : Auto-incrementing primary key
      - project_name : Name of the solar/wind project (required)
      - description  : Optional description of the project
      - state        : Indian state where the project is located (required)
      - latitude     : Geographic latitude (-90 to 90)
      - longitude    : Geographic longitude (-180 to 180)
      - created_at   : Timestamp auto-set by PostgreSQL on insert
    """

    __tablename__ = "projects"

    # ── Primary Key ───────────────────────────────────────────────────────
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # ── Core Fields ───────────────────────────────────────────────────────
    project_name = Column(String(255), nullable=False, index=True)
    description  = Column(Text, nullable=True)
    state        = Column(String(100), nullable=False)

    # ── Geographic Coordinates ────────────────────────────────────────────
    latitude  = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # ── Timestamp ─────────────────────────────────────────────────────────
    # server_default=func.now() → PostgreSQL assigns the timestamp automatically
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"<Project id={self.id} name={self.project_name} state={self.state}>"
