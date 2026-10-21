# Exposé VII translation review

- Complete assigned body translated: introduction; §§1–5; all definitions, propositions, theorem, corollaries, proofs, examples, remarks and nine footnotes, through Remarks 5.14(b). Chapter heading and author block are supplied by the parent.
- Input: `/tmp/sga4-07-body-source.tex`, extracted by the parent from the verified archive reader; 963 lines, 42783 bytes.
- Source SHA-256: `042b72644e52b182451d1ae432fe3e2a7b25934ce7c23af5043ef1beba606c44`.
- Output: `body.tex`, 532 lines, 36787 bytes.
- Output SHA-256: `1e60d1f9ead24bd100ec2a5db7e8860d06b3e1fe332cc80cdcb905f39a90e633`.
- No unfinished prose blocks, invented missing text, summaries or placeholders.

## Checks performed

- 594 mathematical/display segments on each side, identical as multisets after only translating English prose within mathematical displays. Some unchanged mathematical segments move within their paragraph to accommodate Chinese grammar.
- 94 reference/label/target occurrences identical as multisets; all 40 `etiquette` markers preserved.
- Environment counts preserved: 7 `equation*`, 1 `cases`, 6 `enumerate`, 17 `enonce*`, 1 `gather*`; the inherited conditional `end document` also remains.
- 24 original-page markers and all 9 footnotes preserved.
- The original person names and reference titles are retained. Residual-English scan yielded only intended proper names, bibliography titles/publisher, fpqc/fppf abbreviations, the notation `esp`, the first-use term `lien`, and LaTeX identifiers.
- No images or page overlays. All equations and displayed structures remain native LaTeX.
- Zero-argument command boundaries before Chinese were checked and normalized where needed.

## Editorial notes and source questions

- §1.6 calls the relevant functor “restriction to Y”. The read-only French witness also says “restriction à Y”. The source wording is retained; its relation to the restriction along `i_X/Y : X_et -> Y_et` may merit editorial clarification.
- §2(a), in the example of the algebraically closed field, uses `S = Spec k` although the surrounding base is X. The source notation S is retained.
- Proposition 4.3 has “sheaf of varying modules”; French reads “un faisceau de modules variable”. It is translated as the ordinary Chinese term “模层”, consistently with §2(c) and the quasi-coherent-module hypothesis. No new kind of module object has been introduced.
- In the proof following Proposition 4.3, the vanishing display writes `R^q f_*(F)=0`, while the relevant étale coefficient layer is `F_et`; the French witness has the same notation. It is preserved rather than silently emended.
- Remarks 5.14(a): Giraud's “links” are rendered “带 (lien)” to identify the nonabelian-cohomology term, retaining the original person's name.
- None of these notes is a claim that the underlying mathematical issue has been adjudicated. No formula was silently corrected.

Read-only French verification file SHA-256: `f6df53c777a9188eba002beeb241c9bc1c3e735ca6a82847e295eb4843d6dac2`. Targeted collation covered §1.6 and Proposition 4.3 with its proof/Corollary 4.4; not every French line was independently collated.

## Status limits

Body translation and source-preservation checks complete. Self-review only; no independent mathematical-proofreading claim. The parent owns the preamble, heading, full-book compilation, reference resolution, PDF rendering, missing-glyph checks, overflow checks and final package. This subagent did not compile the integrated book and does not claim rendered-page inspection. No commits or pushes were made. Only the assigned body and this review note were written in the repository.
