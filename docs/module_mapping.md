# Module Mapping

This document outlines the core modules of the Solar & Wind Deployment Intelligence Platform and their responsibilities.

## 1. Authentication
- **Responsibilities**: Handles user registration, login, JWT token generation, role-based access control, and session management.

## 2. Solar Prediction
- **Responsibilities**: Processes meteorological data (NASA POWER) to train models and predict solar energy yield (kWh/m²) for specific geographic coordinates.

## 3. Wind Prediction
- **Responsibilities**: Processes wind and climate data (Global Wind Atlas, NASA POWER) to evaluate wind speed, power density, and predict energy yield for wind turbines.

## 4. Site Suitability
- **Responsibilities**: Integrates solar and wind predictions with terrain (SRTM), land use (Sentinel-2), and infrastructure (OSM) data to calculate an overall site viability score (0-100).

## 5. Database
- **Responsibilities**: Manages the storage, retrieval, and relational integrity of user profiles, projects, site metadata, environmental data, predictions, and reports using an ORM framework.

## 6. Reports
- **Responsibilities**: Compiles predictions, suitability scores, and site data into comprehensive, downloadable summaries (PDF/Markdown) for stakeholders.

## 7. Dashboard
- **Responsibilities**: The frontend user interface that visualizes projects, interactive maps, metric charts, predictions, and site comparisons.

## 8. API Services
- **Responsibilities**: The central backend routing layer that exposes endpoints (REST/GraphQL) for the frontend to interact with the authentication, prediction, and database modules.
