# functions to compute aggregates and build answers with provenance
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent / 'sample_data'

def avg_annual_rainfall(states, year_from, year_to):
    rf = pd.read_csv(DATA_DIR / 'imd_rainfall_norm.csv')
    out = {}
    for s in states:
        df = rf[(rf['state_norm']==s.lower()) & (rf['year']>=year_from) & (rf['year']<=year_to)]
        if df.empty:
            out[s] = {'avg_mm': None, 'source': None}
        else:
            out[s] = {'avg_mm': df['annual_rainfall_mm'].mean(), 'source': df['source_url'].unique().tolist()}
    return out

def top_crops_by_state(states, year_from, year_to, topn=3):
    cp = pd.read_csv(DATA_DIR / 'crop_production_norm.csv')
    out = {}
    for s in states:
        df = cp[(cp['state'].str.lower()==s.lower()) & (cp['year']>=year_from) & (cp['year']<=year_to)]
        agg = df.groupby('crop_norm', as_index=False)['production_tonnes'].sum().sort_values('production_tonnes', ascending=False).head(topn)
        out[s] = [{'crop': r['crop_norm'], 'tons': int(r['production_tonnes']), 'source': df['source_url'].unique().tolist()} for _, r in agg.iterrows()]
    return out

def assemble_compare(states, year_from, year_to, topn=3):
    rain = avg_annual_rainfall(states, year_from, year_to)
    crops = top_crops_by_state(states, year_from, year_to, topn)
    return {'rainfall': rain, 'topcrops': crops}
