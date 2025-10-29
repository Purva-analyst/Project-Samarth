"""Simple downloader: in this demo the manifest points to local files
- For production replace URLs with data.gov.in resource CSV links and the code will download them.
"""
import json
import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--manifest', default='etl/sample_manifest.json')
args = parser.parse_args()

m = json.load(open(args.manifest))
for r in m['resources']:
    src = Path(r['url'])
    dest = Path('backend/sample_data') / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    # in prod: download via requests. Here: copy local sample
    shutil.copy(src, dest)
    print('Copied', src, '->', dest)
