# Stacks Project — Mainland Simplified Chinese: direct cumulative LaTeX

This source-format supplement accompanies the existing unofficial Chinese reader: all 116 chapters of the Stacks Project snapshot at commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, 5,906 PDF pages. It does not revise or independently certify the translation.

Download the files in this order:

1. `00_Stacks_Project_zh-Hans-CN_Cumulative_116_Chapters_2026-08-30.pdf` — the unchanged cumulative reader.
2. `00a_Stacks_Project_zh-Hans-CN_Cumulative_116_Chapters_2026-08-30.tex` — the complete cumulative text, directly editable without unpacking the source archive.
3. `01_Stacks_Project_zh-Hans-CN_Cumulative_116_Chapters_2026-08-30_Source_and_Evidence.zip` — the complete original modular source and project dependencies.

The direct `.tex` contains the preamble, all 116 chapter bodies, generated index, licence body and reference definitions. Its SHA-256 is `6E59586446E183D4FDD5AE58F688DF1F066DB5128758D0F4FBC5E4703ED68F1A` (27,013,577 bytes). It was assembled exclusively from the source archive accompanying the released PDF, not from later working translations. Every non-input-directive byte is preserved in original reader order; all 120 literal input directives were expanded. The companion manifest records source identities and a reversible byte-span map.

For typesetting the single-file version, place it beside `stacks-project-book.cls` and `my.bib` from the archive's `src` directory. Use XeLaTeX, BibTeX, then sufficient XeLaTeX passes for references to stabilize. Required TeX packages and fonts are declared in the preamble, including XeCJK, Xy-pic, Latin Modern and Noto Serif/Sans CJK SC. The original modular `src/reader.tex` remains in the ZIP. Its historical `build.ps1 -SkipCompose` builds those frozen sources directly; running the composition stage is unnecessary and may require the original producer workspace. On the project Windows machine, all new TeX invocations must hold `Global\InterlanguageTeXSlotV1` for the full build sequence.

The PDF and original archive are unchanged. This supplement was checked by deterministic archive/byte/span replay; it does not claim a newly compiled or newly visually reviewed PDF. Reproduction with different TeX installations can change PDF metadata and pagination. For the exact previously released build, retain the archived modular sources and historical build receipts.

The old reader's front matter uses provisional wording about future chapters. All 116 chapters in the stated frozen snapshot are present; further terminology normalization and editorial review are separate from that coverage fact. The historical reader is preserved rather than silently edited in a source-only supplement. Existing qualifications remain: this is an unofficial translation, not an endorsement by the Stacks Project or a claim of error-free linguistic certification. The PDF is untagged and some older mathematical fonts lack ToUnicode mappings.

The original work and derivative edition retain the GNU Free Documentation License 1.2-or-later terms and attribution supplied in the source archive and reader. Chinese, Japanese and Korean publication lineages remain separate.
