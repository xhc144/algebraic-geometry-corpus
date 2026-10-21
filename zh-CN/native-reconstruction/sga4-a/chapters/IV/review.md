# Exposé IV §§0–8 — complete assigned translation

Source `/tmp/sga4-04-body-source.tex`, SHA-256 `338960658363596db1d56dfb13c7ff6a14812ac0339801df6e497c1802a1b69e`, 468,386 bytes / 9,930 lines. Translation `body.tex`: SHA-256 `26e3bf1ac3aca30cfe6cf2c3a410598516655063580be7e8c55e669699a01f66`, 210,791 bytes / 2,337 lines.

Coverage: source lines 1–5195 inclusive, complete assigned §§0–8 including all examples, proofs, notes and exercises. Stops before source line5196 (§9), assigned separately by root. Full Exposé IV also requires root-owned sections9–14 and bibliography. No placeholders in this translation body. Root owns wrapper and final integration.

## Verification

Mechanical comparison against the exact source range preserves the complete multisets of 241 etiquette identifiers, 5 hypertarget identifiers, 9 hyperlink targets, 357 hyperref/eqhyperref targets and95 hyperrefext targets. All139 environments match in order; all132 original-page markers,16 Xy-pic diagrams,9 section,48 subsection,68 subsubsection,4 paragraph headings,17 footnotes and7 editorial notes remain present. Chinese adjoining zero-argument control words was normalized with braces/spaces. “Acyclic” is consistently 无环.

Isolated XeLaTeX build `/tmp/sga4iv-build/iv.tex`, five passes, produced50 pages. Latest log has no fatal error, missing character or overfull box. Its101 undefined-reference warning occurrences concern references outside this isolated §§0–8 build; final cross-volume resolution belongs to integration. A local explicit-OTF main-font override was needed because an intermediate shared support revision selected a Type1 font; root has acknowledged and fixed shared support. This wrapper override did not alter source content. One paragraph containing the three Weil-restriction notations has local tolerance/emergency-stretch settings, preserving its formulas.

Rendered pages1,25,27 and50 were visually inspected: introductory page, the previously overflowing Weil paragraph, an induced-topos diagram page, and final exercises. Text, native formulas and native Xy-pic diagrams were readable on those pages. This is a sample visual review, not a claim that all50 rendered pages or the full original book have been independently proofread.

## Source issues retained for editorial review

These were translated faithfully rather than silently repaired:

- IV3.2.1 gives the inverse-image-functor target as Hhom(E,E′), where its direction suggests Hhom(E′,E).
- IV3.4 appears to swap the categories in the identities for uv and vu.
- IV4.7.5 contains an existing editorial note that the stated condition is incorrect; the note is fully retained.
- IV4.9.3 initially says “from C to C′” although the definition proceeds from C′ to C.
- IV4.10.3 writes the direct-image transition arrow in the opposite direction from the adjunction-compatible one, while the subsequent transition formula has the expected direction.
- IV4.10.5 writes H^i(X,F) rather than the following script-F subscript notation; source notation retained.
- IV5.2 has the unusual source subscript j_{X^{*}}.
- IV5.8.3 has the source expression `E'=((B_G)_{X/G)/Z}`, whose parenthesis structure is mathematically suspicious; retained.
- IV7.3's finite-set/simplicial-category wording needs original-source review if amended.
- Some inherited bibliography hyperlinks point at local section identifiers; cross-volume editorial repair belongs to root.

In IV8.5.5 the English source's “neat” corresponds to French *net*, meaning unramified: translated 非分歧. Terminology checked against [SGA1, Exposé I, definition3.2](https://pi.math.cornell.edu/~dkmiller/bin/sga1.pdf), which explicitly identifies *net* and *non ramifié*.

`/tmp/sga4-original-tome1.pdf` is Orgogozo's French retypesetting, a verification witness but not the Springer original scan. Root separately holds `/tmp/sga4-springer-tome1.pdf`; no full independent scan collation is claimed here.
