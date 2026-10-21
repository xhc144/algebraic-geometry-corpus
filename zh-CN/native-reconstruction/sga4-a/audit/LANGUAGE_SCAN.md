# 正文残留英文语言扫描

## 范围、方法及限度

2026-10-21 对 `chapters/**/*.tex` 的全部 32 个文件作独立残留英文扫描，覆盖 I、II、III、IV、V、V bis、VI、VII、VIII、IX 十篇的全部分片及包装文件，以及序言、两卷索引。按协调者要求，不修改共享正文；本次只写本审计文件。

先剔除注释、控制序列名和常见标签/引用键，检查全部 ASCII 词汇候选；再对 `text`、`txt`、`mbox`、`textrm`、`textnormal`、`textit`、`textsf`、`textbf`、`textsc`、`emph`、标题、脚注等命令作平衡花括号参数提取，检查 333 类含拉丁字母的候选；另作两字母英文虚词扫描，防止漏掉 `if`、`by`、`or` 等。对有意义的候选回读上下文，分别识别人名、书刊名、数学记号、首定义双语术语及正文漏译。

未发现整段未译的英文正文。发现 4 处明确漏译，均为图或公式中的普通语言；已报告协调者，并在复读共享文件时确认其已修正，详见下表。此结论是上述语言扫描的结果，不是全文源覆盖证明、独立数学证明审校或 PDF 视觉验收。未展开外部预导宏，因此不对宏定义本身的呈现语言作保证；原始书刊名及人名按要求保留。

## 明确漏译：4 处，现已修正

行号以发现时及末次复核时的共享文件为准；本审计者没有修改这些正文。

| 位置 | 发现时原片段 | 判断及建议 | 末次复核结果 |
| --- | --- | --- | --- |
| `chapters/V/body.tex:542` | `\txt{($\{e\}$ a one-element set).}` | 原生交换图中的说明句漏译；建议“（$\{e\}$ 为单元素集）。” | 已为 `\txt{（$\{e\}$ 为单元素集）。}` |
| `chapters/VII/body.tex:309` | `\mbox{for}` | 公式量词连接词漏译 | 已为 `\mbox{对}` |
| `chapters/VII/body.tex:316` | `\mbox{for}` | 同上 | 已为 `\mbox{对}` |
| `chapters/VII/body.tex:327` | `\mbox{for}` | 同上，位于带 `$\ast$` 标号的公式中 | 已为 `\mbox{对}` |

## 已复核、未列作漏译的候选

下列为排除 TeX 命令、标签和人名后值得记录的实际显示候选。并非将所有拉丁字母机械视作错误。

