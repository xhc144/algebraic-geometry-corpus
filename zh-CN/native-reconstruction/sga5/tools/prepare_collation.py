#!/usr/bin/env python3
"""Consolidate the independently written witness reports and root decisions.

This prepares an auditable exact patch ledger and the reader-visible notes.
It does not modify any translated chapter or any original source.
"""
from pathlib import Path
from collections import Counter
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / 'qa/content-verification-20261021'
names = ['I', 'III-IIIBI', 'IIIBII', 'VVI', 'VIIVIII-XXII', 'XV-front']
items = []
reports = []
ip = json.loads((QA/'I-proposed-corrections.json').read_text())
for name in names:
    path = QA / (name+'-adjudication.json')
    report = json.loads(path.read_text())
    reports.append({'file': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    for raw in report['items']:
        iid = raw['id']
        patches = raw.get('proposed_patches', [])
        if name == 'I':
            patches = [p for p in ip['body_patches'] if p['item_id']==iid and p.get('required')]
        normalized = []
        for patch in patches:
            if not patch.get('apply_recommended', True):
                continue
            file = patch.get('file', patch.get('target_file'))
            file = file.removeprefix('zh-CN/native-reconstruction/sga5/')
            old = patch.get('old_tex', patch.get('old'))
            new = patch.get('new_tex', patch.get('new'))
            # The separate scope-prefix edit originally included the start of
            # the equation also replaced by the following full display patch.
            if iid == 'XXII-06' and old.startswith('事实上, 此时有'):
                old = old.split('\\begin{equation}')[0]
                new = new.split('\\begin{equation}')[0]
            normalized.append({'file': file, 'old': old, 'new': new,
                'expected_occurrences': patch.get('expected_occurrences_in_reviewed_snapshot', patch.get('expected_occurrences', patch.get('occurrences_expected', 1)))})
        note = raw.get('recommended_reader_note_tex', raw.get('proposed_editorial_note_tex', raw.get('suggested_note_tex', raw.get('proposed_visible_collation_note', ''))))
        if 'editorial_notes_for_separate_appendix' in raw:
            note = '\n\n'.join(raw['editorial_notes_for_separate_appendix'])
        note = re.sub(r'^\\footnote\{(.*)\}$', r'\1', note, flags=re.S)
        note = note.replace('正文建议把', '正文把')
        witnesses = raw.get('french_witnesses', raw.get('french_witness', []))
        if not witnesses and 'french_physical_pdf_page' in raw:
            witnesses = [{'pdf_page':raw['french_physical_pdf_page'], 'printed_page':raw['french_printed_body_page'], 'actual_render_viewed':raw['actual_render_viewed'], 'reading':raw['witness_reading']}]
        classification = raw.get('classification', raw.get('category', raw.get('status')))
        rationale = raw.get('mathematical_adjudication', raw.get('rationale', raw.get('mathematical_context_and_resolution', raw.get('mathematical_resolution', raw.get('mathematical_rationale', raw.get('resolution'))))))
        items.append({'id':iid, 'review_report':str(path.relative_to(ROOT)),
            'english_source_lines':raw.get('english_source_lines', raw.get('english_source_lines_exact', [])),
            'classification_as_reviewed':classification,
            'witnesses':witnesses, 'mathematical_rationale':rationale,
            'patches':normalized, 'note_tex':note,
            'remaining_source_uncertainty':None,
            'root_decision':'Accept the witnessed correction or explanation, with the original reading recorded in the notes.'})

byid = {i['id']: i for i in items}
assert len(byid)==len(items), 'duplicate issue ID'
initial = json.loads((QA/'initial-doubt-inventory.json').read_text())['items']
assert {i['id'] for i in initial} <= set(byid), 'initial issue unaccounted for'

# Four residuals have a precise scope; none is silently counted as proved.
residuals = {
    'I-01':'The intended reference and the derivation in the stated unbounded D_c(X) range cannot be uniquely recovered from the printed witness. Original citation and formula retained.',
    'IIIB-20':'The printed extra trivial-action hypothesis on C is coherent but conflicts with the later free-cover application. Replacing C by Y would weaken the hypothesis without a verified extension proof; retained.',
    'XXII-06':'The corrected single Nielsen–Wecken-class calculation is justified for a cover étale above x. The printed argument does not establish that calculation for an arbitrary ramified trivializing cover merely from F being unramified.',
    'FRONT-01':'The later VII for finiteness/class groups is certainly VIII. The broader introductory duality summary (I,VII) may or may not have intended VIII; that summary is retained.'
}
for iid, text in residuals.items():
    byid[iid]['remaining_source_uncertainty']=text
    byid[iid]['root_decision']='Apply only the determinate corrections; preserve and explicitly annotate the stated source uncertainty.'

# Point to the appendix at the locations whose remaining scope matters.
byid['I-01']['patches'].append({'file':'chapters/01-expose-i.tex', 'old':'首先注意, 由命题 1.9(b)(ii),', 'new':'首先注意, 由命题 1.9(b)(ii)\\sgacollationmark{I-01},', 'expected_occurrences':1})
byid['IIIB-20']['patches'].append({'file':'chapters/03-expose-iii-b.tex', 'old':'$G$ 在 $C$ 和 $D$ 上平凡作用, 且', 'new':'$G$ 在 $C$ 和 $D$ 上平凡作用\\sgacollationmark{IIIB-20}, 且', 'expected_occurrences':1})
for p in byid['XXII-06']['patches']:
    if p['new'].startswith('在覆盖 $p$'):
        p['new']=p['new'].rstrip()+'\\sgacollationmark{XXII-06}\n'

byid['FRONT-01']['patches'].append({'file':'chapters/00-frontmatter.tex', 'old':'对偶形式体系 (I, VII) 和', 'new':'对偶形式体系 (I, VII)\\sgacollationmark{FRONT-01} 和', 'expected_occurrences':1})
byid['XV-04']['patches'].append({'file':'chapters/07-expose-xv.tex', 'old':'且 $\\Fr_{X/S}=(\\id_{|X|},\\varphi)$,', 'new':'\\sgacollationmark{XV-04}且 $\\Fr_{X/S}=(\\id_{|X|},\\varphi)$,', 'expected_occurrences':1})
byid['IIIB-24']['patches'].append({'file':'chapters/03-expose-iii-b.tex', 'old':'必要时以 $Z_g$ 替换 $G$, 可假定 $g=e$.', 'new':'必要时以 $Z_g$ 替换 $G$, 可假定 $g=e$.\\sgacollationmark{IIIB-24}', 'expected_occurrences':1})
byid['XV-S1-new']['note_tex'] += '\n\n原文的辅助断言只要求：“$Q_0$ 投射，且 $R$ 为满足 $T(R)\\simeq R_0$ 的 $A$-模”。该任意提升的表述不成立。例如取 $A=\\Z/4\\Z$、$A_0=\\F_2$、$P_0=0$、$Q_0=R_0=\\F_2$ 和 $R=\\F_2$；投射提升 $Q=\\Z/4\\Z$ 到 $R$ 的满射之核约化后非零，不可能恢复原来的 $P_0=0$。正文只使用实际递降构造中 $Q_0,R_0$ 都投射、且可取 $R$ 投射的情形，并写明分裂保证约化正合的理由。'
byid['VVI-07']['note_tex'] += '\n\n例如令循环群 $C_\\ell$ 在 $M=\\Z_\\ell\\oplus\\F_\\ell$ 上由 $g(a,t)=(a,t+\\bar a)$ 作用，则 $g^\\ell=1$，挠子模为 $T=0\\oplus\\F_\\ell$。若商映射有等变截面，$1$ 的像必为 $(1,c)$，但 $g(1,c)=(1,c+1)$，矛盾。这说明原书所需的等变直和分裂一般不存在；商 $M/T$ 的构造不需要这种分裂。'

# The two incorrect English-added editorial notes remain in full translation,
# moved out of the original proof and explicitly adjudicated above.
for old in ip['original_English_editorial_notes_moved']:
    content=old['original_Chinese_note_tex']
    assert content.startswith('\\footnote{') and content.endswith('}')
    byid[old['id']]['note_tex'] += '\n\n英文重构稿原编注的完整译文（其判断已在上文复核）：\n\\begin{quote}\\small\n'+content[len('\\footnote{'):-1]+'\n\\end{quote}'

ledger = {'date':'2026-10-21', 'review_kind':'Independent AI-agent fidelity reading and targeted actual-French-page collation; not professional human certification',
    'frozen_translation_commit':'387a0a0b05081110ddf7140b7b7d96f8a9de621a',
    'initial_recorded_issues':len(initial), 'total_adjudicated_items':len(items),
    'new_findings':sorted(set(byid)-{i['id'] for i in initial}),
    'unadjudicated_initial_ids':[], 'residual_source_uncertainty_ids':list(residuals),
    'source_reports':reports, 'items':items,
    'limits':'Every translated source component has independent English–Chinese fidelity coverage. French original comparison is targeted to every recorded doubt and new finding, not a complete word-for-word French collation or a new proof of every theorem.'}
(QA/'adjudication-ledger.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n')

tex = [r'\clearpage\phantomsection\addcontentsline{toc}{section}{校勘说明（译者附记）}\section*{校勘说明（译者附记）}',
    '本附记为中译重建时加入的校勘材料，不属于原书正文。十篇已出版报告、卷首及索引均由未负责相应初译的独立代理检查源译覆盖、假设和证明步骤；所列疑点又逐项核对了法文原页。这里区分英文重构错误、法文原书错误、成立但需要解释的读法，以及证据不能唯一复原的原文疑义。可确定的修订已用于正文，原读法与依据记在各条中。原版与英文本均未改动。',
    f'本轮最初记录 {len(initial)} 项，复核新增 {len(items)-len(initial)} 项，共 {len(items)} 项均有裁定；没有未处理的清单项。仍有明确保留范围的原文疑义为 I-01、III B-20、XII 的(6.4.7)及导言的概述编号，详见对应条目。正文上标“[校]”可跳至相关说明。独立代理检查不构成专业人工审定；本次也不宣称逐句核对了整部法文本或重新证明了全部定理。以下“原书页码”均指法文印刷页，必要时另列物理PDF页。']
for item in items:
    note = item['note_tex']
    assert note, item['id']
    tex.append('\\hypertarget{collation-'+item['id']+'}{}')
    if not note.startswith('\\paragraph*'):
        tex.append('\\paragraph*{'+item['id']+'。}')
    tex.append(note)
(ROOT/'chapters/09-collation-notes.tex').write_text('\n\n'.join(tex)+'\n')
print(json.dumps({'initial':len(initial), 'total':len(items), 'new':len(items)-len(initial), 'residuals':list(residuals), 'patches':sum(len(i['patches']) for i in items)}, ensure_ascii=False))
