# I09 与 III15–23 独立只读审校

日期：2026-10-23 UTC。审校者未参与这十件旧稿的翻译。本次只读审查，没有修改被审文件、图表、主文件、SOURCE_ISSUES 或其他记录，没有提交。

## 源文与审查范围

已先完整阅读 `audit/SOURCE_ISSUES.md`，特别是 I §6.5.3、§6.6 以及 III19、III21–23 的现有条目，以区分底本问题与译错。

源目录为 `/tmp/sga-native/native/SGA3/SGA3_English_current_buildable_source_20260823/source/`。每件依据中文文件去掉 `-zh` 后的完整同名源文件进行 rglob 唯一定位，使用 `inputs/I/tex/components/09_expose_I_s6_equivariant_objects.tex` 及 `inputs/III/tex/components/15_expose_III_opening_s016.tex` 至 `23_expose_III_s2_infinitesimal_group_morphisms.tex`。没有以其他译本代替选定 ZIP 组件。

全部覆盖 **10 件、4,330 源行**：

- I09：§6.1–6.8.6 全部正文、定义、各项等价、群/幺半群条件、截面作用、拉回/正像证明、稳定子、余法层及全部 8 项书目。
- III15：开篇、§0 的设定、0.1–0.1.6，全部正文、脚注、附论、定义及函子描述。
- III16：0.1.7–0.1.10，全部陈述和证明，包括平方零像条件、扩张集合的主齐性、群作用律的局部计算、两个函子变量及自然性。
- III17：0.1.11–0.2，积和纤维积、自然同构、作用的三项性质及其证明。
- III18：0.3–0.7，平坦性、有限呈示/局部自由假设、截面假设、对偶与向量丛脚注、结构迁移及自同态可逆性的完整证明。
- III19：0.7 bis–0.10，幺半群/群区别、分裂列、两种证明、伴随作用及其计算。
- III20：0.11–0.17，自同构函子、核、平坦基变换、两个阶段的有限呈示/平坦条件，以及平滑仿射提升与唯一性（非唯一同构）陈述。
- III21：1.1–1.2.4，标准复形、标量限制、正合列、一般截面与群态射截面的区别、障碍的必要充分性、共轭商以及 (a)–(d) 全部证明。
- III22：1.3.1–1.3.6，条件 (+) 的 n=1,2,3,4、容许合成律与群律区别、等价关系及 (a)–(f) 全部证明和五边形图题。
- III23：2.0–2.14，类型 a/b、平坦/仿射/有限呈示条件、定理 2.1 三项、2.1.1 的符号约定脚注、2.5(i) 的编者保留意见、所有推论及证明、全部 n 的消灭条件和不变量描述。

逐段核对了正文、条件、量词、否定、陈述、证明、脚注、图题、locator 和书目。未抽样替代通读。未发现明确的正文缺段、条件/否定反转、充要方向错误、变量替换或符号新增。以下把尚未完全中译的源说明列出，不为“审出问题”而重写合格中文。

## 需要处理的明确遗留项

### R1 — 十件文件的 TeX 源说明和定位注释仍为英文

**范围及现文：**

