# VII 已报告引用问题的有界收尾

仅既有VII-A00–08 S3、VII-A09–14 S7、VII-B47–69末段、VII-B70–95跨篇引用记录；概括错链按对应已报键族与组件展开；正常跨篇引用亦列明。SOURCE_ISSUES中VII段未另列精确错链。

仅写本JSON和报告，未修改章节、preamble或main。行号为读取时原源码行；JSON保存完整调用、上下文和原文件hash。相同键在同一行重复出现须按上下文逐项处理。

{'replace_key': 94, 'external': 4, 'retain': 29, 'pending': 1}

## 39个pending的最后补核

{'original_pending': 39, 'resolved': 38, 'remaining_pending': 1, 'unique_new_anchor_count': 17, 'restriction': '仅补核原39个pending；未改正文。insert_target.before_line为当前目标源码原行号；宏须按target_line_after_insertion插入原行内，不应另起行或插在整个item之前。重复同key的insert_target仅执行一次。'}

VII-A02:177 已更正到现成 `sga3:VIIA:2.4:item:ii`。剩余唯一 pending 为 VII-A12:602 的编者注(71)，未由当前标签确认目标，保留文字不点击。

## 新锚点插入清单（每个key执行一次）

### `sga3:VIIA:2.3-invariance-lemma:item:ii`

目标 `chapters/VII-A/02_expose_VIIA_section2_invariant_differential_operators_en-zh.tex:115`，原行：
```tex
\item[\textit{(ii)}] \textit{\(m\) 的下述两个偏差相等：}
```
插宏后的精确整行：
```tex
\item[\textit{\SGAInlineRefTarget{sga3:VIIA:2.3-invariance-lemma:item:ii}(ii)}] \textit{\(m\) 的下述两个偏差相等：}
```

### `sga3:VIIA:3.1:item:i`

目标 `chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:29`，原行：
```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)} \(\sigma\circ\Delta_{\mathcal U}=\Delta_{\mathcal U}\), 其中 \(\sigma(a\otimes b)=b\otimes a\)。
```
插宏后的精确整行：
```tex
\SGAInlineRefTarget{sga3:VIIA:3.1:item:i}\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)} \(\sigma\circ\Delta_{\mathcal U}=\Delta_{\mathcal U}\), 其中 \(\sigma(a\otimes b)=b\otimes a\)。
```

### `sga3:VIIA:3.1:item:ii`

目标 `chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:33`，原行：
```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)} 方块图
```
插宏后的精确整行：
```tex
\SGAInlineRefTarget{sga3:VIIA:3.1:item:ii}\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)} 方块图
```

### `sga3:VIIA:5.2:condition:i`

目标 `chapters/VII-A/08_expose_VIIA_section5_restricted_p_lie_51_52_en-zh.tex:188`，原行：
```tex
  (i) &
```
插宏后的精确整行：
```tex
  \SGAInlineEquationTarget{sga3:VIIA:5.2:condition:i}(i) &
```

### `sga3:VIIA:5.2:condition:ii`

目标 `chapters/VII-A/08_expose_VIIA_section5_restricted_p_lie_51_52_en-zh.tex:199`，原行：
```tex
  (ii)\quad
```
插宏后的精确整行：
```tex
  \SGAInlineEquationTarget{sga3:VIIA:5.2:condition:ii}(ii)\quad
```

### `sga3:VIIA:5.2:condition:0`

目标 `chapters/VII-A/08_expose_VIIA_section5_restricted_p_lie_51_52_en-zh.tex:182`，原行：
```tex
  (0) &
```
插宏后的精确整行：
```tex
  \SGAInlineEquationTarget{sga3:VIIA:5.2:condition:0}(0) &
```

### `sga3:VIIA:7.2:item:i`

目标 `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:74`，原行：
```tex
  \item[\textit{(i)}]
```
插宏后的精确整行：
```tex
  \item[\textit{\SGAInlineRefTarget{sga3:VIIA:7.2:item:i}(i)}]
```

### `sga3:VIIA:7.4-theorem:item:ii`

目标 `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:494`，原行：
```tex
  \item[\textit{(ii)}]
```
插宏后的精确整行：
```tex
  \item[\textit{\SGAInlineRefTarget{sga3:VIIA:7.4-theorem:item:ii}(ii)}]
```

### `sga3:VIIA:8.2:item:i`

