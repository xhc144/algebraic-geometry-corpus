#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p build
export TEXINPUTS="./dependencies//:${TEXINPUTS-}"
export XDG_CACHE_HOME="${TMPDIR:-/tmp}/sga6-font-cache"
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -recorder -output-directory=build -jobname=SGA6-zh-CN main.tex >build/compile-pass1.txt 2>&1
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -recorder -output-directory=build -jobname=SGA6-zh-CN main.tex >build/compile-pass2.txt 2>&1
