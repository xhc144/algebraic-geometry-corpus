#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")/.."
mkdir -p build
for pass in 1 2 3; do
  xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex > "build/pass-${pass}.console.txt" 2>&1
done
cp build/main.pdf SGA4-b-zh-CN.pdf
cp build/main.log evidence/final-xelatex.log
printf 'Built SGA4-b-zh-CN.pdf\n'
