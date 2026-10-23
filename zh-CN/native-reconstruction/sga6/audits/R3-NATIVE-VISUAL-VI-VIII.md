# VI–VIII frozen native-PDF visual review

Inspected PDF: `/tmp/SGA6-R3-frozen-review.pdf`; SHA256 `f62682abf7d50954eeff6099c62d7c29a641073f418f1ead07fa16a2c161b195` (independently verified). All79 assigned physical pages236–314 (native printed231–309) individually viewed as108dpi PNGs. This is not contact-sheet-only review.

Seven complex diagram details were additionally viewed at216dpi: physical277,279,293,295,300,301,305. Restored section arrows, vertical i″, derived cotangent triangle, distinguished triangle, exact-sequence diagrams and Riemann–Roch arrow labels are legible, correctly separated and unclipped. Title demotion and restored VII3.7 calculation chains render normally. No missing glyphs, clipped formulas, overlapping diagram objects/arrows, or unreadable footnotes were found.

Minor typography findings, all reported to root:

|Physical page|Native page|Issue|
|---|---|---|
|278|273|Footnote154 marker occupies a line alone after display|
|280|275|Footnote157 marker starts its own line before 所以/display|
|259|254|Footnote146 marker appears at start of new paragraph after display chain|
|285|280|Footnote159 anchor starts next page after preceding display|
|297|292|Footnote166 anchor starts paragraph after display|
|298|293|Footnote167 anchor starts paragraph after display|
|304|299|Footnote171 anchor starts paragraph after display|
|307|302|Chinese full stop occupies a separate line after displayed formula|
|312|307|Chinese full stop occupies a separate line after displayed formula|

Move the affected footnote anchors to the preceding introductory prose without changing note contents or mathematics. Footnote154 is the clearest isolated line;159 has drifted to the next page. Place the two full stops within their preceding display or adjacent paragraph without a separate line. These are local typographic fixes; they do not reopen source-content review.

Body files were read only. JSON and TSV enumerate every actually viewed page and the exact reviewed PDF hash. Any replacement PDF should be checked again at the affected pages and page-break boundaries; this review certifies only the frozen hash above.
