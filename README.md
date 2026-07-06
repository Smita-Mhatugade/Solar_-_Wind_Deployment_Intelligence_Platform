<div align="center">

# ☀️💨 Solar & Wind Deployment Intelligence Platform

**An AI-powered full-stack platform for renewable energy site assessment and deployment planning**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-PostGIS-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> 🎓 **Infosys Springboard Virtual Internship Project** | Solar & Wind Deployment Intelligence Platform

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Dataset Sources](#-dataset-sources)
- [API Reference](#-api-reference)
- [Getting Started](#-getting-started)
- [Database Schema](#-database-schema)
- [Module Overview](#-module-overview)
- [Internship Progress](#-internship-progress)

---

## 🌍 Overview

The **Solar & Wind Deployment Intelligence Platform** is a full-stack, AI-driven web application that empowers energy planners, researchers, and policymakers to make **data-informed decisions** for renewable energy deployment.

By integrating real-world geospatial datasets (NASA POWER, Global Wind Atlas, Sentinel-2, SRTM, OpenStreetMap), the platform provides:

- 🔮 **Predictive analytics** for solar irradiance and wind energy yield
- 📍 **Site suitability scoring** (0–100) based on terrain, land cover, and infrastructure proximity
- 📊 **Interactive dashboards** with maps and charts
- 📄 **Automated report generation** (PDF / Excel) for stakeholders

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 **Secure Auth** | JWT-based authentication with role-based access control |
| ☀️ **Solar Prediction** | Predict solar energy yield (kWh/m²/day) from NASA POWER climate data |
| 💨 **Wind Prediction** | Estimate wind turbine output (kWh) using Global Wind Atlas data |
| 📍 **Site Suitability** | Multi-factor scoring using terrain, land use, and grid proximity |
| 🗺️ **Interactive Maps** | Visualize energy potential across geographic regions |
| 📄 **Report Export** | One-click PDF/Excel report generation for any assessed site |
| 🐳 **Dockerized** | Full containerized deployment with Docker Compose |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              USER (Browser)                             │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │  HTTPS
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         FRONTEND  ·  React.js  (Port 5173)              │
│                                                                         │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │
│   │  Auth Pages  │  │  Dashboard   │  │  Prediction  │  │ Reports  │  │
│   │  Login/Reg.  │  │  Maps/Charts │  │  Solar/Wind  │  │ PDF/XLSX │  │
│   └──────────────┘  └──────────────┘  └──────────────┘  └──────────┘  │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │  REST API (JSON)
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      API LAYER  ·  FastAPI  (Port 8000)                 │
│                                                                         │
│   POST /api/v1/auth/login        →  Authentication Module               │
│   POST /api/v1/auth/register     →  User Registration                  │
│   POST /api/v1/solar/predict     →  Solar Prediction Module            │
│   POST /api/v1/wind/predict      →  Wind Prediction Module             │
│   POST /api/v1/site/analyze      →  Site Suitability Module           │
│   GET  /api/v1/reports/generate  →  Report Generation Module           │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
        ┌───────────────┐  ┌───────────────┐  ┌──────────────────┐
        │   DATABASE    │  │  ML MODELS    │  │    DATASETS      │
        │  PostgreSQL   │  │               │  │                  │
        │  + PostGIS    │  │  ☀ Solar Mdl │  │  📡 NASA POWER   │
        │               │  │  💨 Wind Mdl │  │  💨 Wind Atlas   │
        │  Tables:      │  │  📍 Site Mdl │  │  🛰  Sentinel-2  │
        │  users        │  │               │  │  🗺  OSM        │
        │  predictions  │  └───────────────┘  │  🏔  SRTM       │
        │  sites        │                     └──────────────────┘
        │  reports      │
        └───────────────┘
```

### Layered Architecture

```
╔═══════════════════════════════════════════════════════════╗
║              PRESENTATION LAYER  (React.js)               ║
║         Dashboard │ Maps │ Prediction UI │ Reports        ║
╠═══════════════════════════════════════════════════════════╣
║              API GATEWAY LAYER  (FastAPI)                 ║
║        /auth  │  /solar  │  /wind  │  /site  │  /reports  ║
╠═══════════════════════════════════════════════════════════╣
║              BUSINESS LOGIC LAYER  (Services)             ║
║  AuthService │ SolarService │ WindService │ SiteService   ║
╠═══════════════════════════════════════════════════════════╣
║           DATA ACCESS LAYER  (SQLAlchemy ORM)             ║
║       Models │ Schemas │ Database Sessions & Queries      ║
╠═══════════════════════════════════════════════════════════╣
║              INFRASTRUCTURE LAYER  (Docker)               ║
║   PostgreSQL + PostGIS (5432)  │  Datasets (CSV/GeoTIFF)  ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | React.js + Vite | Interactive UI, maps, charts |
| **Backend API** | FastAPI (Python) | REST endpoints, request routing |
| **Authentication** | JWT + bcrypt | Secure, stateless auth |
| **ORM** | SQLAlchemy 2.0 | Database abstraction layer |
| **Database** | PostgreSQL + PostGIS | Relational + geospatial data |
| **ML / Data** | scikit-learn, Pandas, GeoPandas | Model training & data processing |
| **Containers** | Docker + Docker Compose | Portable, reproducible deployment |
| **Migrations** | Alembic | Database versioning & schema management |
| **Geospatial** | Rasterio, GDAL | GeoTIFF and raster data handling |

---

## 📁 Project Structure

```
solar-wind-deployment-intelligence/
│
├── backend/                      # FastAPI server-side application
│   ├── app/
│   │   ├── api/                  # Route handlers (auth, solar, wind, site, reports)
│   │   ├── auth/                 # JWT token logic & security dependencies
│   │   ├── database/             # DB connection & session management
│   │   ├── models/               # SQLAlchemy ORM models
│   │   ├── schemas/              # Pydantic request/response schemas
│   │   ├── services/             # Business logic layer
│   │   └── utils/                # Shared helper functions
│   ├── alembic/                  # Database migration scripts
│   ├── tests/                    # Unit & integration tests
│   ├── main.py                   # Application entry point
│   └── requirements.txt          # Python dependencies
│
├── frontend/                     # React + Vite user interface
│   ├── src/
│   │   ├── App.jsx               # Root component & routing
│   │   ├── services/api.js       # Axios API client
│   │   └── index.css             # Global styles
│   ├── public/                   # Static assets
│   └── package.json
│
├── datasets/                     # Renewable energy source datasets
│   ├── nasa_power/               # Solar irradiance & climate data
│   ├── global_wind_atlas/        # Wind speed & resource data
│   ├── sentinel/                 # Satellite imagery (NDVI, NDWI)
│   ├── openstreetmap/            # Infrastructure data (roads, grid lines)
│   └── srtm/                     # Elevation & terrain data (GeoTIFF)
│
├── docs/                         # Project documentation
│   ├── architecture/             # Architecture diagrams & decisions
│   ├── database/                 # DB schema & ER diagrams
│   └── module_mapping.md         # Core module responsibilities
│
├── notebooks/                    # Jupyter notebooks for EDA & analysis
├── models/                       # Trained ML model files (.pkl / .joblib)
├── reports/                      # Generated PDF / Excel output files
├── docker/                       # Additional Docker configuration
├── docker-compose.yml            # Multi-container orchestration
├── requirements.txt              # Root-level Python dependencies
└── README.md
```

---

## 🗂️ Dataset Sources

| Dataset | Source | Format | Purpose |
|---|---|---|---|
| **NASA POWER** | NASA Langley Research Center | CSV / API | Solar irradiance, temperature, humidity |
| **Global Wind Atlas** | DTU / World Bank | GeoTIFF / API | Wind speed at 10m / 50m / 100m heights |
| **Sentinel-2** | ESA Copernicus | GeoTIFF | Land cover classification, NDVI, NDWI |
| **OpenStreetMap** | OSM Contributors | Shapefile | Roads, substations, power transmission lines |
| **SRTM** | NASA / USGS | GeoTIFF | Digital elevation model, slope analysis |

---

## 📡 API Reference

All endpoints are prefixed with `/api/v1/`. Interactive docs available at `http://localhost:8000/docs`.

### Authentication
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Obtain a JWT access token |

### Predictions
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/solar/predict` | Predict solar energy yield for coordinates |
| `POST` | `/wind/predict` | Predict wind energy yield for coordinates |
| `POST` | `/site/analyze` | Run full site suitability analysis (score 0–100) |

### Reports
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/reports/generate` | Export site analysis as PDF or Excel |

> 🔒 All prediction and report endpoints require a valid `Bearer` JWT token in the `Authorization` header.

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.10+](https://python.org)
- [Node.js 18+](https://nodejs.org)
- [Docker & Docker Compose](https://docker.com)

### 1. Clone the Repository

```bash
git clone https://github.com/Smita-Mhatugade/Solar_and_Wind_Deployment_Intelligence_Platform.git
cd Solar_and_Wind_Deployment_Intelligence_Platform
```

### 2. Start the Database (Docker)

```bash
docker-compose up -d
```

This spins up **PostgreSQL + PostGIS** on port `5432`.

### 3. Backend Setup

```bash
cd backend
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Start the FastAPI server
uvicorn main:app --reload --port 8000
```

Backend API → `http://localhost:8000`  
Swagger Docs → `http://localhost:8000/docs`

### 4. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend → `http://localhost:5173`

### 5. Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/solarwind_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🗃️ Database Schema

```
┌──────────────────┐          ┌──────────────────────┐
│      users       │          │   solar_predictions  │
│ ──────────────── │          │ ──────────────────── │
│ id (PK)          │◄─────────│ user_id (FK)         │
│ email            │          │ id (PK)              │
│ password_hash    │          │ latitude             │
│ full_name        │          │ longitude            │
│ created_at       │          │ irradiance_kwh       │
│ is_active        │          │ predicted_output_kwh │
└──────────────────┘          │ created_at           │
         ▲                    └──────────────────────┘
         │
         │                    ┌──────────────────────┐
         │                    │   wind_predictions   │
         └────────────────────│ user_id (FK)         │
         │                    │ id (PK)              │
         │                    │ latitude             │
         │                    │ longitude            │
         │                    │ wind_speed_ms        │
         │                    │ predicted_output_kwh │
         │                    │ created_at           │
         │                    └──────────────────────┘
         │
         │                    ┌──────────────────────┐
         │                    │    site_analyses     │
         └────────────────────│ user_id (FK)         │
                              │ id (PK)              │
                              │ latitude             │
                              │ longitude            │
                              │ suitability_score    │
                              │ elevation_m          │
                              │ slope_deg            │
                              │ dist_grid_km         │
                              │ created_at           │
                              └──────────────────────┘
```

---

## 🧩 Module Overview

| Module | Responsibilities |
|---|---|
| 🔐 **Authentication** | User registration, login, JWT generation, role-based access control |
| ☀️ **Solar Prediction** | Process NASA POWER data, train/infer ML model, return kWh/m²/day |
| 💨 **Wind Prediction** | Process Global Wind Atlas & NASA POWER data, predict turbine output (kWh) |
| 📍 **Site Suitability** | Integrate solar + wind + SRTM + Sentinel-2 + OSM to compute viability score (0–100) |
| 🗄️ **Database** | ORM-managed CRUD for users, predictions, site analyses, and reports |
| 📄 **Reports** | Compile predictions and scores into downloadable PDF/Excel summaries |
| 🗺️ **Dashboard** | React frontend for maps, charts, comparisons, and project management |
| 🔌 **API Services** | FastAPI routing layer exposing all endpoints to the frontend |

---

## 📅 Internship Progress

| Day | Date | Topic |
|---|---|---|
| Day 1 | 30 June 2026 | Renewable Energy Fundamentals – Solar & Wind basics |
| Day 2 | 1 July 2026 | Project Structure Setup & Dataset Analysis (EDA) |
| Day 3 | 2 July 2026 | System Architecture Design & API Planning |
| Day 4 | 3 July 2026 | Database Design & Schema Definition |
| Day 5 | 4 July 2026 | Backend Foundation – FastAPI, Models, Auth |

---

## 👩‍💻 About

**Internship:** Infosys Springboard Virtual Internship  
**Project:** Solar & Wind Deployment Intelligence Platform  
**Intern:** Smita Mhatugade  
**GitHub:** [Smita-Mhatugade](https://github.com/Smita-Mhatugade)

---

<div align="center">

Made with ❤️ for a greener future 🌱

</div>
