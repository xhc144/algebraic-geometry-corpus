# Exposé III complete-body translation checkpoint

- Status: the entire assigned body source is translated, including introductory paragraphs, §§1–5, every statement/proof/example/note, all native Xy-pic diagrams, and the bibliography. No unfinished prose or placeholders in the assigned body.
- Source: `/tmp/sga4-03-body-source.tex`, 1530 lines, extracted by root from the manifest-verified cumulative source ZIP; original included-fragment boundaries 31–1551. Root owns chapter heading, author attribution, cover, main file and integration.
- Source SHA-256: `8425650797e3b6023ecd1a4189beb761ef98cbf069f33dfa0c7fe1117eeb8ba8`.
- Output: `body.tex`, 1255 lines, 59814 bytes, SHA-256 `b9aad5f87cf25fe04bf5c8b8894245e65be7f565df9a05e83e8f134799a9f684` at this checkpoint.
- Mechanical checks: all 46 `etiquette` markers, 3 `hypertarget` markers, 2 explicit labels, 84 `hyperrefext`/`eqhyperref` references, 70 begin-environment commands and 71 end-environment commands are preserved in exact source order (the extra `end{document}` is the inherited standalone conditional). All 101 ordinary hyperref targets preserved as a multiset; local Chinese grammar changes account for order changes. All 1054 dollar-delimited expressions preserved as an exact multiset after whitespace normalization. All 19 bracket display/diagram blocks and five align/gather/displaymath blocks are identical after whitespace normalization. Bibliography key and proper names/book title preserved. Source comments preserved.
- Terms: site 景; continuous 连续; cocontinuous 余连续; bicovering 双覆盖 (first occurrence includes original term); associated sheaf 伴随层; direct image 正像; inverse image 逆像; restriction 限制; localization 局部化; fiber product 纤维积.
- Review: complete source-to-translation pass, followed by label/reference/environment/formula checks and selected French-reference text checks for inherited suspicious readings. This does not claim an independent mathematical proofread. No standalone compile or rendered-page review claimed by this translator; root integration owns compilation, glyph/reference/overflow checks and visual review.

## Source concerns kept visible

The mathematical formulas and references below were preserved, not silently repaired. Several visibly suspicious readings are also present in read-only French `/tmp/sga4-original-tome1.pdf`:

1. Subsection `1.11` is printed as such, with inherited source comment suggesting `1.1.1`. French PDF p. 162 also prints `1.11`.
2. §1.2.1 cites `2.2 iv)` (label `III.prop2.2`), apparently intending 1.2 iv). French p. 164 also says 2.2 iv).
3. Proposition 1.2 iv) proof cites `III.rem1.4` 3) although Remark 1.4 has only two items; its final square has lower-right `C'` rather than its sheaf category. Preserved.
4. Diagram (*) in the proof of 1.5 has upper-right presheaf universe `V` whereas upper-left is `U`; retained verbatim.
5. Proposition 1.7 reverses the displayed direction of `u_s^gamma` relative to `u_s`; item 2 writes `u'_{gamma!}`; item 4 diagram has `u_Y^s`; item 5 repeats `esj^sim` instead of a primed second functor; diagram 1.7.1 has `u^s_{rV}`. Source formulas retained. French p. 168 also prints the `rV` subscript.
6. Proposition 2.3 displays `u^ast:widehat C'→widehat C` although its construction is a functor on sheaves. French p. 170 has these hats too. Retained.
7. Corollary 3.4 cites `(I 3.0.2)` using an II label. Lemma 3.6.1 discussion similarly prints I for an II label. References retained.
8. Comparison-lemma proof uses `u_sH` (rather than explicitly its underlying presheaf) as an input of `u_!` in one formula; its property (*) has a unique-factorization wording that should be reviewed mathematically. No new interpretation inserted.
9. Terminology 5.3 cites `4.3.2` and `2.9.2`, neither a present section here. French PDF pp. 179–180 has these printed citations. Retained.
10. Proposition 5.5 diagrams include inherited shorthand/subscript differences such as `e^hat/X`, `e^sim/X` in prose and diagrams versus `e_X^sim`; all exact diagrams retained for verification, rather than silently renaming them.

No original source, existing Chinese translation, unrelated mounted repository, root index or another author's directory modified. No paid API used. No commit/push performed by this translator.
