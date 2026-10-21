# Exposé V translation review

Complete supplied body translated: introduction, §§0–6, Čech appendix §7, Deligne's local-inductive-limit appendix §8, and all 17 bibliography entries. All definitions, propositions, theorems, proofs, exercises, remarks and footnotes are present. No untranslated body, summary, invented text, unfinished paragraph or placeholder is counted complete. Chapter heading and author block are supplied by the parent.

- Source: `/tmp/sga4-05-body-source.tex`, extracted by the parent from the verified archive reader; 4,471 lines, 187366 bytes.
- Source SHA-256: `0c6e98b1d28b7c812dd3f8e6699185036326951c9beca0ddf5453561b4eba854`.
- Output: `body.tex`, 2785 lines, 165298 bytes.
- Output SHA-256: `15d01f2ed6f63812d75d7db62a4a11b120b0f715dbb6411c85bb1d8bd2098d7c`.

## Mechanical preservation checks

- 2,978 math/display segments in source and translation, identical as multisets after only translating human prose inside displays. Unchanged mathematical segments occasionally move within the same paragraph for Chinese grammar.
- 556 reference/label/target occurrences agree as multisets; all 246 `etiquette` markers retained.
- All 28 citation occurrences and all 17 bibliography identifiers retained.
- All 40 native Xy-pic diagrams retained.
- Environment counts agree: 103 `enonce*`, 44 `enumerate`, 10 `itemize`, 13 `equation`, 60 `equation*`, 8 `align*`, 4 `cases`, 2 `gather*`, 1 `split`, 1 `thebibliography`; inherited conditional `end document` retained.
- All 79 original-page markers, 3 footnotes and 28 `sisi` calls retained.
- Zero-argument command boundaries before Chinese checked and normalized where needed.
- Renderable English-prose scan completed, including prose protected inside display mathematics, footnotes in equations and reference display text. Remaining Latin text consists of original person names, Čech, mathematical notation/abbreviations and original bibliography titles/publisher data. Source comments in English remain as provenance, not untranslated rendered text.

## Terminology

上同调 (cohomology), 无环 (acyclic), 导出函子 (derived functor), 内射 (injective), 松弛层 (flasque/flabby sheaf), 软层 (soft sheaf), 支集族 (family of supports), 骨架/余骨架 (skeleton/coskeleton), 超覆盖 (hypercovering), 半可表 (semi-representable), 局部余滤过 (locally cofiltering), 局部归纳极限 (local inductive limit), 叠 (stack). Person names remain in their original script. Historical publication-status prose in bibliography entries 2 and 9 and “mimeographed notes” in entry 17 is translated; titles remain original.

## Source observations

1. In §8.1.13.0, the archive source formula contains literal `quad` without a backslash before the “for L” text. This is retained, with only “for” translated, to avoid silently changing the assigned mathematical source. The read-only French witness displays ordinary separation there; a documented typographical repair to `\quad` is available to the integrating editor.
2. The source already contains comments flagging the positioning of number 1.10.3. That label/number and native diagram are retained; final placement requires the parent's rendered-page check.
3. The support-cohomology footnote in §6.3 refers literally to “p. 80 below”; this inherited historical page reference is retained. It denotes the original-page system, not a newly inferred Chinese PDF page.
4. French witnesses were used for targeted verification, not as a replacement source. For example, the French rendering of the final Lazard proof visibly uses L2 where the selected English source has L0; the translation follows the selected English source. The English F0/F1 indices in the diagram proving Lemma 8.2.10 are likewise preserved.

Read-only French witness SHA-256: `f6df53c777a9188eba002beeb241c9bc1c3e735ca6a82847e295eb4843d6dac2`. Targeted collation consulted §§7.4 and 8.1.13, and Lemmas 8.2.10–8.2.11/Theorem 8.2.12. This was not a full independent French collation.

## Review and build limits

Translation and mechanical preservation checks complete. Self-review performed; independent mathematical proofreading is not claimed. The parent owns preamble, heading, integrated compilation, cross-exposé reference resolution, PDF rendering, missing-glyph/overflow review and final packaging. No compilation or rendered-page inspection is claimed by this subagent. No commits or pushes were made. Repository writes were confined to this assigned body and review note.

Root integration: three overwide chains of Hom/cohomology isomorphisms were broken into aligned lines with all mathematical symbols/arrows in the original order. The bare `quad` in8.1.13 was restored to `\quad`; the translator verified that the French witness has spacing rather than a variable named quad. This repairs notation, not a mathematical assertion.
