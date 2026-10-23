# Resumed independent source fidelity audit: index and Chinese end matter

- Date: 2026-10-22. Independent AI audit of the assigned full range, source PDF345–354, not a sample. No Astra model or paid API used.
- Source: `FGA/FGA-Explained-Fantechi-AMS-2005.pdf`; independently verified SHA-256 `17ebc9fd0ad15cc352d461c4515199377e64d905f0d5e08c6b3b90c25b43ed8d`.
- Locally rendered all ten pages at 150 dpi and actually opened and visually inspected each page individually: `/tmp/fga-index-audit/source-345.png` through `source-354.png`. Temporary renders are inspection aids, not deliverables.
- Compared the full native `backmatter/index.tex` against all seven scanned index pages, covering every main entry, subentry, second subentry, symbol, hierarchy, duplicate listing, and printed page-reference list. Totals independently recounted: 269 main entries, 379 subentries, 88 second subentries = 736 entries; 716 original printed page references. No confirmed fidelity defect found. Original English alphabetical order is preserved in the Chinese text.

| Source PDF | Printed page | Entries checked | Printed references checked |
| --- | --- | ---: | ---: |
| 345 | 333 | 84 | 93 |
| 346 | 334 | 112 | 102 |
| 347 | 335 | 112 | 106 |
| 348 | 336 | 111 | 108 |
| 349 | 337 | 110 | 102 |
| 350 | 338 | 110 | 107 |
| 351 | 339 | 97 | 98 |
| Total | | 736 | 716 |

- PDF352: visually checked the complete existing Chinese publisher notice, including the heading, all sentences, report telephone numbers `(010) 58581999 58582371 58582488`, fax `(010) 82086060`, email `dd@hep.com.cn`, address, department, and postcode `100120`. Native transcription is faithful; no retranslation or wording change made.
- PDF353: checked catalogue entries 1–26 in full. PDF354: checked entries 27–53 in full. Every listed person name, work title, edition/part/subtitle, translator/editor role, and all 53 thirteen-digit ISBNs were compared directly with the scans. Work titles and personal names retain source script. Entry 34 `Dmitry Chibisov（译）` and entry 39 `A. A. Ranicki（编）` faithfully retain the source role information; these Chinese role words are not defects.
- Independently checked all 53 source-read ISBNs against `evidence/reprint-catalogue.json`, all 53 `\fgaean` calls, and all 53 native barcode definition keys and visible digit labels in `figures/catalogue-barcodes.tex`: exact agreement. A local independent EAN-13 encoder also verified all 95-module native bar patterns and all check digits. Barcode source unchanged.
- Preserved printed-source peculiarities rather than silently correcting them: source index `Zariski topology, 248` (also under `topology`), `topological / group, 18`, distinct `Abelian`/`abelian` scheme listings, repeated Yoneda subdivisions, and the parent `Hilbert / scheme of points, S^{[n]}` without a page number. Catalogue entry 32 prints `Nathanial P. Brown`; retained this source spelling. Catalogue entry 51 prints `Jeffery McNeal`; retained.
- Added exactly ten canonical `% SOURCE-PAGE-ANCHOR: N` comments for PDF345–354. The seven index anchors sit at the existing source-page entry boundaries (including continuation subentries). Publisher anchor 352 is after the page setup and before the first text paragraph/minipage. Catalogue anchor 353 is after the heading and before the first longtable; anchor 354 is after the explicit page break and before the second longtable. No anchor is inside math, a table row, tabular, longtable, or TikZ.
- Final content changes: none. Source edits are only the ten page-anchor comments in the three assigned backmatter files. No layout macros, index hyperlinks, bibliography, chapter, original repository source, JSON evidence, or barcode edits made by this audit.
- Validation: assigned-file `git diff --check` passes; entry/reference totals unchanged; ISBN/EAN checks pass. The parent integration task owns the full build and translated-PDF visual check; no claim of a new integrated build is made here. Source text extraction returned no text, so source comparison was visual, not an assumption that extraction/OCR was authoritative. Optional local Tesseract corroboration was stopped before completion after the direct full visual audit; no OCR result or automated source-reference equality is claimed.
- Remaining blockers: none for this assigned fidelity audit.
