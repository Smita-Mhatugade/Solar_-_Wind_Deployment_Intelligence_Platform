<div align="center">
  <img src="https://via.placeholder.com/1200x300/0f172a/38bdf8?text=Solar+%26+Wind+Deployment+Intelligence+Platform" alt="Platform Banner" />

  <h1>☀️🌬️ Solar & Wind Deployment Intelligence Platform</h1>

  <p>
    <strong>An end-to-end, AI-powered spatial intelligence platform for evaluating site suitability, energy yields, financial feasibility, and 12-month climate forecasts for renewable energy projects globally.</strong>
  </p>

  <p>
    <a href="https://solar-wind-deployment-intelligence.vercel.app/"><img src="https://img.shields.io/badge/Live%20Demo-Vercel-000000.svg?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Demo"></a>
    <a href="https://solar-wind-deployment-intelligence.onrender.com/docs"><img src="https://img.shields.io/badge/API-Render-46E3B7.svg?style=for-the-badge&logo=render&logoColor=white" alt="Backend API"></a>
    <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
    <a href="https://fastapi.tiangolo.com"><img src="https://img.shields.io/badge/FastAPI-0.115+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"></a>
    <a href="https://reactjs.org/"><img src="https://img.shields.io/badge/React-18.3.1-61DAFB.svg?style=for-the-badge&logo=react&logoColor=black" alt="React"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-F7DF1E.svg?style=for-the-badge" alt="License"></a>
  </p>

  <h3>
    🔗 <a href="https://solar-wind-deployment-intelligence.vercel.app/"><strong>Explore Live Application</strong></a>
  </h3>

  <p>
    <a href="#-overview">Overview</a> •
    <a href="#-key-features">Features</a> •
    <a href="#-architecture--workflow">Architecture</a> •
    <a href="#-technology-stack">Tech Stack</a> •
    <a href="#-project-structure">Structure</a> •
    <a href="#-quick-start--local-setup">Quick Start</a> •
    <a href="#-api-reference">API Docs</a> •
    <a href="#-recent-changes--enhancements">Recent Updates</a>
  </p>
</div>

---

## 📖 Overview

The **Solar & Wind Deployment Intelligence Platform** is a full-stack, enterprise-grade spatial analytics and decision-support web application. Designed for clean energy developers, financial analysts, and environmental engineers, it evaluates the feasibility of deploying solar and wind energy projects at any geographic coordinate across the globe in seconds rather than weeks.

By combining a **Random Forest ML Suitability Model (R² = 0.89)** with real-time geospatial data pipelines (**NASA POWER, Global Wind Atlas, OpenStreetMap, SRTM Elevation Models**), the platform outputs:
- **0–100 Site Suitability Score** with breakdown metrics.
- **12-Month Energy Yield Forecasts** for Solar PV, Wind Turbines, or Hybrid configurations.
- **Financial Projections** including Estimated CAPEX, OPEX, LCOE ($/kWh), Annual Revenue, ROI, and Payback Period.
- **Interactive Geospatial Visualization** with Leaflet interactive coordinate pickers and terrain elevation profiling.
- **Automated PDF Report Generation** for instant stakeholder export.

The platform is designed to operate both as an **open-access, zero-friction public intelligence tool** (with server-side in-memory caching and browser LocalStorage persistence) as well as an authenticated enterprise platform backed by PostgreSQL/PostGIS.

---

## 🌐 Live Demo

