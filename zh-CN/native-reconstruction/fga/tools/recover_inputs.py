#!/usr/bin/env python3
"""Regenerate the nine English inputs from the frozen local XML; no network."""
from pathlib import Path
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
parser = etree.XMLParser(resolve_entities=False, no_network=True)
transform = etree.XSLT(etree.parse(str(ROOT / "source/tooling/book.xsl"), parser), access_control=etree.XSLTAccessControl.DENY_ALL)
units = ["fga-foreword", "fga1", "fga2", "fga3.i", "fga3.ii", "fga3.iii", "fga3.iv", "fga3.v", "fga3.vi"]
for unit in units:
    document = etree.parse(str(ROOT / "source/generated-xml" / (unit + ".xml")), parser)
    (ROOT / "source/en-latex" / (unit + ".tex")).write_text(str(transform(document)))
print("Regenerated nine English body inputs only; Chinese author files were untouched.")
