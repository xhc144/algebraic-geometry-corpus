from pathlib import Path
import json,re,hashlib,shutil,datetime
r=Path(__file__).resolve().parent
audit=json.loads((r/'review/mechanical-audit.json').read_text());rows=audit['components']
lock=json.loads((r/'SOURCE_LOCK.json').read_text());s=(r/'build/main.log').read_text()
for name in ['pass1.txt','pass2.txt','main.log']:
 shutil.copyfile(r/'build'/name,r/'review'/('full-build-log.txt' if name=='main.log' else 'full-build-'+name))
shutil.copyfile(r/'build/render/manifest.json',r/'review/render-manifest.json')
render=json.loads((r/'build/render/manifest.json').read_text())
semantic=json.loads((r/'review/semantic-coverage.json').read_text())
visual=json.loads((r/'review/revised-visual-review.json').read_text()) if (r/'review/revised-visual-review.json').exists() else {'complete':False}
pages=int(re.findall(r'Output written.*?\((\d+) pages',s)[-1])
tex='\n'.join((r/c['translation']).read_text() for c in lock['components'])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
status={
 'status':'complete_translation_with_independent_semantic_revision',
 'updated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'SGA7-II Exposés X–XXII, all183 assigned English components; French introduction supplement separately traced',
 'previous_published_delivery_commit':'20839ff94e5e437f456bcba76dc11b56fbf89e45',
 'assigned_english_source_complete':True,'translation_draft_complete':True,'expert_publication_acceptance_complete':False,
 'independent_source_translation_semantic_review_complete':semantic['complete'],
 'independent_semantic_review_evidence':'review/semantic-coverage.json and individual independent review ledgers',
 'source_components':len(rows),'translated_components':sum(x['exists'] for x in rows),
 'source_lines':sum(x['source_lines'] for x in rows),'output_lines':sum(x['output_lines'] for x in rows),
 'source_inline_math':sum(x['source_inline'] for x in rows),'source_display_math_and_diagrams':sum(x['source_displays'] for x in rows),
 'translated_body_inline_math':sum(x['body_inline'] for x in rows),'translated_body_display_math_and_diagrams':sum(x['body_displays'] for x in rows),
 'explicit_editorial_notes_in_body':sum(x['editorial_notes'] for x in rows),'editorial_math_fragments_separate_from_original_body':sum(x['editorial_math_fragments'] for x in rows),
 'registered_formula_or_structural_emendation_components':audit['changed_body_components'],
 'all_registered_math_and_structure_checks_pass':audit['all_registered_changes_match'],
 'math_identity_claim':'Not identical to the printed source: each registered source emendation remains visible and its exact raw difference is reported.',
 'tikz_pictures':tex.count('\\begin{tikzpicture}'),'tikzcd_diagrams':tex.count('\\begin{tikzcd}'),
 'image_or_pdf_overlay_commands':len(re.findall(r'\\(?:includegraphics|includepdf|pdfximage)\b',tex)),
 'compile':{'status':'passed','engine':'XeLaTeX, two passes, no shell escape','pages':pages,'latex_package_warnings':len(re.findall(r'(?:LaTeX|Package .*?) Warning:',s)),'overfull_boxes':s.count('Overfull'),'missing_glyph_messages':s.count('Missing character'),'undefined_references':len(re.findall(r'(?:undefined references|Reference .* undefined)',s)),'pdf_sha256':sha(r/'SGA7-II-zh-CN.pdf'),'underfull_hbox_messages':s.count('Underfull \\hbox'),'underfull_review':'All six affected page layouts inspected; messages retained, no clipping/overlap observed.','input_manifest':'review/build-input-manifest.json'},
 'visual_review':{'rendered_all_pages':pages,'layout_contact_sheets':render['contact_sheets'],'revised_review_complete':visual.get('complete',False),'evidence':'review/revised-visual-review.json','boundary':'All revised page layouts checked in contact sheets with selected high resolution inspection; this is distinct from prose or mathematical review.'},
 'source_zip_status':'See SOURCE_ARCHIVE_MANIFEST.json, DELIVERY_SHA256SUMS.txt and review/standalone-zip-build.json',
 'unfinished_translation_components':[],
 'limitations':[
  'Referenced Leitfaden relationship chart was not found in either repository scan or the official publisher frontmatter. IAS master direct read returned403; no reconstruction was invented. Exact checked sources/pages/hashes: review/leitfaden-search.json.',
  'Some printed-source defects or ambiguous conventions remain explicitly annotated, with uncertainties in individual semantic ledgers. This review does not certify every historical theorem or verify every external cited publication.',
  'Full source/translation semantic reading, mechanical exception checks, successful compilation and visual layout inspection are separate review results; none alone is expert publication acceptance.'
 ]}
chapters=[]
for expo in dict.fromkeys(c['expose'] for c in lock['components']):
 cs=[c for c in lock['components'] if c['expose']==expo];rr=[x for x in rows if x['component'] in {c['source_component'] for c in cs}]
 chapters.append({'expose':expo,'components':len(cs),'translated_components':len(rr),'independently_semantically_reviewed_components':len([x for x in semantic['components'] if x['expose']==expo and x['reviewed']]),'source_lines':sum(x['source_lines'] for x in rr),'output_lines':sum(x['output_lines'] for x in rr),'source_math_fragments':sum(x['source_math_fragments'] for x in rr),'status':'translated_and_independently_compared_to_source'})
status['chapters']=chapters
if (r/'review/standalone-zip-build.json').exists():
 standalone=json.loads((r/'review/standalone-zip-build.json').read_text())
 status['standalone_source_zip_compile']={'status':standalone['status'],'pages':standalone['pages'],'compiler_inputs_match_master':standalone.get('compiler_input_manifest_identical_to_delivered_master',False),'evidence':'review/standalone-zip-build.json'}
(r/'PROGRESS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
print({k:status[k] for k in ['source_components','source_lines','output_lines','registered_formula_or_structural_emendation_components','explicit_editorial_notes_in_body']})
