#!/usr/bin/env python3
"""Freeze native Chinese delivery bundles from one already-integrated Git commit.

This coordinator-owned utility reads Git blobs and ZIP members. It never invokes
any author-supplied build, packaging, audit, or upload script.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import zipfile

import fitz

PREFIX = 'zh-CN/native-reconstruction/'
BOOKS = [
    ('sga3-a', 'SGA3-a', 'sga3-a-zh.pdf', 'sga3-a-source.zip'),
    ('sga3-b', 'SGA3-b', 'SGA3-b-zh.pdf', 'SGA3-b-source.zip'),
    ('sga4-a', 'SGA4-a', 'sga4-a.pdf', 'sga4-a-source.zip'),
    ('sga4-b', 'SGA4-b', 'SGA4-b-zh-CN.pdf', 'SGA4-b-zh-CN-source.zip'),
    ('sga4half', 'SGA4half', 'SGA4half-zh-CN.pdf', 'SGA4half-zh-CN-source.zip'),
    ('sga5', 'SGA5', 'SGA5-zh-CN.pdf', 'SGA5-zh-CN-source.zip'),
    ('sga6', 'SGA6', 'build/SGA6-zh-CN.pdf', 'SGA6-zh-CN-source.zip'),
    ('sga7-i', 'SGA7-I', 'sga7-i-zh.pdf', 'sga7-i-source.zip'),
    ('sga7-ii', 'SGA7-II', 'SGA7-II-zh-CN.pdf', 'SGA7-II-zh-CN-source.zip'),
    ('fga', 'FGA', 'outputs/FGA-zh-working.pdf', 'outputs/FGA-zh-working-source.zip'),
    ('fga-explained', 'FGA-Explained', 'FGA-explained-zh-CN.pdf', 'FGA-explained-zh-CN-source.zip'),
]
SECRET = re.compile(
    rb'(?:ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{60,}|'
    rb'AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|'
    rb'Authorization:\s*(?:Bearer|Basic)\s+[A-Za-z0-9+/=_-]{20,})'
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def safe_member(info):
    p = PurePosixPath(info.filename)
    assert not p.is_absolute() and '..' not in p.parts and '\\' not in info.filename
    assert not stat.S_ISLNK(info.external_attr >> 16)
    assert not any(x in {'.git', '.ssh', '.aws'} for x in p.parts)
    assert p.name not in {'.env', '.netrc', '.git-credentials'}
    assert not p.suffix.lower() in {'.ttf', '.ttc', '.otf', '.pfb'}


def checked_blob(repo, ref, path):
    data = git(repo, 'show', ref + ':' + path)
    assert not SECRET.search(data), 'Credential-shaped bytes in ' + path
    return data


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def write_zip(path, payload):
    assert len(payload) == len(set(payload))
    for name, data in payload.items():
        assert not SECRET.search(data), 'Credential-shaped bytes in ' + name
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == set(payload)
        assert all(z.read(k) == v for k, v in payload.items())
    return {'name': path.name, 'bytes': path.stat().st_size,
            'sha256': digest(path.read_bytes()), 'members': len(payload)}


def add_checksums(payload):
    payload['SHA256SUMS.txt'] = ''.join(
        digest(data) + '  ' + name + '\n' for name, data in sorted(payload.items())
    ).encode('utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--ref', required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--date', default='20261023')
    args = ap.parse_args()
    ref = git(args.repo, 'rev-parse', args.ref + '^{commit}').decode().strip()
    inventory = json.loads(checked_blob(args.repo, ref, PREFIX + '_coord/RESUME_INVENTORY.json'))
    states = {j['id']: j for j in inventory['jobs']}
    status = checked_blob(args.repo, ref, PREFIX + '_coord/RESUMED_STATUS.md')
    pdfs, sources, rows, omissions, source_files = {}, {}, [], [], []
    for number, (book, label, pdf_rel, zip_rel) in enumerate(BOOKS, 1):
        assert 'integrated' in states[book]['resume_state'], 'Unintegrated handoff: ' + book
        subprocess.run(['git', '-C', str(args.repo), 'merge-base', '--is-ancestor',
                        states[book]['checkpoint'], ref], check=True)
        base = PREFIX + book + '/'
        pdf = checked_blob(args.repo, ref, base + pdf_rel)
        archive = checked_blob(args.repo, ref, base + zip_rel)
        doc = fitz.open(stream=pdf, filetype='pdf')
        assert len(doc) == states[book]['pages'], 'Outdated PDF page count: ' + book
        if states[book].get('pdf_sha256'):
            assert digest(pdf) == states[book]['pdf_sha256'], book
        if states[book].get('source_zip_sha256'):
            assert digest(archive) == states[book]['source_zip_sha256'], book
        pdf_name = f'PDFs/{number:02d}_{label}-zh-CN.pdf'
        pdfs[pdf_name] = pdf
        row = {'id': book, 'label': label, 'content_commit': ref,
               'accepted_checkpoint': states[book]['checkpoint'],
               'author_checkpoint': states[book].get('author_checkpoint', states[book]['checkpoint']),
               'pages': len(doc), 'PDF_repository_path': base + pdf_rel,
               'PDF_member': pdf_name, 'PDF_sha256': digest(pdf),
               'source_archive_repository_path': base + zip_rel,
               'source_archive_sha256': digest(archive),
               'review_and_source_limits': states[book]['remaining'],
               'original_frontmatter_gap': states[book].get('original_frontmatter_gap'),
               'source_entrypoints': []}
        z = zipfile.ZipFile(io.BytesIO(archive))
        assert z.testzip() is None
        assert len(z.namelist()) == len(set(z.namelist()))
        for info in z.infolist():
            safe_member(info)
            if info.is_dir():
                continue
            name, data = info.filename, z.read(info)
            assert not SECRET.search(data), 'Credential-shaped bytes in ' + book + '/' + name
            assert not name.lower().endswith('.zip'), 'Unexpected nested source archive: ' + name
            if data.lstrip().startswith(b'%PDF-'):
                assert name.lower().endswith('.pdf'), 'Unexpected disguised PDF: ' + name
            if name.lower().endswith('.pdf'):
                # The sole known PDF in the native source archives is an optional
                # Chinese publisher-catalogue audit preview, never a build input.
                assert book == 'sga6' and name == 'SGA6-zh-CN/audits/R3-PUBLISHER-preview.pdf'
                preview = fitz.open(stream=data, filetype='pdf')
                assert 'XeTeX' in (preview.metadata.get('producer') or '')
                assert not any(p.get_images() for p in preview)
                assert '版本说明' in preview[0].get_text()
                omissions.append({'book': book, 'member': name, 'sha256': digest(data),
                                  'reason': 'Optional generated Chinese audit preview; source bundle contains no PDF files. Original author archive remains intact in Git.'})
                continue
            target = 'books/' + book + '/' + name
            assert target not in sources
            sources[target] = data
            source_files.append({'book': book, 'member': target, 'source_archive_member': name,
                                 'bytes': len(data), 'sha256': digest(data)})
            leaf = PurePosixPath(name).name
            if leaf == 'main.tex' and '/source/en-latex/' not in '/' + name:
                row['source_entrypoints'].append(target)
            elif book == 'sga5' and leaf == 'SGA5-zh-CN.tex':
                row['source_entrypoints'].append(target)
        assert row['source_entrypoints'], 'No entrypoint recorded for ' + book
        shallowest = min(n.count('/') for n in row['source_entrypoints'])
        row['source_entrypoints'] = [n for n in row['source_entrypoints']
                                     if n.count('/') == shallowest]
        rows.append(row)
    manifest = {'status': 'native_Chinese_revised_draft_delivery_snapshot_not_professional_human_final',
                'content_commit': ref, 'books': 9, 'workspaces': 11,
                'PDF_pages': sum(r['pages'] for r in rows), 'items': rows,
                'source_file_count': len(source_files), 'source_files': source_files,
                'source_bundle_omissions': omissions,
                'policy': 'No original foreign-language PDF, credentials, system font files or Git metadata. Native source-member bytes preserved; each book keeps its own style. No repository scripts executed.',
                'build_boundary': 'Individual selected source archives have recorded real rebuilds. This wrapper verifies CRC/SHA and preserves their editable build inputs; it does not claim a new mathematical review.'}
    readme = ("# 中文原生重建交付快照\n\n"
              f"底本提交：`{ref}`。9种书、11个分卷，共{manifest['PDF_pages']}页。\n\n"
              "这是本轮修订稿汇总，不是专业人工审定本。每书版式、名字、编号和原生图形保持各自版本；原著疑误与尚未闭合的引文见STATUS.md及bundle-manifest.json。\n\n"
              "PDF包只收录11份当前中文合卷PDF。源码包按books/分书保存原作者独立包的全部可编辑文件与依赖结构，解压后进入对应主文件所在目录，按该书BUILD.md使用XeLaTeX等已记录命令；不要混用不同书的模板。编译所需系统字体需自行安装，未捆绑字体文件。\n\n"
              "源码包不包含任何PDF；唯一省略项是SGA6可选的中文出版目录审计预览，完整原作者包仍在仓库。源码文件未因打总包而改写，逐文件哈希在清单中。两包均不含原始外文PDF、凭据或Git元数据。\n\n"
              "某些源文件或书目保留原文人名和必要原文引文，这是可编辑译稿的组成部分。编译和链接目标存在不等于所有原著数学证明或全部链接语义已获专业终审。\n").encode('utf-8')
    for payload in (pdfs, sources):
        payload['README.md'] = readme
        payload['STATUS.md'] = status
        payload['bundle-manifest.json'] = json_bytes(manifest)
        add_checksums(payload)
    args.out.mkdir(parents=True, exist_ok=True)
    results = [write_zip(args.out / f'AGC-zh-CN-all-PDFs-{args.date}.zip', pdfs),
               write_zip(args.out / f'AGC-zh-CN-all-sources-{args.date}.zip', sources)]
    (args.out / 'BUNDLE_RECEIPT.json').write_bytes(json_bytes(
        {'content_commit': ref, 'PDF_pages': manifest['PDF_pages'], 'artifacts': results,
         'source_members_preserved_byte_for_byte': len(source_files),
         'source_bundle_PDF_members': 0, 'original_foreign_PDFs': 0,
         'credential_findings': 0, 'CRC_and_member_byte_comparison': 'passed'}))
    print(json.dumps({'content_commit': ref, 'PDF_pages': manifest['PDF_pages'],
                      'artifacts': results, 'source_files': len(source_files)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
