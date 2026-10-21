# SGA3 maintained-English buildable source archive

This deterministic archive contains the active maintained-English source closure used on 2026-08-23.
It excludes generated PDFs, TeX auxiliaries, caches, QA renders, historical snapshots, credentials, and private absolute paths.

- Build driver: `source/SGA3_English_Full_Volume_Native_Cumulative.tex`
- Engine: `pdflatex`
- Selected source files: 914
- Included existing README/rights/build documents: 4
- Selection basis: active master plus every TeX source under its inputs tree; QA/build directories excluded

Run the stated engine twice from the build driver's containing directory. A normal TeX installation supplies external package dependencies.
`BUILDABLE_CLOSURE_SHA256.tsv` records every other archive member by path, byte count, and SHA-256.

The archive carries the maintained lineage's existing rights/provenance files verbatim; those files, not this packaging note, govern provenance and rights.
