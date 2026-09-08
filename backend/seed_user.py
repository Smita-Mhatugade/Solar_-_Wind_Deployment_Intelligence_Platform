import sys
import os

# Add backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import User
from app.auth.security import get_password_hash

def seed_user():
    db = SessionLocal()
    email = "user@gmail.com"
    existing = db.query(User).filter(User.email == email).first()
    
    if not existing:
        user = User(
            email=email,
            full_name="Test User",
            password_hash=get_password_hash("123456"),
            role="admin"
        )
        db.add(user)
        db.commit()
        print(f"User {email} created successfully with password '123456'.")
    else:
        existing.password_hash = get_password_hash("123456")
        db.commit()
        print(f"User {email} already exists. Password updated to '123456'.")
    
    db.close()

if __name__ == "__main__":
    seed_user()
