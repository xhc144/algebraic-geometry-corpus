#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
python3 assemble.py
mkdir -p build/texmf
# Pinned LPPL TeX runtime packages; no fonts or network downloads are needed here.
for package in dependencies/*.tar.xz; do
  tar -xf "$package" -C build/texmf --wildcards 'tex/*'
done
export TEXMFHOME="$PWD/build/texmf"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:-/tmp/sga7ii-cache}"
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=build main.tex >build/pass1.txt 2>&1
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=build main.tex >build/pass2.txt 2>&1
cp build/main.pdf SGA7-II-zh-CN.pdf
