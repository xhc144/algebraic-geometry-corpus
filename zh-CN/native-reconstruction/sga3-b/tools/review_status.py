#!/usr/bin/env python3
"""Aggregate actual bilingual review ledgers, separately from source validity."""
from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parents[1]
lock=json.loads((p/'SOURCE_LOCK.json').read_text())
root=p/'review/20261022'
records=[]
for unit in lock['expanded_units']:
 u=unit['unit']; names=['XXVI-prefix','XXVI-tail'] if u=='XXVI' else [u]
 intervals=[]; complete=True;ledgers=[]
 for name in names:
  f=root/(name+'.json')
  if not f.exists(): complete=False;continue
  d=json.loads(f.read_text());intervals.extend(d.get('reviewed_source_intervals',[]));complete&=d.get('complete',False)
  ledgers.append(str(f.relative_to(p)))
 intervals.sort();merged=[]
 for a,z in intervals:
  assert 1<=a<=z<=unit['lines'],u+' invalid review interval'
  if merged and a<=merged[-1][1]+1:merged[-1][1]=max(z,merged[-1][1])
  else:merged.append([a,z])
 full=bool(complete and merged==[[1,unit['lines']]])
 tf=p/'chapters'/(u+'-zh.tex')
 records.append({'unit':u,'source_lines':unit['lines'],'reviewed_source_intervals':merged,'reviewed_source_lines':sum(z-a+1 for a,z in merged),'independent_fidelity_reading_complete':full,'ledgers':ledgers,'source_sha256':unit['sha256'],'current_translation_sha256':hashlib.sha256(tf.read_bytes()).hexdigest()})
result={'review_type':'Independent paragraph-by-paragraph bilingual fidelity reading, with explicit historical review reuse forXXV and parts ofXXIV.','independent_fidelity_reading_complete':all(r['independent_fidelity_reading_complete'] for r in records),'reviewed_source_lines':sum(r['reviewed_source_lines'] for r in records),'source_lines_total':sum(r['source_lines'] for r in records),'units':records,'mathematical_source_validity_certified':False,'limits':['Full fidelity reading does not prove every source mathematical statement.','French verification is limited to explicitly recorded source locations.','The previous source and historical review hashes are retained; annotated source emendations and hyperlink-only post-review changes are recorded separately.']}
(root/'STATUS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Independent fidelity review',result['reviewed_source_lines'],'/',result['source_lines_total'],'complete',result['independent_fidelity_reading_complete'])
