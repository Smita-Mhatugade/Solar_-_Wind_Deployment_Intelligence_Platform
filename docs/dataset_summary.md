# Dataset Summary

This document provides a summary of the datasets used in the Solar & Wind Deployment Intelligence Platform, based on the `dataset_analysis_report.md`.

## 1. NASA POWER Dataset

### Rows & Columns
- **Rows**: 6,651
- **Columns**: 53

### Column Names & Data Types
| Column Name | Data Type | Group |
|---|---|---|
| `city` | string | Location & Metadata |
| `iso_alpha3` | string | Location & Metadata |
| `latitude` | float | Location & Metadata |
| `longitude` | float | Location & Metadata |
| `continent` | string | Location & Metadata |
| `who_region` | string | Location & Metadata |
| `wb_income_group` | string | Location & Metadata |
| `year` | int | Location & Metadata |
| `data_days` | float | Location & Metadata |
| `temp_mean_c` | float | Temperature |
| `temp_max_c` | float | Temperature |
| `temp_min_c` | float | Temperature |
| `temp_std_c` | float | Temperature |
| `temp_range_mean_c` | float | Temperature |
| `temp_seasonal_amp` | float | Temperature |
| `temp_yoy_change` | float | Temperature |
| `temp_5yr_mean` | float | Temperature |
| `temp_anomaly` | float | Temperature |
| `days_above_35c` | int / float | Extreme Temperature |
| `days_above_40c` | int / float | Extreme Temperature |
| `days_below_0c` | int / float | Extreme Temperature |
| `days_below_minus10c` | int / float | Extreme Temperature |
| `heat_stress_index` | float | Extreme Temperature |
| `cold_stress_index` | float | Extreme Temperature |
| `solar_total_mj` | float | Solar Energy |
| `solar_mean_mj` | float | Solar Energy |
| `solar_clear_mean_mj` | float | Solar Energy |
| `solar_clearness_idx` | float | Solar Energy |
| `solar_peak_days` | int / float | Solar Energy |
| `solar_annual_kwh_m2` | float | Solar Energy |
| `ideal_climate_days` | int / float | Solar Energy |
| `wind_mean_ms` | float | Wind Energy |
| `wind_max_ms` | float | Wind Energy |
| `wind_std_ms` | float | Wind Energy |
| `high_wind_days` | int / float | Wind Energy |
| `wind_power_density` | float | Wind Energy |
| `precip_total_mm` | float | Precipitation |
| `precip_mean_mm` | float | Precipitation |
| `precip_max_day_mm` | float | Precipitation |
| `precip_std_mm` | float | Precipitation |
| `precip_yoy_change` | float | Precipitation |
| `days_heavy_rain` | int / float | Precipitation |
| `days_moderate_rain` | int / float | Precipitation |
| `days_dry` | int / float | Precipitation |
| `rh_mean_pct` | float | Humidity |
| `rh_max_pct` | float | Humidity |
| `dewpoint_mean_c` | float | Humidity |
| `humidity_stress_days` | int / float | Humidity |
| `gdp_per_capita_usd` | float | Socioeconomic |
| `population` | int / float | Socioeconomic |
| `urban_pop_pct` | float | Socioeconomic |
| `energy_use_kg_oil_eq` | float | Socioeconomic |
| `pressure_mean_kpa` | float | Atmospheric |
| `pressure_std_kpa` | float | Atmospheric |
| `climate_volatility` | float | Atmospheric |

### Missing Values
- **`temp_yoy_change`, `temp_5yr_mean`, `temp_anomaly`, `solar_clearness_idx`**: Missing for years 1990 and 1991 (expected due to lack of prior data for rolling calculations).
- **`energy_use_kg_oil_eq`**: Missing for 2024 (expected due to data reporting lag).

### Unnecessary Columns
Based on the analysis context, the following columns are likely unnecessary or of secondary importance for the core Solar & Wind prediction models, and can be considered for removal during feature selection:
- `who_region` (WHO region code - less relevant than lat/lon or continent)
- `wb_income_group` (Socioeconomic, not meteorological)
- `gdp_per_capita_usd` (Socioeconomic, not meteorological)
- `population` (Socioeconomic, not meteorological)
- `urban_pop_pct` (Socioeconomic, not meteorological)
- `energy_use_kg_oil_eq` (Socioeconomic, not meteorological)
- `wind_mean_ms` from NASA POWER is a 10m surface observation, which is generally considered unrepresentative for wind turbine operations compared to 50m/100m data from the Global Wind Atlas.

---

## 2. Global Wind Atlas Dataset (Sample)
- **Rows & Columns**: 3 rows × 4 columns
- **Column Names & Data Types**: `latitude` (float), `longitude` (float), `wind_speed_10m` (float), `wind_speed_50m` (float)
- **Missing Values**: None in sample, but real dataset requires `wind_speed_100m`, `wind_direction`, `wind_power_density`, `capacity_factor`.
- **Unnecessary Columns**: `wind_speed_10m` is less useful as turbines operate at 80-120m hub height.

## 3. Sentinel-2 Dataset (Sample)
- **Rows & Columns**: 3 rows × 4 columns
- **Column Names & Data Types**: `latitude` (float), `longitude` (float), `ndvi` (float), `ndwi` (float)
- **Missing Values**: None in sample, but real dataset requires `land_cover_class`, `cloud_cover_pct`, `slope`.
- **Unnecessary Columns**: None identified.

## 4. OpenStreetMap (OSM) Infrastructure Dataset (Sample)
- **Rows & Columns**: 3 rows × 4 columns
- **Column Names & Data Types**: `id` (int), `type` (string), `dist_grid` (float), `dist_road` (float)
- **Missing Values**: None in sample, but real dataset requires `lat`, `lon`, `voltage_level`, `substation_capacity_mva`.
- **Unnecessary Columns**: `road_type` is considered low priority.

## 5. SRTM Elevation Dataset (Sample)
- **Rows & Columns**: 3 rows × 4 columns
- **Column Names & Data Types**: `latitude` (float), `longitude` (float), `elevation` (float), `slope` (float)
- **Missing Values**: None in sample.
- **Unnecessary Columns**: None identified.
