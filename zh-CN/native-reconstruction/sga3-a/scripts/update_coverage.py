#!/usr/bin/env python3
"""Record actual assembled component and native figure coverage after a build."""
from pathlib import Path
import argparse,json,re
import fitz
p=argparse.ArgumentParser();p.add_argument('--completed',nargs='+',required=True);a=p.parse_args()
r=Path(__file__).resolve().parents[1]
checks=json.loads((r/'audit/COMPONENT_CHECKS.json').read_text())
scope=json.loads((r/'audit/SCOPE.json').read_text())
seen=set()
def visit(f):
 f=f.resolve()
 if f in seen or not f.is_file():return
 seen.add(f)
 if f.suffix!='.tex':return
 for n in re.findall(r'\\input\{([^{}#]+)\}',f.read_text())+re.findall(r'\{((?:chapters|figures)/[^{}#]+)\}',f.read_text()):
  if '\\' in n:continue
  q=r/n
  if not q.suffix:q=q.with_suffix('.tex')
  if not q.is_file() and Path(str(q)+'.tex').is_file():q=Path(str(q)+'.tex')
  visit(q)
visit(r/'main.tex')
pdf=fitz.open(r/'build/main.pdf')
end=scope['loose_reader_exact_boundaries_inclusive'][a.completed[-1]][1]
rows=checks['components'];toc=pdf.get_toc()
d={'completed_exposes':a.completed,'complete_frontmatter':['Editorial Notice','Introduction'],'source_component_count':len(rows),'source_component_lines':sum(x['source_lines'] for x in rows),'translation_component_lines':sum(x['translation_lines'] for x in rows),'native_external_diagram_files':sum(1 for x in seen if 'figures' in x.relative_to(r).parts),'all_reference_key_multisets_preserved':all(k['same_key_multiset'] for x in rows for k in x['keys'].values()),'all_environment_multisets_preserved':all(x['environment_multisets_preserved'] for x in rows),'all_footnote_command_counts_preserved':all(x['footnote_commands_source']==x['footnote_commands_translation'] and x['footnotetext_source']==x['footnotetext_translation'] for x in rows),'unresolved_sga_ref_keys':len(checks['unresolved_sga_ref_links']),'source_line_span_for_completed_exposes':[489,end],'next_loose_reader_line':end+1,'pdf_pages':len(pdf),'pdf_bookmark_count':len(toc),'pdf_bookmark_key_leaks':[t for _,t,_ in toc if 'sga3:' in t],'pdf_image_object_count':sum(len(page.get_images()) for page in pdf),'note':str(len(a.completed))+' of14 assigned units integrated; known source doubts and actual review limits remain in SOURCE_ISSUES.md. Figure counts use the active input closure, excluding future diagrams on disk.','upstream_provenance_notice_translated_source_lines':[179,205]}
(r/'audit/COVERAGE.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(d,ensure_ascii=False))
