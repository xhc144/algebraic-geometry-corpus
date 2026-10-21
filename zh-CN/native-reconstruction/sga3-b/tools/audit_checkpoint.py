#!/usr/bin/env python3
"""Mechanical coverage/reference check, not a mathematical proofreading claim."""
from pathlib import Path
from collections import Counter
import json,re,hashlib
p=Path(__file__).resolve().parents[1]
lock=json.loads((p/'SOURCE_LOCK.json').read_text())
units={r['unit']:r for r in lock['expanded_units']}
target_re=re.compile(r'\\(?:SGARefTarget|SGAInlineRefTarget|SGAInlineEquationTarget|SGANextSectionTarget|label)\{([^{}]+)\}')
link_re=re.compile(r'\\(?:SGARefLink|ref|eqref|pageref)\{([^{}]+)\}')
strip_comments=lambda s:re.sub(r'(?<!\\)%[^\n]*','',s)
compiled=[];records=[];targets=[];links=[]
for unit,entry in units.items():
 src=(p/entry['path']).read_text();b=(p/entry['path']).read_bytes()
 assert hashlib.sha256(b).hexdigest()==entry['sha256'],unit+' frozen source changed'
 cf=p/'coverage'/(unit+'.json');tf=p/'chapters'/(unit+'-zh.tex')
 c=json.loads(cf.read_text()) if cf.exists() else {}
 intervals=next((c[k] for k in ['translated_source_intervals','translated_source_lines','covered_source_intervals'] if k in c),[])
 count=sum(z-a+1 for a,z in intervals)
 complete=bool(c.get('complete',c.get('translation_complete',False)))
 if not tf.exists():records.append({'unit':unit,'source_lines':entry['lines'],'translated_source_lines':0,'complete':False});continue
 s='\n'.join(src.splitlines()[a-1:z][i] for a,z in [] for i in []) if False else '\n'.join('\n'.join(src.splitlines()[a-1:z]) for a,z in intervals)
 t=tf.read_text();ss=strip_comments(s);tt=strip_comments(t)
 src_targets=target_re.findall(ss);tr_targets=target_re.findall(tt)
 targets.extend(tr_targets);links.extend(link_re.findall(tt));compiled.append(t)
 norm=lambda x:re.sub(r'\s+','',x)
 inline=lambda x:re.findall(r'\\\((.*?)\\\)',x,re.S)
 display=lambda x:re.findall(r'\\\[(.*?)\\\]',x,re.S)
 math_record={}
 for name,extract in [('inline',inline),('display',display)]:
  sm=Counter(map(norm,extract(ss)));tm=Counter(map(norm,extract(tt)))
  math_record[name]={'source_count':sum(sm.values()),'translation_count':sum(tm.values()),'exact_token_multiset_equal':sm==tm,'source_difference_count':sum((sm-tm).values()),'translation_difference_count':sum((tm-sm).values()),'note':'Prose within formulas, punctuation placement and diagram spacing need human review when exact tokens differ.'}
 records.append({'unit':unit,'source_lines':entry['lines'],'translated_source_intervals':intervals,'translated_source_lines':count,'complete':complete,'target_counts':[len(src_targets),len(tr_targets)],'source_targets_absent_in_translation':list((Counter(src_targets)-Counter(tr_targets)).elements()),'translation_targets_not_in_source':list((Counter(tr_targets)-Counter(src_targets)).elements()),'math':math_record})
all_targets=set(targets)
# Completeness of a link target is checked separately from link semantic correctness.
unresolved=Counter(x for x in links if x not in all_targets)
log=(p/'build/main.log').read_text(errors='replace') if (p/'build/main.log').exists() else ''
result={'complete':all(r['complete'] for r in records),'units':records,'total_assigned_source_lines':sum(x['lines'] for x in units.values()),'translated_source_lines':sum(r['translated_source_lines'] for r in records),'duplicate_translated_targets':{k:v for k,v in Counter(targets).items() if v>1},'unresolved_reference_targets_in_checkpoint':dict(sorted(unresolved.items())),'unresolved_reference_explanation':'Includes references to the first-half sibling volume, untranslated future material and inherited source errors. SGARefLink falls back to visible text. Existence does not establish semantic correctness.','last_live_build_log':{'missing_character_lines':re.findall(r'^Missing character:.*$',log,re.M),'overfull_lines':re.findall(r'^Overfull.*$',log,re.M),'undefined_reference_warning_lines':re.findall(r'^.*(?:undefined|multiply defined).*$' ,log,re.M)},'independent_mathematical_proofreading':'not completed','source_and_translation_prose_completeness':'only the declared translated intervals are represented; no summarization or placeholders count as completion'}
(p/'evidence/CHECKPOINT_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Source lines',result['translated_source_lines'],'/',result['total_assigned_source_lines'],'completed units',sum(r['complete'] for r in records),'/',len(records),'unresolved target identities',len(unresolved))