目标 `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:105`，原行：
```tex
  \item[\textup{(i)}] \(\pi\) 是平滑的；
```
插宏后的精确整行：
```tex
  \item[\textup{\SGAInlineRefTarget{sga3:VIIA:8.2:item:i}(i)}] \(\pi\) 是平滑的；
```

### `sga3:VIIA:8.2:item:ii`

目标 `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:106`，原行：
```tex
  \item[\textup{(ii)}] \(G'\) 是平滑的；
```
插宏后的精确整行：
```tex
  \item[\textup{\SGAInlineRefTarget{sga3:VIIA:8.2:item:ii}(ii)}] \(G'\) 是平滑的；
```

### `sga3:VIIA:8.2:item:iii`

目标 `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:107`，原行：
```tex
  \item[\textup{(iii)}] 对于每个整数 \(n>0\)，由 \(\tau\) 和 \(\pi\) 诱导的列
```
插宏后的精确整行：
```tex
  \item[\textup{\SGAInlineRefTarget{sga3:VIIA:8.2:item:iii}(iii)}] 对于每个整数 \(n>0\)，由 \(\tau\) 和 \(\pi\) 诱导的列
```

### `sga3:VIIA:8.3.1:item:ii`

目标 `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:192`，原行：
```tex
  \item[\textup{(ii)}]
```
插宏后的精确整行：
```tex
  \item[\textup{\SGAInlineRefTarget{sga3:VIIA:8.3.1:item:ii}(ii)}]
```

### `sga3:VIIB:2.1:item:ii`

目标 `chapters/VII-B/36_expose_VIIB_section21_formal_group_cogroups_en-zh.tex:20`，原行：
```tex
\item[\textup{(ii)}]存在必然唯一的\emph{增广}，即预有限 \(k\)-代数同态 \[
```
插宏后的精确整行：
```tex
\item[\textup{\SGAInlineRefTarget{sga3:VIIB:2.1:item:ii}(ii)}]存在必然唯一的\emph{增广}，即预有限 \(k\)-代数同态 \[
```

### `sga3:VIIB:2.6.2:prop:item:ii`

目标 `chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:38`，原行：
```tex
\item[\textup{(ii)}] \(\mathscr G(\mathbf L)\) 是无穷小的。
```
插宏后的精确整行：
```tex
\item[\textup{\SGAInlineRefTarget{sga3:VIIB:2.6.2:prop:item:ii}(ii)}] \(\mathscr G(\mathbf L)\) 是无穷小的。
```

### `sga3:VIIB:2.9.1:item:ii`

目标 `chapters/VII-B/56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en-zh.tex:126`，原行：
```tex
\item[\textup{(ii)}]
```
插宏后的精确整行：
```tex
\item[\textup{\SGAInlineRefTarget{sga3:VIIB:2.9.1:item:ii}(ii)}]
```

### `sga3:viib:subsection:4-4:item:i`

目标 `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:19`，原行：
```tex
\item[\textup{(i)}] 存在一个在 \(\mathcal O_k\) 上平坦的 \(p\)-Lie代数 \(\mathbf L\)，使 \(G\) 同构于 \(\mathscr G_p(\mathbf L)\)。此时，由 \SGARefLink{sga3:VIIB:4.2.2}{4.2.2}，有 \(\mathbf L=\operatorname{Lie}(G)\)。
```
插宏后的精确整行：
```tex
\item[\textup{\SGAInlineRefTarget{sga3:viib:subsection:4-4:item:i}(i)}] 存在一个在 \(\mathcal O_k\) 上平坦的 \(p\)-Lie代数 \(\mathbf L\)，使 \(G\) 同构于 \(\mathscr G_p(\mathbf L)\)。此时，由 \SGARefLink{sga3:VIIB:4.2.2}{4.2.2}，有 \(\mathbf L=\operatorname{Lie}(G)\)。
```

### `sga3:viib:subsection:4-4:item:ii`

目标 `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:21`，原行：
```tex
\item[\textup{(ii)}] 存在投射伪紧 \(k\)-模 \(\omega\)，使 \(G\) 的仿射代数同构于 \(k[[\omega]]\) 对由元素 \(x^p\)，\(x\in\omega\) 生成的闭理想的商。此时，\(\omega\simeq\omega_{G/k}\)。
```
插宏后的精确整行：
```tex
\item[\textup{\SGAInlineRefTarget{sga3:viib:subsection:4-4:item:ii}(ii)}] 存在投射伪紧 \(k\)-模 \(\omega\)，使 \(G\) 的仿射代数同构于 \(k[[\omega]]\) 对由元素 \(x^p\)，\(x\in\omega\) 生成的闭理想的商。此时，\(\omega\simeq\omega_{G/k}\)。
```

