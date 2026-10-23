# Resumed independent bibliography fidelity audit

Date: 2026-10-22. Scope: actual source PDF pages 335–344, printed pages 323–332. This is a full page-by-page independent AI comparison of all 181 bibliography entries, not a sample or external bibliographic fact-check. Source and original Chinese references were read-only. No network research, external paid APIs, commits or pushes were used. Only `backmatter/bibliography.tex` and this report were edited by this auditor; the parent owns the full-book build.

The existing `PAUSED-CHECKPOINT.json` and `bibliography-review.md` were read for orientation, then the actual source was re-rendered locally with `pdftoppm -f 335 -l 344 -scale-to 1900 -png` and **each individual page image** `/tmp/fga-bib-335.png` through `/tmp/fga-bib-344.png` was viewed. PDF341 was additionally rendered at 3800 px and its Nak97/Nak99 labels inspected in a crop (`/tmp/fga-nak.png`). The views are direct scan images, not extracted text or a previous translation. Source-page names, diacritics, original-language titles and mathematical notation, citation labels, years, series/journal names, volumes/issues/pages, repeated-author rules and translated annotations were checked against each entry. PDF344 was actually viewed and confirmed blank. Incidental dust does not constitute printed text.

## Complete coverage

Every key below was individually compared against its page scan; entries not listed in the change table were retained after comparison. Work titles, subtitles, series and institution/publisher names retain original script under the established workflow; ordinary connective annotations are Chinese. Line-wrap hyphenation and spacing may normalize without changing content.

| PDF page | Printed page | Entry count | All checked citation labels in source order |
|---|---:|---:|---|
| 335 | 323 | 17 | AK70, AK74, AK79, AK80, AM69, Art69a, Art69b, Art71, Art73, Art74a, Art74b, Ati57, Bat99, BB73, BBD82, BCP04, Bea83 |
| 336 | 324 | 20 | BLR90, BLR00, Bor69, Bor94a, Bor94b, Bor94c, Bou61, Bou64, Bou78, BR70, Bri77, Car60, Che96, Cho57, Con02, CS01, Dan70, dCM00, dCM02, Del68 |
| 337 | 325 | 22 | Del73, Del81, DG70, DHVW85, DHVW86, DI87, DIX68, DL99, DM69, EG00, EGAI, EGAII, EGAIII1, EGAIII2, EGAIV1, EGAIV2, EGAIV3, EGAIV4, EGAG, EGK02, Eke86, Ell |
| 338 | 326 | 22 | ES87, ES98, Fal03, FGA, FK88, FK95, FM98, Fog68, Fos81, Gir64, Gir71, God58, Göt90, Göt01, Göt02, Gra66, Gro95a, Gro95b, Gro95c, Gro96, GS93, Har66 |
| 339 | 327 | 20 | Har70, Har77, Har92, Hir62, Hir99, HS, Iar72, Iar77, Iar85, Iar87, Igu55, Ill71, Ill72a, Ill72b, Ill85, Ill02, Ive70, Jou79, JT84, Kis00 |
| 340 | 328 | 21 | Kle71, Kle73, Kle04, Knu71, KO74, Kod05, KR04a, KR04b, KS04, Lan79, Leh99, Leh04, Lip74, Lip75, Lip76, LLR04, LMB00, LN80, LQW02, LS67, LS01 |
| 341 | 329 | 23 | Mac62, Mat89, MFK94, Mil80, ML98, Moe02, Mum, Mum61a, Mum61b, Mum65, Mum66, Mum67, Mum69, Mum70, Mur64, Mur95, Nag56, Nak97, Nak99, Nyg79, OB72, Ols, Oor62 |
| 342 | 330 | 19 | Oor71, OV00, Ray66, Ray70, Ray71, Ray94, RŠ76, Sch68, Seg37, Sei50, Ser55, Ser56, Ser58, Ser59, Ser61, Ser, SGA1, SGA2, SGA4 |
| 343 | 331 | 17 | SGA4-1/2, SGA5, SGA6, SGA7, Str96, Str03, Tam04, Tho87, Vid01, Vis97, VW94, Wat79, Wei54, Wei79, Zar58, Zar71, ZS60 |
| 344 | 332 | 0 | Actual blank page viewed; no content to transcribe. |

Counts: 17 + 20 + 22 + 22 + 20 + 21 + 23 + 19 + 17 = **181**. No omitted or added entries. Nine canonical `% SOURCE-PAGE-ANCHOR: N` comments, N=335…343, were inserted after the bibliography environment/heading setup at safe entry boundaries; there is no anchor for blank PDF344 and no layout macro was added.