| 候选及位置 | 上下文及判断 |
| --- | --- |
| I `01-sections-0-4.tex:3,79,91,119,167,295,322,338,506,518,555,772`：`universe`、`strongly inaccessible cardinal`、`Artinian set`、`small`、`presheaf of sets`、`representable presheaf`、`projective limit`、`inductive limit`、`universal`、`pseudo-filtered`、`filtered`、`sieve` | 均有中文定义/译名，英文是首次术语对照，不是未译叙述。 |
| I `03-section-8a.tex:20`：`cofinal`；II `body.tex:16,37,73,81,95,295,359,670,1515`：`topology`、`refinement`、`site`、`covering family`、`pretopology`、`canonical topology`、`topologically generating family`、`associated sheaf`、`bicovering morphism` | 均处在已有中文译名之后的括号中。III 的 `bicovering` 同样为“双覆盖”的术语对照。 |
| IV `body.tex:505,559,2005`：`sober`、`point`、`gerbe`；IV `part-9.tex:2769`：`precoherent`、`coherent` | 中文术语后附原词。 |
| VI `part-0-5.tex:10,11,65,946,1027,1329,2325`：`quasi-compactness`、`quasi-separatedness`、`coherence`、`constructible object`、`perfect`、`pre-Noetherian object`、`algebraic topos`、`pretopos`；VI `part-8-9.tex:73,1315,1354`：`bisplitting`、`local topos`、`bicleavage` | 中文定义/术语后附原词。 |
| I `02-sections-5-7.tex:582,866,868`；IV `part-9.tex:385,1065,1085,1149,1187,1398,1712,1748,2847`：`Cartesian` | “Cartesian 图/态射”“余 Cartesian”“2-Cartesian”等惯用数学术语。按本次明确排除的“既有拉丁数学术语”处理；可另作全书术语风格统一，不能据此称作未译英文句子。 |
| IX `body.tex:1392,1627`：`Jacobian` | 雅可比簇的惯用名称；属既有数学术语保留。 |
| I `01-sections-0-4.tex:402,738`：`source` | 公式中的源函数/算子名称；正文已写“源函子”。属数学记号，不是说明句。 |
| II `body.tex:1996`：`𝒰-A-\mbox{module}` | 模范畴的名称，邻文明确写 $A$-模及自由模；属数学类别记号。 |
| I `06-glossary-appendix.tex:324`：`cum grano salis` | 原文保留的拉丁短语，不是英文漏译。 |
| IV `part-9.tex:739,746,749` 与 `index-tome-I.tex:201`：`Karfiness`；`Topfin`、`Topan`、`Topanloc`、`Homtop`、`Morsite`、`Fl`、`Ob`、`res`、`tr` 等 | 所定义的范畴名、符号或算子，索引亦为符号索引；未将其翻译为普通语言。 |
| 全篇的 `ind-`、`pro-`、`fppf`、`fpqc`、`ét`、`Noether`、`Abel`，以及 `Čech`、`Cartan--Leray`、`Hochschild--Serre`、`de Rham`、`Hodge` 等 | 既有数学前缀、缩写或应保持原脚本的人名及人名术语。 |
| I 附录、II、III、IV §14 后、V、V bis、VI §9 后、VII 脚注、IX 末及序言脚注中的外文书刊名 | 包括 *Theory of Categories*、*General Topology*、*Homotopy Theory and Calculus of Fractions*、*Higher Topos Theory*、*Algebraic cycles and the Weil conjectures* 等，均为引文或书刊标题；按要求排除。 |
| `front-prefaces.tex:208`：`May 1964` | 引文中的出版日期。属于可选的书目格式统一事项；若希望连书目日期一律中文，可作“1964 年 5 月”。不构成正文漏译。`Vol`、`No`、`Bd`、`p.` 等同属书目缩写。 |

扫描中出现的 `guide`、`north west`、`anchor`、`width`、`at` 等均是序言原生 TikZ 图的样式或布局参数；`source/...` 是注释中的源映射路径；`page112`、`terminology` 等是引用标识。已查看上下文，均非读者可见英文叙述。

## 末次复核文件快照

以下为四处修正已在共享文件中可见之后的内容快照。SHA256 用于固定本次语言扫描所对应的版本；后续协调者可能继续作术语、编译或版面修正。