## 逐次决策

### 1. `chapters/VII-A/01_expose_VIIA_par13_through_par15_en-zh.tex:215`

- old_key: `sga3:VIIB:1.3.prop`
- visible_tex: `1.3`
- decision: **replace_key** → `sga3:VIIA:1.3`
- 证据：本篇相应编号与所述内容一致：1.3；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:1.3.prop}{1.3}
```

### 2. `chapters/VII-A/01_expose_VIIA_par13_through_par15_en-zh.tex:249`

- old_key: `sga3:VIIB:1.3.prop`
- visible_tex: `1.3`
- decision: **replace_key** → `sga3:VIIA:1.3`
- 证据：本篇相应编号与所述内容一致：1.3；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:1.3.prop}{1.3}
```

### 3. `chapters/VII-A/01_expose_VIIA_par13_through_par15_en-zh.tex:271`

- old_key: `sga3:VIIB:1.3.prop`
- visible_tex: `1.3`
- decision: **replace_key** → `sga3:VIIA:1.3`
- 证据：本篇相应编号与所述内容一致：1.3；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:1.3.prop}{1.3}
```

### 4. `chapters/VII-A/02_expose_VIIA_section2_invariant_differential_operators_en-zh.tex:122`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:2.3-invariance-lemma:item:ii`
- 证据：所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 5. `chapters/VII-A/02_expose_VIIA_section2_invariant_differential_operators_en-zh.tex:146`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:2.3-invariance-lemma:item:ii`
- 证据：所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 6. `chapters/VII-A/02_expose_VIIA_section2_invariant_differential_operators_en-zh.tex:177`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:2.4:item:ii`
- 证据：补核更正：本条位于定理2.4的编者脚注，明确说补入断言(ii)；现有2.4:item:ii位于同一定理左不变算子断言，不能指2.3引理。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 7. `chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:19`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:3.1:item:i`
- 证据：所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 8. `chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:29`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:3.1:item:i`
- 证据：所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 9. `chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:33`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:3.1:item:ii`
- 证据：所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 10. `chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:481`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:3.1:item:i`
- 证据：所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 11. `chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:481`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:3.1:item:ii`
- 证据：所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 12. `chapters/VII-A/05_expose_VIIA_par413_through_par414_en-zh.tex:141`

- old_key: `sga3:VIIB:3.1:lemma`
- visible_tex: `3.1`
- decision: **replace_key** → `sga3:VIIA:3.1`
- 证据：本篇相应编号与所述内容一致：3.1；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:3.1:lemma}{3.1}
```

### 13. `chapters/VII-A/08_expose_VIIA_section5_restricted_p_lie_51_52_en-zh.tex:130`

- old_key: `sga3:VIIB:3.2:prop`
- visible_tex: `3.2`
- decision: **external**
- 证据：脚注明指 [DG70] III.7,3.2，外部书目，保留显示文字不点击。

```tex
\SGARefLink{sga3:VIIB:3.2:prop}{3.2}
```

### 14. `chapters/VII-A/08_expose_VIIA_section5_restricted_p_lie_51_52_en-zh.tex:217`

