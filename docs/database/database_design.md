# Database Design

This document outlines the core database tables for the Solar & Wind Deployment Intelligence Platform.

## 1. Users
- **Primary Key**: `user_id`
- **Important Columns**: `username`, `email`, `password_hash`, `role`, `created_at`
- **Description**: Stores user account information and authentication credentials for platform access.

## 2. Projects
- **Primary Key**: `project_id`
- **Important Columns**: `user_id` (FK), `project_name`, `description`, `status`, `created_at`
- **Description**: Represents a deployment project created by a user to assess specific geographic regions.

## 3. Sites
- **Primary Key**: `site_id`
- **Important Columns**: `project_id` (FK), `site_name`, `latitude`, `longitude`, `elevation`, `slope`
- **Description**: Geographic locations under consideration for solar or wind deployment within a project.

## 4. EnvironmentalData
- **Primary Key**: `data_id`
- **Important Columns**: `site_id` (FK), `year`, `temp_mean_c`, `precip_total_mm`, `rh_mean_pct`, `ndvi`
- **Description**: Annual environmental and topographical data points collected for each site.

## 5. SolarPrediction
- **Primary Key**: `solar_pred_id`
- **Important Columns**: `site_id` (FK), `solar_annual_kwh_m2`, `solar_clearness_idx`, `predicted_yield`, `confidence_score`
- **Description**: Machine learning predictions regarding solar energy yield for a given site.

## 6. WindPrediction
- **Primary Key**: `wind_pred_id`
- **Important Columns**: `site_id` (FK), `wind_speed_50m`, `wind_power_density`, `predicted_yield`, `confidence_score`
- **Description**: Machine learning predictions regarding wind energy yield for a given site.

## 7. SuitabilityScore
- **Primary Key**: `score_id`
- **Important Columns**: `site_id` (FK), `solar_score`, `wind_score`, `terrain_score`, `infrastructure_score`, `final_suitability_score`
- **Description**: Composite scores indicating the overall viability of a site for deployment.

## 8. Reports
- **Primary Key**: `report_id`
- **Important Columns**: `project_id` (FK), `site_id` (FK), `report_url`, `generated_at`, `summary`
- **Description**: Generated analysis reports for sites and projects, usually stored as downloadable documents.
