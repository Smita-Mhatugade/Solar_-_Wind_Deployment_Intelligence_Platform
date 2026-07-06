"""
app/models/user.py – SQLAlchemy ORM model for the Users table.

SQL Concept: PRIMARY KEY & UNIQUE constraints
  - id (PK): Every user gets a unique integer ID automatically assigned
    by the database. No two rows can have the same id.
  - email (UNIQUE): Enforces that no two users can register with the
    same email address — enforced at the database level, not just application level.

Table: users
  id            SERIAL PRIMARY KEY
  email         VARCHAR(255) UNIQUE NOT NULL
  password_hash VARCHAR(255) NOT NULL
  full_name     VARCHAR(255)
  role          VARCHAR(50) DEFAULT 'user'
  is_active     BOOLEAN DEFAULT TRUE
  created_at    TIMESTAMP DEFAULT NOW()
  updated_at    TIMESTAMP

Day 5 – Infosys Virtual Internship | 5 July 2026
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from app.database.connection import Base


class User(Base):
    """
    ORM model mapped to the 'users' table in PostgreSQL.

    Relationships:
      - solar_predictions → one user can have many solar predictions (1:N)
      - wind_predictions  → one user can have many wind predictions  (1:N)
      - site_analyses     → one user can have many site analyses     (1:N)
      - reports           → one user can have many reports           (1:N)
    """

    __tablename__ = "users"

    # ── Primary Key ───────────────────────────────────────────────────────
    # SERIAL = auto-incrementing integer. Database assigns the next ID.
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # ── Core Fields ───────────────────────────────────────────────────────
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)

    # ── Role & Status ─────────────────────────────────────────────────────
    # role: 'admin' | 'analyst' | 'user'
    role = Column(String(50), default="user", nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # ── Timestamps ────────────────────────────────────────────────────────
    # server_default=func.now() → PostgreSQL sets the timestamp automatically
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # ── Relationships ─────────────────────────────────────────────────────
    # back_populates creates a two-way link: user.solar_predictions ↔ prediction.user
    solar_predictions = relationship("SolarPrediction", back_populates="user", cascade="all, delete-orphan")
    wind_predictions = relationship("WindPrediction", back_populates="user", cascade="all, delete-orphan")
    site_analyses = relationship("SiteAnalysis", back_populates="user", cascade="all, delete-orphan")
    reports = relationship("Report", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email} role={self.role}>"