- old_key: `sga3:VIIB:5.1:proposition`
- visible_tex: `5.1`
- decision: **replace_key** → `sga3:VIIA:5.1`
- 证据：本篇相应编号与所述内容一致：5.1；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:5.1:proposition}{5.1}
```

### 15. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:20`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **replace_key** → `sga3:VIIA:5.2`
- 证据：相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 16. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:82`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **retain**
- 证据：前紧连“公式5.1”，现有目标为5.1 Jacobson第一公式，正常。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 17. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:82`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **replace_key** → `sga3:VIIA:5.2`
- 证据：相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 18. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:82`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:5.2:condition:i`
- 证据：紧连5.2，应指5.2的(i)，而现键指5.1第一公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 19. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:105`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **retain**
- 证据：此调用紧连5.1，指Jacobson第二公式，目标正确。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 20. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:105`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:5.2:condition:ii`
- 证据：紧连5.2，应指5.2条件(ii)而非5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 21. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:125`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **replace_key** → `sga3:VIIA:5.2`
- 证据：相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 22. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:125`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:5.2:condition:i`
- 证据：本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 23. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:126`

- old_key: `sga3:VIIB:0`
- visible_tex: `(0)`
- decision: **replace_key** → `sga3:VIIA:5.2:condition:0`
- 证据：当前句连引5.2的(i)、(0)、(ii)，此处(0)唯一对应5.2齐次性条件。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。

```tex
\SGARefLink{sga3:VIIB:0}{(0)}
```

### 24. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:126`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:5.2:condition:ii`
- 证据：本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 25. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:186`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **retain**
- 证据：本处直接使用5.1的Jacobson第二公式，现有公式键可保留。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 26. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:206`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:5.2:condition:i`
- 证据：本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 27. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:212`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **retain**
- 证据：紧连“Jacobson第二个公式5.1”，现键正确。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 28. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:213`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:5.2:condition:ii`
- 证据：本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 29. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:213`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **replace_key** → `sga3:VIIA:5.2`
- 证据：相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 30. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:343`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **replace_key** → `sga3:VIIA:5.2`
- 证据：相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 31. `chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:343`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:5.2:condition:ii`
- 证据：本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 32. `chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:120`

- old_key: `sga3:VIIB:3.2:prop`
- visible_tex: `3.2`
- decision: **replace_key** → `sga3:VIIA:3.2`
- 证据：此处定义群余代数，VII-A3.2正是该定义；VII-B3.2是指数映射命题。

```tex
\SGARefLink{sga3:VIIB:3.2:prop}{3.2}
```

### 33. `chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:139`

- old_key: `sga3:VIIB:5.1:proposition`
- visible_tex: `5.1`
- decision: **replace_key** → `sga3:VIIA:5.1`
- 证据：本篇相应编号与所述内容一致：5.1；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:5.1:proposition}{5.1}
```

### 34. `chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:139`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **replace_key** → `sga3:VIIA:5.2`
- 证据：相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 35. `chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:305`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:5.5.3:item:i`
- 证据：5.5.3证明中的本地(i)/(ii)，已存在精确分项标签。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 36. `chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:305`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:5.5.3:item:ii`
- 证据：5.5.3证明中的本地(i)/(ii)，已存在精确分项标签。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 37. `chapters/VII-A/11_expose_VIIA_section6_p_lie_group_scheme_en-zh.tex:29`

- old_key: `sga3:VIIB:2.5:proposition`
- visible_tex: `2.5`
- decision: **replace_key** → `sga3:VIIA:2.5-proposition`
- 证据：本篇相应编号与所述内容一致：2.5；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:2.5:proposition}{2.5}
```

### 38. `chapters/VII-A/11_expose_VIIA_section6_p_lie_group_scheme_en-zh.tex:29`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **replace_key** → `sga3:VIIA:5.2`
- 证据：相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 39. `chapters/VII-A/11_expose_VIIA_section6_p_lie_group_scheme_en-zh.tex:41`

- old_key: `sga3:VIIB:2.5:proposition`
- visible_tex: `2.5`
- decision: **replace_key** → `sga3:VIIA:2.5-proposition`
- 证据：本篇相应编号与所述内容一致：2.5；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:2.5:proposition}{2.5}
```

### 40. `chapters/VII-A/11_expose_VIIA_section6_p_lie_group_scheme_en-zh.tex:45`

- old_key: `sga3:VIIB:2.5:proposition`
- visible_tex: `2.5`
- decision: **replace_key** → `sga3:VIIA:2.5-proposition`
- 证据：本篇相应编号与所述内容一致：2.5；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:2.5:proposition}{2.5}
```

### 41. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:162`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:7.2:item:ii`
- 证据：当前证明7.2的(ii)情形，已存在精确标签。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 42. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:280`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:7.2:item:i`
- 证据：当前证明7.2的(i)情形。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 43. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:280`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:7.2:item:ii`
- 证据：当前证明7.2的(ii)情形，已存在精确标签。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 44. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:318`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:7.2:item:i`
- 证据：当前证明7.2的(i)情形。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 45. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:331`

- old_key: `prop:sga3-VIB-11.6.1`
- visible_tex: `11.6.1`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{prop:sga3-VIB-11.6.1}{11.6.1}
```

### 46. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:339`

- old_key: `prop:sga3-VIB-11.6.1`
- visible_tex: `11.6.1`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{prop:sga3-VIB-11.6.1}{11.6.1}
```

### 47. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:455`

