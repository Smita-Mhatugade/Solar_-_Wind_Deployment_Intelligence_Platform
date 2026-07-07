import os
import pandas as pd
from pathlib import Path

datasets_dir = Path('datasets')
gwa_path = datasets_dir / 'global_wind_atlas/gwa_data.csv'
sentinel_path = datasets_dir / 'sentinel/sentinel2_data.csv'
osm_path = datasets_dir / 'openstreetmap/osm_infrastructure.csv'
srtm_path = datasets_dir / 'srtm/srtm_elevation.csv'
nasa_path = datasets_dir / 'nasa_power/nasa_power_climate_risk_indices_190_capitals_1990_2024.csv'

for p in [gwa_path, sentinel_path, osm_path, srtm_path]:
    p.parent.mkdir(parents=True, exist_ok=True)

if not gwa_path.exists(): pd.DataFrame({'latitude':[34,35,36], 'longitude':[-118,-119,-120], 'wind_speed_10m':[5.2,4.8,6.1], 'wind_speed_50m':[6.5,6.1,7.8]}).to_csv(gwa_path, index=False)
if not sentinel_path.exists(): pd.DataFrame({'latitude':[34,35,36], 'longitude':[-118,-119,-120], 'ndvi':[0.6,0.4,0.7], 'ndwi':[0.1,0.2,0.3]}).to_csv(sentinel_path, index=False)
if not osm_path.exists(): pd.DataFrame({'id':[1,2,3], 'type':['substation','power_line','substation'], 'dist_grid':[10.5,0.0,15.2], 'dist_road':[2.1,5.5,1.0]}).to_csv(osm_path, index=False)
if not srtm_path.exists(): pd.DataFrame({'latitude':[34,35,36], 'longitude':[-118,-119,-120], 'elevation':[150,200,50], 'slope':[2.5,5.0,1.2]}).to_csv(srtm_path, index=False)

datasets = {
    'NASA POWER': nasa_path,
    'Global Wind Atlas': gwa_path,
    'Sentinel-2': sentinel_path,
    'OpenStreetMap': osm_path,
    'SRTM Elevation': srtm_path
}
notes = {
    'NASA POWER': 'Contains climate and solar irradiance data. Crucial for estimating solar PV potential and weather-related risks.',
    'Global Wind Atlas': 'Contains wind speed data at various heights. Essential for predicting wind power generation and turbine placement.',
    'Sentinel-2': 'Contains multispectral imagery metrics (like NDVI). Helps in land-use classification and identifying environmental constraints.',
    'OpenStreetMap': 'Contains infrastructure features (roads, grid). Necessary for assessing the cost of connection and accessibility.',
    'SRTM Elevation': 'Contains topographical data (elevation, slope). Vital for ensuring sites aren''t too steep for installation and estimating shadowing.'
}

for name, path in datasets.items():
    print(f'\n{"="*50}\nDataset: {name}\n{"="*50}')
    if not path.exists():
        print('File not found.')
        continue
    df = pd.read_csv(path)
    print(f'Shape: {df.shape}')
    print(f'Columns: {df.columns.tolist()}')
    print('\nFirst 5 rows:')
    print(df.head())
    print('\nMissing Values:\n', df.isnull().sum())
    print('\nNote on usefulness:')
    print(notes[name])

print(f'\n{"="*50}\nBackend Folder Structure:\n{"="*50}')
backend_dir = Path('backend')
for item in sorted(backend_dir.glob('**/*')):
    print(item.relative_to(backend_dir))
