from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint – confirms the API is running."""
    return {
        "message": "Welcome to the Solar & Wind Deployment Intelligence Platform API",
        "version": "1.0.0",
        "docs": "/docs",
    }