- old_key: `sga3:VIIB:2.5:proposition`
- visible_tex: `2.5`
- decision: **replace_key** → `sga3:VIIA:2.5-proposition`
- 证据：本篇相应编号与所述内容一致：2.5；非 VII-B 同号条目。

```tex
\SGARefLink{sga3:VIIB:2.5:proposition}{2.5}
```

### 48. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:520`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:7.4-theorem:item:i`
- 证据：7.4.1证明的本地条件，7.4定理对应分项。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 49. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:520`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:5.5.3:item:i`
- 证据：紧连5.5.3，应指该定理(i)/(ii)，该精确标签已存在。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 50. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:520`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:7.4-theorem:item:i`
- 证据：7.4.1证明的本地条件，7.4定理对应分项。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 51. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:520`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:7.4-theorem:item:ii`
- 证据：7.4.1证明的本地条件(ii)。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。该(ii)实际为仿射性、omega局部自由有限型及截断对称代数结构，前轮near的简写不准确，本轮已以原行495核清。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 52. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:526`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:5.5.3:item:ii`
- 证据：紧连5.5.3，应指该定理(i)/(ii)，该精确标签已存在。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 53. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:546`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:7.4-theorem:item:i`
- 证据：7.4.1证明的本地条件，7.4定理对应分项。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 54. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:546`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:7.4-theorem:item:ii`
- 证据：7.4.1证明的本地条件(ii)。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。该(ii)实际为仿射性、omega局部自由有限型及截断对称代数结构，前轮near的简写不准确，本轮已以原行495核清。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 55. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:602`

- old_key: `sga3:VIIB:nde:71`
- visible_tex: `(71)`
- decision: **pending**
- 证据：当前引“编者注(71)”但现有VIIB nde71属于1.5形式平滑代数，与本处7.4证明无关；未能由现存标签唯一定位本篇所需脚注。保留(71)不点击。

```tex
\SGARefLink{sga3:VIIB:nde:71}{(71)}
```

### 56. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:610`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **external**
- 证据：显式 [BAC] II §5.2 定理1/推论2，为 Bourbaki 外部文献，不能指本书 VII-B；保留完整文字不点击。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 57. `chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:636`

- old_key: `sga3:VIIB:2.8`
- visible_tex: `2.8`
- decision: **external**
- 证据：显式 [BAC] I §2.8 引理9，外部文献；保留文字不点击。

```tex
\SGARefLink{sga3:VIIB:2.8}{2.8}
```

### 58. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:96`

- old_key: `sga3:VIIB:5.2:theorem`
- visible_tex: `5.2`
- decision: **replace_key** → `par:sga3-VIA-5.2`
- 证据：同一脚注明指 VIA 3.2 和 5.2；VI-A5.2 讨论正规子群商。

```tex
\SGARefLink{sga3:VIIB:5.2:theorem}{5.2}
```

### 59. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140`

- old_key: `prop:sga3-VIB-9.2`
- visible_tex: `9.2`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{prop:sga3-VIB-9.2}{9.2}
```

### 60. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140`

- old_key: `concl:sga3-VIB-9.2-vii`
- visible_tex: `(vii)`
- decision: **retain**
- 证据：前缀VIB9.2及(vii)明确为外引，用于后面的(i)⇔(ii)；这一个不是当前局部(iii)，保留。

```tex
\SGARefLink{concl:sga3-VIB-9.2-vii}{(vii)}
```

### 61. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIA:8.2:item:i`
- 证据：8.2证明中的本地条件，非5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 62. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:8.2:item:ii`
- 证据：8.2证明中的本地条件，非5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 63. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140`

- old_key: `concl:sga3-VIB-9.2-iii`
- visible_tex: `(iii)`
- decision: **replace_key** → `sga3:VIIA:8.2:item:iii`
- 证据：此处是8.2本地条件间蕴含，后接本地(iv)/(v)及Frobenius正合行图，不是VIB9.2的条件。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{concl:sga3-VIB-9.2-iii}{(iii)}
```

### 64. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:142`

- old_key: `concl:sga3-VIB-9.2-ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:8.2:item:ii`
- 证据：此处是8.2本地条件间蕴含，后接本地(iv)/(v)及Frobenius正合行图，不是VIB9.2的条件。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{concl:sga3-VIB-9.2-ii}{(ii)}
```

### 65. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:142`

