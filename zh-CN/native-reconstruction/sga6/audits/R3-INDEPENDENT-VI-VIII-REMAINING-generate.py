from pathlib import Path
import difflib,json
root=Path('zh-CN/native-reconstruction/sga6')
changes=[]
texts={n:(root/'chapters'/f'expose-{n}.tex').read_text() for n in ('06','07','08')}
original=texts.copy()
def rep(n,old,new,source):
    assert texts[n].count(old)==1,(n,source,texts[n].count(old),old[:100])
    line=texts[n][:texts[n].index(old)].count('\n')+1
    texts[n]=texts[n].replace(old,new,1)
    changes.append(dict(file=f'expose-{n}.tex',snapshot_line=line,source=source,old=old,new=new))
rep('06','使用 Hakim 意义下的相对概形','使用 Hakim 意义下的相对概形（[3]）','printed380/physical394, VI1.14 original [3]')
rep('06',r'f_*:K^\bullet_{\mathrm{parf}}(X)\longrightarrow K^\bullet_{\mathrm{parf}}(S).',r'f_*:K^\bullet_{\mathrm{parf}}(X)\longrightarrow K^\bullet_{\mathrm{parf}}(S)\qquad\text{（IV 2.11.1）}.','printed389/physical403, VI2.8')
rep('06','这是 \\(K^\\bullet(S)\\)-模的直和分解，其中滤过是增广 \\(\\lambda\\)-环的典范滤过。','这是 \\(K^\\bullet(S)\\)-模的直和分解，其中滤过是 V 3.9.1 和 3.10 中定义的增广 \\(\\lambda\\)-环的滤过。','printed403/physical417, VI5.3')
rep('06','两种定义，即用有限型局部自由层的定义和用完美复形的定义，彼此相同。','两种定义，即用有限型局部自由层的定义和用完美复形的定义，彼此相同（IV 2.9）。','printed407/physical421, VI6 opening')
rep('07','则 \\(J\\) 拟正则：','则 \\(J\\) 拟正则（EGA IV 16.9.7），即（EGA IV 16.9.8）：','printed418/physical432, VII1.3')
rep('07',r'\textbf{命题 1.5.} 若',r'\textbf{命题 1.5.} （比较 EGA IV 19.1.5 (ii)。）若','printed420/physical434, VII1.5')
rep('07',r'\textbf{命题 1.7.} 设',r'\textbf{命题 1.7.} （比较 EGA IV 19.1.5 (iv)。）设','printed422/physical436, VII1.7')
rep('07','接着使用传递性谱序列\n','接着使用传递性谱序列（[1], XVI 5）\n','printed423/physical437, VII1.7')
rep('07','有限分次消解。\n\\end{enumerate}','有限分次消解（VI 1.2）。\n\\end{enumerate}','printed425/physical439, VII1.8(iii)')
rep('07','则 \\(i,f\\) 都是完美态射。','则 \\(i,f\\) 都是完美态射（III 4.1）。','printed428/physical442, VII1.9')
# Keep the existing normalized notation but make the original local reversal visible.
rep('07','其中 \\(i:T\\to Y\\)、\\(j:T\\to Z\\) 是相应的浸入。','其中 \\(i:T\\to Y\\)、\\(j:T\\to Z\\) 是相应的浸入。\\footnote{译校注：原书第 432、434、435 页在本命题中将这些余法层记作 \\(N_{Y/X},N_{Z/X},N_{T/X}\\)，下标次序与 1.6 的定义相反；此处沿用 1.6 的次序，分别写作 \\(N_{X/Y},N_{X/Z},N_{X/T}\\)。}','printed432,434,435/physical446,448,449, VII2.5 notation')
rep('07','取 \\(i_*M\\) 的投射消解，再应用 \\(f^*\\)。','取 \\(i_*M\\) 的投射消解，再应用 \\(f^*\\)。\\footnote{译校注：原书第 441 页在此处印作函子 \\(f_*\\)；由前后的逆像构造及 Tor 公式，应为 \\(f^*\\)。}','printed441/physical455, VII3.4 functor typo')
start=texts['07'].index('首先，\\(u\'\\circ u=1\\)')
end=texts['07'].index('\n为证明最后的满射性断言',start)
old=texts['07'][start:end]
new=r'''首先，\(u\) 有左逆 \(u'\)，因而为单射。事实上，由投影公式，
\[
 g_*\bigl(g^*(y)\lambda_{-1}(F)\bigr)
 =y\,g_*(\lambda_{-1}(F)).
\]
另一方面，\(g_*(\lambda_{-1}(F))=1\)（VI 5.9），所以得到结论。

其次，\(v\circ u=0\)。若 \(y\in K^\bullet(Y)\)，由命题 3.4，确有
\[
\begin{aligned}
 v\circ u(y)
 &=v\bigl(g^*(y)\lambda_{-1}(F),-i_*(y)\bigr)\\
 &=j_*\bigl(g^*(y)\lambda_{-1}(F)\bigr)-f^*(i_*(y))=0.
\end{aligned}
\]
\footnote{译校注：原书第 445 页此计算末项印作 \(f^*(i_*(x))\)，其中 \(x\) 未定义；依本行的元素 \(y\)，此处采用 \(f^*(i_*(y))\)。}

因此还需证明 \(\Ker(v)\subset\Imf(u)\)。设 \(x\in K^\bullet(X)\)、\(y'\in K^\bullet(Y')\) 满足
\[
 j_*(y')+f^*(x)=0.
\]
须找到 \(y\in K^\bullet(Y)\)，使
\begin{equation}\tag{\sgaStableTargetInline{sga6.e07.eq.3-7-1}3.7.1}
x=-i_*(y),\qquad y'=g^*(y)\lambda_{-1}(F).
\end{equation}
由于 \(u\) 有左逆 \(u'\)，必有
\[
 y=u'(y',x)=g_*(y').
\]
所以须证明此 \(y\) 满足关系式 (3.7.1)。为证明 \(x=-i_*(y)\)，从关系 \(f^*(x)=-j_*(y')\) 出发并应用 \(f_*\)，得到
\[
 f_*\bigl(f^*(x)\bigr)
 =-f_*\bigl(j_*(y')\bigr)
 =-i_*\bigl(g_*(y')\bigr)
 =-i_*(y),
\]
最后一个等号来自 \(y\) 的定义。而由命题 3.6，\(f_*(f^*(x))=x\)，故得所需关系。

为完成证明，还需证明
\[
 y'=g^*(g_*(y'))\lambda_{-1}(F).
\]
令 \(z=y'-g^*(g_*(y'))\lambda_{-1}(F)\)，得到
\[
 g_*(z)=g_*(y')-g_*(y')\,g_*(\lambda_{-1}(F))=0.
\]
另一方面，由假设及上述关系，并由命题 3.4，
\[
 j_*(y')=-f^*(x)=f^*(i_*(y))
 =j_*\bigl(g^*(y)\lambda_{-1}(F)\bigr),
\]
所以也有 \(j_*(z)=0\)。\footnote{译校注：原书第 446 页此处先印作 \(j_*(y')=f^*(x)\)，漏掉负号；上文的假设是 \(j_*(y')+f^*(x)=0\)。此处补出负号，并保留其后的计算链。}
而 \(\Ker(j_*)\cap\Ker(g_*)=0\)。事实上，若 \(j_*(z)=0\)，则 \(j^*(j_*(z))=0\)；由命题 2.7，
\[
 j^*(j_*(z))=z(1-L).
\]
要使 \(z(1-L)=0\)，由 VI 5.10，必须存在 \(z'\in K^\bullet(Y)\)，使
\[
 z=z'\lambda_{-1}(F).
\]
应用 \(g_*\)，得到 \(z'=g_*(z)=0\)，因而 \(z=0\)。这就证明了在中间项处的正合性。
'''
rep('07',old,new,'printed445–446/physical459–460, restore every explicit proof calculation')
rep('07','其局部环也正则。因此','其局部环也正则（见 EGA \\(0_{\\mathrm{IV}}\\) 17.1.8）。因此','printed446/physical460, VII3.7 regular-local-ring reference') if '其局部环也正则。因此' in texts['07'] else rep('07','的局部环也正则。因此','的局部环也正则（见 EGA \\(0_{\\mathrm{IV}}\\) 17.1.8）。因此','printed446/physical460, VII3.7 regular-local-ring reference')
rep('07','因此，\\(X\'\\) 上支集包含于 \\(Y\'\\) 的凝聚模都是完美的。','因此，\\(X\'\\) 上支集包含于 \\(Y\'\\) 的凝聚模都是完美的：在 \\(Y\'\\) 的各点处，这是因为 \\(X\'\\) 在这些点正则；在 \\(X\'\\setminus Y\'\\) 的各点处，这是因为该模为零。','printed447/physical461, VII3.7 both local cases for perfection')
rep('07','其类属于 \\(\\Imf(j_*)\\)。这里使用：','由上面的论证，这些上同调层是完美 \\(\\mathcal O_{X\'}\\)-模，它们的类属于 \\(\\Imf(j_*)\\)，所以 \\(N\'\\) 的类也属于 \\(\\Imf(j_*)\\)。这里使用：','printed447/physical461, VII3.7 classes of every cohomology sheaf')
rep('07','特别可对 \\(Y\'\\) 应用此事实。所以','特别可对 \\(Y\'\\) 应用此事实。\\footnote{译校注：原书第 447 页在此处印作“对 \\(X\'\\) 尤其如此”；已知正则的是 \\(Y\'\\) 及 \\(X\'\\) 沿 \\(Y\'\\) 的局部环，\\(X\'\\) 在其余点未必正则。对支集包含于 \\(Y\'\\) 的层所需的 Grothendieck 群比较可在 \\(Y\'\\) 上使用；这里将原印的 \\(X\'\\) 订为 \\(Y\'\\)。}所以','printed447/physical461, VII3.7 original unjustified global regularity inference')
note=r"\footnote{译校注：原书第 474 页此图的 $p$ 箭头印作由 $V$ 到 $V'$，与其定义的光滑态射相反；此处依定义反向绘出。}"
rep('08',note+'\n','','VIII1.8 remove misplaced source-error note after first decomposition')
rep('08','V\' \\arrow[r,"p"] \\arrow[dr] & V \\arrow[d]\\\\\n& Y,\n\\end{tikzcd}\n\\]\n推出','V\' \\arrow[r,"p"] \\arrow[dr] & V \\arrow[d]\\\\\n& Y,\n\\end{tikzcd}\n\\]\n'+note+'\n推出','printed474/physical488, VIII1.8 attach note after all-smooth triangle')
rep('08',r'\Omega^1_{V/Y}\otimes_{\mathcal O_V}\mathcal O_X'+'\n\\]\n它在',r'\Omega^1_{V/Y}\otimes_{\mathcal O_V}\mathcal O_X'+'\n\\]\n'+r'\footnote{译校注：原书第 475 页此链的末项印作 \(\Omega^1_{V/X}\otimes\mathcal O_X\)，与前面的相对微分层及 (2.1.1) 不合；此处将原印的 \(V/X\) 订为 \(V/Y\)。}'+'\n它在','printed475/physical489, VIII2.1 source V/X typo')
# Remove the assertion-only placeholder from the deliverable metadata.
changes=[c for c in changes if c['source']!='no-op placeholder']
out=root/'audits/R3-INDEPENDENT-VI-VIII-REMAINING.patch'
patch=''
for n in ('06','07','08'):
 path=f'zh-CN/native-reconstruction/sga6/chapters/expose-{n}.tex'
 patch+=''.join(difflib.unified_diff(original[n].splitlines(True),texts[n].splitlines(True),fromfile='a/'+path,tofile='b/'+path))
out.write_text(patch)
(root/'audits/R3-INDEPENDENT-VI-VIII-REMAINING.json').write_text(json.dumps({'status':'proposal only; body files not written','changes':changes},ensure_ascii=False,indent=2)+'\n')
print(f'{len(changes)} exact replacements; {len(patch.splitlines())} patch lines; bodies read only')
