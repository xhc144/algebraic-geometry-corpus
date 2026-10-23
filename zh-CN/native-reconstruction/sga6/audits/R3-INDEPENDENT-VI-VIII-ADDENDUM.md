# R3 VI–VIII full-text review addendum

Full controlling French original printed365–497 (all133pages) extracted text has been read and compared with all native VI/VII/VIII body text. Native bodies were read-only to this worker. All 133 original pages have now also been individually inspected at readable raster resolution. The final frozen native PDF has not been supplied; native typeset visual review remains pending. This is an original-source comparison completion, not a final-book completion certificate.

Final original-image scope: printed365–497 inclusive, 133/133 pages individually inspected, including formulas, arrows, indices, headings, numbered prose and bibliography. Contact sheets were not counted as formula-resolution inspection. Physical page = printed page+14. Historical progress milestones below describe earlier checkpoints only.

The coverage TSV now records the full133page text comparison and individual-image work separately. A temporary exec-server transport disconnection was recovered; the addendum was read back and verified.

## Confirmed native errors and omissions

- VII4.11, native `expose-07.tex:1282–1285`; original465/physical479: native displays `cl(O_Z) ≡ i_*(1_{O_{Z∩U}})` in incompatible ambient rings. Original explicitly gives `u^*(O_Z)=i_*(O_{Z∩U})`. Restore `u^*(cl(O_Z))=i_*(1_{O_{Z∩U}})` in K(U)_Q. Individual original465 image checked.
- VIII1.3, native `expose-08.tex:45`; original467/physical481: square omits upward section arrow j′:X→X′ shown alongside p′:X′→X. Add a shifted upward arrow, retaining both arrows. Same omission in native VIII2.2 at305, corresponding to original477/physical491 (original477 detailed image now inspected and omission confirmed).
- VIII1.3 last diagram, native `expose-08.tex:105`; original469/physical483: vertical i″:U→Z×_YV is missing. Add `arrow[d,"i''"]`. Individual original469 image checked.

## Original errors requiring visible 译校注

- VII4.6, original455/physical469: individually inspected image prints `γ^{d+i}(i_*y)∈Fil^{i+d+1}`. Native921 correctly repairs the right exponent to i+d but does so silently. Add visible note identifying original exponent. Original455 itself omits rationalization in two intermediate memberships; these are not translation errors.
- VII4.11, original465/physical479: after introducing y in the localization image, original final paragraph switches to x twice. Native correctly uses y. Add visible note if keeping corrected text.
- VIII5.2, native928; original494/physical508: original itself prints `Ω¹_{V/Y}=g^*E`, although g:Z→Y. Native faithfully repeats it. Intended left side is Ω¹_{Z/Y}; keep original with visible note rather than silently repair. Original B(-1) on this page agrees with native; no graded-shift error was found.
- VIII3.3, native504; original483/physical497: both original and native give `Todd:1+Â⁺→1+Â⁺` without Q. Rationalization is required for the general Todd series (compare5.3.1). Any codomain repair must identify the original omission visibly. Image checked.
- VIII1.3(iv), original469/physical483: original first says q∘j is an immersion, then says q∘i is regular (intended q∘j); native repairs to qj silently.
- VIII1.4, original471/physical485: U′ flat overY is printed where U is intended; native repairs to U.
- VIII2.1, original475/physical489: `(1.5.1)` printed where `(2.1.1)` is intended; native repairs to2.1.1.

VI findings are in R3-INDEPENDENT-VI-VIII-FINDINGS.md. Root is applying body edits concurrently, so cited native line positions are the read snapshot and may move. No permission denial occurred; the blocker is an infrastructure transport failure, not automatic approval review.

## Additional mathematical source-error confirmation

VI1.6, original372/physical386, native `expose-06.tex` last paragraph of1.6: original defines Z_i=ker(L_i→L_{i−1}), then replaces L_{r+1} by Z_{r+1}. This induced arrow Z_{r+1}→L_r is zero, so that truncation cannot be the announced resolution. The last term should be Z_r, whose projectivity follows from projective dimension≤r+1. Native faithfully repeats the original index and only has a hidden source comment; add a visible 译校注 identifying the original index error while retaining printed body. Individual original372 image inspected.

