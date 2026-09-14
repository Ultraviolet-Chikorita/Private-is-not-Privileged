from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

# README/navigation documentation may be improved after a research bundle is frozen.
# Scientific artifacts and the existing provenance documents remain checksum-verified.
MUTABLE_DOCUMENTATION = {"README.md"}

notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
if len(notebooks) != 30:
    errors.append(f"expected 30 notebooks, found {len(notebooks)}")

for notebook in notebooks:
    try:
        json.loads(notebook.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid notebook {notebook.name}: {exc}")

paper = ROOT / "paper" / "Private_Is_Not_Privileged.docx"
if not paper.exists():
    errors.append("paper missing")

manifest = ROOT / "SHA256SUMS.txt"
verified = 0
skipped_mutable = 0
if manifest.exists():
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue

        expected, rel = line.split("  ", 1)
        if rel in MUTABLE_DOCUMENTATION:
            skipped_mutable += 1
            continue

        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing file: {rel}")
            continue

        file_hash = hashlib.sha256()
        with path.open("rb") as file_handle:
            for chunk in iter(lambda: file_handle.read(1024 * 1024), b""):
                file_hash.update(chunk)

        if file_hash.hexdigest() != expected:
            errors.append(f"checksum mismatch: {rel}")
        else:
            verified += 1
else:
    errors.append("SHA256SUMS.txt missing")

if errors:
    raise SystemExit("\n".join(errors))

print(
    f"OK: {len(notebooks)} notebooks parsed; paper present; "
    f"{verified} frozen checksum entries verified; "
    f"{skipped_mutable} mutable documentation entry skipped."
)
