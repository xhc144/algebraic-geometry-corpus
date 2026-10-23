# Exposé I §10 and Bourbaki appendix — translation review

Coverage: complete assigned source `/tmp/06-glossary-appendix-source.tex`, source flat-I lines 7976–9631; glossary §10.1–10.11, both bibliography blocks, Bourbaki Appendix II §§1–7 including all proofs and exercises. Source-fragment boundary comments and final `danslelivre` conditional are retained. No summarization or invented missing material.

- Source bytes: 87,000; SHA-256 `7ca2e28bb202f34e99146f163693e2e5df8288a35f5b926d6110a83adef5ee4b`.
- Translation bytes: 78,714; SHA-256 `69b34d6384b690ce86a245ced61f772814f1ed2ee2d7a688ad31e23f9a645d02`; 826 lines (paragraphs reflowed).
- Structural checks: all 86 hypertarget IDs, all reference-target multisets, environment multisets, 3 Xy-pic diagrams, 38 original-page markers, 12 etiquette tags, 2 bibliography entries, 9 section and 11 subsection commands retained. No Chinese characters adjoining TeX control words.
- Human-language diagram labels and prose in math boxes translated; names and bibliography titles retained. Textual `n°` reference markers are rendered 第…节 (42 inline-math wrappers removed), and the humorous Spanish `pequeños` is rendered 小家伙. Some inline variables move with Chinese sentence order; these formatting counts are not evidence of omitted formulas.

## Compile and visual checks

Isolated wrapper using the coordinator's actual support files compiled with XeLaTeX (no shell escape), three runs, to `/tmp/sga4appendix-build/appendix.pdf`, 19 pages. Latest log has no missing-character messages, no overfull boxes and no fatal error. Three cross-exposé references (`II.def2.5`, `II.prop2.6`, `II.cor2.4`) remain undefined in this isolated wrapper, as expected; integration must resolve them. Native Xy-pic diagram directions preserved.

Actually inspected rendered PDF pages 1, 4 (blank), 5 (bibliography), 6, 7 and 19. Pages 1, 6 and 7 show readable Chinese and native formulas/diagrams; bibliography names are preserved. This is a sample visual inspection, not a claim of reviewing every page. Other pages have not been visually inspected by this translator.

## Source issues preserved, requiring editorial adjudication

1. Glossary §10.3 refers the term “pullbackable” to 10.3, while its definition is 10.7. Preserved source reference.
2. Appendix §1 Proposition 1 has `X\in U` but `y\subset x`. This mismatch is also visible in the Orgogozo French retypeset witness `/tmp/sga4-original-tome1.pdf` (text at original margin 186). Preserved; this does not independently establish the Springer scan reading.
3. Appendix §2 starred tensor example repeats `\ZZ^{X\times Y}` in both places. Potential loss of direct-sum parentheses. Also repeated in extracted Orgogozo French text; the Springer original scan has not been checked by this translator. Preserved.
4. Appendix §3 cross-references to `§1, n°2, Ex.c`, `§1, n°4`, `§4, n°2, Definition2` etc. are inherited references to Bourbaki's work, not to the identically numbered appendix sections; source hyperlinks point inside this appendix. Targets retained, no invented replacements.
5. Appendix defines strongly inaccessible cardinals to include 0 and the countable infinite cardinal. This is the source's explicit convention and is preserved.
6. Joking Bourbaki phrasing (“secret papers”, “Tribe”, “cannot possibly be useful”, “decanulate the ordered pair”) is translated rather than omitted. “去掉有序对的管子表示” follows the historical Bourbaki tau/couple terminology; mathematical content was not modernized.

Chosen English source completeness and Springer-original completeness are distinct. This translator did not proofread the complete French original, nor verify source prefaces or missing front matter. Full book and final integrated PDF verification remain with the coordinator.

## 2026-10-22续校更新

张量积例的原扫描第一卷物理207页保有有限支撑括号，已恢复ZZ^{(X×Y)}。上次“重排文本亦同”不足以证明原扫描同形，相关疑点已据原扫描结案。
