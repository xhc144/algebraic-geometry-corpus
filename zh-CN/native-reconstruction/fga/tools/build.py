#!/usr/bin/env python3
"""Build only this book with explicit, restricted TeX passes."""
from pathlib import Path
import os
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)
environment = os.environ.copy()
environment["BIBINPUTS"] = str(ROOT) + os.pathsep + str(BUILD) + os.pathsep + environment.get("BIBINPUTS", "")
commands = [
    ["xelatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-recorder", "-output-directory=build", "main.tex"],
    ["bibtex", "build/main"],
    ["xelatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-recorder", "-output-directory=build", "main.tex"],
    ["xelatex", "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-recorder", "-output-directory=build", "main.tex"],
]
for index, command in enumerate(commands, 1):
    with (BUILD / f"pass-{index}.txt").open("w") as output:
        result = subprocess.run(command, cwd=ROOT, env=environment, stdout=output, stderr=subprocess.STDOUT)
    if result.returncode:
        raise SystemExit(f"Build failed: pass {index}; see build/pass-{index}.txt")
log = (BUILD / "main.log").read_text(errors="replace")
for error in ["There were undefined references", "Missing character:", "LaTeX Error", "Package fontspec Error"]:
    if error in log:
        raise SystemExit(f"Review required: {error}")
(ROOT / "outputs").mkdir(exist_ok=True)
shutil.copyfile(BUILD / "main.pdf", ROOT / "outputs/FGA-zh-working.pdf")
print("Built outputs/FGA-zh-working.pdf; eight-report Chinese draft, review status in PROGRESS.json.")