## Exact changes and dispositions

| Source page / location | Before | After | Source evidence / disposition |
|---|---|---|---|
| PDF335, Art71 annotation | `1969 年在 Yale University 讲授的 A James K. Whittemore Lecture in Mathematics` | `1969 年在 Yale University 举行的 James K. Whittemore 数学讲座` | Source: “A James K. Whittemore Lecture in Mathematics given at Yale University, 1969”. The dangling English article and untranslated ordinary lecture description were repaired; name, place and date retained. |
| PDF341, Nakajima 1999 entry | `\bibitem[Naq99]{Naq99}` | `\bibitem[Nak99]{Nak99}` | The actual printed label is **Nak99**, clearly k, also compared at 3800 px against the preceding Nak97 label. This corrects a transcription defect, not a printed-source error. |
| PDF341, comment after that entry | `% source-error: the source printed key is Naq99 (q), retained.` | `% Independent scan review: printed key is Nak99 (k); corrected prior Naq99 transcription.` | Old checkpoint/report assertion was false. They were not edited because they are outside this auditor's allowed files; this report supersedes that assertion. Parent was notified. A read-only search found chapter 7 already uses literal `[Nak99]`, so the correction restores consistency there. |
| PDF335–343, before first entry of each page | No canonical anchor (only `% PDFN / printedM`) | `% SOURCE-PAGE-ANCHOR: N` immediately before the existing page comment | Added 9 provenance comments; original page comments retained. |

Confirmed printed-source oddities retained, with no external-source correction:

- PDF336 Bou61: `filtra- tions` is printed with the internal hyphen/space and remains retained with its existing comment.
- PDF338 God58: `Actualit’es` / native TeX `Actualit'es` is printed rather than an accented é; existing literal spelling/comment retained.
- PDF338 Fog68: `Amer. J. Math` lacks the journal's final abbreviation period in the scan; retained.
- PDF339 Har92: `Algebraic geometry. a first course` has lowercase `a`; retained.
- PDF341 Ols: lowercase `artin stacks` in title and prospective “to appear” publication note retained, the note already translated as `将发表于`.
- PDF342 Seg37: lowercase `hodge` in title retained.
- PDF342 SGA1: year **1964** printed here; retained with existing source-error comment.
- PDF342 SGA4: `Voll. 270, 305, 569` printed here; retained with existing source-error comment.
- PDF343 SGA5: `Séminaire de Géometrie` spelling retained as printed.
- PDF343 Wei79: duplicated `vol. Vol. I` and the source's punctuation before the publisher retained. All three page ranges 518–574, 526–553 and 443–465 verified.
- Accent-bearing keys Göt90/Göt01/Göt02 and RŠ76, author names Białynicki-Birula, Lütkebohmert, Bénabou, Briançon, Göttsche, Strømme, Gagné and Šafarevič, and original source title accents were checked visually and retained.

No new dates, identifiers, missing bibliographic details or publication updates were invented. No unresolved source-reading ambiguity remains in this assigned range.

## Validation and hashes

- Source PDF SHA-256: `17ebc9fd0ad15cc352d461c4515199377e64d905f0d5e08c6b3b90c25b43ed8d` (matches delegated source).
- Bibliography before SHA-256: `82da3970ec8d010c90a98d68b9cfcc4f18a08234fe310bbbc6d5d1353533cbec` (matches paused checkpoint).
- Bibliography after SHA-256: `d603ae88862bb8432e1000d0ed1098a368c77a601e53f9a76c9789a6f625a12c`.
- Structural check: 181 unique display keys and 181 unique internal keys; each display/internal pair matches. Nine unique canonical anchors, exactly 335–343, all inside the bibliography environment. `git diff --check` passed for the two permitted files.
- No standalone or full-book build claimed by this auditor; parent performs compilation and resulting layout review. No source/original reference files were changed. No blockers encountered.

The report's own SHA-256 is supplied in the auditor's completion message (a document cannot stably include its own cryptographic hash).

## Bounded coverage-gap confirmation: PDF334

On 2026-10-23, source PDF page **334** (original pagination position **322**, no page number printed on the blank leaf) was independently rendered directly from `FGA/FGA-Explained-Fantechi-AMS-2005.pdf` with `pdftoppm -f 334 -l 334 -scale-to 1900 -png` and its actual scan image `/tmp/fga-gap334-334.png` was individually viewed. **Confirmed genuinely blank:** no printed text, mathematics, figure, heading, folio or other matter; only incidental scan specks. This adds PDF334 to this report’s explicit independently viewed coverage. No TeX or other project file was changed for this bounded check.
