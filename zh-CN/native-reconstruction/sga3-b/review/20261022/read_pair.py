from pathlib import Path
import re,sys
b=Path(__file__).resolve().parents[2]
u,a,z=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]);s=(b/f'source-reference/{u}.tex').read_text().splitlines();t=(b/f'chapters/{u}-zh.tex').read_text();raw='\n'.join(s[a-1:z]);keys=re.findall(r'\\SGARefTarget\{([^}]+)\}',raw)
allkeys=list(re.finditer(r'\\SGARefTarget\{([^}]+)\}', '\n'.join(s)))
prefix='\n'.join(s[:a-1]);before=list(re.finditer(r'\\SGARefTarget\{([^}]+)\}',prefix));start=before[-1].group(1) if before else None
suffix='\n'.join(s[z:]);after=re.search(r'\\SGARefTarget\{([^}]+)\}',suffix);end=after.group(1) if after else None
beg=t.find('\\SGARefTarget{'+start+'}') if start else 0;fin=t.find('\\SGARefTarget{'+end+'}') if end else len(t)
def clean(x):
 x=re.sub(r'(?m)^%.*\n?','',x);x=re.sub(r'\\SGARefLink\{[^}]+\}', '',x);x=re.sub(r'\\SGARefTarget\{[^}]+\}', '',x);x=re.sub(r'\\label\{[^}]+\}', '',x);x=re.sub(r'\n(?=[^\n])',' ',x);return x
print('SOURCE',u,a,z);print(clean(raw));print('\nTRANSLATION (overlapping endpoint context)');print(clean(t[beg:fin]))
