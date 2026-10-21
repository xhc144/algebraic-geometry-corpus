# Chapter 1 independent agent source comparison

Reviewed file: `chapters/ch01.tex`, SHA-256 `a8f52b45c0e7ec9f6100d463ffb94c5e775cf29408663358f22b25a10653e4f7`.
Source: `FGA/FGA-Explained-Fantechi-AMS-2005.pdf`, SHA-256 `17ebc9fd0ad15cc352d461c4515199377e64d905f0d5e08c6b3b90c25b43ed8d`.
Scope: all six actual scan pages PDF19–24 / printed7–12, rendered160dpi and visually read in full. This review was performed by a different agent from the translator. It is not human or independent expert certification. No root/ch01 file was modified by the reviewer.

## Findings

No missing paragraph, numbered statement, proof (the chapter intentionally recalls results without proofs), list item, mathematical formula or figure was found. Numbered items1.1–1.16 occur in source order, and conditions/quantifiers were compared. The twelve properties in proposition1.15 and its paragraph about the locally finitely presented extension are present. The category-theory definitions and all displayed formulas for F*, F_*, projections and product preservation are present.

One small explicit qualifier is omitted in translation: at ch01.tex line39, proposition1.4(ii), the source says “an open affine subscheme **of Y**”; the translation says “每个仿射开子概形的逆像都是拟紧的” without naming Y. The ambient target is inferable from f:X→Y, so this does not change the intended theorem, but for full wording coverage, recommend “$Y$ 的每个仿射开子概形在 $X$ 中的逆像都是拟紧的.” This is a translation wording omission, not a printed-source problem.

## Source anomalies preserved rather than introduced by translation

At printed p11, the definition of a finite-product-preserving functor says the comparison arrow is an isomorphism “in C”, although its target category is D. The translation deliberately preserves C and has an explicit SOURCE ISSUE comment. This is not a translation defect. Proposition1.13's redundant “faithfully flat surjective” likewise matches the printed source.

## Diagram inventory

There are eight separate source figure blocks and eight native `tikzcd` environments, not nine separate blocks. The first p11 block contains two adjacent squares; counting those separately gives nine diagram components. All vertices, directions and labels match:

| Source page | Figure(s) checked |
| --- | --- |
| p7 / PDF19 | base-change square in proposition1.2(iii) |
| p8 / PDF20 | base-change squares in propositions1.6(ii),1.9(ii) |
| p9 / PDF21 | base-change square preceding proposition1.15 |
| p10 / PDF22 | no figure; all category/functor formulas checked |
| p11 / PDF23 | two-square A′–B′–C′ grid, combined A′–C′ square, comma-category triangle |
| p12 / PDF24 | product-preservation naturality square with F(f1×⋯×fr), Ff1×⋯×Ffr labels |

All inspected source diagrams are reconstructed natively; no source image overlay appears in ch01.tex. The bibliography keys cited in ch1 agree with the original displayed references. Compilation/typographical validation of the integrated book remains root's responsibility; this is a source comparison, not a new build claim.

Root disposition: explicit Y/X qualifier restored in Proposition1.4(ii); figure inventory corrected to8TikZ-CD blocks.
