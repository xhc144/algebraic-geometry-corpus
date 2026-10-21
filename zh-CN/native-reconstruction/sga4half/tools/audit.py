#!/usr/bin/env python3
"""Compare stable native structures; this is not a semantic translation certificate."""
from pathlib import Path
import argparse,re,json,hashlib,collections,datetime
p=argparse.ArgumentParser();p.add_argument('--english',required=True);a=p.parse_args()
root=Path(__file__).resolve().parents[1];src=Path(a.english).resolve();text=src.read_text();parts={int(m[1]):m[2] for m in re.finditer(r'% BEGIN INCLUDED components/sga4half_(\d+)_en\.tex\n(.*?)% END INCLUDED',text,re.S)}
patterns={'labels':r'\\label\{([^}]+)\}','references':r'\\(?:ref|eqref|nameref)\{([^}]+)\}','hyperreferences':r'\\hyperref\[([^\]]+)\]','citations':r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}','tags':r'\\tag\{([^}]+)\}','environments':r'\\(?:begin|end)\{([^}]+)\}'}
result=[]
for i,en in sorted(parts.items()):
 f=root/f'chapters/chapter-{i:02}.tex';zh=f.read_text();r={'chapter':i,'source_lines':len(en.splitlines()),'output_lines':len(zh.splitlines()),'output_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'native_xymatrix':{'source':en.count('\\xymatrix'),'output':zh.count('\\xymatrix')},'display_delimiters':{'source':en.count('\\['),'output':zh.count('\\[')},'review_file':f'audit/chapter-{i:02}-review.md'}
 for name,pat in patterns.items():
  x=re.findall(pat,en);y=re.findall(pat,zh);cx=collections.Counter(x);cy=collections.Counter(y);r[name]={'source_count':len(x),'output_count':len(y),'missing_tokens':list((cx-cy).elements()),'added_tokens':list((cy-cx).elements()),'exact_sequence_match':x==y}
 result.append(r)
allzh='\n'.join(f.read_text() for d in ['chapters','frontmatter'] for f in (root/d).glob('*.tex'));labs=re.findall(patterns['labels'],allzh);refs=re.findall(patterns['references'],allzh)+re.findall(patterns['hyperreferences'],allzh)
obj={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'chapters':result,'source_component_lines':sum(r['source_lines'] for r in result),'all_stable_source_labels_preserved':all(not r['labels']['missing_tokens'] for r in result),'undefined_internal_reference_keys':sorted(set(refs)-set(labs)),'duplicate_label_keys':[(k,v) for k,v in collections.Counter(labs).items() if v>1],'raster_includegraphics_commands':allzh.count('\\includegraphics'),'source_review_warning':'Verified French-supported repairs and original hierarchy restoration intentionally create recorded differences. No token count certifies prose completeness or mathematical correctness.'}
(root/'audit/structural-comparison.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'source_component_lines':obj['source_component_lines'],'all_source_labels_preserved':obj['all_stable_source_labels_preserved'],'undefined':obj['undefined_internal_reference_keys'],'duplicates':obj['duplicate_label_keys'],'native_diagrams':sum(r['native_xymatrix']['output'] for r in result)},ensure_ascii=False))
