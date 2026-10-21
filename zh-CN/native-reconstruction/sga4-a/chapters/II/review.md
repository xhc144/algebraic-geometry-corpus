# Exposé II 翻译与检查记录

状态：所给底稿的全部可见正文已译出；完成一轮译者对照检查，尚未经独立审校。原底稿注 3.3 含未能补齐的引文缺损，不能将“可见内容已全部翻译”表述为底稿完整性无问题。本文件为工作记录，不属于书籍正文。

## 覆盖与身份

- 来源：`/tmp/sga4-02-body-source.tex`，由主代理从已校验的仓库源 ZIP 提取。
- 精确覆盖：输入第 1–2133 行，含导言、§§1–6、全部定义、陈述、证明、例、注、4 个脚注、4 条书目以及末尾独立编译条件。章节标题与总工程前置由主代理负责。
- 对应 ZIP 原生分片：`SGA4_II_LINES_31_212_English.texfrag` 至 `SGA4_II_LINES_1820_2120_English.texfrag`，共 11 个连续分片。
- 输出：`chapters/II/body.tex`，2051 行，81498 字节（UTF-8）。中文换行重排不代表删节。
- 输入 SHA-256：`a0be9a4449a4bf05b7a946994c37260735731a453113085089f853888dc1fbb5`。
- 输出 SHA-256：`fbc8505ad987d7406780d7a8f9514ab9d6dc8d9e3a47c3ea4191f80f3978c532`。

## 机械对照

82 个 `etiquette` 标签和 12 个 `setcounter` 调用的内容与顺序完全相同。环境起止序列完全相同（127 个 `begin`、128 个 `end`；多出的 `end{document}` 来自源稿的条件式独立编译结尾）。保留 45 个原页码标记、19 个 Xy-pic 交换图、88 个 `item`、4 个脚注和全部 4 个 `bibitem` 键。

按行内数学、双美元行间数学、方括号行间数学及 `align*`/`gather*` 提取，输入和输出各有 1469 个数学片段。忽略空白与中文语序引起的片段次序变化后，多重集只有一处差异：命题 3.0.4 的 `\mbox{ where }` 译为 `\mbox{ 其中 }`；其余公式内容相同。各零参数控制词与相邻中文之间均明确分隔，未发现 `\pageoriginale中文` 这种被 XeTeX 合成未定义控制词的情况。

原稿 182 次 `hyperref`/`eqhyperref`/`hyperrefext` 调用中保留 181 次；另 1 次以具有明确法文证据的图目标 `hyperlink` 取代，详见下节。其他目标未改。首次出现的数学术语适当附英文；人名和书目原题保留原文拼写。全篇统一使用“双覆盖态射 / 双覆盖族”。

## 法文核验与明确更正

只读核验材料：`/tmp/sga4-original-tome1.pdf`，334 页法文可搜索重排本。此轮只对下列具体疑点核验，不声称逐页对照法文。

1. 注 3.3 最后的英文引文断于 `recovers the construction of [`。法文重排本物理第 140 页（重排页 134，原页边号 234）也断于 `En explicitant les formules on retrouve la construction de [`。该证据不能恢复缺失书目号。译文保留可见句意及开方括号，并加来源缺损注释，未臆造引文。此项仍未解决。
2. 定理 4.4 证明中的图 (4.6.2) 原本具有目标 `sga4.exp.II.equation.4.6.2`；后文英文却使用 `\hyperref[II.cor4.6.2]{4.6.2}`，链接到后面的推论 4.6.2。法文重排本物理第 146 页（重排页 140，原页边号 243）明确说该段公式来自图 (4.6.2) 的交换性。因此将这一处改为 `\hyperlink{sga4.exp.II.equation.4.6.2}{4.6.2}`，保留显示编号。正文源码有 `SOURCE-CORRECTION` 注释。

## 保留而未擅改的底稿疑点

- 注 6.2 的公式为 `Hom_D(S,F(X)) → lim_{C/R} F(.)`，右端未出现 `Hom_D(S,-)`，一般范畴下类型不合。法文重排本物理第 155 页（重排页 149，原页边号 258）也是同一写法。译文原样保留，待更高层次的数学审校裁定。
- 命题 3.2 证明 3) 中若干 `pr_1`、`pr_2` 复合式有类型疑点；法文重排本物理第 140 页也保留这些写法。未擅自修补证明。
- §5.5.0 两个行间式的源稿写作 `\Caf{quoi}` 与 `\Tt{quoi}`，其中 `quoi` 缺少反斜线，可能导致字面字母印出；为保持底稿公式代码，未私改为 `\quoi`。
- 命题 4.7 中 `\Pi`/`\pi` 及 `\epsilon_C`/`J_C` 的记号不一致、若干不准确的原交叉引用均保持，未假定其为排版笔误后统一。

## 编译与视觉边界

未独立编译此分片，未声称 PDF、字体、警告或溢出检查通过；由主代理统一集成编译及检查。正文没有未译段落或续写占位。注 3.3 的缺损来自当前全部已查见证，保留的缺损不计作已恢复原文。

## Integration correction: literal `quoi`

Root restored the missing backslash in the two §5.5.0 map targets `\Caf{\quoi}` and `\Tt{\quoi}`. `\quoi` is the source empty punctuation helper, not an extra mathematical variable. The selected English TeX had printed literal `quoi`; the French recomposed witness (physical pp.154–155, original margins256–257) displays just the categories, agreeing with the mathematical declarations. The original typescript scan physical p.272 (printed256) was rendered for direct comparison. Source originals were not changed.
