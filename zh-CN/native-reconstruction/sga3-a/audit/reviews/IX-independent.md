# 第 IX 篇独立内容审校

按 `inputs/IX/body.tex` 的实际顺序，对五个冻结源组件与 `chapters/IX/` 对应译文逐段全文对照。覆盖定义、量词与否定、全部陈述及证明、58 个 `footnote`、1 个 `footnotetext`、各脚注标记复用、8 个原生图及书目。未改动 IX。审校不是编译验收，也未独立重证全部命题。

## 覆盖

|组件 stem（译文加 -zh.tex）|源行|footnote|footnotetext|图|
|---|---:|---:|---:|---:|
|01_expose_IX_opening_and_section_1|213|3|0|1|
|02_expose_IX_sections_2_3|587|8|0|0|
|03_expose_IX_sections_4_5|1248|29|0|2|
|04_expose_IX_sections_6_7|839|11|0|5|
|05_expose_IX_section_8_and_bibliography|219|7|1|0|
|合计|3106|58|1|8|

## 明确译错或残留

### R1：将概形错称为环

- 文件：`chapters/IX/03_expose_IX_sections_4_5-zh.tex`，引理 4.4 证明，第 195 行。
- 现文：“由于 \(S_n\) 是 Artin 局部环，且 \(Z_n^i\) 在 \(S_n\) 上平坦……”
- 源文：Since \(S_n\) is local Artinian；此处 \(S_n=\operatorname{Spec}(A/\mathfrak m^{n+1})\)。
- 建议：“由于 \(S_n\) 是 Artin 局部概形，且……”。
- 理由：源文主语是概形，译文新增“环”而改变对象种类；本质自由及表示性论证作用于概形上方的态射。

### R2：否定结论被弱化成“不必”

- 文件：`chapters/IX/01_expose_IX_opening_and_section_1-zh.tex`，说明 1.2，第 62 行。
- 现文：“\(G\) 可以局部平凡而非等平凡，因而\emph{更不必}平凡。”
- 源文：and hence a fortiori without being trivial。
- 建议：“……因而更不是平凡的。”或“……因而当然也非平凡。”
- 理由：源文说上述例子必然非平凡，现文“不必”只表示不要求/不一定平凡，弱化了这个蕴涵。

### R3：两处引用显示文本残留英文 below

- 文件：`chapters/IX/03_expose_IX_sections_4_5-zh.tex`，引理 4.4 证明，第 148、312 行。
- 现文：`\SGARefLink{sga3:ix:lemma:4:5}{引理~4.5 below}`。
- 建议：显示文本改为“下文引理~4.5”，键不动。
- 理由：源文 Lemma 4.5 below 的定位说明未完整翻译。

### R4：图内源稿说明注释仍为英文

- 文件：`chapters/IX/03_expose_IX_sections_4_5-zh.tex`，引理 4.4 第一图，第 132–133 行。
- 现文：`% The source visibly prints the n-subscripts in the upper middle and`，下一行 `% upper right nodes; they are retained despite the surrounding prose.`。
- 建议：译为“英文底本说明：源稿上中、右上节点明确印有 n 下标；尽管与周围正文有出入，仍予保留。”
- 理由：任务包含源注的中文化；注释不排印，但也应处理。图的公式原样保留。

## 底本已有疑点（非译错）

1. **4.10 选取 m 的例子。** 源文及译文均说可取类型的挠子群之阶。环面时该阶为 1；此时 \({}_{m^r}G\) 只是单位子群，通常不能概形稠密于非零维环面，并可能违背前述“不是剩余特征的幂”条件。需核对原法文或另行勘误；译者未改变这段数学内容，不应作为译错修补。
2. **已有修订说明应保留其层次。** 引理 4.4 中 B''/A'' 与 \(Z_n^{i''}=\operatorname{Spec}(B_n'')\) 的说明、5.5 中 H/K 的说明、5.6 未定义局部环 B 的说明，以及 7.1 中 C/C_n 的说明，均已经存在于冻结英文源，并非中译者擅改。中文忠实保留，不应据此回退公式。
3. **源稿引用键目标可疑。** 2.3 中 SGA 1, VIII 2.1 的键为 `sga3:viii:proposition:2:1`；3.1 的 loc. cit., 5.3 以 `sga3:ix:corollary:5:3` 链接，但上下文指第 I 篇 Hochschild 上同调；5.5 两处 VI_A 2.4 使用 `sga3:ix:corollary:2:4`。2.11(i) 的 3.2(b) 使用 `sga3:ix:theorem:3:2:item:b`，该目标实际被放在 3.6 bis(b)，与所援引的域上可对角化群分类内容不相称。译文键与英文源相同，需集成者核对目标，不在本次审校自行改键。

## 辅助检查

五对文件全部引用键/目标键及环境的多重集合一致，脚注与 footnotetext 数一致。7 个 tikzcd 块与英文源逐字相同；第 1 节 tikzpicture 六节点自然语言均已译，节点名、坐标、箭头方向与连接均保留。对照通读了八图的上下文与图示关系。去除注释、排除转义花括号后，五文件花括号均平衡。公式差异逐项核对，仅为公式中的自然语言说明中文化，未发现变量、等式或编号丢失。书目完整保留 N. Bourbaki、原题、章节、出版社及年份，并有中文题名。

证据：`/tmp/ix-integrity-review.json`、`/tmp/ix-integrity-review.txt`；对照辅助脚本 `/tmp/ix_review_pair.py`。机械守恒仅作全文语义审查的辅助，不构成数学正确性的独立证明。