- old_key: `concl:sga3-VIB-9.2-iii`
- visible_tex: `(iii)`
- decision: **replace_key** → `sga3:VIIA:8.2:item:iii`
- 证据：此处是8.2本地条件间蕴含，后接本地(iv)/(v)及Frobenius正合行图，不是VIB9.2的条件。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{concl:sga3-VIB-9.2-iii}{(iii)}
```

### 66. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:189`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:8.3.1:item:ii`
- 证据：本地8.3.1的(ii)，不是5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 67. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:198`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIA:8.3.1:item:ii`
- 证据：本地8.3.1的(ii)，不是5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 68. `chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:198`

- old_key: `prop:sga3-VIB-1.3`
- visible_tex: `1.3`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{prop:sga3-VIB-1.3}{1.3}
```

### 69. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:34`

- old_key: `prop:sga3-VIB-1.3`
- visible_tex: `1.3`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{prop:sga3-VIB-1.3}{1.3}
```

### 70. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:105`

- old_key: `sga3:VIIA:8.4`
- visible_tex: `8.4`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{sga3:VIIA:8.4}{8.4}
```

### 71. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:105`

- old_key: `sga3:VIIA:8.5`
- visible_tex: `8.5`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{sga3:VIIA:8.5}{8.5}
```

### 72. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:105`

- old_key: `sga3:VIIA:5`
- visible_tex: `引理~5`
- decision: **external**
- 证据：脚注明指 [TO70] 引理5，非本书第5节；保留文字不点击。

```tex
\SGARefLink{sga3:VIIA:5}{引理~5}
```

### 73. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:107`

- old_key: `sga3:VIIA:8.5`
- visible_tex: `8.5`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{sga3:VIIA:8.5}{8.5}
```

### 74. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:132`

- old_key: `sga3:VIIA:7.0`
- visible_tex: `7.0`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{sga3:VIIA:7.0}{7.0}
```

### 75. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:136`

- old_key: `cor:sga3-VIB-1.6.1`
- visible_tex: `1.6.1`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{cor:sga3-VIB-1.6.1}{1.6.1}
```

### 76. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:136`

- old_key: `sga3:VIIA:3.3.1`
- visible_tex: `3.3.1`
- decision: **replace_key** → `sga3:VIIB:3.3.1`
- 证据：当前明确写VIIB3.3.1，故先修篇别到现有同号标签；引用是否充分不是本次链接判断。

```tex
\SGARefLink{sga3:VIIA:3.3.1}{3.3.1}
```

### 77. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:143`

- old_key: `sga3:VIIA:7.4`
- visible_tex: `7.4`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{sga3:VIIA:7.4}{7.4}
```

### 78. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:143`

- old_key: `sga3:VIIA:5.3.3`
- visible_tex: `5.3.3`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{sga3:VIIA:5.3.3}{5.3.3}
```

### 79. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:211`

- old_key: `sga3:VIIB:1.3.6`
- visible_tex: `1.3.6`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{sga3:VIIB:1.3.6}{1.3.6}
```

### 80. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:230`

- old_key: `sga3:VIIA:4.3`
- visible_tex: `4.3`
- decision: **replace_key** → `sga3:VIIB:4.3`
- 证据：当前句明指VIIB4.3，讨论受限包络代数滤过；VII-A4.3是Verschiebung。

```tex
\SGARefLink{sga3:VIIA:4.3}{4.3}
```

### 81. `chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:291`

- old_key: `sga3:VIIA:8.5`
- visible_tex: `8.5`
- decision: **retain**
- 证据：篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。

```tex
\SGARefLink{sga3:VIIA:8.5}{8.5}
```

### 82. `chapters/VII-B/51_expose_VIIB_section26_lie_algebra_opening_en-zh.tex:82`

- old_key: `sga3:VIIA:2.1`
- visible_tex: `2.1`
- decision: **replace_key** → `sga3:VIIB:2.1`
- 证据：当前用形式群仿射代数的增广余乘法公式，VIIB2.1定义该结构；VII-A2.1仅原点偏差。

```tex
\SGARefLink{sga3:VIIA:2.1}{2.1}
```

### 83. `chapters/VII-B/51_expose_VIIB_section26_lie_algebra_opening_en-zh.tex:82`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:2.1:item:ii`
- 证据：紧连2.1并使用增广恒等式，所指为VIIB2.1(ii)。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 84. `chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:19`

