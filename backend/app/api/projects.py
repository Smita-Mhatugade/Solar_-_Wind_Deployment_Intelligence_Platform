from fastapi import APIRouter

router = APIRouter()

@router.get("/projects", tags=["Projects"])
def get_projects():
    """Returns a list of demo projects."""
    return [
        {
            "id": 1,
            "project_name": "Demo Solar Project",
            "location": "Odisha"
        }
    ]
