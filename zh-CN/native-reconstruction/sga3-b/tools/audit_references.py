#!/usr/bin/env python3
"""Classify exact target identities; this does not validate citation semantics."""
from pathlib import Path
from collections import Counter
import json,re
p=Path(__file__).resolve().parents[1]
tr=re.compile(r'\\(?:SGARefTarget|SGAInlineRefTarget|SGAInlineEquationTarget|SGANextSectionTarget|label)\{([^{}]+)\}')
lr=re.compile(r'\\(?:SGARefLink|ref|eqref|pageref)\{([^{}]+)\}')
allref=re.compile(r'\\(?:SGARefLink|SGAUnlinkedRef|ref|eqref|pageref)\{([^{}]+)\}')
clean=lambda s:re.sub(r'(?<!\\)%[^\n]*','',s)
full=json.loads((p/'evidence/NATIVE_REFERENCE_TARGET_INDEX.json').read_text())['targets']
sources={f.stem:clean(f.read_text()) for f in (p/'source-reference').glob('*.tex') if f.stem!='original-master'}
translations={f.stem.removesuffix('-zh'):clean(f.read_text()) for f in (p/'chapters').glob('*-zh.tex')}
assigned_targets=set(k for s in sources.values() for k in tr.findall(s))
translated_targets=set(k for s in translations.values() for k in tr.findall(s))
unresolved=Counter(k for s in translations.values() for k in lr.findall(s) if k not in translated_targets)
classes={'first_half_external':{},'assigned_target_missing':{},'inherited_missing_in_native_source':{}}
for k,n in sorted(unresolved.items()):
 c='assigned_target_missing' if k in assigned_targets else 'first_half_external' if k in full else 'inherited_missing_in_native_source'
 classes[c][k]={'occurrences':n,'native_target_locations':full.get(k,[])}
comparison={}
for u,s in sources.items():
 t=translations.get(u,'')
 a=Counter(allref.findall(s));b=Counter(allref.findall(t))
 comparison[u]={'source_references':sum(a.values()),'translated_references':sum(b.values()),'key_multiset_equal':a==b,'source_keys_absent':dict(a-b),'translation_keys_added':dict(b-a)}
result={'classification':classes,'identity_counts':{k:len(v) for k,v in classes.items()},'source_translation_reference_comparison':comparison,'limits':['Exact identities only: a target that exists can still be the wrong mathematical citation.','The source macro falls back to visible citation text when a target is absent. No target or visible number has been invented.','Original inherited wrong links and mathematical source concerns remain in coverage/*.json and SOURCE_REVIEW.md.'],'full_source_index_archive_sha256':json.loads((p/'evidence/NATIVE_REFERENCE_TARGET_INDEX.json').read_text())['source_archive_sha256']}
result['intentionally_unlinked_external_source_keys']=dict(Counter(k for s in translations.values() for k in re.findall(r'\\SGAUnlinkedRef\{([^{}]+)\}',s)))
result['semantic_repair_records']=['review/20261022/ROOT_REFERENCE_CORRECTIONS.json']+[str(f.relative_to(p)) for f in sorted((p/'review/20261022').glob('*reference-corrections.json'))]
(p/'evidence/REFERENCE_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Unresolved target identities:',result['identity_counts'])
