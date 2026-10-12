"""Write the public copies of the working records.

The working records in ../records/ are complete and stay local: they hold the agents'
research notes, corrections to earlier entries and clear_fields reasons, which are
internal editorial history (CODEBOOK.md: the Editorial Log is never public). This script
copies every record to ../data/records/ without those keys. Source citations, coding
notes, participation notes and unverified items stay public so the data can be checked.
Run from tools/: python3 publish_records.py
"""
import json, pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent / 'records'
OUT = pathlib.Path(__file__).resolve().parent.parent / 'data' / 'records'
INTERNAL = ('research_notes', 'corrections', 'clear_fields')
for f in sorted(SRC.rglob('*.json')):
    d = json.load(open(f))
    if isinstance(d, dict):
        for k in INTERNAL: d.pop(k, None)
    out = OUT / f.relative_to(SRC)
    out.parent.mkdir(parents=True, exist_ok=True)
    json.dump(d, open(out, 'w'), ensure_ascii=False, indent=1)
    print(out.relative_to(OUT.parent.parent))
