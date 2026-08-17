from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
errors=[]
notebooks=sorted((ROOT/'notebooks').glob('*.ipynb'))
if len(notebooks)!=30:
    errors.append(f'expected 30 notebooks, found {len(notebooks)}')
for p in notebooks:
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'invalid notebook {p.name}: {e}')
paper=ROOT/'paper'/'Private_Is_Not_Privileged.docx'
if not paper.exists(): errors.append('paper missing')
manifest=ROOT/'SHA256SUMS.txt'
if manifest.exists():
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        expected, rel=line.split('  ',1)
        p=ROOT/rel
        if not p.exists():
            errors.append(f'missing file: {rel}'); continue
        h=hashlib.sha256()
        with p.open('rb') as f:
            for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
        if h.hexdigest()!=expected: errors.append(f'checksum mismatch: {rel}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(notebooks)} notebooks parsed; paper present; checksums verified.')
