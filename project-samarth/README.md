# Project Samarth — Minimal Prototype

This repository contains a minimal end-to-end prototype for Project Samarth:
an intelligent Q&A system that queries crop production and IMD rainfall data
(sample) and returns answers with provenance.

## Requirements
- Python 3.10+
- pip

## Setup
1. Create virtual env & install:
```bash
python -m venv venv
source venv/bin/activate    # on Windows use venv\Scripts\activate
pip install -r requirements.txt
```

2. Run ETL (creates normalized CSVs in backend/sample_data):
```bash
python etl/download.py --manifest etl/sample_manifest.json
python etl/normalize.py
```

3. Start backend (FastAPI):
```bash
cd backend
uvicorn app:app --reload --port 8000
```

4. Open `frontend/index.html` in your browser (or run a simple HTTP server):
```bash
python -m http.server 8080 --directory frontend
# then open http://localhost:8080
```

## Testing the prototype
Open the frontend, type a sample question (examples included in UI), and press Ask.
The backend will answer using the included sample CSVs and provide inline citations pointing
to the original resource (sample URLs). See `assemble.py` for citation format.

## Recording Loom
Use the included Loom script (LOOM_SCRIPT.md) found in the repo root and follow the storyboard.

