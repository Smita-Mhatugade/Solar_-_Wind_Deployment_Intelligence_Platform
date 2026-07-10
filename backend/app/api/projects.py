"""
app/api/projects.py – Project Management API endpoints.

Endpoints:
  GET  /projects  → Returns all projects stored in PostgreSQL
  POST /projects  → Creates a new project after validating request data

Validation is handled automatically by Pydantic (ProjectCreate schema).
Invalid requests (empty name, bad lat/lon, missing fields) return HTTP 422.

Day 6 – Infosys Virtual Internship | 10 July 2026
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectResponse

router = APIRouter()


# ── GET /projects ─────────────────────────────────────────────────────────────
@router.get(
    "",
    response_model=List[ProjectResponse],
    summary="List all projects",
    description="Retrieves all solar/wind deployment projects stored in the database.",
    tags=["Projects"],
)
def get_projects(db: Session = Depends(get_db)):
    """
    Returns every project row from the PostgreSQL 'projects' table.

    - Uses SQLAlchemy ORM query: db.query(Project).all()
    - Pydantic (ProjectResponse) serialises each ORM object into JSON
    - Projects created via POST /projects appear here immediately
    """
    projects = db.query(Project).all()
    return projects


# ── POST /projects ────────────────────────────────────────────────────────────
@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new project",
    description=(
        "Creates a new solar/wind deployment project in PostgreSQL. "
        "All required fields are validated before insertion. "
        "Invalid data (empty name, out-of-range coordinates) is rejected with HTTP 422."
    ),
    tags=["Projects"],
)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    """
    Accepts a JSON body, validates it via Pydantic, then inserts into PostgreSQL.

    Steps:
      1. Pydantic deserialises + validates the incoming JSON (ProjectCreate schema)
      2. A new Project ORM object is constructed from validated data
      3. db.add() stages the insert
      4. db.commit() writes to PostgreSQL
      5. db.refresh() reloads the row (so created_at and id are populated)
      6. The saved project is returned as ProjectResponse JSON

    Validation errors (HTTP 422) are raised automatically by FastAPI/Pydantic for:
      - Missing required fields (project_name, state, latitude, longitude)
      - Empty or whitespace-only project_name / state
      - latitude outside [-90, 90]
      - longitude outside [-180, 180]
    """
    new_project = Project(
        project_name=payload.project_name,
        description=payload.description,
        state=payload.state,
        latitude=payload.latitude,
        longitude=payload.longitude,
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)   # reload to get DB-generated id + created_at

    return new_project
