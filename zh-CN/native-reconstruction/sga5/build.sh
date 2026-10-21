#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
mkdir -p .build
export TEXMFHOME="$PWD/texmf"
export XDG_CACHE_HOME="${TMPDIR:-/tmp}/sga5-tex-cache"
mkdir -p "$XDG_CACHE_HOME"
for pass in 1 2 3; do
  xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder -output-directory=.build SGA5-zh-CN.tex > ".build/pass-${pass}.stdout" 2>&1
done
cp .build/SGA5-zh-CN.pdf SGA5-zh-CN.pdf
