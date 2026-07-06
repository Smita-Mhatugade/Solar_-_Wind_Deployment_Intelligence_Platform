"""
app/services – Business logic layer.

The services layer sits between the API routes and the database/ML models.
It keeps route handlers thin and business logic testable.

Services planned:
  - solar_service.py   → Load NASA POWER data, run solar ML model
  - wind_service.py    → Load GWA data, run wind ML model
  - site_service.py    → Combine all datasets for suitability scoring
  - report_service.py  → Generate PDF/Excel reports from prediction data
  - auth_service.py    → User management, password validation
"""
