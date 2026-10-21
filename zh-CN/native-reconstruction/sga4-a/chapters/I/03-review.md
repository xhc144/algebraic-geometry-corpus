# Exposé I §§8.1–8.7 translation checkpoint

- Status: assigned range fully translated, not a summary. Includes all statements, proofs, notes, exercises and native Xy-pic diagrams in the assigned source.
- Source: `/tmp/03-section-8a-source.tex`, 1553 lines; root extraction from manifest-verified cumulative source ZIP, flat Exposé I lines 3199–4751. This covers §8 heading, §§8.1–8.7, ending after Exercise 8.7.9 and before §8.8.
- Source SHA-256: `1c3f55cc5f2ba8f16e3d1956cb3a58f331bf4d191993cd57db0d60cb0f225a33`.
- Output: `03-section-8a.tex`, 1331 lines, SHA-256 `6d50163997cd6f4ad08759fd57bfa21d318f1b48a438eafb02f150c36603bac9` at this checkpoint.
- Mechanical checks: all 54 `etiquette` markers, all 59 `hypertarget` markers, and all 43 begin/end environments preserved in exact source order. All 148 hyperref/hyperlink targets preserved as a multiset; some local prose order changes for Chinese grammar. All 20 source comments preserved. Three bracket display-math environments preserved. Dollar-delimited math count is exactly 1069 on both sides. After whitespace normalization, dollar-math multisets differ only in the four expressions whose human text is translated: `or`→`或` in 8.2.4.5; `source`→`起点` and `target`→`终点` in three Exercise 8.2.8 expressions. Mathematical parts are unchanged. Control words `pageoriginale`, `ie`, `resp`, `cf`, `Cf`, `cqfd` adjoining Chinese are explicitly terminated where applicable.
- Review: full translation produced against source, then structural and formula comparison; targeted French-reference text check for suspicious inherited readings. This is not an independent mathematical proofread. Compilation and rendered-page review belong to root integration and have not been independently claimed here.

## Inherited source issues, preserved rather than silently corrected

The read-only French reference `/tmp/sga4-original-tome1.pdf` contains the same readings at the PDF pages cited below; it therefore does not resolve the mathematical concern. The source TeX and Chinese translation retain them. These items should remain visible in the overall review status rather than being treated as translation mistakes or silently corrected:

1. Proposition 8.1.6 proof: `x∈D'` in definition of terminal object, arrow target `y` although `Hom(x,e)` is written; later finite subdiagram `of E`, `j` terminal in `D'` where the construction uses `D''`. French PDF pp. 46–47 has these readings.
2. Equation 8.2.4.1 indexes `𝒴` by `j∈I` although surrounding prose specifies `J`; text also writes `Ind_{𝒱'}(,𝒰)` with missing `C`. Source preserved; not corrected by translator.
3. Exercise 8.2.8 uses `F(s)`, `F(p_1)=F(p_2)` while asking about a functor `G`. Source preserved.
4. Theorem 8.3.3 (iii bis) combines upper-bound terminology with an arrow `X_i→X`; (v) says **filtered** inductive limits in `C`, although the usual finite-limit criterion suggests **finite**; (ii)⇒(i) writes canonical `C_{/F}→F` instead of the earlier target `C`, and cites 8.3.2.1 rather than 8.3.2.2. French PDF pp. 52–53 has the same readings, so all retained.
5. Remark 8.3.4 says presheaf on `C^circ` despite writing `C'=C^circ`; French p. 53 has this wording. Retained.
6. Exercise 8.5.5 (i),(ii) says small inductive limits without the qualifier filtered, although (iii),(iv) concern Ind-completion. Retained.
7. Corollary 8.6.5 says `Ind(E)` rather than the surrounding `Ind(C)` and uses capital `P` on the arrows for projector `p`. French p. 59 agrees. Retained.
8. In 8.7.1.7 prose `X∈ob Ind(C)'` appears before applying `c(X)`; 8.7.4.2 prints an unadorned `lim`. Retained.
9. Proposition 8.7.5 proof describes arbitrary ind-objects **of E** and writes `Hom(bar f(𝒳_j),𝒴)`; French p. 62 agrees. Retained.
10. Corollary 8.7.6 switches from `bar g` to `bar f` in prose. French p. 63 agrees. Retained.
11. Corollary 8.7.7 proof says the arrow `X_i→X` has a **left inverse** and applies 8.6.4 b) to `E→E_PF`; French p. 64 agrees. Retained.
12. Exercise 8.7.8 b) gives `Hom(K,F)→Hom(K,F)` for composition with `φ:C→K`; d) cites `8.5.4 b)` (the matching equivalence is apparently 8.6.4 b)); its cross-reference `IV 7.5` uses the inherited label `I.cor7.5`. French pp. 64–65 has the printed duplicate Hom target and 8.5.4 citation. Retained.

No external paid API used. No original, existing Chinese translation, unrelated repository, root/global index or another author's output modified. No commit/push performed by this translator.
