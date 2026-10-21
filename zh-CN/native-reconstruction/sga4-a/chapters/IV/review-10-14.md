# Exposé IV §§10–14 translation review

Complete supplied tail translated: §§10–14, all definitions, statements, proofs, exercises, examples, notes, and the complete 17-item bibliography through the inherited conditional end guards. This assignment corresponds to full-IV source lines 8239–9930 (1,692 supplied lines). No untranslated prose, omitted proof, invented material, summary or placeholder is counted complete. Other authors own §§0–9 and the parent owns integration.

- Input: `/tmp/sga4-04-part-10-14-source.tex`, supplied by the parent from the verified archive witness; 74739 bytes.
- Source SHA-256: `36e840dc4310e8be35f0c5f7a83ce065787eccb7cf21577130451226c4a1923a`.
- Output: `part-10-14.tex`, 1047 lines, 66300 bytes.
- Output SHA-256: `729deb062a0376de5ca30145417aa334a974677244f397bfad1192d76737f3c4`.

## Source-preservation checks

- 1,110 math/display segments in each file, identical as multisets after translating only human prose inside mathematical displays. Some unchanged mathematical segments move within a paragraph for Chinese syntax.
- 268 reference/label/target occurrences match as multisets; all 85 `etiquette` markers retained.
- All 17 `bibitem` identifiers, 2 native Xy-pic diagrams, 29 original-page markers and 26 `sisi` calls retained. No footnotes occur in this supplied tail.
- Environment counts match: 34 `enonce*`, 10 `equation*`, 9 `alignat*`, 11 `enumerate`, 3 `itemize`, 9 `align*`, 1 `tabbing`, 1 `gather`, 1 `thebibliography`, 1 `tabular`; inherited conditional `end document` retained.
- All rendered-prose blocks translated. An additional residual-English scan covered display annotations such as “adjunction”, “is left exact”, and “objects of”; these are translated. Original person names, titles, publisher data and mathematical notation remain in their original script.
- Zero-argument commands before Chinese checked and normalized where needed.
- All mathematics remains native LaTeX; no source-page overlays or image mathematics.

## Terminology and editorial details

态射层, 赋环拓扑斯, 局部化, 标量限制, 底阿贝尔层, 补零延拓, 补空集延拓, 自由模, 张量积, 局部赋环拓扑斯, 容许态射, 剩余域, 几何点, 支集. The distinction between extension by zero for modules and extension by the empty set for set-valued sheaves in Remark 11.3.2 is retained explicitly.

For Proposition 12.7, “eight morphisms” is consistent with the source: the three displayed families are indexed by ranges 1–3, 4–6 and 7–8. The eight defining formulas and all original index ranges are retained. A targeted read-only French comparison confirms this grouping; no missing maps were invented.

Bibliographic commentary (“cited as”, collection of talks, notes by, mimeographed thesis, and the August/September date) is translated. All 17 original bibliography entries, including the modern additions numbered 15–17, remain. No new bibliography items have been supplied.

French witness SHA-256: `cf1682d956806cabcf4ad1b4d9930d757df1254a4214d2b61846461a4e3d496f`. Targeted verification consulted the construction in Proposition 12.7. This is not a full independent French collation or a mathematical-proofreading certification. No mathematical source repair was made in this assignment.

## Review and build limits

Complete translation and mechanical preservation checks; self-review performed. Independent mathematical proofreading is not claimed. This fragment has no standalone preamble. The parent owns integrated compilation, cross-exposé reference resolution, rendered-page inspection, missing-glyph and overflow checks, and final PDF/source ZIP packaging. No successful compilation or rendered-page inspection is claimed by this subagent. No commits or pushes were made. Repository writes for this assignment are confined to `part-10-14.tex` and this review note.
