"""
app/services/energy_estimation.py – Energy Estimation Service

Provides logic to estimate the annual energy generation (in MWh) for
Solar, Wind, and Hybrid renewable energy sites based on their installed 
capacity and capacity factor.
"""

from typing import Any, Dict

HOURS_PER_YEAR = 8760.0

def estimate_solar_energy(capacity_mw: float, capacity_factor_pct: float) -> float:
    """
    Estimate the annual solar energy generation in MWh.
    
    Formula: Capacity (MW) * (Capacity Factor / 100) * 8760 hours
    
    Args:
        capacity_mw: Installed solar capacity in Megawatts.
        capacity_factor_pct: Solar capacity factor as a percentage (0-100).
        
    Returns:
        Estimated annual solar energy in Megawatt-hours (MWh).
    """
    if capacity_mw < 0 or capacity_factor_pct < 0:
        raise ValueError("Capacity and capacity factor must be non-negative.")
    
    return capacity_mw * (capacity_factor_pct / 100.0) * HOURS_PER_YEAR


def estimate_wind_energy(capacity_mw: float, capacity_factor_pct: float) -> float:
    """
    Estimate the annual wind energy generation in MWh.
    
    Formula: Capacity (MW) * (Capacity Factor / 100) * 8760 hours
    
    Args:
        capacity_mw: Installed wind capacity in Megawatts.
        capacity_factor_pct: Wind capacity factor as a percentage (0-100).
        
    Returns:
        Estimated annual wind energy in Megawatt-hours (MWh).
    """
    if capacity_mw < 0 or capacity_factor_pct < 0:
        raise ValueError("Capacity and capacity factor must be non-negative.")
        
    return capacity_mw * (capacity_factor_pct / 100.0) * HOURS_PER_YEAR


def estimate_annual_energy(
    site_evaluation: Dict[str, Any], 
    deployment_type: str, 
    capacity_mw: float, 
    hybrid_split_ratio: float = 0.5
) -> Dict[str, float]:
    """
    Calculate the estimated annual energy generation for a site based on its 
    deployment type recommendation.
    
    For Hybrid sites, the total installed capacity is split between Solar and Wind 
    based on the hybrid_split_ratio (default 50/50 split).
    
    Args:
        site_evaluation: Dictionary containing at least:
                         'solar_capacity_factor' (%) and 'wind_capacity_factor' (%)
        deployment_type: "Solar", "Wind", or "Hybrid"
        capacity_mw: Total installed capacity in Megawatts.
        hybrid_split_ratio: The fraction (0.0 to 1.0) of capacity allocated to Solar 
                            in a Hybrid deployment. The rest goes to Wind.
                            
    Returns:
        Dictionary containing solar_energy_mwh, wind_energy_mwh, and total_energy_mwh.
    """
    if capacity_mw < 0:
        raise ValueError("Capacity must be non-negative.")
        
    # Extract capacity factors from the site evaluation
    solar_cf = site_evaluation.get("solar_capacity_factor", 0.0)
    wind_cf = site_evaluation.get("wind_capacity_factor", 0.0)
    
    solar_energy = 0.0
    wind_energy = 0.0
    
    deployment = deployment_type.strip().lower()
    
    if deployment == "solar":
        solar_energy = estimate_solar_energy(capacity_mw, solar_cf)
    elif deployment == "wind":
        wind_energy = estimate_wind_energy(capacity_mw, wind_cf)
    elif deployment == "hybrid":
        solar_capacity = capacity_mw * hybrid_split_ratio
        wind_capacity = capacity_mw * (1.0 - hybrid_split_ratio)
        
        solar_energy = estimate_solar_energy(solar_capacity, solar_cf)
        wind_energy = estimate_wind_energy(wind_capacity, wind_cf)
    else:
        # If "Not Recommended" or an unknown type is passed, returns 0.
        pass
        
    return {
        "solar_energy_mwh": round(solar_energy, 2),
        "wind_energy_mwh": round(wind_energy, 2),
        "total_energy_mwh": round(solar_energy + wind_energy, 2)
    }
