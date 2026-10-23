# Independent navigation and TOC review

- Reviewed 2026-10-23 using GPT-6.1 sol; no Astra or paid API. Scope is the resumed navigation/TOC work only, not a repeat of the complete 354-page independent source-fidelity audit.
- Original source independently hashed, read only: `FGA/FGA-Explained-Fantechi-AMS-2005.pdf`, SHA-256 `17ebc9fd0ad15cc352d461c4515199377e64d905f0d5e08c6b3b90c25b43ed8d`.
- Final inspected deliverable: `FGA-explained-zh-CN.pdf`, 313 physical pages, SHA-256 `6b75d174b8fb0e7b3d06c4e5dd690c6e32df5e59c5a9231152d394f12498e8fd`. Validation was against this actual PDF, its annotations and named destinations, the final AUX/TOC, and the native sources. Earlier-build PDF findings were rechecked after rebuilding.

## Code, preservation, and interval policy

Read `source-navigation.tex`, `scripts/source_navigation.py`, `backmatter/source-page-map.tex`, `backmatter/index.tex`, `main.tex`, and the Part-author macro in `book-style.tex`.

Independently recomputed the required body-anchor set as source PDF13–351 less the eleven recorded blank pages: exactly 328 anchors, with no missing or extra body anchor. There are 340 total canonical source anchors including front/end matter. Independently recomputed all 339 map rows' strict predecessor/successor nonblank source anchors, including first/last-page fallback and blank-page handling; all agree. Source PDF number is original printed number plus 12 in every row.

The displayed Chinese interval uses the preceding and following source anchors and expands one translated page at each end, clamping its start to the first main-matter page. This is a conservative search window with intentional overlaps. The PDF's explanation explicitly says it does not represent exact word-for-word pagination. The generated map and evidence make no false exact-pagination claim. This bounded review does not prove every source page's entire translated content fits its window; source-anchor placement relies on the completed separate source audit, with the five direct checks below corroborating usefulness.

Unwrapped all `sourceindex` calls and removed only the new source-anchor comments/calls; the remaining index is exactly identical to the repository HEAD index. Independently recounted 269 main entries + 379 subentries + 88 second subentries = 736 entries, and 716 original page references. All original entry text, ordering, hierarchy, and reference numbers are preserved.

## Actual PDF navigation

An independent temporary PyMuPDF checker (not the production audit script) extracted all rendered map rows and all PDF annotations/named destinations. It verified:

- All 339 original pages have one correctly located map destination and one rendered row, with correct original/source numbers, blank-page stars, Chinese printed ranges, and Chinese physical-PDF ranges. Printed ranges were independently checked against AUX labels; physical ranges against actual source-anchor named-destination pages.
- Exactly 716 actual index-to-map annotations on physical PDF295–302. Their target-number multiset exactly equals the preserved original index reference multiset, not merely its unique-page set. All targets resolve to the map page containing the corresponding row.
- Exactly 339 actual map-to-physical-page annotations. Each annotation rectangle contains the correct displayed Chinese printed-range text, and its `nativeabs.N` target matches that row's displayed physical-PDF range start and resolves to physical page N. End numbers were also checked against the independently recomputed endpoint range.
- Exactly 313 dedicated `nativeabs.N` destinations cover every physical page 1–313 without a numbering gap. Every target resolves to its own physical page. Every target's raw PDF vertical coordinate equals that page's height (rounded to 0.001 point), so the targets lie at the page top and within its bounds.

Found and reported one defect in the preceding build (SHA-256 `1b8efc55e02c54a5c4315a172df664cf4461cad23d23089b3a00e4021871f2a7`): the shipout hook's raised link placed physical-page destinations 13.39 points above the page top. Parent removed the raising wrapper and rebuilt. All 313 final destinations pass the bounds/top-position check. Named-destination coordinates here use raw PDF bottom-left coordinates; this was explicitly distinguished from text/annotation rectangle top-left coordinates during the check.

## TOC and visual inspection

Actually opened original scanned TOC PDF10–12 and final native TOC PDF10–12. All 71 original visible structural entries are present, plus the clearly editorial source-page-map entry. All five Part authors are correctly retained on separate indented lines: Angelo Vistoli; Nitin Nitsure; Barbara Fantechi and Lothar Göttsche; Luc Illusie; Steven L. Kleiman. The longer Part IV entry wraps cleanly. Chinese page numbers describe translated pagination, rather than retaining the source pagination.

Independently checked all 72 visible-level TOC entries' named destinations against the final PDF: 71 Arabic entries resolve to their displayed translated page (physical offset +13), and the prefatory `vii` entry resolves to physical PDF6. All 78 actual TOC link annotations resolve; split title/author links account for annotation count exceeding entry count. No missing original TOC entry or author found.

Actually opened all eight rendered map pages PDF306–313: headers, columns, longtable continuations, range digits, blank-page markers, and the last row are readable, with no observed collision or clipping. Reopened final first/last TOC/map views after the anchor fix; the fix changes destination coordinates without changing visible content.

## Direct source/native lookup checks

Opened actual source scans and native rendered pages for each case, also read the nearby TeX source. These are navigation checks of recognizable content, not a new full translation review.

| Original printed page | Source PDF | Displayed Chinese printed interval | Displayed Chinese PDF interval | Directly observed relevant material |
| --- | ---: | --- | --- | --- |
| 7 | 19 | 3–6 | 16–19 | Chapter 1 / algebraic geometry, finite presentation, definitions 1.1 and 1.3 and Proposition 1.2, native PDF18 / printed 5. |
| 143 | 155 | 118–122 | 131–135 | Chapter 6 / elementary deformation theory, conventions 6.0.1 and 6.1.1, Artin algebra category and deformation functor, native PDF134 / printed 121. |
| 223 | 235 | 185–189 | 198–202 | Abelian-scheme lifting proof, product obstruction equation and sum morphism, native PDF200–201 / printed 187–188. |
| 301 | 313 | 248–252 | 261–265 | Exercise 9.6.29 at native PDF262 / printed 249, then Appendix A heading and answers at native PDF264–265 / printed 251–252. The shared source-page boundary is retained and included by the window. |
| 319 | 331 | 264–268 | 277–281 | Duality/Riemann–Roch continuation and Theorem B.27 (Hodge index), native PDF280 / printed 267. |

## Result and limits

No remaining confirmed navigation or TOC defect; no blocker. This is independent AI review of PDF structure, rendered navigation/TOC pages, preservation, and selected source lookup cases. It is not human mathematical sign-off, a full repeat of source-content review, or interactive testing in every PDF viewer. Only this review file was edited by this reviewer; source, layout, PDFs, production scripts, originals, commits, and remote repositories were not changed by this reviewer.
