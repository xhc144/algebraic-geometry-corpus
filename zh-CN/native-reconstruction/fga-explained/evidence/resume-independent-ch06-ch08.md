# Resumed independent fidelity review: Chapters 6 and 8 endings

Date: 2026-10-22. New independent AI reviewer, not either chapter's initial translator; this is not human professional certification. User-authorized resumption was relayed by root. Baseline branch: `translation/fga-explained-resume-20261022`, based on main `dbb4b7440031f51a3545d6ed172a987846e4db53`.

## Source and method

Original, read-only source: `FGA/FGA-Explained-Fantechi-AMS-2005.pdf`, SHA-256 `17ebc9fd0ad15cc352d461c4515199377e64d905f0d5e08c6b3b90c25b43ed8d` (recomputed locally).

Read `evidence/PAUSED-CHECKPOINT.json` and the relevant prior independent audit records (`independent-audit-front-ch03-ch06.md`, `independent-audit-ch08.md`) to identify exactly the outstanding pages. Rendered the seven assigned PDF pages locally with PyMuPDF at 1.8 scale to `/tmp/resume-ch06-ch08/`. Actually opened and visually read **every one of all seven assigned scan pages: PDF 168, 169, 170, 243, 244, 245, 246**, including the blank page 246. Rendering alone was not counted as review. Compared all clauses, hypotheses, formulas, proof steps, labels, references and letter closing against `chapters/ch06.tex` and `chapters/ch08.tex`; no OCR was used as authority.

| Source PDF / printed page | Actual scan viewed | Comparison coverage and disposition |
| --- | --- | --- |
| 168 / 156 | Yes | Proof of 6.4.9; 6.4.10–6.4.12 and proofs; Hilbert local dimension bounds; separatedness and affine-cover/Čech gluing argument. No confirmed fidelity defect. |
| 169 / 157 | Yes | §6.5, 6.5.1 proof, local complete intersection definition, 6.5.2 and beginning of proof. No confirmed fidelity defect; printed-source flatness anomaly retained, see below. |
| 170 / 158 | Yes | Remainder of 6.5.2 proof, all local liftings and Čech class formulas; 6.5.3; final cotangent-complex/lci references. No confirmed fidelity defect. |
| 243 / 231 | Yes | 8.6.7, its argument, minimal examples, 8.6.8; §8.7 introduction, date, greeting, notation, Theorems 1–2 and beginning of Theorem 2 proof. One changed mathematical hypothesis corrected below. |
| 244 / 232 | Yes | Remainder of Theorem 2 proof; full Theorem 1 setup, polynomial basis and freeness, proposition, its application, and lemma. Original anomalies retained, see below. |
| 245 / 233 | Yes | Full lemma proof, expansion and coefficient calculation, final formula, informal closing and J-P. Serre signature. No confirmed fidelity defect. |
| 246 / 234 | Yes | Independently confirmed original blank page. No missing translated text; no canonical content anchor added. |

## Confirmed defect fixed

- **PDF 243, Serre letter, Notations:** before `设 $n>1$, $n<p$.`; after `设 $n>1$, $n\leq p$.` The original French visibly prints “Soit n > 1, avec n ≤ p.” The strict inequality had excluded the permitted boundary case. Restored the printed weak inequality only. Theorem 2's separate hypothesis `p>n` remains exactly as printed.

No other confirmed translation/transcription defects were found in the assigned scope. Names remain in their original script.

## Printed-source anomalies independently verified and preserved

- **PDF 169, 6.5.1 proof:** original explicitly says the sheaf is “flat over X_ε”; existing Chinese wording `在 $X_\varepsilon$ 上平坦` and explanatory source comment retained. No silent replacement by flatness over the dual-number base.
- **PDF 244, start of Theorem 2 proof:** French says `un relèvement z'' de s` although the preceding element is named z. Existing translated s and explicit source comment retained.
- **PDF 244, application of the proposition:** original prints `t_1(x)^p=0`, rather than `t_1(x^p)=0`. Existing formula and explicit source comment retained. The surrounding proposition itself correctly retains the source's `t_1(x^p)`; the two formulas were not conflated or silently repaired.

## Canonical page anchors

Added exactly one `% SOURCE-PAGE-ANCHOR: N` for each nonblank assigned page: **168, 169, 170, 243, 244, 245**. All are plain comments at safe boundaries outside math and TikZ. Page 170 begins mid-sentence: its anchor is placed at the preceding paragraph start (“对于一般情形…”), retaining the existing exact page-break comment inside the sentence. Page 244 begins mid-paragraph: its anchor is placed at the preceding paragraph start (“定理 2 几乎是直接的…”), retaining the existing exact page-break comment. Other anchors coincide with proof/section/statement/paragraph boundaries at the page start. No layout macros or navigation integration were added.

## Verification and handoff

`git diff --check -- chapters/ch06.tex chapters/ch08.tex` passed. Diff review confirms only six anchor-comment insertions plus the single inequality restoration. No main/style/scripts/index changes, no commits, no push, and no source-PDF changes. Root owns the integrated build, final output-page visual review, and navigation integration; this reviewer did not compile and does not claim final rendered-output validation. No permission or access blocker occurred.

## TeX hashes

- `chapters/ch06.tex` before: `047eb4e2dc70527f1771896680d72c6607a140813cc5456b869adb4674fd2836`; after: `757f732b4f6931d8456b4bad99e1736c7296ebfa2be5e000afceaf004717adb5`.
- `chapters/ch08.tex` before: `2e3badb2911ac6c17c0f59804d9c7352a0eb0a19d35a190ef7c079bfd7b6c0db`; after: `85c961284673c79482150df9ffe9df3e638559b46bb609485de8b5e02bca974a`.

## Viewed-render hashes (temporary local supporting evidence)

- PDF 168: `7d49a3c874c435a9d1f2586b2b8ffe1fb17823dca9477b9350ea19a36387cd75`.
- PDF 169: `c7f2c6e5cb1d89a6cbf0a817315eb7b89c919632404e51ec09267a50595209ff`.
- PDF 170: `672f567ec3159b1cc234985ea588fd1fcbafa7cb632b7a68e8d2eb7ceaac2129`.
- PDF 243: `ac8cff5dec17408a296b31ac05ac629bea5c511c0af28bbf65fd1d0b19b53734`.
- PDF 244: `a4be493f01f14b47435c14810de81f4b6d110942c0d8819932198c830a142211`.
- PDF 245: `5f3cdcf9c05355aedef41a8a489949ac50f59040cd574c233582a26f0196e0db`.
- PDF 246: `45a01e403c55939183d49de8f564a0baef85f054190133fdd5760da3a5c1549e`.
