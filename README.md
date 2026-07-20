<div align="center">

#  Solar & Wind Deployment Intelligence Platform

**An AI-powered platform for identifying, evaluating, and optimizing renewable energy deployment sites**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+PostGIS-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Vite](https://img.shields.io/badge/Vite-5-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

>  **Infosys Springboard Virtual Internship** — Smita Mhatugade

*Empowering renewable energy companies, government agencies, and sustainability consultants with AI-driven geospatial intelligence.*

</div>

---

##  Table of Contents

- [What This Project Does](#-what-this-project-does)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Quick Start (Running Locally)](#-quick-start-running-locally)
  - [Step 1 – Clone the Repository](#step-1--clone-the-repository)
  - [Step 2 – Set Up PostgreSQL](#step-2--set-up-postgresql)
  - [Step 3 – Backend Setup](#step-3--backend-setup)
  - [Step 4 – Frontend Setup](#step-4--frontend-setup)
  - [Step 5 – Verify Everything Works](#step-5--verify-everything-works)
- [Environment Variables Reference](#-environment-variables-reference)
- [API Reference](#-api-reference)
- [Database Schema](#-database-schema)
- [Running Tests](#-running-tests)
- [User Roles & Access Control](#-user-roles--access-control)
- [Data Sources](#-data-sources)
- [Milestone Roadmap](#-milestone-roadmap)
- [Troubleshooting](#-troubleshooting)

---

## 🎯 What This Project Does

The Solar & Wind Deployment Intelligence Platform helps analysts and energy planners decide **where** and **what type** of renewable energy to deploy. Given a geographic location (latitude / longitude), the platform:

1. **Fetches real climate data** from NASA POWER API (solar irradiance, temperature, humidity)
2. **Classifies the solar and wind resource quality** (Poor / Moderate / Good / Excellent)
3. **Estimates capacity factors** using engineering rule tables (no black-box ML required)
4. **Recommends a deployment strategy** — Solar, Wind, or Hybrid — with a confidence score and plain-English reason
5. **Scores site suitability** across 5 weighted criteria (resource availability, terrain, infrastructure, environment, economics)

---

##  System Architecture

```
┌────────────────────────────────────────────────────────────────┐
│              BROWSER (React + Vite, port 5173)                 │
│  Login/Register → Dashboard → Projects → Site Analysis        │
└───────────────────────────────┬────────────────────────────────┘
                                │  REST / JSON  (Axios + JWT)
                                ▼
┌────────────────────────────────────────────────────────────────┐
│              BACKEND API  (FastAPI, port 8000)                 │
│                                                                │
│  /api/v1/auth      – register, login, me, user list           │
│  /api/v1/projects  – CRUD project management                  │
│  /api/v1/solar     – solar features endpoint                  │
│  /api/v1/wind      – wind prediction endpoint (stub)          │
│  /api/v1/site      – spatial suitability analysis             │
│  /api/v1/reports   – report generation (stub)                 │
└──────────┬──────────────────────────┬──────────────────────────┘
           │                          │
           ▼                          ▼
┌──────────────────┐      ┌──────────────────────────────────────┐
│  PostgreSQL 15   │      │  External Data Sources               │
│  + PostGIS       │      │                                      │
│  (port 5433)     │      │  NASA POWER REST API (live)          │
│                  │      │  Global Wind Atlas (planned)         │
│  users           │      │  SRTM Elevation (planned)            │
│  projects        │      │  OpenStreetMap (planned)             │
│  solar_predicts  │      │  Sentinel-2 Imagery (planned)        │
│  wind_predicts   │      └──────────────────────────────────────┘
│  site_analyses   │
│  reports         │      ┌──────────────────────────────────────┐
└──────────────────┘      │  Business Logic Services             │
                          │                                      │
                          │  solar_assessment.py                 │
                          │  wind_assessment.py                  │
                          │  deployment_strategy.py              │
                          │  feature_builder.py                  │
                          │  spatial/analysis_coordinator.py     │
                          └──────────────────────────────────────┘
```

### Layered Architecture

```
╔══════════════════════════════════════════════════════════╗
║  PRESENTATION  –  React 18 + Vite + React Router v6      ║
║  Login · Register · Dashboard · Projects · Site Analysis ║
╠══════════════════════════════════════════════════════════╣
║  API GATEWAY   –  FastAPI + JWT OAuth2                   ║
║  /auth · /projects · /solar · /wind · /site · /reports   ║
╠══════════════════════════════════════════════════════════╣
║  BUSINESS LOGIC SERVICES                                 ║
║  SolarAssessment · WindAssessment · DeploymentStrategy   ║
║  FeatureBuilder · SpatialAnalysisService                 ║
╠══════════════════════════════════════════════════════════╣
║  DATA ACCESS   –  SQLAlchemy 2.0 ORM + Pydantic schemas  ║
║  User · SolarPrediction · WindPrediction · SiteAnalysis  ║
╠══════════════════════════════════════════════════════════╣
║  INFRASTRUCTURE                                          ║
║  PostgreSQL 15 + PostGIS · NASA POWER API · Docker       ║
╚══════════════════════════════════════════════════════════╝
```

---

##  Tech Stack

| Layer | Technology | Version | Purpose |
|---|---|---|---|
| **Frontend** | React.js | 18.3 | UI components |
| **Frontend Build** | Vite | 5.4 | Dev server & bundler |
| **Frontend Routing** | React Router DOM | 6.26 | Client-side routing |
| **HTTP Client** | Axios | 1.7 | API calls + JWT interceptors |
| **Backend API** | FastAPI | 0.111+ | REST endpoints |
| **ASGI Server** | Uvicorn | 0.30+ | Run the FastAPI app |
| **ORM** | SQLAlchemy | 2.0+ | PostgreSQL access |
| **Migrations** | Alembic | 1.13+ | DB schema versioning |
| **Auth** | python-jose + passlib | latest | JWT + bcrypt hashing |
| **Database** | PostgreSQL | 15 + PostGIS | Relational + spatial |
| **GIS** | GeoPandas, Rasterio, Shapely | latest | Spatial processing |
| **ML / Data** | Scikit-learn, Pandas, NumPy | latest | Feature engineering |
| **External APIs** | NASA POWER (httpx) | latest | Solar irradiance data |
| **Config** | pydantic-settings | 2.3+ | .env file loading |
| **Testing** | pytest | 8.2+ | Unit tests |
| **Containers** | Docker + Docker Compose | latest | DB containerisation |

---

##  Project Structure

```
solar-wind-deployment-intelligence/
│
├── backend/
│   ├── app/
│   │   ├── api/                          # FastAPI route handlers
│   │   │   ├── auth.py                   # POST /auth/register, /login, GET /me
│   │   │   ├── projects.py               # Full CRUD for projects
│   │   │   ├── solar.py                  # GET /solar/features (live NASA call)
│   │   │   ├── wind.py                   # POST /wind/predict (stub – Milestone 2)
│   │   │   ├── site.py                   # POST /site/analyze (spatial scoring)
│   │   │   └── reports.py                # Report generation (stub)
│   │   │
│   │   ├── auth/
│   │   │   ├── security.py               # JWT creation, bcrypt hashing
│   │   │   ├── dependencies.py           # get_current_user() dependency
│   │   │   └── roles.py                  # require_admin(), require_analyst_or_admin()
│   │   │
│   │   ├── data_sources/
│   │   │   ├── nasa_power.py             # Live NASA POWER API client
│   │   │   ├── global_wind_atlas.py      # GWA client (stub)
│   │   │   ├── srtm.py                   # SRTM elevation client (stub)
│   │   │   └── osm.py                    # OpenStreetMap client (stub)
│   │   │
│   │   ├── database/
│   │   │   └── database.py               # SQLAlchemy engine + SessionLocal
│   │   │
│   │   ├── models/                       # SQLAlchemy ORM table definitions
│   │   │   ├── user.py
│   │   │   ├── solar_prediction.py
│   │   │   ├── wind_prediction.py
│   │   │   ├── site_analysis.py
│   │   │   ├── project.py
│   │   │   └── report.py
│   │   │
│   │   ├── schemas/                      # Pydantic request/response models
│   │   │   ├── user.py
│   │   │   ├── solar.py
│   │   │   ├── wind.py
│   │   │   ├── site.py
│   │   │   ├── project.py
│   │   │   └── report.py
│   │   │
│   │   ├── services/                     # Business logic (no DB, no HTTP)
│   │   │   ├── solar_assessment.py       # ✅ Solar classification & capacity factor
│   │   │   ├── wind_assessment.py        # ✅ Wind classification & capacity factor
│   │   │   ├── deployment_strategy.py    # ✅ Solar/Wind/Hybrid recommendation
│   │   │   ├── feature_builder.py        # Orchestrates data source clients
│   │   │   └── spatial/
│   │   │       ├── analysis_coordinator.py  # Suitability scoring coordinator
│   │   │       ├── raster_processor.py      # GeoTIFF raster processing
│   │   │       └── vector_processor.py      # Shapefile vector processing
│   │   │
│   │   ├── utils/
│   │   │   └── coordinates.py            # Coordinate validation helpers
│   │   │
│   │   ├── config.py                     # Pydantic settings (reads .env)
│   │   └── main.py                       # FastAPI app + router registration
│   │
│   ├── alembic/                          # Database migration scripts
│   ├── tests/
│   │   ├── test_coordinates.py           # Coordinate validation tests
│   │   ├── test_solar_features.py        # NASA POWER client tests
│   │   └── test_wind_solar_deployment.py # ✅ 140 tests for all new services
│   ├── .env                              # Local environment variables
│   ├── requirements.txt                  # Python dependencies
│   └── Dockerfile                        # Backend container definition
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                       # Root component + all routes
│   │   ├── main.jsx                      # ReactDOM.createRoot entry point
│   │   ├── index.css                     # Global design system styles
│   │   ├── App.css                       # Layout styles
│   │   ├── pages/
│   │   │   ├── LoginPage.jsx             # /login
│   │   │   ├── RegisterPage.jsx          # /register
│   │   │   ├── DashboardPage.jsx         # /dashboard (protected)
│   │   │   ├── ProjectsPage.jsx          # /projects (protected) – full CRUD
│   │   │   └── SiteAnalysisPage.jsx      # /site-analysis
│   │   ├── components/
│   │   │   ├── Sidebar.jsx               # Navigation sidebar
│   │   │   └── ProtectedRoute.jsx        # Auth guard component
│   │   └── services/
│   │       └── api.js                    # Axios instance + auth/project helpers
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
│
├── datasets/                             # Source data (gitignored for large files)
│   ├── nasa_power/
│   ├── global_wind_atlas/
│   ├── sentinel/
│   ├── openstreetmap/
│   └── srtm/
│
├── models/                               # Trained ML model artifacts (.joblib)
├── notebooks/                            # Jupyter EDA notebooks
├── docs/                                 # Architecture & design docs
├── reports/                              # Generated PDF/Excel reports (output)
├── docker-compose.yml                    # PostgreSQL + PostGIS container
└── README.md                             # This file
```

---

##  Prerequisites

Before you begin, make sure you have the following installed:

| Tool | Minimum Version | Download |
|---|---|---|
| **Python** | 3.10+ | https://python.org |
| **Node.js** | 18+ | https://nodejs.org |
| **npm** | 9+ | Bundled with Node.js |
| **PostgreSQL** | 15+ | https://postgresql.org OR use Docker |
| **Git** | any | https://git-scm.com |
| **Docker** *(optional)* | 24+ | https://docker.com |

> **Windows users:** All commands below use PowerShell. Replace `./venv/Scripts/Activate.ps1` with the appropriate activation script if you're in CMD.

---

##  Quick Start (Running Locally)

### Step 1 – Clone the Repository

```powershell
git clone https://github.com/Smita-Mhatugade/Solar_and_Wind_Deployment_Intelligence_Platform.git
cd "Solar_and_Wind_Deployment_Intelligence_Platform"
cd "solar-wind-deployment-intelligence"
```

---

### Step 2 – Set Up PostgreSQL

You have two options:

#### Option A — Use Docker (Recommended, zero config)

```powershell
# From the project root (solar-wind-deployment-intelligence/)
docker-compose up -d
```

This starts a **PostgreSQL 15 + PostGIS** container on port **5432**.

> Default credentials: `postgres` / `postgres`, database: `solar_wind_db`

#### Option B — Use an Existing Local PostgreSQL

1. Open **pgAdmin** or `psql` and create the database:
   ```sql
   CREATE DATABASE solar_wind_db;
   ```
2. Note your PostgreSQL host, port, username, and password for the `.env` file below.

> **Note:** This project currently uses port **5433** in its `.env`. If your local PostgreSQL runs on port **5432**, update `POSTGRES_PORT` accordingly.

---

### Step 3 – Backend Setup

```powershell
# Navigate to the backend folder
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Install all Python dependencies
pip install -r requirements.txt
```

#### Start the Backend Server

```powershell
# Still inside backend/, with venv activated
uvicorn app.main:app --reload --port 8000
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Application startup complete.
```

**Backend URLs:**
| URL | Purpose |
|---|---|
| `http://localhost:8000` | API root / health check |
| `http://localhost:8000/docs` | Swagger UI (interactive API docs) |
| `http://localhost:8000/redoc` | ReDoc API docs |
| `http://localhost:8000/ping` | Liveness check |
| `http://localhost:8000/db-health` | Database connection check |

---

### Step 4 – Frontend Setup

Open a **new terminal window** (keep the backend running in the first one).

```powershell
# Navigate to frontend (from project root)
cd frontend

# Install Node.js dependencies
npm install

# Start the Vite development server
npm run dev
```

You should see:
```
  VITE v5.x  ready in XXX ms

  ➜  Local:   http://localhost:5173/
```

**Frontend URL:** `http://localhost:5173`

---

### Step 5 – Verify Everything Works

Open your browser and go to:

1. **`http://localhost:5173`** → redirects to `/login`
2. Click **"Register"** to create a new account
3. Log in with your new credentials
4. The dashboard should load with your user name and role badge

Also verify the backend:
- `http://localhost:8000/docs` → Swagger should show all endpoints
- `http://localhost:8000/db-health` → should return `{"status":"ok","database":"connected"}`

---

##  Environment Variables Reference

All variables live in `backend/.env`. Here is the complete reference:

| Variable | Default | Description |
|---|---|---|
| `APP_NAME` | `Solar & Wind...` | Application display name |
| `APP_VERSION` | `1.0.0` | API version string |
| `DEBUG` | `True` | Enable debug mode |
| `SECRET_KEY` | *(set this)* | App-level secret |
| `DATABASE_URL` | *(see below)* | Full PostgreSQL connection string |
| `POSTGRES_DB` | `solar_wind_db` | Database name |
| `POSTGRES_USER` | `postgres` | DB username |
| `POSTGRES_PASSWORD` | *(set this)* | DB password |
| `POSTGRES_HOST` | `localhost` | DB host |
| `POSTGRES_PORT` | `5433` | DB port |
| `JWT_SECRET_KEY` | *(set this)* | Key for signing JWT tokens |
| `JWT_ALGORITHM` | `HS256` | JWT signing algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | JWT token lifetime |
| `API_V1_STR` | `/api/v1` | API prefix |

> **DATABASE_URL format:** `postgresql://USER:PASSWORD@HOST:PORT/DBNAME`

---

## 📡 API Reference

All endpoints are prefixed with `/api/v1/`. Use the Swagger UI at `http://localhost:8000/docs` to try them interactively.

### 🔐 Authentication — `/auth`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `POST` | `/auth/register` |  Public | Register a new user account |
| `POST` | `/auth/login` |  Public | Login; returns JWT access token |
| `GET` | `/auth/me` |  Any role | Get current user profile |
| `GET` | `/auth/users` | Admin only | List all registered users |
| `PUT` | `/auth/users/{id}/role` | Admin only | Change a user's role |

**Login response example:**
```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer",
  "user_id": 1,
  "email": "user@example.com",
  "full_name": "Smita Mhatugade",
  "role": "user"
}
```

---

###  Projects — `/projects`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `GET` | `/projects` | ✅ Any role | List all my projects |
| `POST` | `/projects` | ✅ Any role | Create a new project |
| `GET` | `/projects/{id}` | ✅ Owner or Admin | Get project by ID |
| `PUT` | `/projects/{id}` | ✅ Owner or Admin | Update a project |
| `DELETE` | `/projects/{id}` | ✅ Owner or Admin | Delete a project |

**Create project request body:**
```json
{
  "project_name": "Rajasthan Wind Farm",
  "description": "Wind feasibility study for western Rajasthan",
  "state": "Rajasthan",
  "latitude": 26.9124,
  "longitude": 70.9123
}
```

---

###Solar — `/solar`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `GET` | `/solar/features?latitude=&longitude=` |  Public | Fetch live solar irradiance from NASA POWER API |
| `POST` | `/solar/predict` |  Analyst/Admin | Solar energy yield prediction *(Milestone 2)* |
| `GET` | `/solar/history` |  Any role | User's solar prediction history *(Milestone 2)* |

**Solar features response example:**
```json
{
  "solar_irradiance": 5.8,
  "temperature": 28.4,
  "relative_humidity": 42.1
}
```

---

### 💨 Wind — `/wind`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `POST` | `/wind/predict` |  Analyst/Admin | Wind energy yield prediction *(Milestone 2)* |
| `GET` | `/wind/history` | Any role | User's wind prediction history *(Milestone 2)* |

---

### 📍 Site Analysis — `/site`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `POST` | `/site/analyze` |  Public (temp) | Run spatial suitability analysis for lat/lon |
| `GET` | `/site/history` |  Any role | Site analysis history *(Milestone 2)* |

**Site analyze request body:**
```json
{
  "latitude": 26.9124,
  "longitude": 70.9123
}
```

**Site analyze response example:**
```json
{
  "site_id": 1,
  "latitude": 26.9124,
  "longitude": 70.9123,
  "overall_score": 87.5,
  "recommendation": "Highly Suitable",
  "criteria_evaluation": {
    "solar_irradiance": { "value": 5.9, "status": "Pass" },
    "wind_speed":       { "value": 7.2, "status": "Pass" },
    "slope":            { "value": 4.0, "status": "Pass" },
    "distance_to_grid": { "value": 1.8, "status": "Pass" },
    "distance_to_road": { "value": 0.45,"status": "Pass" }
  },
  "constraints": { "protected_area": false, "water_body": false },
  "remarks": ["High solar potential.", "Good road accessibility."]
}
```

---

###  Reports — `/reports`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `POST` | `/reports/generate` | 🔒 Analyst/Admin | Generate PDF/Excel report *(Milestone 2)* |

---

###  Health Checks

| URL | Description |
|---|---|
| `GET /` | App name, version, status |
| `GET /ping` | Liveness probe |
| `GET /health` | Health status |
| `GET /db-health` | Database connection status |
| `GET /db-status` | Table record counts |

---

##  Database Schema

```
users
  id            SERIAL PK
  email         VARCHAR(255) UNIQUE NOT NULL
  password_hash VARCHAR(255) NOT NULL
  full_name     VARCHAR(255)
  role          VARCHAR(50)  DEFAULT 'user'   -- 'admin' | 'analyst' | 'user'
  is_active     BOOLEAN      DEFAULT TRUE
  created_at    TIMESTAMP    DEFAULT NOW()
  updated_at    TIMESTAMP

projects (FK → users)
  id            SERIAL PK
  user_id       INTEGER FK → users.id  CASCADE DELETE
  project_name  VARCHAR(200) NOT NULL
  description   TEXT
  state         VARCHAR(100)
  latitude      FLOAT
  longitude     FLOAT
  created_at    TIMESTAMP DEFAULT NOW()

solar_predictions (FK → users)
  id                   SERIAL PK
  user_id              INTEGER FK → users.id
  city_name            VARCHAR(100)
  latitude / longitude FLOAT
  solar_irradiance_kwh FLOAT      -- annual kWh/m²
  clearness_index      FLOAT      -- 0–1
  temp_mean_c          FLOAT
  predicted_output_kwh FLOAT
  capacity_factor      FLOAT
  confidence_score     FLOAT
  created_at           TIMESTAMP

wind_predictions (FK → users)
  id                    SERIAL PK
  user_id               INTEGER FK → users.id
  city_name             VARCHAR(100)
  latitude / longitude  FLOAT
  wind_speed_10m_ms     FLOAT  -- NASA POWER at 10m
  wind_speed_50m_ms     FLOAT  -- GWA at 50m
  wind_speed_100m_ms    FLOAT  -- GWA at 100m
  wind_power_density    FLOAT  -- W/m²
  predicted_output_kwh  FLOAT
  capacity_factor       FLOAT
  wind_class            INTEGER  -- 1–4
  confidence_score      FLOAT
  created_at            TIMESTAMP

site_analyses (FK → users)
  id                    SERIAL PK
  user_id               INTEGER FK → users.id
  site_name             VARCHAR(200)
  latitude / longitude  FLOAT
  -- Resource inputs
  solar_irradiance_kwh  FLOAT
  wind_speed_50m_ms     FLOAT
  elevation_m / slope_deg FLOAT
  ndvi / ndwi           FLOAT
  dist_grid_km / dist_road_km FLOAT
  -- Sub-scores (0–100)
  solar_score           FLOAT  -- 30% weight
  wind_score            FLOAT  -- 25% weight
  terrain_score         FLOAT  -- 20% weight
  land_use_score        FLOAT  -- 15% weight
  infrastructure_score  FLOAT  -- 10% weight
  suitability_score     FLOAT  -- composite
  recommendation        VARCHAR(50)
  created_at            TIMESTAMP

reports (FK → users)
  id            SERIAL PK
  user_id       INTEGER FK → users.id
  created_at    TIMESTAMP
```

All tables use **CASCADE DELETE** on the user foreign key — deleting a user removes all their data.

---

##  Running Tests

The project uses **pytest**. All tests live in `backend/tests/`.

```powershell
# Navigate to backend and activate venv
cd backend
.\venv\Scripts\Activate.ps1

# Run all tests
.\venv\Scripts\python.exe -m pytest tests/ -v

# Run only the wind/solar/deployment tests
.\venv\Scripts\python.exe -m pytest tests/test_wind_solar_deployment.py -v

# Run with coverage (if pytest-cov is installed)
.\venv\Scripts\python.exe -m pytest tests/ --cov=app --cov-report=term-missing
```

**Current test suite:** `140 tests · 0 failures`

| Test File | What it Tests |
|---|---|
| `test_coordinates.py` | Coordinate validation (lat/lon bounds) |
| `test_solar_features.py` | NASA POWER API client (mocked HTTP) |
| `test_wind_solar_deployment.py` | Wind classification, solar classification, all 16 deployment rule combos, capacity factor, confidence score, boundary values, invalid inputs |

---

##  User Roles & Access Control

Every registered user is assigned a **role** that controls what they can access.

| Role | Created By | Access Level |
|---|---|---|
| `user` | Self-registration | Create/view their own projects |
| `analyst` | Admin promotion | Run predictions + all `user` access |
| `admin` | Admin promotion | All endpoints including user management |

**Promote a user to analyst (admin required):**
```http
PUT /api/v1/auth/users/{user_id}/role?role=analyst
Authorization: Bearer <admin_token>
```

JWT tokens expire after **30 minutes** (configurable via `ACCESS_TOKEN_EXPIRE_MINUTES`).

---

##  Data Sources

| Dataset | Status | How Used |
|---|---|---|
| **NASA POWER REST API** | ✅ Live | Fetches solar irradiance, temperature, humidity for any lat/lon |
| **Global Wind Atlas** | 🔄 Stub | Will provide wind speed at 10m / 50m / 100m |
| **NASA SRTM** | 🔄 Stub | Will provide elevation and slope data |
| **OpenStreetMap** | 🔄 Stub | Will provide road and grid proximity data |
| **Copernicus Sentinel-2** | 🔄 Stub | Will provide NDVI / NDWI / land cover |

**NASA POWER API** is the only live external call right now. No API key is required — it is a free, publicly accessible API from NASA Langley Research Center.

---

##  Milestone Roadmap

### Milestone 1 — Foundation (Weeks 1–2)

- [x] System architecture & database design
- [x] FastAPI backend with JWT authentication
- [x] PostgreSQL database + SQLAlchemy ORM
- [x] User registration, login, role-based access control
- [x] Project CRUD API (create / read / update / delete)
- [x] NASA POWER API integration (solar irradiance fetching)
- [x] React frontend: Login, Register, Dashboard, Projects pages
- [x] Axios API client with JWT interceptors and auto-logout
- [x] **Wind Assessment Service** (classification + capacity factor)
- [x] **Solar Assessment Service** (classification + capacity factor)
- [x] **Deployment Strategy Service** (16-rule recommendation engine)
- [x] 140 unit tests covering all assessment logic

### Milestone 2 — ML Prediction Engines (Weeks 3–4)

- [ ] Connect real ML models for solar energy yield prediction
- [ ] Connect real ML models for wind energy yield prediction
- [ ] Integrate Global Wind Atlas live data
- [ ] Populate prediction history endpoints
- [ ] SRTM elevation + OSM proximity integration

### Milestone 3 — Site Intelligence & Optimisation (Weeks 5–6)

- [ ] Full site suitability scoring with real GIS data
- [ ] Deployment optimisation engine
- [ ] Energy forecasting (daily / monthly / annual)
- [ ] Interactive GIS maps (Leaflet / Mapbox)

###  Milestone 4 — Analytics, Reports & Deployment (Weeks 7–8)

- [ ] PDF / Excel report generation (ReportLab + openpyxl)
- [ ] Role-specific dashboards with charts (Plotly / Chart.js)
- [ ] End-to-end integration testing
- [ ] Docker production build
- [ ] Cloud deployment (AWS / Azure)

---

##  Troubleshooting

### `npm run dev` fails with "Cannot find package.json"

You must be **inside the `frontend/` directory**:
```powershell
cd frontend
npm run dev
```

### `uvicorn` fails to start / database errors

1. Check your `.env` values — especially `POSTGRES_PORT` and `POSTGRES_PASSWORD`
2. Verify PostgreSQL is running: `pg_isready -h localhost -p 5433`
3. Check the db-health endpoint: `http://localhost:8000/db-health`

### `psycopg2` installation fails on Windows

Install the pre-built binary instead:
```powershell
pip install psycopg2-binary
```

### Tables don't exist / `relation "users" does not exist`

FastAPI auto-creates all tables on startup via `Base.metadata.create_all()`. If it fails:
1. Make sure the database exists in PostgreSQL
2. Check the startup logs for any connection errors
3. Try running Alembic migrations manually:
   ```powershell
   alembic upgrade head
   ```

### Frontend shows "Network Error" when calling the API

- Backend must be running on port `8000`
- CORS is configured to allow `localhost:5173` — do not change the frontend dev port

### JWT token expired / auto-redirected to login

Tokens expire after 30 minutes. Simply log in again. To increase the lifetime, change `ACCESS_TOKEN_EXPIRE_MINUTES` in `.env`.

---

##  About

| | |
|---|---|
| **Internship** | Infosys Springboard Virtual Internship |
| **Project** | Solar & Wind Deployment Intelligence Platform |
| **Intern** | Smita Mhatugade |
| **GitHub** | [@Smita-Mhatugade](https://github.com/Smita-Mhatugade) |
| **Repository** | [Solar_and_Wind_Deployment_Intelligence_Platform](https://github.com/Smita-Mhatugade/Solar_and_Wind_Deployment_Intelligence_Platform) |

---

<div align="center">

Made with for a greener, smarter energy future 

</div>