VI5.10, original407/physical421: the intermediate expression in the calculation is printed `(-1)^r γ^r(F−x′)` where substitution E−r−1−x′=F−r requires `F−r`. Native silently uses F−r. Add visible 译校注 identifying original F−x′. Individual original407 image checked.

VII4.11 original465 high-resolution glyph check: `/tmp/sga6-r3-p465-K-crop.png` (4× crop) confirms the localization sequence first term is a **superscript** dot `K^•(Z′)`, exactly like the next K^•(X), K^•(U), not a subscript. The later y∈j_*(K^•(Z′)) is also superscript. Preserve printed form and note that the use for possibly singular Z′ here is the coherent-sheaf Grothendieck group; do not silently normalize the original glyph.

VI6.2 original409/physical423 last reference individually inspected is `(V3.9.1)`; native currently givesV3.9.6. Restore original reference or visibly identify a deliberate correction; this is a glyph/source-reference discrepancy.

Image-review milestone: all51 VI original pages365–415 now individually viewed at readable resolution, equations and diagrams compared with already-read native body. VII/VIII image review remains in progress, per ledger.

VII1.8 numbering: native canonical short exact sequence explicitly bears tag(1.8.1), but original425/physical439 has no printed number on that sequence. Original424/physical438 instead has a wrong reference to “suite(1.8.1)” for the preceding conormal sequence; native removed that reference but introduced the same visible tag on the next proposition. Preserve semantic anchors but remove an unoriginal printed tag; identify the original wrong reference visibly. Both pages individually inspected.

Original-heading fidelity: native VI gives descriptive headings not printed in the original at1.2,1.8,1.9,1.10–1.11,2.2–2.4,2.7–2.8,6.5 (originals are numbered paragraphs or named statements); native VIII adds “定理3.6的证明（续）” before original486, which contains only the sentence announcing that the proof occupies the rest of the exposé. These are not original titles. Preserve anchors and return to the original numbered-paragraph hierarchy if following original layout.

Omitted original citations confirmed: VI1.14 original380[3] (native names Hakim without citation); VI2.8 original389(IV2.11.1); VI5.3 original403V3.9.1 and3.10; VI6 opening407IV2.9; VII1.3 original418EGAIV16.9.7 and16.9.8; VII1.5 original420compareEGAIV19.1.5(ii); VII1.7 original422compareEGAIV19.1.5(iv) and423[1],XVI5 for the transitivity spectral sequence; VII1.8(iii) original425VI1.2; VII1.9 original428III4.1. Restore these original references rather than treating citation loss as mathematical simplification.

VII2.5 first proof sentence, original432/physical446, says “On a vu en2.3…” for the O_T-algebra structure; native currently says “在2.2中已看到” before the correctly cited alternation result2.2. Restore the first citation to2.3 (native reference transcription error).

VII2.5 original433/physical447 writes `Tor_1≅(O_T)^n` after computing the common-generator rank p; original434/physical448 similarly writes `Λ(O_T)^n` for the algebra isomorphism. The n is undefined here; native correctly uses p, but a visible note must identify the original n/p slip.

VII2.5 original432/434/435 uses the conormal subscripts N_{Y/X},N_{Z/X},N_{T/X}, opposite to the earlier printed definition1.6 N_{X/Y}; native consistently normalizes these to N_{X/Y},N_{X/Z},N_{X/T}. Preserve local original notation or add a visible notation note identifying the original reversal, rather than silently treating it as scan OCR. Original images individually checked.

VI5.9 notation, original405/physical419: the coefficientwise extension map is printed `\bar f_*`, not ξ_t. Native's `\xi_t` throughout this paragraph is an unoriginal map name. Minimal replacement throughout5.9: ξ_t→\bar f_* (retaining original formulas otherwise). This is an original-symbol transcription discrepancy, not an original mathematical error.

VII4.7 original457/physical471 prints `K_1=K/(P)` and similarly `1+(K/(P))[[t]]` although456 defines P∈K[L]. Native correctly spells K[L]/(P), but should identify the printed missing[L] via visible 译校注.

VII3.4 original441/physical455 says apply the functor f_* to a projective resolution, while its surrounding formulas and the construction require f^*. Native correctly says f^*, so identify the original functor-index slip visibly.

