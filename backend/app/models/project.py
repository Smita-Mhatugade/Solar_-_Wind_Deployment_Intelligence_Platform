"""
app/models/project.py – SQLAlchemy ORM model for the Projects table.

Table: projects
  id            SERIAL PRIMARY KEY
  user_id       INTEGER FK → users.id (project owner)
  project_name  VARCHAR NOT NULL
  description   TEXT
  state         VARCHAR NOT NULL
  latitude      FLOAT NOT NULL
  longitude     FLOAT NOT NULL
  created_at    TIMESTAMP DEFAULT NOW()

Day 6 – Infosys Virtual Internship | 10 July 2026
"""

from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database.database import Base


class Project(Base):
    """
    ORM model mapped to the 'projects' table in PostgreSQL.

    Each project is owned by a user (user_id FK). A user can have many
    projects (1:N relationship). Projects store the geographic location
    and description of a solar/wind deployment site.
    """

    __tablename__ = "projects"

    # ── Primary Key ───────────────────────────────────────────────────
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # ── Foreign Key → users.id ────────────────────────────────────────
    # ondelete="CASCADE": if the user is deleted, their projects are too
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # ── Core Fields ───────────────────────────────────────────────────
    project_name = Column(String(255), nullable=False, index=True)
    description  = Column(Text, nullable=True)
    state        = Column(String(100), nullable=False)

    # ── Geographic Coordinates ────────────────────────────────────────
    latitude  = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # ── Timestamp ─────────────────────────────────────────────────────
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # ── Relationship back to User ─────────────────────────────────────
    user = relationship("User", back_populates="projects")

    def __repr__(self) -> str:
        return f"<Project id={self.id} name={self.project_name} owner={self.user_id}>"