- **Web Application (Vercel):** [https://solar-wind-deployment-intelligence.vercel.app/](https://solar-wind-deployment-intelligence.vercel.app/)
- **Backend API & OpenAPI Docs (Render):** [https://solar-wind-deployment-intelligence.onrender.com/docs](https://solar-wind-deployment-intelligence.onrender.com/docs)

---

## ✨ Key Features

- 🌍 **Geospatial & Climate Data Integration:** Automatically fetches and computes data from NASA POWER (solar irradiance & temp), Global Wind Atlas (50m/100m wind speeds), OpenStreetMap (road & grid distance), and SRTM (elevation & slope).
- 🧠 **ML Suitability Scoring Engine:** Trained Random Forest Regressor predicts site viability based on environmental parameters, topography, and infrastructure constraints.
- ⚡ **12-Month Energy Forecasting:** Generates monthly kWh/m² energy yield curves tailored for Solar, Wind, or Hybrid deployment strategies.
- 💰 **Financial Feasibility Analysis:** Dynamically calculates Initial Capital Expenditure (CAPEX), Operational Cost (OPEX), Levelized Cost of Energy (LCOE), ROI, and Payback Period based on configurable target capacity (MW).
- 🗺️ **Interactive Geographic Map:** Built with Leaflet, offering click-to-select coordinate pinning, latitude/longitude validation, and elevation profile visualization.
- 📄 **Instant PDF Export:** One-click generation of comprehensive PDF executive summary reports using `jsPDF` and `html2canvas`.
- 📊 **Multi-Site Comparison Grid:** Compare up to 3 candidate sites side-by-side on metrics like GHI, Wind Speed, Elevation, and ROI.
- ⚡ **High Performance & Zero-Friction:** In-memory `@lru_cache` pipeline caching on the backend and LocalStorage persistence on the frontend eliminate deployment bottlenecks and login friction.
- 🛡️ **Bulletproof UI Resilience:** Integrated React `ErrorBoundary` safeguards and fallback state handling guarantee 100% uptime with zero blank screen crashes.

---

## 📐 Architecture & Workflow

```mermaid
graph TD
    subgraph Client ["🖥️ Client Layer (Vercel)"]
        UI["React 18 Dashboard & Site Analysis"]
        Map["Leaflet Map Locator"]
        Storage["LocalStorage (Projects & History Fallback)"]
        EB["React ErrorBoundary"]
    end

    subgraph API Gateway ["⚙️ Backend Layer (Render)"]
        FastAPI["FastAPI App (Python 3.11)"]
        CORS["CORS Middleware"]
        PublicAPI["Public & Authenticated Endpoints"]
    end

    subgraph Processing ["🧠 Pipeline & Inference Engine"]
        Cache["LRU Cache Layer"]
        Pipeline["Analysis Pipeline Coordinator"]
        MLModel["Random Forest Model (R² = 0.89)"]
        EnergyCalc["Energy Yield & 12-Month Forecaster"]
        FinCalc["Financial Feasibility Engine"]
    end

    subgraph Data Sources ["🌍 Data & Infrastructure Layer"]
        NASA["NASA POWER API"]
        GWA["Global Wind Atlas API"]
        OSM["OpenStreetMap Services"]
        SRTM["SRTM Elevation Provider"]
        DB[("PostgreSQL + PostGIS (Optional Persisted Mode)")]
    end

    UI <--> |REST JSON| FastAPI
    Map --> UI
    UI <--> Storage
    EB --> UI
    
    FastAPI --> CORS --> PublicAPI --> Pipeline
    Pipeline <--> Cache
    Pipeline --> MLModel
    Pipeline --> EnergyCalc
    Pipeline --> FinCalc
    
    Pipeline <--> NASA
    Pipeline <--> GWA
    Pipeline <--> OSM
    Pipeline <--> SRTM
    FastAPI <-.-> |Optional Auth/DB| DB
```

---

## 🛠️ Technology Stack

### Backend
- **Framework & Server:** Python 3.11+, FastAPI, Uvicorn
- **Machine Learning & Data Science:** Scikit-learn, Pandas, NumPy, Joblib
- **Geospatial & Topography:** GeoPandas, Rasterio, Shapely, PyProj
- **Performance & Caching:** Python `functools.lru_cache`, In-Memory Cache
- **Database & ORM (Optional Mode):** PostgreSQL 15, PostGIS 3.3, SQLAlchemy 2.0, Alembic
- **Testing:** Pytest (160+ unit & integration tests)

### Frontend
- **Framework & Tooling:** React 18, Vite 5, React Router DOM v6
- **Maps & Charts:** Leaflet, React-Leaflet, Recharts, Lucide React
- **Document Export:** jsPDF, html2canvas
- **HTTP Client:** Axios with response interceptors
- **Styling:** CSS3 Design Tokens & Glassmorphism Aesthetics

### Hosting & Infrastructure
- **Frontend Hosting:** Vercel (CD/CI connected to `master`)
- **Backend Hosting:** Render.com (Python 3.11 Docker Web Service)

---

## 📁 Project Structure

```
solar-wind-deployment-intelligence/
├── backend/
│   ├── alembic/                  # Database migration scripts
│   ├── app/
│   │   ├── api/                  # FastAPI routers (analysis, projects, auth, reports)
│   │   ├── data_sources/         # Geospatial integrations (NASA, GWA, OSM, SRTM)
│   │   ├── schemas/              # Pydantic data schemas
│   │   ├── services/             # Core analysis pipeline, ML inference, financial models
│   │   └── main.py               # FastAPI application entry point
│   ├── models/                   # Trained Random Forest models (.joblib)
│   ├── tests/                    # Pytest suite
│   ├── Dockerfile                # Docker configuration
│   └── requirements.txt          # Python dependencies
├── frontend/
│   ├── public/                   # Static assets
│   ├── src/
│   │   ├── api/                  # API communication wrappers
│   │   ├── components/           # UI components (MapLocator, Charts, ErrorBoundary, Sidebar)
│   │   ├── pages/                # Page views (Dashboard, SiteAnalysis, Projects, Reports)
│   │   ├── services/             # Axios client & LocalStorage fallback handlers
│   │   ├── App.jsx               # Main application routing
│   │   └── main.jsx              # Application entry
│   ├── package.json              # Node.js dependencies
│   ├── vercel.json               # Vercel deployment configuration & Cache-Control rules
│   └── vite.config.js            # Vite build setup
├── docs/                         # Project documentation and performance metrics
├── docker-compose.yml            # PostgreSQL + PostGIS local container setup
├── render.yaml                   # Render deployment specification
└── README.md                     # Project documentation
```

---

## 🚀 Quick Start & Local Setup

### Prerequisites
- **Node.js** 18+
- **Python** 3.11+
- **Git**

### 1. Clone the Repository
```bash
git clone https://github.com/Smita-Mhatugade/Solar_-_Wind_Deployment_Intelligence_Platform.git
cd Solar_-_Wind_Deployment_Intelligence_Platform
```

### 2. Backend Setup
Navigate to the `backend` directory, create a virtual environment, and install dependencies:

```bash
cd backend
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

Start the FastAPI local development server:
```bash
python -m uvicorn app.main:app --reload --port 8000
```
> 🔗 **Local Swagger API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Frontend Setup
Open a **new terminal**, navigate to the `frontend` folder, install dependencies, and launch Vite:

```bash
cd frontend
npm install
npm run dev
```
> 🔗 **Local Application:** [http://localhost:5173/](http://localhost:5173/)

---

## 📡 API Reference

All backend endpoints are accessible without friction in public mode.

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/` | Health check & API status | ❌ |
| `POST` | `/api/v1/analysis/` | Run full unified analysis (ML Score, Energy Forecast, Financial Metrics) | ❌ |
| `GET` | `/api/v1/analysis/history` | Retrieve historical site analyses | ❌ |
| `DELETE` | `/api/v1/analysis/history/{id}` | Delete a saved site analysis | ❌ |
| `GET` | `/api/v1/projects/` | List saved deployment projects | ❌ |
| `POST` | `/api/v1/projects/` | Create a new deployment project | ❌ |

---

## ⚙️ Environment Variables & Configuration

### Frontend (`frontend/.env`)
```env
VITE_API_URL=https://solar-wind-deployment-intelligence.onrender.com/api/v1
```
*(For local testing, set `VITE_API_URL=http://localhost:8000/api/v1`)*

### Backend (`backend/.env` - Optional DB Mode)
```env
PROJECT_NAME="Solar & Wind Deployment Intelligence Platform"
API_V1_STR="/api/v1"
CORS_ORIGINS=["http://localhost:5173","https://solar-wind-deployment-intelligence.vercel.app"]
# DATABASE_URL=postgresql://user:password@localhost:5432/solar_wind_db
```

---

## 🔄 Recent Changes & Enhancements

- **Instant Public Tool Deployment:** Transformed the application into an open-access public intelligence tool, eliminating login/registration barriers and Neon database dependency issues.
- **LocalStorage & In-Memory Fallbacks:** Integrated seamless browser `localStorage` fallbacks in `api.js` for project saving and analysis history, backed by `@lru_cache` on FastAPI.
- **UI Crash Prevention (ErrorBoundary):** Created a dedicated React `ErrorBoundary` component to catch runtime exceptions gracefully.
- **Defensive Property Handling:** Safeguarded all numeric property formatting (`Number(val || 0).toFixed()`) across all components to prevent React unmounting errors.
- **Vercel Caching Optimization:** Added custom `Cache-Control: no-cache, no-store, must-revalidate` rules in `vercel.json` to prevent browsers from caching stale JavaScript bundles.

---

## 🔮 Future Scope

- 🛰️ **High-Resolution Satellite Imagery Integration:** Ingest Sentinel-2 & Landsat 8 multispectral band imagery for automatic land cover (NDVI) classification.
- ⚡ **Grid Connection Capacity Mapping:** Overlay high-voltage transmission line substations and capacities to estimate grid connection costs.
- 📈 **Real-Time Battery Storage (BESS) Modeling:** Evaluate battery storage pairing (Solar + Storage / Wind + Storage) for peak shaving and energy arbitrage.
- 🌍 **Global Policy & Tariff Simulator:** Incorporate country-specific feed-in tariffs, carbon credits, and tax incentives.

---

## 📜 License & Acknowledgements

This project is licensed under the **MIT License**.

Developed by **Smita Mhatugade** as part of the **Infosys Springboard Virtual Internship Program**.

**Data Sources & Providers:**
- [NASA POWER Project](https://power.larc.nasa.gov/) — Solar irradiance & meteorological datasets
- [Global Wind Atlas](https://globalwindatlas.info/) — Wind speed resource datasets
- [OpenStreetMap](https://www.openstreetmap.org/) — Infrastructure & road spatial data
- [SRTM](https://www2.jpl.nasa.gov/srtm/) — NASA Shuttle Radar Topography Mission elevation models

---

<div align="center">
  <sub>Built with ❤️ for a cleaner, sustainable energy future.</sub>
</div>
