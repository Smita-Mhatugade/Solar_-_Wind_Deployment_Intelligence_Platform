# ☀️ Solar & Wind Deployment Intelligence Platform

> **Infosys Virtual Internship Project** | Week 1 – Project Architecture & Setup

A full-stack AI-powered platform to predict solar and wind energy potential, assess site suitability, and generate deployment reports using real-world geospatial and climate datasets.

---

## 📌 Project Overview

| Property | Details |
|---|---|
| **Platform** | Solar & Wind Deployment Intelligence |
| **Stack** | FastAPI (Backend) · React (Frontend) · PostgreSQL · Docker |
| **AI/ML** | Python · scikit-learn · Pandas · NumPy |
| **Datasets** | NASA POWER · Global Wind Atlas · Sentinel-2 · OSM · SRTM |

---

## 📁 Project Structure

```
solar-wind-deployment-intelligence/
│
├── backend/                  # FastAPI server-side code & APIs
│   ├── app/                  # Core application package
│   │   ├── api/              # API route handlers
│   │   ├── auth/             # Authentication (JWT)
│   │   ├── database/         # DB connection & session management
│   │   ├── models/           # SQLAlchemy ORM models
│   │   ├── schemas/          # Pydantic input/output schemas
│   │   ├── services/         # Business logic layer
│   │   └── utils/            # Helper functions & utilities
│   ├── tests/                # Unit & integration tests
│   ├── main.py               # Application entry point
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # Environment variables (not committed)
│
├── frontend/                 # React user interface
├── datasets/                 # Renewable energy datasets
│   ├── nasa_power/           # Solar irradiance & climate data
│   ├── global_wind_atlas/    # Wind speed & resource data
│   ├── sentinel/             # Satellite imagery (NDVI, NDWI)
│   ├── openstreetmap/        # Infrastructure data (roads, grid)
│   └── srtm/                 # Elevation & terrain data
│
├── docs/                     # Project documentation
│   ├── architecture/         # Architecture diagrams & decisions
│   ├── api_docs/             # API reference documentation
│   ├── database_design/      # DB schema & ER diagrams
│   └── weekly_notes/         # Daily/weekly session notes
│
├── notebooks/                # Jupyter notebooks for EDA & analysis
├── models/                   # Trained ML model files (.pkl, .joblib)
├── reports/                  # Generated PDF/Excel reports
├── docker/                   # Additional Docker config files
├── .gitignore
├── docker-compose.yml        # Multi-container Docker setup
├── README.md
└── requirements.txt          # Root-level dependencies
```

---

## 🗂️ Dataset Overview

| Dataset | Source | Purpose |
|---|---|---|
| **NASA POWER** | NASA | Solar irradiance, temperature, humidity for solar prediction |
| **Global Wind Atlas** | DTU/World Bank | Wind speed at 10m/50m/100m for wind prediction |
| **Sentinel-2** | ESA | Satellite imagery for land cover & NDVI analysis |
| **OpenStreetMap** | OSM | Roads, substations, power lines for infrastructure analysis |
| **SRTM** | NASA/USGS | Elevation & slope data for site suitability |

---

## 🔧 Project Modules

| Module | Input | Output |
|---|---|---|
| **Authentication** | User Login | Secure JWT Access |
| **Solar Prediction** | NASA POWER data | Solar energy output (kWh) |
| **Wind Prediction** | Global Wind Atlas | Wind energy output (kWh) |
| **Site Suitability** | NASA + Wind + SRTM + OSM | Suitability score (0–100) |
| **Reports** | Prediction data | PDF/Excel reports |
| **Dashboard** | All predictions | Interactive maps & graphs |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- Node.js 18+

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Database Setup
```bash
docker-compose up -d
```

### API Documentation
Once running, visit: http://localhost:8000/docs

---

## 📅 Internship Progress

| Day | Date | Topic |
|---|---|---|
| Day 1 | 30 June 2026 | Renewable Energy Basics |
| Day 2 | 1 July 2026 | Project Folder Structure & Dataset Analysis |
| Day 3 | 2 July 2026 | Project APIs, Backend & Architecture |

---

## 👩‍💻 Internship
**Infosys Virtual Internship – Solar & Wind Deployment Intelligence Platform**
