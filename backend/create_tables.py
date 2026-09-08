"""
create_tables.py - Directly creates all database tables using SQLAlchemy create_all().
Run this from the backend/ directory with the venv active.
"""
import sys
import os

# Add backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.config import settings
from app.database.database import engine, Base

# Import ALL models so their table definitions are registered on Base.metadata
import app.models  # noqa

print(f"Connecting to: {settings.DATABASE_URL}")
print("Creating tables...")

try:
    Base.metadata.create_all(bind=engine)
    tables = list(Base.metadata.tables.keys())
    print(f"\n✅ Successfully created {len(tables)} tables:")
    for t in sorted(tables):
        print(f"   - {t}")
    print("\nDatabase is ready!")
except Exception as e:
    print(f"\n❌ Error: {e}")
    sys.exit(1)
