"""
app/api/auth.py – Authentication and User endpoints.

Day 5 & 6 – Infosys Virtual Internship
"""

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import UserCreate, UserLogin, UserResponse
from app.models import User
from app.auth.security import get_password_hash, verify_password, create_access_token
from app.auth.dependencies import get_current_user
from app.config import settings

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    # Check if user already exists
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
        
    # Hash password and create user object
    hashed_password = get_password_hash(user_in.password)
    db_user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        password_hash=hashed_password,
    )
    
    # Save to database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


@router.post("/login")
def login_user(
    db: Session = Depends(get_db),
    # Use OAuth2PasswordRequestForm to support standard form-data login (good for swagger)
    # Alternatively, you can use JSON body like: user_in: UserLogin
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """Authenticate a user and return a JWT token."""
    # 1. Fetch user by email (form_data.username is used for email here due to OAuth2 spec)
    user = db.query(User).filter(User.email == form_data.username).first()
    
    # 2. Verify existence and password
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # 3. Create JWT Token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, 
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "email": user.email,
        "role": user.role
    }


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Get the currently authenticated user.
    Requires a valid JWT Bearer token in the Authorization header.
    """
    return current_user
