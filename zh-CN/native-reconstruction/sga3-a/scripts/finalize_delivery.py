#!/usr/bin/env python3
"""Write external final-byte manifests, deliberately excluded from sourceZIP."""
from pathlib import Path
import hashlib,json,subprocess,zipfile
r=Path(__file__).resolve().parents[1]
sha=lambda data:hashlib.sha256(data).hexdigest()
rebuilt=json.loads((r/'audit/PACKAGE_REBUILD.json').read_text())
assert rebuilt['state']=='passed'
frozen=rebuilt['frozen_archive_tex_manifest']
with zipfile.ZipFile(r/'sga3-a-source.zip') as z:
    names=z.namelist();assert 'SHA256SUMS' not in names and 'DELIVERY.json' not in names
    actual={n:sha(z.read(n)) for n in names if n.endswith('.tex')}
    assert actual==frozen,'Final package TeX differs from actually rebuilt extraction'
    # The obsolete root delivery table must not survive in a nested archive path.
    assert not any(Path(n).name=='SHA256SUMS' for n in names)
native=json.loads((r/'audit/PDF-CURRENT.json').read_text())
assert native['pdf_sha256']==sha((r/'sga3-a-zh.pdf').read_bytes())
assert not native['missing_pdf_named_destinations'] and not native['off_page_text_spans']
ledger=json.loads((r/'audit/reference-wrapup/APPLIED.json').read_text())
verified=json.loads((r/'audit/reference-wrapup/VERIFIED.json').read_text());assert verified['result']=='passed'
def artifact(name):
    data=(r/name).read_bytes();return {'path':name,'sha256':sha(data),'bytes':len(data)}
pdf=artifact('sga3-a-zh.pdf');pdf['pages']=native['pages'];source=artifact('sga3-a-source.zip')
source.update({'files':len(names),'rebuilt_TeX_dependency_files':len(frozen),'all_rebuilt_TeX_hashes_identical':True,'root_checksum_table_in_zip':False,'delivery_manifest_in_zip':False})
d={'scope':'SGA3 first 14 of 28 published exposés plus frontmatter and Tome I index','branch':subprocess.check_output(['git','branch','--show-current'],cwd=r,text=True).strip(),'translation_first_pass_commit':subprocess.check_output(['git','rev-parse','9217d3d'],cwd=r,text=True).strip(),'reference_cleanup_baseline_commit':ledger['baseline_commit'],'current_commit':'Containing normal git commit, verified on the remote after commit creation; exact hash is supplied in task result.','pdf':pdf,'source_zip':source,'tex_entry':'main.tex','checksum_table':'SHA256SUMS','checksum_verification':'Final PDF/ZIP byte hashes; both this manifest and SHA256SUMS are outside sourceZIP, avoiding self-reference.','coverage':'audit/COVERAGE.json','independent_source_closure':'audit/reviews/SCOPE-CLOSURE-independent.json','clean_rebuild':'audit/PACKAGE_REBUILD.json','reference_cleanup':{'ledger':'audit/reference-wrapup/APPLIED.json','human_readable':'audit/reference-wrapup/APPLIED.md','counts':ledger['counts'],'new_exact_anchors':len(ledger['new_anchors']),'verification':'audit/reference-wrapup/VERIFIED.json','remaining':['VI-B definition6.5 citation6.2(iv)','VII-A7.4.3 editor note(71)','XI4.5 citation3.7'],'pending_policy':'Original citation wording retained, misleading hyperlink removed, visible 〔引文待核〕 marker.'},'review_limits':{'english_source_chinese_independent_first_pass':'Complete for all14assigned units, frontmatter and292-entry TomeI index.','systematic_french_final_collation':'Unperformed for the whole assigned scope: all14units, frontmatter and index. Only historical I6.5.3/I6.6 spot checks are evidenced.','french_evidence':'audit/reference-wrapup/FRENCH_COLLATION_COVERAGE.json','source_mathematical_doubts':'Unresolved and honestly preserved in audit/SOURCE_ISSUES.md; not mathematical certification.','loose_release_TeX_manifest_mismatch':'Still unresolved; verified sourceZIP chosen and recorded in audit/SOURCE_LOCK.json.'}}
(r/'DELIVERY.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(r/'SHA256SUMS').write_text(''.join(d[k]['sha256']+'  '+d[k]['path']+'\n' for k in ('pdf','source_zip')))
print(json.dumps({'pages':pdf['pages'],'pdf_sha256':pdf['sha256'],'source_zip_sha256':source['sha256'],'tex_files':len(frozen),'archive_files':len(names),'no_checksum_self_reference':True},ensure_ascii=False))
