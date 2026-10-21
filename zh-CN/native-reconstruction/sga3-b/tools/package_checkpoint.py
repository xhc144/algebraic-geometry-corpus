#!/usr/bin/env python3
"""Build a committed immutable source snapshot and package matching TeX/PDF."""
from pathlib import Path
import subprocess,tarfile,io,os,json,hashlib,zipfile,re,shutil
p=Path(__file__).resolve().parents[1];repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=p,text=True).strip())
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip();rel=p.relative_to(repo).as_posix()
work=Path('/tmp/sga3-build-snapshots')/commit[:12];work.mkdir(parents=True,exist_ok=True)
data=subprocess.check_output(['git','archive',commit+':'+rel],cwd=repo)
with tarfile.open(fileobj=io.BytesIO(data)) as tar:tar.extractall(work,filter='data')
(work/'build').mkdir(exist_ok=True)
env={**os.environ,'XDG_CACHE_HOME':'/tmp/sga3-font-cache'}
local=Path('/tmp/sga3-tex-deps/debian/usr/share/texlive/texmf-dist/tex')
if local.exists():env['TEXINPUTS']=str(local)+'//:'+env.get('TEXINPUTS','')
passes=[]
for n in range(1,5):
 with (work/'build'/('pass-'+str(n)+'.txt')).open('w') as f:
  r=subprocess.run(['xelatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-output-directory=build','main.tex'],cwd=work,env=env,stdout=f,stderr=subprocess.STDOUT)
 passes.append({'pass':n,'exit_code':r.returncode})
 print('pass',n,'exit',r.returncode,flush=True)
 if r.returncode:break
 if n>=2:
  log=(work/'build/main.log').read_text(errors='replace')
  if 'Rerun to get' not in log and 'Label(s) may have changed' not in log and 'File `main.out\' has changed' not in log:break
log=(work/'build/main.log').read_text(errors='replace');pdf=work/'build/main.pdf'
evidence={'source_commit':commit,'source_subtree':rel,'immutable_build_directory':str(work),'passes':passes,'compile_success':all(x['exit_code']==0 for x in passes),'missing_glyph_lines':re.findall(r'^Missing character:.*$',log,re.M),'overfull_lines':re.findall(r'^Overfull.*$',log,re.M),'reference_warning_lines':re.findall(r'^.*(?:undefined|multiply defined|Rerun to get|Label\(s\)).*$',log,re.M),'font_warning_lines':re.findall(r'^LaTeX Font Warning:.*$',log,re.M),'proofreading':'Not independently completed; exact source coverage is recorded separately.','visual_review':'pending inspection of this immutable build'}
if evidence['compile_success']:
 import fitz
 doc=fitz.open(pdf);evidence['pdf_pages']=len(doc);evidence['pdf_sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest();shutil.copyfile(pdf,p/'SGA3-b-zh.pdf')
# Keep the compiler log even on failure and do not claim a failed PDF is delivered.
(p/'evidence').mkdir(exist_ok=True);shutil.copyfile(work/'build/main.log',p/'evidence'/('build-'+commit[:12]+'.log'))
source_files=[]
for f in sorted(work.rglob('*')):
 if not f.is_file() or 'build' in f.relative_to(work).parts:continue
 if f.suffix.lower() in ['.pdf','.zip','.log','.png']:continue
 if f.name in ['BUILD_STATUS.json','BUILD_EVIDENCE.json']:continue
 source_files.append(f)
source_manifest={f.relative_to(work).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in source_files}
archive=p/'SGA3-b-source.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in source_files:z.write(f,'sga3-b/'+f.relative_to(work).as_posix())
 z.writestr('sga3-b/CHECKPOINT_SOURCE.json',json.dumps({'source_commit':commit,'sha256':source_manifest},ensure_ascii=False,indent=2)+'\n')
 z.writestr('sga3-b/BUILD_EVIDENCE.json',json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
evidence['source_zip_sha256']=hashlib.sha256(archive.read_bytes()).hexdigest();evidence['source_zip_members']=len(source_files)+2
(p/'evidence/BUILD_STATUS.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(evidence,ensure_ascii=False,indent=2))