| 文件（相对 `chapters/`） | 行数 | SHA256 |
| --- | ---: | --- |
| `I/01-sections-0-4.tex` | 855 | `afdb0d29106f76f62b98cc770e663cbbb3f75ebe4f1f10814661c1c282ba2ff7` |
| `I/02-sections-5-7.tex` | 1463 | `b559a597e8c8b72c641055d643fedf03487270f214a337da3cf06ce233d61a3c` |
| `I/03-section-8a.tex` | 1331 | `6d50163997cd6f4ad08759fd57bfa21d318f1b48a438eafb02f150c36603bac9` |
| `I/04-section-8b.tex` | 1321 | `6bc38e69a4c5d111682d2d0e75786f56f906674b45c6079ab96e36538f9722c6` |
| `I/05-section-9.tex` | 875 | `a7a9ec11c9ab26dc46c30173da085abfc46b9c1d6e2dab3d03bb46101bc98e0c` |
| `I/06-glossary-appendix.tex` | 826 | `69b34d6384b690ce86a245ced61f772814f1ed2ee2d7a688ad31e23f9a645d02` |
| `I/expose-I.tex` | 19 | `f4773e80caab4f9091e8d9b590fb772a445646428c93d07ea2bac12d570d30db` |
| `II/body.tex` | 2051 | `a290e9bcf42c5f59df5c07415847c691cd4213ad02666d47d6b4ee208df7ad1a` |
| `II/expose-II.tex` | 7 | `18dbdbeb18c2f6b0ce90e88f1a17559549b34e621c63e5fa8948aed3ff71747b` |
| `III/body.tex` | 1255 | `c8b2e1ddfdbd8cfd59e5e844952dcb42bcc934ccba339ab18ceeec96b5a2f499` |
| `III/expose-III.tex` | 7 | `b7ae5a3bda8c1d1e290fd92352c352719623c266b57ffa1a31e1e5671291faad` |
| `IV/body.tex` | 2337 | `26e3bf1ac3aca30cfe6cf2c3a410598516655063580be7e8c55e669699a01f66` |
| `IV/expose-IV.tex` | 9 | `10ce6895c3e67e9ae8019f95e941eed0aaccbb079eb0d34073187215864a7af5` |
| `IV/part-10-14.tex` | 1049 | `1d65c34d368bbed67a00c34061b2df89fe3ad020cebd4b8ce76a3140305d9eca` |
| `IV/part-9.tex` | 2934 | `c2eb5cf71f8e87857a3652764572b9b24ffcc16454e4e9e2bc1204b8b51c1d3a` |
| `IX/body.tex` | 1673 | `2a4297f5515f44b3fc36259c7053cd52427c82b91c7cdac08f82695908adaa1c` |
| `IX/expose-IX.tex` | 7 | `81ab389b48e8b323d01dc2aac2168685c35af400a634b1632cbb409903f12977` |
| `V/body.tex` | 2791 | `1b3981cbcea70b2b5a32b57c22f6886f12eb8a3fbf3ba13b09e60cabdb40c6ec` |
| `V/expose-V.tex` | 8 | `bf838ca538cd6a5c80665de35098e9c1572db128be22b620152b69eb38f6bde1` |
| `VI/expose-VI.tex` | 7 | `b3b5d485044485820488797fbb043b79a0a0e2500c84658d7326581e4c506de6` |
| `VI/part-0-5.tex` | 3528 | `0eac099ac63e06e29d28b7d64a5ce808e5413ad8eff630a82df84e2650818624` |
| `VI/part-6-7.tex` | 1734 | `5bf52059f62f1ca989f6c0102381879a573323b341677879df3e36cf63bab8f4` |
| `VI/part-8-9.tex` | 2169 | `9697d49f2ce5f2bd32228fbe88c919921f2738011f80bceaec6058e47a5ae288` |
| `VII/body.tex` | 532 | `3b0266a926ac083c9c4513af21da7fb8b4bd96abf2e224b7430ba47dae639fae` |
| `VII/expose-VII.tex` | 7 | `f3be477ce6bca8181c5893db0292e876fbcae604aeb02c3c55aa076e8b936ca7` |
| `VIII/body.tex` | 1829 | `fbf2a666a3283cdcca3105adca03404caf21974ca03ec665f510cdd0564d1ee6` |
| `VIII/expose-VIII.tex` | 7 | `f028080d7e86f42676887592b06b2341eab989d33506bfdeb25f2f177ba77bfc` |
| `Vbis/body.tex` | 3508 | `fef282f9e57b72260c18752c80c90fd9b4ca861f535e796c1ee595004de5d0bc` |
| `Vbis/expose-Vbis.tex` | 12 | `5a423e2645bd9342d4b022462ff9ace20674e3879996df2e9cf163c086cc999f` |
| `front-prefaces.tex` | 289 | `df278c2b9c5dab10ad734ab8ca0f189404d4bd31c2c4c14bab635e63626a26c5` |
| `index-tome-I.tex` | 236 | `b36a990fc0cfc1f8fb5ab1912aa69b3f16a4180e2591e39016876a2d47a3ef4a` |
| `index-tome-II.tex` | 266 | `f2b739c3634f8cb3e2d869874356582b6342adc281a8fa0b1956912c98a6b022` |
