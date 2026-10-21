#!/usr/bin/env python3
"""Build this native XeLaTeX project without shell escape or network access."""
from pathlib import Path
import argparse, subprocess, os, shutil, json, re, hashlib, datetime
p=argparse.ArgumentParser();p.add_argument('--out',default='build');p.add_argument('--texmfhome');a=p.parse_args()
root=Path(__file__).resolve().parents[1];out=(root/a.out).resolve();out.mkdir(parents=True,exist_ok=True)
env=os.environ.copy()
if a.texmfhome:env['TEXMFHOME']=str(Path(a.texmfhome).resolve())
env.setdefault('TEXMFVAR','/tmp/sga4half-tex-var');env.setdefault('TEXMFCONFIG','/tmp/sga4half-tex-config');env.setdefault('XDG_CACHE_HOME','/tmp/sga4half-cache')
commands=[]
def run(cmd,name):
 with (out/name).open('w') as f:r=subprocess.run(cmd,cwd=root,env=env,stdout=f,stderr=subprocess.STDOUT)
 commands.append({'command':cmd,'exit_code':r.returncode,'console':str((out/name).relative_to(root)) if (out/name).is_relative_to(root) else str(out/name)})
 if r.returncode:
  print((out/name).read_text(errors='replace')[-6500:]);raise SystemExit(r.returncode)
tex=['xelatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder',f'-output-directory={out}','main.tex']
def auxiliary_state():
 return {suffix:hashlib.sha256((out/f'main.{suffix}').read_bytes()).hexdigest()
         for suffix in ['aux','toc','out','brf'] if (out/f'main.{suffix}').exists()}
run(tex,'xelatex-pass1.txt');run(['bibtex',str((out/'main').relative_to(root))],'bibtex.txt')
run(tex,'xelatex-pass2.txt')
convergence=[]
for pass_number in range(3,8):
 before=auxiliary_state();run(tex,f'xelatex-pass{pass_number}.txt')
 log=(out/'main.log').read_text(errors='replace');after=auxiliary_state()
 needs_rerun='Label(s) may have changed' in log or 'Rerun to get cross-references right' in log
 convergence.append({'pass':pass_number,'auxiliary_hashes':after,'stable':before==after,'rerun_warning':needs_rerun})
 if before==after and not needs_rerun:break
else:
 print('Auxiliary files did not converge after seven XeLaTeX passes.');raise SystemExit(3)
warning_blocks=[b.strip() for b in re.split(r'\n\s*\n',log) if 'Warning:' in b]
issues={'undefined_references':[b for b in warning_blocks if 'undefined' in b.lower()],
 'multiply_defined_labels':[b for b in warning_blocks if 'multiply defined' in b.lower()],
 'missing_glyphs':re.findall(r'Missing character:[^\n]*',log),
 'overfull_hbox':re.findall(r'Overfull \\hbox[^\n]*',log),
 'overfull_vbox':re.findall(r'Overfull \\vbox[^\n]*',log),
 'underfull_boxes':re.findall(r'Underfull \\[hv]box[^\n]*',log),
 'font_warnings':re.findall(r'(?:LaTeX Font|Package fontspec) Warning:[^\n]*',log),
 'other_warnings':[b for b in warning_blocks if not any(x in b.lower() for x in ['undefined','multiply defined','font warning'])]}

pdf=root/'SGA4half-zh-CN.pdf';shutil.copy2(out/'main.pdf',pdf)
result={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'engine':subprocess.check_output(['xelatex','--version'],text=True).splitlines()[0],'commands':commands,'auxiliary_convergence':convergence,'pdf':pdf.name,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'issues':issues,'note':'Compilation and mechanical diagnostics do not certify source completeness, translation accuracy or full visual proofreading.'}
(root/'audit/build-status.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');shutil.copy2(out/'main.log',root/'audit/final-build.log');print(json.dumps(result,ensure_ascii=False,indent=2))
if issues['undefined_references'] or issues['missing_glyphs'] or issues['multiply_defined_labels']:raise SystemExit(2)
