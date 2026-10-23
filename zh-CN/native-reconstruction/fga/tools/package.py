#!/usr/bin/env python3
"""Package this native project and expand its one-file TeX edition. No network."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
units = ["fga-foreword", "fga1", "fga2", "fga3.i", "fga3.ii", "fga3.iii", "fga3.iv", "fga3.v", "fga3.vi"]
for unit in units:
    if not (ROOT / "chapters" / (unit + ".tex")).is_file():
        raise SystemExit("Missing translated leaf: " + unit)
text = (ROOT / "main.tex").read_text()
for path in ["preamble", *["chapters/" + unit for unit in units]]:
    needle = "\\input{" + path + "}"
    if text.count(needle) != 1:
        raise SystemExit("Unexpected input multiplicity: " + path)
    text = text.replace(needle, "\n% BEGIN " + path + ".tex\n" + (ROOT / (path + ".tex")).read_text() + "\n% END " + path + ".tex\n")
if re.search(r"\\(?:input|include|includegraphics)\s*\{", text):
    raise SystemExit("One-file edition still has a local file dependency")
bib = (ROOT / "fga-bibliography.bib").read_text()
standalone = "% Native Chinese working draft; public TeX/font dependencies remain required.\n"
standalone += "\\begin{filecontents*}{fga-bibliography.bib}\n" + bib + "\n\\end{filecontents*}\n" + text
(OUT / "FGA-zh-working-standalone.tex").write_text(standalone)

def included(path):
    rel = path.relative_to(ROOT)
    if not path.is_file() or any(part in {"build", "__pycache__", ".git"} for part in rel.parts):
        return False
    if rel.parts[0] == "outputs":
        return rel.name == "FGA-zh-working-standalone.tex"
    # Generated TeX outputs may also sit next to a driver; keep the source ZIP clean.
    if path.suffix.lower() in {".pdf", ".aux", ".bbl", ".blg", ".fls", ".log", ".out", ".toc", ".xdv", ".synctex", ".gz"}:
        return False
    if rel.name.endswith(("-blx.bib", ".run.xml", ".fdb_latexmk")):
        return False
    return rel.name not in {"SOURCE_PACKAGE_MANIFEST.json", "SHA256SUMS.txt"} and path.suffix != ".pyc"

files = sorted(p for p in ROOT.rglob("*") if included(p))
manifest = {"format": "sha256", "files": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
manifest_path = ROOT / "SOURCE_PACKAGE_MANIFEST.json"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
files.append(manifest_path)
with zipfile.ZipFile(OUT / "FGA-zh-working-source.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in sorted(files):
        info = zipfile.ZipInfo(str(path.relative_to(ROOT)), date_time=(2026, 10, 21, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, path.read_bytes())
print("Wrote native one-file TeX and source ZIP; clean rebuild must be checked separately.")
