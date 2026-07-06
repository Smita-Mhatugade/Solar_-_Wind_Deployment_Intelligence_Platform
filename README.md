<div align="center">

# ☀️💨 Solar & Wind Deployment Intelligence Platform

**An AI-powered platform for identifying, evaluating, and optimizing renewable energy deployment sites**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://reactjs.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-PostGIS-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![MongoDB](https://img.shields.io/badge/MongoDB-Secondary_DB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-ML-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

> 🎓 **Infosys Springboard Virtual Internship** | Solar & Wind Deployment Intelligence Platform

*Empowering renewable energy companies, government agencies, utility providers, and sustainability consultants with AI-driven geospatial intelligence.*

</div>

---

## 📖 Table of Contents

- [Objective](#-objective)
- [Key Outcomes](#-key-outcomes)
- [System Architecture](#-system-architecture)
- [Modules](#-modules)
- [Site Scoring Engine](#-site-scoring-engine)
- [Tech Stack](#-tech-stack)
- [Dataset Sources](#-dataset-sources)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Getting Started](#-getting-started)
- [Database Schema](#-database-schema)
- [Milestone Roadmap](#-milestone-roadmap)
- [Evaluation Criteria](#-evaluation-criteria)
- [Performance Metrics](#-performance-metrics)
- [Internship Progress](#-internship-progress)

---

## 🎯 Objective

Build an **AI-powered Solar & Wind Deployment Intelligence Platform** that recommends optimal locations for renewable energy projects by analyzing:

- 🌤️ **Environmental & climatic** factors (irradiance, wind speed, rainfall, temperature)
- 🏔️ **Geographic & terrain** data (elevation, slope, land cover)
- 🛰️ **Satellite imagery** (Sentinel-2 NDVI/NDWI land-use classification)
- 🏗️ **Infrastructure proximity** (roads, substations, transmission lines)
- 💰 **Economic feasibility** (ROI, investment scoring, capacity planning)

The platform leverages **geospatial analytics, machine learning, optimization algorithms, and weather forecasting** to identify deployment hotspots, estimate energy generation potential, evaluate project feasibility, and support investment decisions.

**Target Users:** Renewable energy companies · Government agencies · Utility providers · Environmental organizations · Infrastructure planners · Sustainability consultants

---

## ✅ Key Outcomes

- 🚀 Deployed AI-powered renewable energy intelligence platform
- 🔐 Secure authentication with role-based access control (4 user roles)
- 🌍 Geospatial and environmental data analysis workflows
- ☀️💨 Solar and wind potential prediction ML models
- 📍 Site suitability and deployment optimization engines
- 📈 Energy generation forecasting and investment analytics
- 🖥️ Role-specific dashboards for planners, analysts, and managers
- 🐳 Docker containerization + AWS/Azure cloud deployment

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           USER  (Browser)                               │
│    Energy Planner │ GIS Analyst │ Project Manager │ Administrator        │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │  HTTPS
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    FRONTEND  ·  React.js + Next.js  (Port 5173)         │
│                                                                         │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────┐ ┌────────┐ │
│  │ Auth/Login │ │  Dashboard │ │ Prediction │ │   Maps   │ │Reports │ │
│  │  Register  │ │ Analytics  │ │Solar + Wind│ │ Leaflet/ │ │PDF/XLSX│ │
│  └────────────┘ └────────────┘ └────────────┘ │  Mapbox  │ └────────┘ │
│                                                └──────────┘            │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │  REST API (JSON)
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    API GATEWAY  ·  FastAPI  (Port 8000)                 │
│                                                                         │
│  /auth    /projects   /sites    /solar     /wind                        │
│  /site    /forecast   /optimize /score     /reports   /notifications    │
└──────────────────┬────────────────────────────────────┬─────────────────┘
                   │                                    │
        ┌──────────┼──────────┐              ┌──────────┴───────────┐
        ▼          ▼          ▼              ▼                      ▼
┌─────────────┐ ┌─────────┐ ┌────────┐ ┌──────────────────┐ ┌──────────┐
│  PostgreSQL │ │ MongoDB │ │ML/AI   │ │ Datasets & APIs  │ │  Docker  │
│  + PostGIS  │ │(Docs/   │ │Models  │ │                  │ │  AWS /   │
│  (Port 5432)│ │ Logs)   │ │XGBoost │ │ NASA POWER API   │ │  Azure   │
│             │ │         │ │RandFrst│ │ Global Wind Atlas│ │          │
│  users      │ │         │ │LGBM    │ │ Sentinel Hub     │ │  CI/CD   │
│  predictions│ │         │ │TF/PyTch│ │ OpenWeather API  │ │ GH Actions│
│  sites      │ │         │ └────────┘ │ OpenStreetMap    │ └──────────┘
│  reports    │ └─────────┘            │ NASA SRTM        │
└─────────────┘                        └──────────────────┘
```

### Layered Architecture

```
╔═══════════════════════════════════════════════════════════════════╗
║              PRESENTATION LAYER  (React.js + Next.js)             ║
║  Energy Planner │ GIS Analyst │ Project Manager │ Admin Dashboards ║
╠═══════════════════════════════════════════════════════════════════╣
║              API GATEWAY LAYER  (FastAPI + JWT/OAuth2)            ║
║  /auth │ /projects │ /solar │ /wind │ /site │ /forecast │ /reports ║
╠═══════════════════════════════════════════════════════════════════╣
║              BUSINESS LOGIC LAYER  (Services)                     ║
║  AuthSvc │ SolarSvc │ WindSvc │ SiteSvc │ ForecastSvc │ OptimizeSvc║
╠═══════════════════════════════════════════════════════════════════╣
║              ML / AI LAYER                                        ║
║  XGBoost │ Random Forest │ LightGBM │ TensorFlow │ PyTorch        ║
╠═══════════════════════════════════════════════════════════════════╣
║              DATA ACCESS LAYER  (SQLAlchemy ORM + PyMongo)        ║
║  Models │ Schemas │ Queries │ GIS Processing (GeoPandas/Rasterio) ║
╠═══════════════════════════════════════════════════════════════════╣
║              INFRASTRUCTURE LAYER  (Docker + Cloud)               ║
║  PostgreSQL+PostGIS │ MongoDB │ Datasets (CSV/GeoTIFF/Shapefile)  ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## 🧩 Modules

### Module 1 · 🔐 User Authentication & Role-Based Access

Handles all identity, access, and session management for the platform.

- User registration, login, and profile management
- JWT authentication + OAuth2 login (Google/GitHub)
- Role-based access control (RBAC)
- Secure password hashing with bcrypt

**User Roles:**

| Role | Access Level |
|---|---|
| 🌞 **Renewable Energy Planner** | Site recommendations, forecasts, investment reports |
| 🗺️ **GIS Analyst** | Geospatial visualizations, terrain maps, environmental analytics |
| 📋 **Project Manager** | Project progress, feasibility reports, timelines, cost-benefit |
| ⚙️ **Administrator** | User management, platform analytics, system monitoring |

---

### Module 2 · 📂 Project & Site Management

Manages the full lifecycle of renewable energy projects and site registrations.

- Project creation and region management
- Site registration and comparison
- Deployment history tracking

**Site Information Fields:**

| Field | Description |
|---|---|
| Project ID | Unique project identifier |
| Geographic Coordinates | Latitude / Longitude |
| Region | Administrative region |
| Land Area | Area in hectares |
| Elevation | Height above sea level (m) |
| Existing Infrastructure | Roads, substations, transmission lines |
| Land Ownership | Public / Private / Government |

---

### Module 3 · 🌦️ Environmental Data Collection Engine

Collects, processes, and integrates real-world environmental data from multiple sources.

- Weather data collection (NASA POWER, OpenWeather)
- Satellite image processing (Sentinel-2)
- Terrain analysis (SRTM DEM)
- Climate data integration and geographic information analysis

**Environmental Factors Tracked:**

`Solar Irradiance` · `Wind Speed & Direction` · `Temperature` · `Rainfall` · `Cloud Cover` · `Elevation` · `Land Slope` · `Vegetation Index (NDVI)`

---

### Module 4 · 🗺️ Geographic Intelligence Engine

Processes geospatial data to assess site accessibility and land suitability.

- GIS data processing with GeoPandas, GDAL, Rasterio
- Terrain mapping and slope analysis
- Infrastructure proximity analysis
- Land suitability assessment

**Geographic Features Analyzed:**

`Roads` · `Transmission Lines` · `Substations` · `Urban Areas` · `Protected Zones` · `Water Bodies` · `Agricultural Land`

---

### Module 5 · ☀️ Solar Potential Prediction Engine

Estimates solar energy generation capacity for any geographic location.

- Solar energy estimation from NASA POWER irradiance data
- Panel efficiency and tilt optimization
- Seasonal energy forecasting
- Shading analysis and solar resource mapping

**Solar Metrics Predicted:**

| Metric | Description |
|---|---|
| Annual Irradiance | kWh/m²/year |
| Peak Sun Hours | Hours/day of optimal irradiance |
| Expected Energy Output | MWh/year for a given installation |
| Capacity Factor | Actual vs. rated output ratio |
| Performance Ratio | System efficiency (%) |

---

### Module 6 · 💨 Wind Potential Prediction Engine

Assesses wind resource quality and turbine energy output.

- Wind resource assessment from Global Wind Atlas data
- Turbine suitability and hub-height analysis
- Wind power density estimation
- Seasonal wind forecasting and resource mapping

**Wind Metrics Predicted:**

| Metric | Description |
|---|---|
| Average Wind Speed | m/s at 10m / 50m / 100m height |
| Wind Power Density | W/m² |
| Turbulence Intensity | Stability and reliability index |
| Capacity Factor | Actual vs. rated output ratio |
| Expected Annual Energy Production | MWh/year per turbine |

---

### Module 7 · 📍 Site Suitability Intelligence Engine

Combines all prediction engines into a unified suitability assessment.

- Multi-factor site ranking and scoring
- Deployment feasibility assessment
- Environmental impact evaluation
- Investment prioritization

**Suitability Factors:**

`Renewable Resource Availability` · `Terrain Suitability` · `Infrastructure Accessibility` · `Environmental Constraints` · `Economic Viability`

---

### Module 8 · 📈 Energy Forecasting Engine

Provides short-term and long-term energy production forecasts.

- Energy production forecasting (daily / weekly / monthly)
- Seasonal generation prediction
- Long-term energy estimation (20–25 year horizon)
- Grid contribution forecasting
- Revenue prediction and cash-flow modeling

---

### Module 9 · 🔧 Deployment Optimization Engine

Recommends the best configuration for renewable energy deployment.

- Optimal location recommendation using AI
- Technology selection (solar panels vs. wind turbines vs. hybrid)
- Capacity planning and layout optimization
- Hybrid solar-wind system recommendations
- Expansion planning for existing sites

---

### Module 10 · 🏆 Site Scoring Engine

Aggregates all analysis factors into a single, interpretable score.

*(See [Site Scoring Engine](#-site-scoring-engine) section below for the full scoring model)*

---

### Module 11 · 🖥️ Dashboard & Analytics

Role-specific dashboards for all user types.

| Dashboard | Key Features |
|---|---|
| 🌞 **Energy Planner** | Recommended sites · Forecasts · Suitability scores · Investment recommendations |
| 🗺️ **GIS Analyst** | GIS visualization · Environmental analytics · Terrain maps · Site comparison reports |
| 📋 **Project Manager** | Project progress · Feasibility reports · Cost-benefit analysis · Deployment timelines |
| ⚙️ **Admin** | User management · Platform analytics · Data source management · System monitoring |

---

### Module 12 · 🔔 Notification & Alert System

Keeps users informed of critical events and changes.

- ⛈️ Weather alerts for monitored regions
- 📊 Site suitability score updates
- ⚠️ Environmental risk alerts
- 🔄 Forecast update notifications
- 📬 Project status notifications

---

### Module 13 · 📄 Reports & Export System

Generates comprehensive, downloadable reports for stakeholders.

- Site assessment reports
- Solar potential reports
- Wind potential reports
- Feasibility reports
- Investment analysis reports
- **Export formats:** PDF · Excel (XLSX)

---

### Module 14 · 🚢 Final Integration, Testing & Deployment

Production-readiness and platform hardening.

- Frontend ↔ Backend integration
- API validation and end-to-end testing
- Security penetration testing
- Performance optimization
- Docker containerization
- Cloud deployment (AWS / Azure)
- Monitoring, logging, and alerting setup
- Documentation and user guides

---

## 🏆 Site Scoring Engine

### Weighted Scoring Model

$$\text{Deployment Suitability Score} = \sum w_i \times f_i$$

| Factor | Weight | Description |
|---|---|---|
| ☀️💨 **Renewable Resource Availability** | **35%** | Solar irradiance + wind speed potential |
| 🏔️ **Geographic Suitability** | **25%** | Terrain, slope, elevation, land cover |
| 🏗️ **Infrastructure Accessibility** | **15%** | Distance to roads, substations, grid |
| 🌿 **Environmental Impact** | **15%** | Protected zones, water bodies, NDVI |
| 💰 **Economic Feasibility** | **10%** | Land cost, ROI potential, grid tariff |

### Suitability Categories

| Score Range | Category | Action |
|---|---|---|
| 85 – 100 | 🟢 **Excellent** | Immediate deployment recommended |
| 70 – 84 | 🟩 **Highly Suitable** | Strong candidate, proceed with detailed feasibility |
| 50 – 69 | 🟡 **Moderately Suitable** | Viable with mitigation measures |
| 30 – 49 | 🟠 **Low Suitability** | Significant constraints, review alternatives |
| 0 – 29 | 🔴 **Unsuitable** | Not recommended for deployment |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | React.js, Next.js, Tailwind CSS | UI, routing, styling |
| **Backend API** | FastAPI (Python) | REST endpoints, request routing |
| **Authentication** | JWT + OAuth2 + bcrypt | Secure, stateless auth |
| **ORM** | SQLAlchemy 2.0 | PostgreSQL database abstraction |
| **Primary Database** | PostgreSQL + PostGIS | Relational + geospatial data |
| **Secondary Database** | MongoDB | Documents, logs, unstructured data |
| **ML Models** | XGBoost, Random Forest, LightGBM, TensorFlow, PyTorch | Prediction & forecasting |
| **Data Analytics** | Scikit-learn, Pandas, NumPy | Model training & data processing |
| **GIS / Remote Sensing** | QGIS, GDAL, Rasterio, GeoPandas, Shapely | Spatial data processing |
| **Visualization** | Plotly, Leaflet.js, Mapbox, Chart.js | Maps & interactive charts |
| **Satellite / Weather APIs** | NASA POWER, OpenWeather, Sentinel Hub, OSM | Data ingestion |
| **Migrations** | Alembic | Database versioning |
| **Containers** | Docker + Docker Compose | Portable deployment |
| **Cloud** | AWS / Azure | Production hosting |
| **CI/CD** | GitHub Actions | Automated testing & deployment |
| **Dev Tools** | VS Code, Git, Postman | Development workflow |

---

## 🗂️ Dataset Sources

| Dataset | Provider | Format | Key Purpose |
|---|---|---|---|
| **NASA POWER** | NASA Langley | CSV / REST API | Solar irradiance, temperature, humidity, climate |
| **Global Wind Atlas** | DTU / World Bank | GeoTIFF / REST API | Wind speed at 10m / 50m / 100m heights |
| **NASA SRTM** | NASA / USGS | GeoTIFF (DEM) | Elevation mapping, slope & terrain analysis |
| **OpenStreetMap (OSM)** | OSM Community | Shapefile / PBF | Road networks, infrastructure, urban areas |
| **Copernicus Sentinel-2** | ESA | GeoTIFF / Sentinel Hub | Land cover, NDVI/NDWI, environmental monitoring |
| **OpenWeather API** | OpenWeather | JSON / REST API | Real-time weather data & alerts |

---

## 📁 Project Structure

```
solar-wind-deployment-intelligence/
│
├── backend/                            # FastAPI server-side application
│   ├── app/
│   │   ├── api/                        # Route handlers
│   │   │   ├── auth.py                 # /auth endpoints
│   │   │   ├── solar.py                # /solar/predict
│   │   │   ├── wind.py                 # /wind/predict
│   │   │   ├── site.py                 # /site/analyze, /site/score
│   │   │   ├── reports.py              # /reports/generate
│   │   │   ├── projects.py             # /projects CRUD
│   │   │   └── notifications.py        # /notifications
│   │   ├── auth/                       # JWT + OAuth2 logic
│   │   ├── database/                   # PostgreSQL + MongoDB connections
│   │   ├── models/                     # SQLAlchemy ORM models
│   │   ├── schemas/                    # Pydantic request/response schemas
│   │   ├── services/                   # Business logic
│   │   │   ├── solar_service.py
│   │   │   ├── wind_service.py
│   │   │   ├── site_suitability.py
│   │   │   ├── forecasting.py
│   │   │   └── optimization.py
│   │   └── utils/                      # Helper functions, GIS utilities
│   ├── alembic/                        # Database migrations
│   ├── tests/                          # Unit & integration tests
│   ├── main.py                         # Application entry point
│   └── requirements.txt
│
├── frontend/                           # React + Next.js user interface
│   ├── src/
│   │   ├── App.jsx                     # Root component
│   │   ├── pages/                      # Next.js pages / React routes
│   │   ├── components/                 # Reusable UI components
│   │   ├── services/api.js             # Axios API client
│   │   └── index.css                   # Global styles (Tailwind CSS)
│   └── package.json
│
├── datasets/                           # Source datasets
│   ├── nasa_power/                     # Solar irradiance & climate CSV
│   ├── global_wind_atlas/              # Wind GeoTIFF rasters
│   ├── sentinel/                       # Sentinel-2 imagery
│   ├── openstreetmap/                  # OSM shapefiles
│   └── srtm/                          # DEM elevation GeoTIFF
│
├── ml_models/                          # Trained model artifacts
│   ├── solar_model.pkl
│   ├── wind_model.pkl
│   └── site_suitability_model.pkl
│
├── notebooks/                          # EDA and model development
│   ├── dataset_analysis.ipynb
│   └── day2_complete_analysis.ipynb
│
├── docs/                               # Project documentation
│   ├── architecture/project_architecture.md
│   ├── database/database_design.md
│   └── module_mapping.md
│
├── reports/                            # Generated PDF / Excel reports
├── docker/                             # Docker configurations
├── docker-compose.yml                  # Multi-container orchestration
├── requirements.txt                    # Root Python dependencies
└── README.md
```

---

## 📡 API Reference

All endpoints are prefixed with `/api/v1/`. Interactive docs: `http://localhost:8000/docs`

### 🔐 Authentication
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Obtain JWT access token |
| `POST` | `/auth/oauth2` | OAuth2 login (Google/GitHub) |
| `GET` | `/auth/me` | Get current user profile |

### 📂 Projects & Sites
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/projects/` | Create a new project |
| `GET` | `/projects/` | List all projects |
| `POST` | `/sites/register` | Register a new site |
| `GET` | `/sites/compare` | Compare multiple sites |

### ☀️💨 Predictions
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/solar/predict` | Solar energy yield for coordinates |
| `POST` | `/wind/predict` | Wind energy yield for coordinates |
| `POST` | `/site/analyze` | Full site suitability analysis |
| `GET` | `/site/score` | Get weighted suitability score (0–100) |

### 📈 Forecasting & Optimization
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/forecast/energy` | Long-term energy production forecast |
| `POST` | `/optimize/location` | AI-powered optimal location recommendation |
| `POST` | `/optimize/hybrid` | Hybrid solar-wind system recommendation |

### 📄 Reports & Notifications
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/reports/generate` | Export site report (PDF / Excel) |
| `GET` | `/notifications/` | Get user notifications and alerts |

> 🔒 All prediction, optimization, and report endpoints require a valid `Bearer` JWT token in the `Authorization` header.

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.10+](https://python.org)
- [Node.js 18+](https://nodejs.org)
- [Docker & Docker Compose](https://docker.com)
- [Git](https://git-scm.com)

### 1. Clone the Repository

```bash
git clone https://github.com/Smita-Mhatugade/Solar_and_Wind_Deployment_Intelligence_Platform.git
cd Solar_and_Wind_Deployment_Intelligence_Platform
```

### 2. Start Databases (Docker)

```bash
docker-compose up -d
```

Starts **PostgreSQL + PostGIS** on port `5432` and **MongoDB** on port `27017`.

### 3. Backend Setup

```bash
cd backend
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env

# Run database migrations
alembic upgrade head

# Start the FastAPI server
uvicorn main:app --reload --port 8000
```

- Backend API → `http://localhost:8000`
- Swagger Docs → `http://localhost:8000/docs`
- ReDoc → `http://localhost:8000/redoc`

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
# Database
DATABASE_URL=postgresql://postgres:password@localhost:5432/solarwind_db
MONGO_URL=mongodb://localhost:27017/solarwind_logs

# Auth
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# External APIs
NASA_POWER_API_KEY=your-nasa-power-key
OPENWEATHER_API_KEY=your-openweather-key
SENTINEL_HUB_CLIENT_ID=your-sentinel-client-id
SENTINEL_HUB_CLIENT_SECRET=your-sentinel-secret
MAPBOX_TOKEN=your-mapbox-token
```

### 6. Production Deployment (Docker)

```bash
# Build and run all services
docker-compose -f docker-compose.prod.yml up --build -d
```

---

## 🗃️ Database Schema

```
┌──────────────────┐       ┌──────────────────────┐   ┌──────────────────────┐
│      users       │       │   solar_predictions  │   │   wind_predictions   │
│ ──────────────── │       │ ──────────────────── │   │ ──────────────────── │
│ id (PK)          │◄──────│ user_id (FK)         │   │ user_id (FK)    ─────┤►users
│ email            │       │ id (PK)              │   │ id (PK)              │
│ password_hash    │       │ latitude             │   │ latitude             │
│ full_name        │       │ longitude            │   │ longitude            │
│ role             │       │ irradiance_kwh       │   │ wind_speed_ms        │
│ created_at       │       │ predicted_output_kwh │   │ predicted_output_kwh │
│ is_active        │       │ capacity_factor      │   │ capacity_factor      │
└──────────────────┘       │ created_at           │   │ created_at           │
         ▲                 └──────────────────────┘   └──────────────────────┘
         │
         │  ┌──────────────────────┐   ┌──────────────────────┐
         │  │    site_analyses     │   │       projects       │
         └──│ user_id (FK)         │   │ ──────────────────── │
            │ id (PK)              │   │ id (PK)              │
            │ project_id (FK) ─────┼──►│ name                 │
            │ latitude             │   │ region               │
            │ longitude            │   │ user_id (FK)    ─────┼─►users
            │ suitability_score    │   │ created_at           │
            │ elevation_m          │   └──────────────────────┘
            │ slope_deg            │
            │ dist_grid_km         │   ┌──────────────────────┐
            │ ndvi_index           │   │       reports        │
            │ land_cover_type      │   │ ──────────────────── │
            │ solar_score          │   │ id (PK)              │
            │ wind_score           │   │ site_id (FK)    ─────┼─►site_analyses
            │ infra_score          │   │ user_id (FK)    ─────┼─►users
            │ invest_score         │   │ format (PDF/XLSX)    │
            │ overall_score        │   │ file_path            │
            │ created_at           │   │ created_at           │
            └──────────────────────┘   └──────────────────────┘
```

---

## 🗓️ Milestone Roadmap

### Milestone 1 — Weeks 1 & 2 · Project Initialization & Core Setup

| Task | Status |
|---|---|
| Define project objectives and renewable energy workflows | ✅ |
| Design system architecture and database schema | ✅ |
| Create UI wireframes and workflow planning | ✅ |
| Setup frontend and backend environments | ✅ |
| Implement authentication and RBAC | ✅ |
| Build project and site management workflows | ✅ |
| Integrate GIS and environmental datasets | 🔄 |

**Outcomes:** Working authentication · Site management system · Environmental datasets integrated

---

### Milestone 2 — Weeks 3 & 4 · Environmental Intelligence & Resource Prediction

| Task | Status |
|---|---|
| Implement environmental data engine | ⬜ |
| Build GIS processing workflows | ⬜ |
| Develop solar potential prediction models | ⬜ |
| Implement wind resource estimation | ⬜ |
| Generate resource assessment reports | ⬜ |

**Outcomes:** Environmental intelligence engine · Solar & wind prediction workflows · Resource assessment

---

### Milestone 3 — Weeks 5 & 6 · Site Intelligence & Optimization

| Task | Status |
|---|---|
| Implement site suitability engine | ⬜ |
| Build deployment optimization workflows | ⬜ |
| Develop forecasting models | ⬜ |
| Generate investment recommendations | ⬜ |
| Create renewable energy dashboards | ⬜ |

**Outcomes:** Site intelligence engine · Deployment optimization · Recommendation workflows

---

### Milestone 4 — Weeks 7 & 8 · Analytics, Testing & Deployment

| Task | Status |
|---|---|
| Build executive dashboards (all 4 roles) | ⬜ |
| Add reports and GIS visualization modules | ⬜ |
| Implement testing and validations | ⬜ |
| Deploy platform on Docker + AWS/Azure | ⬜ |
| Prepare final documentation and presentation | ⬜ |

**Outcomes:** Fully deployed production-ready platform · Complete end-to-end workflow demonstrable

---

## 📊 Evaluation Criteria

| Milestone | Deliverables |
|---|---|
| **Week 2** | Project initialized · Authentication live · Site management operational · Datasets integrated |
| **Week 4** | Solar prediction engine · Wind prediction engine · GIS analytics implemented |
| **Week 6** | Site suitability engine · Forecasting models · Optimization recommendations |
| **Week 8** | Full frontend + backend deployed · Dashboards & reporting live · End-to-end workflow demonstrated |

---

## 📏 Performance Metrics

### Solar Prediction
- Solar irradiance prediction accuracy (RMSE, MAE)
- Energy generation estimation accuracy
- Capacity factor prediction error (%)

### Wind Prediction
- Wind speed prediction accuracy (RMSE)
- Wind power estimation accuracy (kWh)
- Seasonal forecast accuracy

### Site Selection
- Suitability classification accuracy (F1-score)
- Recommendation precision (top-5 sites)
- Infrastructure assessment accuracy

### Forecasting
- Annual energy prediction accuracy (MAPE < 10%)
- Revenue estimation accuracy
- Investment recommendation effectiveness

### System Performance
- GIS processing latency (< 2s per query)
- API response time (< 500ms p95)
- Dashboard loading speed (< 3s)
- Concurrent geospatial analysis capacity

---

## 📅 Internship Progress

| Day | Date | Topic |
|---|---|---|
| Day 1 | 30 June 2026 | Renewable Energy Fundamentals – Solar & Wind basics |
| Day 2 | 1 July 2026 | Project Structure Setup & Dataset Analysis (EDA) |
| Day 3 | 2 July 2026 | System Architecture Design & API Planning |
| Day 4 | 3 July 2026 | Database Design & Schema Definition |
| Day 5 | 4 July 2026 | Backend Foundation – FastAPI, Models, Auth |
| Day 6 | 7 July 2026 | *(upcoming)* |

---

## 👩‍💻 About

| | |
|---|---|
| **Internship** | Infosys Springboard Virtual Internship |
| **Project** | Solar & Wind Deployment Intelligence Platform |
| **Intern** | Smita Mhatugade |
| **GitHub** | [@Smita-Mhatugade](https://github.com/Smita-Mhatugade) |
| **Repository** | [Solar_and_Wind_Deployment_Intelligence_Platform](https://github.com/Smita-Mhatugade/Solar_and_Wind_Deployment_Intelligence_Platform) |

---

<div align="center">

Made with ❤️ for a greener, smarter energy future 🌱⚡

</div>
