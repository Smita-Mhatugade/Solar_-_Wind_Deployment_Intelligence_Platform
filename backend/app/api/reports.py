"""
app/api/reports.py – Report Generation endpoints.

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import ReportRequest, ReportResponse

router = APIRouter()

@router.post("/generate", response_model=ReportResponse, status_code=202)
def request_report_generation(request: ReportRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Request the generation of a PDF/Excel report.
    Because generation can be slow, this returns a 202 Accepted and processes in the background.
    """
    # TODO: Save report request to DB with status='generating'
    # TODO: Add actual generation function to background_tasks
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("/", response_model=List[ReportResponse])
def get_user_reports(db: Session = Depends(get_db)):
    """Get the authenticated user's generated reports."""
    # TODO: Fetch reports for current user from DB
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("/{report_id}/download")
def download_report(report_id: int, db: Session = Depends(get_db)):
    """Download a specific generated report file."""
    # TODO: Check report exists, verify user owns it, return FileResponse
    raise HTTPException(status_code=501, detail="Not implemented yet")