- old_key: `sga3:VIIA:3.2.2`
- visible_tex: `3.2.2`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:3.2.2}{3.2.2}
```

### 85. `chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:19`

- old_key: `sga3:VIIA:2.2`
- visible_tex: `2.2`
- decision: **replace_key** → `sga3:VIIB:2.2`
- 证据：此处由双代数用Spf*构造形式群，VIIB2.2为此定义；VII-A2.2是平移偏差。

```tex
\SGARefLink{sga3:VIIA:2.2}{2.2}
```

### 86. `chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:31`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:2.6.2:prop:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:2.6.2:prop:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 87. `chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:31`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:2.6.2:prop:item:ii`
- 证据：本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 88. `chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:70`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:2.6.2:prop:item:ii`
- 证据：本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 89. `chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:97`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:2.6.2:prop:item:ii`
- 证据：本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 90. `chapters/VII-B/56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en-zh.tex:176`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:2.9.1:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:2.9.1:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 91. `chapters/VII-B/56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en-zh.tex:177`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:2.9.1:item:ii`
- 证据：本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 92. `chapters/VII-B/56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en-zh.tex:202`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:2.9.1:item:ii`
- 证据：本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 93. `chapters/VII-B/58_expose_VIIB_section32_exponential_logarithm_en-zh.tex:37`

- old_key: `sga3:VIIA:2.2`
- visible_tex: `2.2`
- decision: **replace_key** → `sga3:VIIB:2.2`
- 证据：此处由双代数用Spf*构造形式群，VIIB2.2为此定义；VII-A2.2是平移偏差。

```tex
\SGARefLink{sga3:VIIA:2.2}{2.2}
```

### 94. `chapters/VII-B/58_expose_VIIB_section32_exponential_logarithm_en-zh.tex:37`

- old_key: `sga3:VIIA:3.2.3`
- visible_tex: `3.2.3`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:3.2.3}{3.2.3}
```

### 95. `chapters/VII-B/58_expose_VIIB_section32_exponential_logarithm_en-zh.tex:141`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:3.2:prop:item:ii`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.2:prop:item:ii；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 96. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:39`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 97. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:40`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:ii`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 98. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:82`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 99. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:84`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:ii`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 100. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:117`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 101. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:126`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 102. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:126`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:ii`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 103. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:158`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 104. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:158`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:ii`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 105. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:179`

- old_key: `sga3:VIIA:7.4`
- visible_tex: `7.4`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:7.4}{7.4}
```

### 106. `chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:202`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 107. `chapters/VII-B/61_expose_VIIB_section331_smoothness_corollary_en-zh.tex:45`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:3.3:cartier-theorem:item:ii`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 108. `chapters/VII-B/62_expose_VIIB_section332_lie_formal_group_equivalence_en-zh.tex:32`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:3.2:prop:item:ii`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.2:prop:item:ii；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 109. `chapters/VII-B/62_expose_VIIB_section332_lie_formal_group_equivalence_en-zh.tex:41`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:VIIB:3.2:prop:item:ii`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.2:prop:item:ii；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 110. `chapters/VII-B/67_expose_VIIB_sections42_421_restricted_enveloping_group_en-zh.tex:14`

- old_key: `sga3:VIIA:2.3`
- visible_tex: `2.3`
- decision: **replace_key** → `sga3:VIIB:2.3`
- 证据：此处Lie(G)作为H(G)本原元素子代数使用VIIB2.3；VII-A2.3是右不变偏差。

```tex
\SGARefLink{sga3:VIIA:2.3}{2.3}
```

### 111. `chapters/VII-B/67_expose_VIIB_sections42_421_restricted_enveloping_group_en-zh.tex:41`

- old_key: `sga3:VIIA:5.3`
- visible_tex: `5.3`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:5.3}{5.3}
```

### 112. `chapters/VII-B/67_expose_VIIB_sections42_421_restricted_enveloping_group_en-zh.tex:41`

- old_key: `sga3:vii:corollary:5-4`
- visible_tex: `5.4`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:vii:corollary:5-4}{5.4}
```

### 113. `chapters/VII-B/67_expose_VIIB_sections42_421_restricted_enveloping_group_en-zh.tex:41`

- old_key: `sga3:VIIA:2.2`
- visible_tex: `2.2`
- decision: **replace_key** → `sga3:VIIB:2.2`
- 证据：此处由双代数用Spf*构造形式群，VIIB2.2为此定义；VII-A2.2是平移偏差。

