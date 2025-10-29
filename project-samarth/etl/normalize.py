"""Minimal normalization: read sample CSVs and produce cleaned files used by backend.
Example normalizations:
- lowercasing crop names
- ensure numeric columns are floats
- map state names to canonical names (simple mapping)
"""
import pandas as pd
from pathlib import Path

DATA_DIR = Path('backend/sample_data')

# Crop production sample normalizer
cp = pd.read_csv(DATA_DIR / 'crop_production_sample.csv')
# basic normalize
cp['crop_norm'] = cp['crop'].str.lower().str.strip()
cp['production_tonnes'] = pd.to_numeric(cp['production_tonnes'], errors='coerce').fillna(0)
cp.to_csv(DATA_DIR / 'crop_production_norm.csv', index=False)
print('Wrote crop_production_norm.csv')

# Rainfall sample normalizer
rf = pd.read_csv(DATA_DIR / 'imd_rainfall_sample.csv')
rf['state_norm'] = rf['state'].str.lower().str.strip()
rf['annual_rainfall_mm'] = pd.to_numeric(rf['annual_rainfall_mm'], errors='coerce').fillna(0)
rf.to_csv(DATA_DIR / 'imd_rainfall_norm.csv', index=False)
print('Wrote imd_rainfall_norm.csv')
