# Chapter 2 checkpoint

Source: `FGA/FGA-Explained-Fantechi-AMS-2005.pdf`, printed pp.13–40 / PDF25–52.

Current saved translation: the entire chapter, printed pp.13–40 / PDF25–52, all paragraphs, statements 2.1–2.64, named Yoneda lemmas, examples, diagrams, and proofs, including the full proof of theorem 2.55 and the sheafification construction. All 28 actual source pages have been rendered and visually read while translating. No independent review has been performed. A standalone wrapper compiled twice with shared book-style.tex under XeLaTeX, producing 23 native pages. The second compilation has no errors, overfull boxes, missing glyphs, undefined references or rerun warnings. All 23 rendered output pages were visually inspected as contact sheets; selected dense diagrams were inspected at page resolution. This is a translation/reconstruction review, not independent mathematical certification.

The following are actual printed-source anomalies, verified against the scan and preserved verbatim in mathematical meaning, with `source-error` comments in TeX. They are not OCR readings silently promoted into text:

- p15 example (ii): `{1}` called “closed” although open sets are listed as ∅,{1},{0,1}.
- p15 example (iii): displayed restriction has no `op`.
- p16 continuation of (iii): “closed subset σ that is not open” although the functor classifies open subsets.
- p16 example 2.4: prints O(V)→O(V), rather than O(V)→O(U).
- p16 example 2.5: prints O(S) as target of image of x although the morphism has source U.
- p17 example 2.6: prints O_S^n in the quotient sentence, whereas the preceding sentence uses O_U^{n+1}.
- p17 example 2.7: the pullback display starts ψ*E, whereas M is the sheaf being pulled back.
- p18 example 2.9: prints Spec ξ at first occurrence, then Spec κ.

Original names remain in Latin script. All reconstructed diagrams use native TikZ, not scan overlays. External references retain their printed numbers for later integration.


Further printed-source anomalies preserved in TeX comments:

- p23 refers to action on U after fixing X; the definition of the coproduct map mentions φ(j) for i∈I.
- p25 proposition 2.22 prints “finite group objects” rather than “discrete group objects”.
- p27 proof of proposition 2.33: the passage from (iii) to (iv) does not explicitly restrict f to U′; U″ is only called open before concluding U′∪U″ is quasi-compact.
- p28 proof of proposition 2.35 labels the base-change argument (iii), and says the inverse image defining U_i′ is in X rather than X′.
- p30 equalizer prose says maps f,g where its diagram uses g,h.
- p31 proof of proposition 2.39 calls f:T→U instead of T→U_i, and calls f*ξ_i an element of FU rather than FT.
- p32 proof of proposition 2.42 twice references “Corollary 2.42”; proof of lemma 2.43 uses “presheaf” where separation is needed; subsequent prose uses U_j instead of V_j.
- p34 definition 2.52 saturates by all refinements, with the printed refinement convention; this is retained, not mathematically repaired.
- p35 remark 2.56 gives a restricted map V_p→U where target X is required.
- p36 proof of proposition 2.59 first equalizer display has U_i×_U U_i in an i,j product; the first injection repeats Hom_S rather than using Hom.
- p37 proof of lemma 2.60 calls V_ia open without explicitly affine; its following displayed product is indexed k although its terms are V_ia.
- p38 proof of theorem 2.55 prints V_i=g^{-1}V_i and displays an extra V_i between g|_{V_i} and X_i.
- p39 proof of lemma 2.62 prints U instead of Y as target of both composites; definition 2.63 calls set elements “isomorphic”; proof of theorem 2.64 says the η-pullbacks in G have images in F^a though no G→F^a morphism is given.