VII3.7 source445/physical459 formula for v∘u(y) ends with f^*(i_*(x)) (x undefined; y intended), and source446/physical460 later writes j_*y′=f^*x with the sign missing although the paragraph starts from j_*y′+f^*x=0. Native's compressed proof and correct starting relation eliminate these source slips; retain a visible note if presenting the corrected argument.

Image-review milestone: all50 VII original pages416–465 individually viewed, including high-resolution465 K-symbol crop. No unexplained λ-operation variable error was found in457(4.7.2): enlarged crop confirms its first factor is λ^{n−p}(x), which agrees with native. Native final-PDF visual pass remains pending.

VIII1.8 original474/physical488 draws p:V→V′ in the all-smooth triangle, although the preceding paragraph defines p:V′→V. Native correctly draws V′→V, silently. Add visible 译校注 explaining the original reversed p arrow.

VIII2.1 original475/physical489 chain before(2.1.1) ends in Ω¹_{V/X}⊗O_X while its preceding module and intended target use Ω¹_{V/Y}. Native correctly uses V/Y twice, but identify the original V/X subscript slip visibly. Same page source `(1.5.1)` reference slip is already listed.

VIII1.5 original472/physical486 last sentence says smooth over undefined W (the displayed diagram uses Z). Native adds an unsupported explanation “其中W是Z的相应开集”. Remove this invented clause; retain original W with visible note that W is not introduced and the diagram indicates Z is intended, or use corrected Z with an explicit original-print note.


## Final original-image pass (133/133 pages)

VIII466–497 (all32pages) now individually viewed and compared against the complete native text already read. This completes the original image pass for VI51 + VII50 + VIII32 =133pages. Native frozen-PDF visual review is still pending. No body file was edited by this worker.

- VIII3.3, native `expose-08.tex:496`, original483/physical497: original high-resolution crop `/tmp/sga6-r3-p483-chern-crop.png` clearly prints `Ch(Gr_λ Λ)`: **lowercase lambda subscript and separate baseline capital Lambda**. Native `\operatorname{Ch}(\Gr_{\Lambda})` drops λ and moves Λ into the subscript. Minimal correction: `\operatorname{Ch}(\Gr_\lambda\Lambda)`. An earlier tentative γ reading was explicitly withdrawn before implementation.
- VIII2.6, original480/physical494, transitivity triangle: its left bottom object is `Lf^*(L^{Y/Z}_•)`; native ordinary `f^*` drops the derived-functor L. Restore the initial L (root notified).
- VIII5.2, native `expose-08.tex:925–933`, original494/physical508: Chinese syntax is broken by displaced “定义。” after the displayed Ω¹_{B/Y} formula. Minimal repair: change the first fragment “所以 \(\Omega^1_{V/Y}\) 由” to “所以 \(\Omega^1_{V/Y}\) 由下列模定义：”, then delete the stray “定义。” before “为看出其分次”. Preserve the separate visible note about the original V/Z slip.

All exposé and section titles, descriptive subsection additions, named-statement headings, numbered paragraphs and bibliography titles were compared with the original. The precise 27-change, body-read-only proposal is saved in `R3-INDEPENDENT-VI-VIII-HEADINGS.patch` and JSON. These proposals retain semantic stable targets while removing unoriginal visible heading text/numbers. Root is integrating them; the proposal is a snapshot, not an instruction to reapply already integrated edits.


## Final remaining-item patch handoff

`R3-INDEPENDENT-VI-VIII-REMAINING.patch` contains20 exact replacement proposals against the root's current native text snapshot; `patch --dry-run -p1` passes for all three body files. The worker did not write body files. JSON records individual source pages and exact old/new strings; the audit-only generator preserves reproducibility.

The patch restores all previously reported missing citations, identifies VII2.5's reversed conormal indices and VII3.4's printed f_* slip, restores the explicit VII3.7 calculation chain on original445–446 with visible x/y and sign notes, identifies original447's unsupported extension of regularity to all X′, and restores both local cases of perfection and the cohomology-class argument. It also moves VIII1.8's reversed-arrow note to the all-smooth triangle and identifies VIII2.1's printed V/X slip. Original445–447 rasters were revisited for this patch. No claims of final native-PDF inspection are made here.
