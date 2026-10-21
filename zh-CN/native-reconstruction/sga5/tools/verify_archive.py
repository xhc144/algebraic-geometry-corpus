#!/usr/bin/env python3
"""Check the final source ZIP and bind it to the successful clean build.

The external result and SHA256SUMS are excluded from the archive, avoiding an
archive that would have to contain its own final checksum.
"""
from pathlib import Path
import hashlib, json, stat, zipfile

r=Path(__file__).resolve().parents[1]
sha=lambda data:hashlib.sha256(data).hexdigest()
archive=r/'SGA5-zh-CN-source.zip'
replay=json.loads((r/'qa/clean-replay.json').read_text())
assert replay['clean_replay']=='SUCCESS'
assert replay['main_pdf_sha256']==sha((r/'SGA5-zh-CN.pdf').read_bytes())
assert replay['extracted_text_equal_all_pages']
assert replay['word_bounding_boxes_equal_all_pages']
assert replay['rendered_pixel_hash_equal_all_pages_at_scale_0_7']
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(set(z.namelist()))
    manifest=z.read('sga5/SOURCE_BUNDLE_MANIFEST.sha256').decode()
    members={}
    for line in manifest.splitlines():
        h,name=line.split('  ',1)
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
        data=z.read('sga5/'+name)
        assert sha(data)==h,name
        assert data==(r/name).read_bytes(),('archive/current file mismatch',name)
        members[name]=h
    assert set(z.namelist())=={'sga5/'+n for n in members}|{'sga5/SOURCE_BUNDLE_MANIFEST.sha256'}
    for name,h in replay['compiled_input_manifest'].items():
        assert members[name]==h,('replayed build input changed',name)
    build_mode=stat.S_IMODE(z.getinfo('sga5/build.sh').external_attr>>16)
    assert build_mode==0o755
    assert not any(n.lower().endswith(('.pdf','.png','.jpg')) for n in members)
fls=r/'.build/SGA5-zh-CN.fls'
if fls.exists():
    current=set()
    for line in fls.read_text().splitlines():
        if not line.startswith('INPUT '):continue
        p=Path(line[6:]);p=(r/p).resolve() if not p.is_absolute() else p.resolve()
        if p.is_relative_to(r) and '.build' not in p.relative_to(r).parts:
            current.add(p.relative_to(r).as_posix())
    assert current==set(replay['compiled_input_manifest']), 'main/replay compiled input set differs'
result={
    'status':'PASS', 'date':'2026-10-21',
    'source_zip_sha256':sha(archive.read_bytes()),
    'source_zip_bytes':archive.stat().st_size,
    'manifest_sha256':sha(manifest.encode()),
    'hashed_source_members':len(members),
    'archive_members':len(members)+1,
    'all_member_hashes_and_current_source_bytes_match':True,
    'CRC_test':'PASS', 'build_sh_Unix_mode':'0755',
    'clean_replay_proof':'qa/clean-replay.json',
    'clean_replay_staged_archive_sha256':replay['staged_source_zip_sha256'],
    'compiled_input_files_identical_to_clean_replay':len(replay['compiled_input_manifest']),
    'changed_compiled_input_files':[],
    'main_and_replay_input_sets_equal':True if fls.exists() else 'not checked in this invocation',
    'final_pdf_sha256':replay['main_pdf_sha256'],
    'final_pdf_pages':replay['pages'],
    'independent_replay_comparison':'All271 page texts, word bounding boxes and rendered pixel hashes equal main PDF.',
    'packaging_note':'Final archive contains finalized QA metadata and packaging tools added after the staged clean build. Every actual compiled input byte is identical to that successful independent replay. This external record is deliberately outside the archive.',
}
(r/'FINAL_ARCHIVE_VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
checks=['SGA5-zh-CN.tex','preamble.tex','SGA5-zh-CN.pdf','SGA5-zh-CN-source.zip','FINAL_ARCHIVE_VERIFICATION.json']
(r/'SHA256SUMS').write_text(''.join(sha((r/n).read_bytes())+'  '+n+'\n' for n in checks))
print(json.dumps(result,ensure_ascii=False,indent=2))
