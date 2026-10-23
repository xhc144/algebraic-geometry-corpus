"""Balanced TeX reference-call scanner; never interprets mathematics."""
import re

def group(s,p):
    if p>=len(s) or s[p]!='{':raise ValueError(('expected brace',p,s[p:p+60]))
    start=p+1;depth=1;p+=1
    while p<len(s):
        if s[p]=='\\' and p+1<len(s) and s[p+1] in '{}%':p+=2;continue
        if s[p]=='%':
            q=s.find('\n',p);p=len(s) if q<0 else q+1;continue
        if s[p]=='{':depth+=1
        elif s[p]=='}':
            depth-=1
            if not depth:return s[start:p],start,p,p+1
        p+=1
    raise ValueError(('unclosed group',start))

def calls(s,commands=('SGARefLink','SGARefPending','SGARefExternal')):
    pat=re.compile(r'\\('+'|'.join(map(re.escape,commands))+r')\b')
    for m in pat.finditer(s):
        # A percent comment before the macro on its own line makes it non-rendering.
        line_start=s.rfind('\n',0,m.start())+1
        if re.search(r'(?<!\\)%',s[line_start:m.start()]):continue
        p=m.end()
        while p<len(s) and s[p].isspace():p+=1
        key,ks,ke,p=group(s,p)
        while p<len(s) and s[p].isspace():p+=1
        visible,vs,ve,end=group(s,p)
        yield {'command':m.group(1),'start':m.start(),'command_end':m.end(),'end':end,'key':key,'key_start':ks,'key_end':ke,'visible_tex':visible,'visible_start':vs,'visible_end':ve,'line':s.count('\n',0,m.start())+1,'macro_tex':s[m.start():end]}

def visible_only(s):
    found=list(calls(s))
    # Recursively substitute the visible second argument; outermost calls own their children.
    out=[];cursor=0
    for c in found:
        if c['start']<cursor:continue
        out.append(s[cursor:c['start']]);out.append(visible_only(c['visible_tex']));cursor=c['end']
    out.append(s[cursor:]);return ''.join(out)

def hyperref_visible_only(s):
    """Discard optional-key hyperlink wrappers, preserving their balanced text."""
    out=[];cursor=0
    for m in re.finditer(r'\\hyperref\[[^\]]*\]\s*',s):
        if m.start()<cursor:continue
        visible,vs,ve,end=group(s,m.end())
        out.extend((s[cursor:m.start()],hyperref_visible_only(visible)));cursor=end
    out.append(s[cursor:]);return ''.join(out)