```tex
\SGARefLink{sga3:VIIA:2.2}{2.2}
```

### 114. `chapters/VII-B/68_expose_VIIB_section422_restricted_universal_property_en-zh.tex:15`

- old_key: `sga3:VIIA:5.3.3`
- visible_tex: `5.3.3`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:5.3.3}{5.3.3}
```

### 115. `chapters/VII-B/68_expose_VIIB_section422_restricted_universal_property_en-zh.tex:15`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:VIIB:2.6.2:prop:item:i`
- 证据：根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:2.6.2:prop:item:i；5.1公式键跨错到VII-A。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 116. `chapters/VII-B/68_expose_VIIB_section422_restricted_universal_property_en-zh.tex:23`

- old_key: `sga3:VIIA:3.2.3`
- visible_tex: `3.2.3`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:3.2.3}{3.2.3}
```

### 117. `chapters/VII-B/68_expose_VIIB_section422_restricted_universal_property_en-zh.tex:23`

- old_key: `sga3:VIIA:5.5.3`
- visible_tex: `5.5.3`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:5.5.3}{5.5.3}
```

### 118. `chapters/VII-B/71_expose_VIIB_section432_no_functorial_campbell_hausdorff_en-zh.tex:17`

- old_key: `sga3:VIIA:4.3.1`
- visible_tex: `4.3.1`
- decision: **replace_key** → `sga3:VIIB:4.3.1`
- 证据：当前处讨论VIIB4.3.1中群状元素参数化，VII-A4.3.1为Verschiebung常群例。

```tex
\SGARefLink{sga3:VIIA:4.3.1}{4.3.1}
```

### 119. `chapters/VII-B/71_expose_VIIB_section432_no_functorial_campbell_hausdorff_en-zh.tex:46`

- old_key: `sga3:VIIA:4.2.1`
- visible_tex: `4.2.1`
- decision: **replace_key** → `sga3:VIIB:4.2.1`
- 证据：源注明确指本讲4.2.1的群状元素集合，VIIB4.2.1定义G_p。

```tex
\SGARefLink{sga3:VIIA:4.2.1}{4.2.1}
```

### 120. `chapters/VII-B/71_expose_VIIB_section432_no_functorial_campbell_hausdorff_en-zh.tex:66`

- old_key: `sga3:VIIA:4.3.1`
- visible_tex: `4.3.1`
- decision: **replace_key** → `sga3:VIIB:4.3.1`
- 证据：当前处讨论VIIB4.3.1中群状元素参数化，VII-A4.3.1为Verschiebung常群例。

```tex
\SGARefLink{sga3:VIIA:4.3.1}{4.3.1}
```

### 121. `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:28`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:viib:subsection:4-4:item:i`
- 证据：本地命题/定理(i)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 122. `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:28`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:viib:subsection:4-4:item:ii`
- 证据：本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 123. `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:50`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:viib:subsection:4-4:item:i`
- 证据：本地命题/定理(i)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 124. `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:50`

- old_key: `sga3:vii:paragraph:5-1:equation:ii`
- visible_tex: `(ii)`
- decision: **replace_key** → `sga3:viib:subsection:4-4:item:ii`
- 证据：本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:ii}{(ii)}
```

### 125. `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:50`

- old_key: `sga3:VIIA:4.3.1`
- visible_tex: `4.3.1`
- decision: **replace_key** → `sga3:VIIB:4.3.1`
- 证据：当前处讨论VIIB4.3.1中群状元素参数化，VII-A4.3.1为Verschiebung常群例。

```tex
\SGARefLink{sga3:VIIA:4.3.1}{4.3.1}
```

### 126. `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:57`

- old_key: `sga3:VIIA:7.4.1`
- visible_tex: `7.4.1`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:7.4.1}{7.4.1}
```

### 127. `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:79`

- old_key: `sga3:vii:paragraph:5-1:equation:i`
- visible_tex: `(i)`
- decision: **replace_key** → `sga3:viib:subsection:4-4:item:i`
- 证据：本地命题/定理(i)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。

```tex
\SGARefLink{sga3:vii:paragraph:5-1:equation:i}{(i)}
```

### 128. `chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:102`

- old_key: `sga3:VIIA:5.5.3`
- visible_tex: `5.5.3`
- decision: **retain**
- 证据：附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。

```tex
\SGARefLink{sga3:VIIA:5.5.3}{5.5.3}
```
