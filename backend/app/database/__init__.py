"""
app/database/__init__.py – Database package initialization.

Exposes the key database objects so other modules can import cleanly:
    from app.database import Base, get_db, engine

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from app.database.connection import Base, get_db, engine, SessionLocal, test_db_connection

__all__ = ["Base", "get_db", "engine", "SessionLocal", "test_db_connection"]
