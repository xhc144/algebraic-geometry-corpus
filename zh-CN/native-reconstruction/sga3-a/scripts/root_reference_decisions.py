#!/usr/bin/env python3
"""Freeze bounded VIII–XI decisions against the pre-patch snapshot."""
from pathlib import Path
import hashlib,json
from tex_reference_scan import calls
r=Path(__file__).resolve().parents[1]
items=[]
def add(unit,component,line,key,visible,decision,new,evidence):
    files=[f for f in (r/'chapters'/unit).glob(component+'*-zh.tex') if not any(x in f.name for x in ('section5_en','section6_en'))];assert len(files)==1,files
    f=files[0];s=f.read_text();matches=[c for c in calls(s) if c['line']==line and c['key']==key and c['visible_tex']==visible]
    assert len(matches)==1,(f,line,key,visible,matches)
    c=matches[0];same=[x for x in calls(s) if x['macro_tex']==c['macro_tex']]
    items.append({'file':str(f.relative_to(r)),'line':line,'old_key':key,'visible_tex':visible,'call_tex':c['macro_tex'],'identical_call_occurrence_in_file':1+next(i for i,x in enumerate(same) if x['start']==c['start']),'file_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'decision':decision,'new_key':new,'evidence':evidence,'context_tex':s[max(0,c['start']-150):c['end']+150]})
add('VIII','02_',196,'sga3:viii:proposition:2:1','2.1','external',None,'显式SGA 1 VIII 2.1：仿射概形有效下降，不是本书可对角化群的VIII 2.1。')
add('VIII','02_',196,'sga3:viii:corollary:5:6','5.6','replace_key','sga3:x:theorem:5-6','同一脚注的X 5.4–5.6；X定理5.6即拟等平凡群的有效下降。')
add('VIII','05_',15,'sga3:viii:corollary:3:2','定理 3.2','replace_key','thm:sga3-VIA-3.2','明引VI-A定理3.2：平坦正规子群的商存在。')
add('VIII','05_',96,'sga3:viii:corollary:3:2','3.2','replace_key','thm:sga3-VIA-3.2','明引VI-A 3.2，构造H_n/G_n；非本篇3.2。')
add('VIII','05_',75,'sga3:viii:corollary:4:3','4.3','replace_key','cor:sga3-VIB-4.3','明引VI-B 4.3：平坦群概形纤维维数恒定。')
add('VIII','05_',73,'sga3:viii:corollary:5:7','5.7','external',None,'同一已报附录段明引SGA 1 I 5.7，纤维上开浸入判据；非本篇VIII 5.7。')
add('VIII','06_',136,'sga3:viii:proposition:7:9:item:b','(b)','external','sga3:xvi:subsection:1:1','明引后篇XVI 1.1(b)，英文XVI源有该例但无(b)标签；超出本目录范围，保留文字不跳转。')
add('VIII','06_',156,'sga3:viii:proposition:7:9:item:b','(b)','retain',None,'此处确为本篇7.9(b)假设，不可与136行同键的XVI例(b)一并改动。')
add('IX','02_',44,'sga3:viii:proposition:2:1','VIII~2.1','retain',None,'乘法型群性质由可对角化群性质下降，此处确引本书VIII 2.1。')
add('IX','02_',63,'sga3:viii:proposition:2:1','VIII~2.1','external',None,'明引SGA 1 VIII 2.1，仿射概形有效下降。')
add('IX','02_',166,'sga3:ix:theorem:3:2:item:b','3.2(b)','replace_key','sga3:viii:corollary:3:2:item:b:01','承前VIII 1.5，字符群满射对应闭浸入是VIII 3.2(b)；旧键误锚在IX 3.6 bis(b)。')
add('IX','02_',186,'sga3:ix:corollary:5:3','5.3','replace_key','sga3:i:subsection:5-3','同上所指为第I篇5.3的Hochschild上同调复形；本篇IX 5.3是中心同态相等的开闭性。')
add('IX','03_',656,'sga3:ix:corollary:5:3','5.3','retain',None,'此处应用中心同态相等的开闭性，确为本篇IX 5.3。')
for ln in (661,666):
    add('IX','03_',ln,'sga3:ix:corollary:2:4','2.4','replace_key','prop:sga3-VIA-2.4','显式VI-A 2.4，域上局部有限型连通群几何连通；IX 2.4为关系的图浸入，不相关。')
add('XI','09_',94,'sga3:xi:proposition:3:7','3.7','pending',None,'源段承接IX 3.6 bis的提升及共轭，却引3.7；IX明注无3.7，现键XI 3.7是可表性判据且与此论断无关。具体原始目标未能确认，保留3.7并标待核。')
f=r/'chapters/XI/05_expose_XI_section_2-zh.tex';s=f.read_text();old='因此由第八讲，3.6，存在元素';new=r'因此由\SGARefLink{sga3:ix:theorem:3:6}{第 IX 篇，3.6}，存在元素'
assert s.count(old)==1
items.append({'file':str(f.relative_to(r)),'line':s.count('\n',0,s.index(old))+1,'decision':'replace_plain_citation','old_text':old,'new_text':new,'new_key':'sga3:ix:theorem:3:6','evidence':'IX定理3.6正是乘法型群到平滑群的同态提升及模幂零理想共轭；XI 2.4同一论证已正确明引IX 3.6。VIII不存在3.6。旧引用纯文字而非超链接。','file_sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(r/'audit/reference-wrapup/VIII-XI-decisions.json').write_text(json.dumps({'scope':'仅既报VIII–XI错链及定位时同一段紧邻的明确同类错链；无X、XII新审查。','items':items},ensure_ascii=False,indent=2)+'\n')
print(len(items))