|文件（均在 chapters/）|条款/位置|现文举例|
|---|---|---|
|`09_expose_I_s6_equivariant_objects-zh.tex`|文件开头、各源页标识和文件末尾|`Scope: Section 6, "G-equivariant objects and modules," ...`；`Source page: ...`；`End of Expose I ...`|
|`15_expose_III_opening_s016-zh.tex`|开头、各源页及末尾|`Scope: opening through Remark 0.1.6 ...`；`The PDF controls text, formulas, numbering, notes, and diagram images.`；`Continue with Reminders 0.1.7.`|
|`16_expose_III_s017_s0110_functorial_liftings-zh.tex`|开头、各源页及末尾|`Scope: Reminders 0.1.7 through Corollary 0.1.10 ...`；`Source page: ...`；`Continue with Lemma 0.1.11.`|
|`17_expose_III_s0111_s02_products_action-zh.tex`|开头、源页及末尾|`pagination 88--90 also shown by the re-edition`；`Continue with Remark 0.3.`|
|`18_expose_III_s03_s07_flat_liftings-zh.tex`|开头、源页及末尾|`Scope: Remark 0.3 through Corollary 0.7 ...`；`Continue with Corollary 0.7 bis.`|
|`19_expose_III_s07bis_s010_group_actions-zh.tex`|开头、源页及末尾|`a drafting locator; English wording was compared ...`；`Continue with Proposition 0.11.`|
|`20_expose_III_s011_end_s0_automorphisms-zh.tex`|开头、源页及末尾|`mathematics, numbering, notes, and the two temporary diagram images`；`Continue with section 1 ...`|
|`21_expose_III_s11_s12_extensions_cohomology-zh.tex`|开头、源页及末尾|`The final item occupies the top of source p. 28.`；`Source lines: 441; translated body lines before this audit comment: 417.`|
|`22_expose_III_s13_group_law_extensions-zh.tex`|开头、源页及末尾|`was used only as a comparison. The PDF controls ...`；`Continue with Section 2 ...`；末尾英文行数说明|
|`23_expose_III_s2_infinitesimal_group_morphisms-zh.tex`|开头、源页及末尾|`with only the section-2 portions of the first and last pages admitted`；`Continue with section 3 ...`；末尾英文行数说明|

**建议：**仅把注释中的自然语言翻译成中文；不得改变 PDF 文件名、commit、CC BY 4.0、页码、源范围或图识别信息。例如：

- `Source page: Exp3 component-local p. 5; combined-reader p. 115.` → `源页：Exp3 分篇第 5 页；合订本第 115 页。`
- `Continue with Lemma 0.1.11.` → `接续引理 0.1.11。`
- `Force-OCR is a drafting locator; English wording was compared with ...` → `Force-OCR 仅作起草定位；英文措辞曾与……比对。`

**理由：**全文翻译要求包含源说明和 locator；TeX 注释不显示在 PDF 中，不等于可忽略这些语言内容。这些遗留没有造成正文数学变化。译文自加的行数审计注也不是底本内容，可保留在审计资料中或翻译，不能把它们误算成原著正文。

本轮未发现第二项明确的正文译错或遗漏。I09 八项书目均已采用中文题名加〔原题〕，人名、期刊名及出版者保留原文，版次和页码完整，不建议重译。

## 源文疑点：不得列为译错或静默修补

### S1 — 已登记的 I09 疑点

`SOURCE_ISSUES.md` 中 I §6.5.3 的转置连等式、Lambda/varphi 混用与反变方向，以及 §6.6 在一般 p:X→Y 下写 p_T:X_T→T 的问题，均来自所选英文源。当前译稿的相关公式、变量和条件与源一致。本轮没有把它们改成“正确版本”，也不计作中译错误。

### S2 — 已登记的 III19、III21–23 疑点

- III19 0.7 bis 外部 [DG70] 定理3.5及第II篇引理3.10错链；显示文字与键由源继承。
- III21–22 的 D_s=0、e_M 及加法/乘法记号混用由源继承。
- III23 2.10 显示“II,2.1”但键为 III2.1，以及 2.6 的仿射性条件，均已在 SOURCE_ISSUES 列为待核。

这些内容已逐段对照，未发现中译另外改变其符号或删掉保留意见。2.5(i) 仅保留编者脚注而无有效新陈述，正是源版结构，不是翻译遗漏。

### S3 — III16，0.1.10(b) 证明末的复合态射类型（本轮新增待核）

