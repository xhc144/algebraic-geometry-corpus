# Exposé I, §9 translation review

- Coverage: complete §9, including 9.0–9.26 and Exercise 9.20.1. The assignment is flat Exposé I witness lines 6284–7975, 1,692 source lines; the trailing source-fragment boundary comment is retained.
- Source witness: verified archive reader selected by the parent; local extracted chunk `/tmp/05-section-9-source.tex`.
- Source chunk SHA-256: `78ab8b1353895fab9fca135e415840cc51c1f183fbccc6bb9a8d4228620144ab`.
- Output SHA-256: `4efb9d577f8092661ae21effe28fba778f8ab3658c5229192e2a59d1c90a0d3c`; 873 lines, 71475 bytes.
- Every prose block was translated. Original person name P. Deligne is retained. No uncompleted prose blocks, placeholders, or omitted proofs are used.
- Native exchange diagrams and all mathematical expressions remain in LaTeX. English prose in mathematical displays and reference display text was translated.

## Mechanical verification performed

- 1,315 math/display segments on each side, identical as multisets after applying only the explicitly translated prose within math displays. A change of phrase order in Chinese sometimes moves an unchanged mathematical segment within the same paragraph.
- 289 label/reference/target occurrences on each side, identical as multisets; 54 `etiquette` markers retained.
- Environment occurrences agree: 41 `enonce*`, 16 `enumerate`, 21 `equation`, 1 `equation*`, 2 `tabular`, 1 `displaymath`, 1 `cases`.
- 41 original-page markers and 1 footnote retained.
- Residual-English scan after removal of LaTeX identifiers and mathematical content found only the original name Deligne and the intended `ind-` terminology.
- Control-word boundaries before Chinese normalized where needed.

## Source questions retained for editorial adjudication

These are not silently corrected in the translation. They are separate from translation completeness.

1. Definition 9.1 uses literal `$pi$` in the English witness, where the read-only French witness has π. The literal English formula is retained.
2. Proposition 9.6 uses lower-case π for the cardinal in its introduction and in part (ii), while the functor subcategory uses upper-case Π. The French witness has the same distinction; its compatibility may require mathematical review.
3. Corollary 9.8 first writes `card Fℓ ≤ Π` without an explicit J, and display 9.8.3 uses `varinjlim_j`. Both also occur in the French witness. Retained as written.
4. Corollary 9.9 is problematic: the English prose says “projective limit” and displays `varprojlim X_j`, while its proof identifies the represented covariant functor with a projective limit of the functors represented by the X_j. The French witness instead says “limite inductive” but displays `varprojlim` in the statement and `varinjlim` in its proof. This is an inherited source inconsistency requiring adjudication, not a completed mathematical correction.
5. Exercise 9.20.1 uses `Pi_0 in card Fℓ C` rather than an evident cardinal inequality; retained from the source.
6. The second diagram in Lemma 9.21.19 has lowercase `x(alpha)_i`, `lambda(i,j)`, and `f^*X(alpha)` at positions whose consistency with the adjacent statement should be reviewed. The diagram is preserved natively and verbatim.
7. Theorem 9.22 quantifies `alpha in ob E`, and the following filtration is written `Filt^Pi(E)` without alpha; both also occur in the French witness. The subsequent proof writes `Filt^C(E_alpha)` with an uppercase C. All are retained.

French read-only verification file SHA-256: `cf1682d956806cabcf4ad1b4d9930d757df1254a4214d2b61846461a4e3d496f`. Verification consulted the corresponding definitions, 9.6–9.9, 9.21.9, 9.21.19, and 9.22; it was not a full line-by-line French collation.

## Status limits

Translation and source-preservation checks for this assigned section are complete. Self-review performed; no independent mathematical proofreading claim. This fragment has no standalone preamble. Compilation, rendered-page inspection, glyph checks, overflow review, and resolution of references to other exposés belong to the parent integration step and have not been claimed here. No commits, pushes, or files outside this section and this review note were made by this subagent.
