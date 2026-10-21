#!/usr/bin/env python3
"""Compare source/body and report explicit, frozen editorial exceptions separately.
The exception register is reviewed evidence, never generated or updated by this audit.
Compilation and semantic review remain independent evidence.
"""
from pathlib import Path
from collections import Counter
import re,json,hashlib
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
lock=json.loads((ROOT/'SOURCE_LOCK.json').read_text())
source=(REPO/lock['chosen_source']).read_text()
parts={m[1]:m[3] for m in re.finditer(r'% Original input: (.*?)\n\\begin\{filecontents\*\}\[overwrite,noheader\]\{(.*?)\}\n(.*?)\\end\{filecontents\*\}',source,re.S)}
pat=re.compile(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|tikzcd|tikzpicture)\}.*?\\end\{\1\}|\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',re.S)
def textless(s):
    nested_math=[]
    def minipage(m):
        nested_math.extend(re.findall(r'(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',m[2]))
        return m[1]+m[3]
    s=re.sub(r'(\\begin\{minipage\}\{[^}]*\})(.*?)(\\end\{minipage\})',minipage,s,flags=re.S)
    while (m:=re.search(r'\\(?:text|textrm|textnormal|textup|mbox)\s*\{',s)):
        depth=1;j=m.end()
        while j<len(s) and depth:
            if s[j]=='{' and s[j-1]!='\\':depth+=1
            if s[j]=='}' and s[j-1]!='\\':depth-=1
            j+=1
        if depth:raise ValueError('Unbalanced text macro')
        inner=s[m.end():j-1]
        nested_math.extend(re.findall(r'(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',inner))
        s=s[:m.start()]+s[j:]
    s=re.sub(r'\\mathrm\{(?:proximate|to|on)\}','',s)
    # This original first-draft transcription correction has explicit French evidence.
    s=s.replace('q^{,i-\\dim X}','q^{i-\\dim X}')
    return re.sub(r'\s+','',s)+';TEXTMATH:'+repr(sorted(re.sub(r'\s+','',x) for x in nested_math))
def strip_editorials(s):
    notes=[]
    def block(m):notes.append(m[0]);return ''
    s=re.sub(r'\\begin\{editorialnote\}.*?\\end\{editorialnote\}',block,s,flags=re.S)
    while (m:=re.search(r'\\EditorialFootnote\s*\{',s)):
        depth=1;j=m.end()
        while j<len(s) and depth:
            if s[j]=='{' and s[j-1]!='\\':depth+=1
            if s[j]=='}' and s[j-1]!='\\':depth-=1
            j+=1
        if depth:raise ValueError('Unbalanced EditorialFootnote')
        notes.append(s[m.start():j]);s=s[:m.start()]+s[j:]
    if '\\begin{editorialnote}' in s or '\\end{editorialnote}' in s:raise ValueError('Unbalanced editorialnote')
    return s,notes

def difference(src,dst):
    sm=[m[0] for m in pat.finditer(src)];dm=[m[0] for m in pat.finditer(dst)]
    si=[textless(x) for x in sm if x.startswith('$')];di=[textless(x) for x in dm if x.startswith('$')]
    sd=[textless(x) for x in sm if not x.startswith('$')];dd=[textless(x) for x in dm if not x.startswith('$')]
    a=Counter(si);b=Counter(di);changes={}
    if a!=b:changes['inline_math']={'source_only':sorted((a-b).elements()),'translation_only':sorted((b-a).elements())}
    if sd!=dd:
        changes['display_math']={'source_count':len(sd),'translation_count':len(dd),'differences':[{'index':i,'source':sd[i] if i<len(sd) else None,'translation':dd[i] if i<len(dd) else None} for i in range(max(len(sd),len(dd))) if (sd[i] if i<len(sd) else None)!=(dd[i] if i<len(dd) else None)]}
    for key,regexp in [('tags',r'\\tag\*?\{([^}]*)\}'),('labels_refs',r'\\(?:label|ref|eqref|pageref)\{[^}]*\}'),('environment_sequence',r'\\(?:begin|end)\{[^}]*\}')]:
        x=re.findall(regexp,src);y=re.findall(regexp,dst)
        if x!=y:changes[key]={'source':x,'translation':y}
    return changes,{'source_math_fragments':len(sm),'body_math_fragments':len(dm),'source_inline':len(si),'body_inline':len(di),'source_displays':len(sd),'body_displays':len(dd)}

def main():
    registry_path=ROOT/'review/registered-formula-emendations.json'
    registry=json.loads(registry_path.read_text())['components'] if registry_path.exists() else {}
    rows=[];failed=[]
    for c in lock['components']:
        src=parts[c['source_component']];p=ROOT/c['translation'];num=p.name[:3]
        row={'component':c['source_component'],'number':num,'translation':c['translation'],'exists':p.exists(),'source_lines':len(src.splitlines())}
        if not p.exists():rows.append(row);failed.append(num);continue
        dst=p.read_text();body,notes=strip_editorials(dst);changes,counts=difference(src,body)
        registered=registry.get(num,{}).get('exact_body_differences',{})
        row.update(counts,output_lines=len(dst.splitlines()),editorial_notes=len(notes),editorial_math_fragments=sum(len(list(pat.finditer(n))) for n in notes),source_body_equal_without_registered_emendations=not changes,raw_body_differences=changes,registered_differences_match=(registered==changes),translation_sha256=hashlib.sha256(dst.encode()).hexdigest(),editorial_notes_sha256=hashlib.sha256('\n'.join(notes).encode()).hexdigest())
        rows.append(row)
        if registered!=changes:failed.append(num)
    obsolete=sorted(set(registry)-{x['number'] for x in rows})
    report={'method':'Mechanical source/body comparison. Only explicit editorialnote and EditorialFootnote additions are removed, leaving original author notes intact. Prose in text nodes/minipages is ignored while embedded dollar math is retained; inline math is a multiset, display math an ordered sequence. This does not prove semantic completeness or mathematical correctness.','original_first_draft_q_exponent_normalization':'XXI Theorem2.1 extra comma; FrenchPDF387/printed377, see review/xxi-xxii.json.','exception_register':'review/registered-formula-emendations.json','changed_body_components':sum(bool(x.get('raw_body_differences')) for x in rows),'all_registered_changes_match':not failed and not obsolete,'unregistered_or_changed_components':failed,'obsolete_register_components':obsolete,'components':rows}
    (ROOT/'review/mechanical-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('Translated',sum(x['exists'] for x in rows),'/',len(rows),'changed body components',report['changed_body_components'],'registered checks',report['all_registered_changes_match'])
    if failed or obsolete:raise SystemExit('Explicit review/register required: '+repr(failed+obsolete))
if __name__=='__main__':main()