源文先写：令 g' 为由 (g,m·g) 定义的 X-态射 `Y→Δ^(1)_{X/S}`；紧接着写“与 `(f∘g,f∘g')` 对应”的元素。此时 f:X→W，而 g' 的目标已是第一无穷小邻域，`f∘g'` 若按字面并无定义；可能需要以 Δ^(1)f 作用于 g'，或重新区分第二个扩张 g' 与二元组态射的记号。

中文“令 g' 为由 (g,m·g) 定义的 X-态射……与 (f∘g,f∘g') 对应”忠实保留了源文，相关数学片段逐字一致。这只是源文类型/记号待核项；未做法文核验，不能据此断言法文底本必错，更不能直接改公式。

## 机械证据及验证边界

- 十件行内数学片段的多重集全部相同；显示公式和 align 的差异只在 `respectively`、`and`、`for every`、`in case` 等自然语言译文，不涉及数学标记。
- 全部 **371 个引用/目标宏**（SGARefLink、SGARefTarget、SGAInlineRefTarget）的键守恒；环境序列守恒，剔除转义花括号和注释后花括号配对正常。
- **68 条 footnote/footnotetext** 的数量与源相同；已逐条阅读其内容，不以计数代替内容核对。
- **37 个原生图表**调用目标全部存在，逐文件比较与选定源文件字节相同；没有重画。图题与图下 PDF/页码 locator 在中文组件中完整翻译。图内没有发现需要翻译的英文自然语言标签；Hom、Aut、pr、id、alg 等是数学符号。
- 这些结果不表示链接目标均正确；SOURCE_ISSUES 已记的错链仍存在。
- 没有编译新 PDF、进行本轮逐页视觉检查、逐式独立重证，或逐页核查新版权威法文 PDF。本报告是英中全文独立对照，不是数学认证或法文终审。
- 被审文件未改。下列哈希记录审查时的实际快照，后续任何改动需重新核验相关部分。

## 文件快照

|文件|源行数|脚注及脚注文本|图表|SHA-256|
|---|---:|---:|---:|---|
|`09_expose_I_s6_equivariant_objects-zh.tex`|881|3|7|`179496546677324e691ca21520b67ad00a720dfbd4c1f145df7d1f675b53b784`|
|`15_expose_III_opening_s016-zh.tex`|365|11|2|`c090375d33df1355a891879619233242c0fbb5d862d3ae36938949b3ee653242`|
|`16_expose_III_s017_s0110_functorial_liftings-zh.tex`|591|7|12|`b003f6b6c8e5aeaf1833502d85e37a4919d0aae4fbf0390a56f0d4a548449b93`|
|`17_expose_III_s0111_s02_products_action-zh.tex`|179|3|7|`e2b10065f5d71b2384bbae5d432183142528dfb82a6d3b21fd7f8928a47efa82`|
|`18_expose_III_s03_s07_flat_liftings-zh.tex`|319|6|2|`6db06056aa1cf4e1baa0c8d7dd734eed6e672ed881a01106b9b8bb669e501324`|
|`19_expose_III_s07bis_s010_group_actions-zh.tex`|263|2|2|`df7a8815f6aa595fafde5e90ae9b8aa31a5718db30ac5ca4408a1425551f7ea0`|
|`20_expose_III_s011_end_s0_automorphisms-zh.tex`|366|6|2|`3a0e2454b4eab580ba9b77819536b552cc8974bb6f501110b817d7013fc81a1f`|
|`21_expose_III_s11_s12_extensions_cohomology-zh.tex`|441|11|1|`78644122bf3e8cdee75dcb6c163b2acf8fa620c4060262f0dbcfb1b50598cfc0`|
|`22_expose_III_s13_group_law_extensions-zh.tex`|343|6|2|`b35612f943654bf44d68f0a9e6e1e9c30c815382f2b04c75ee4c83e4e24b5176`|
|`23_expose_III_s2_infinitesimal_group_morphisms-zh.tex`|582|13|0|`0012155c89f4d06cf82b34b216bc9358a8cd5e0f7e53d0ea08970b7a440b248a`|
