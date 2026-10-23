# VII-B70–95 独立逐段审校（含 81b）

审校日期：2026-10-23 UTC。只读核对其他译者正文，未改动任何章节文件。主线程统一裁定与修正。

## 实际覆盖与方法

已逐段对照 70–95 及 81b 共 27 个完整组件（源文件共 3567 行），不是抽样。70、71 为旧稿复核；其余为本轮新译。正文、定义中的条件/量词/否定、定理陈述、全部证明、所有脚注与源注均已阅读；95 的 34 条书目全部逐条核对中文题名、保留的原题、作者、刊物/出版社、年份、卷期页码。对换位排列的公式（77、87）另读完整上下文，语义对应无误。

逐文件自动比对：所有行内数学片段、引用/目标键、环境开始/结束清单保持相同；脚注、图形输入和公式 tag 数量保持相同；显示公式忽略 `\text{...}` 中已译文字后数学内容保持相同（用多重集合比较，容许语序导致的公式换位）。27 件合计 34 个脚注、13 个原生图形输入，图形目标全部存在。正文中未发现英语整句漏译；图形没有新增独立图题。英文原题、人名、刊名、出版社名和 TeX 标识符按要求保留。

## 明确的局部问题（供主线程统一处理）

1. **95，[Il85] 书名词义误译**：`95_expose_VIIB_bibliography_en-zh.tex:70` 将 *pinceaux arithmétiques* 译作“算术铅笔”。这里是数学意义的线系/束，不是文具。建议主线程核定为“算术线系讨论班：Mordell 猜想”或项目采用的同义数学译法，保留 `〔Séminaire sur les pinceaux arithmétiques: la conjecture de Mordell〕` 原题及全部出版数据。

2. **95，[Di55] 中文题名条件不完整**：同文件第 52 行中文题名写“特征 p 的域上的……”，原题明确为 `caractéristique \(p>0\)`。原题括注中的公式仍完整，故不是公式丢失；为使中文题名自身也完整，建议写“特征 \(p>0\) 的域上的 Lie 群与 Lie 超代数”。不建议在此次审校中擅自更改“超代数”的项目译法。

3. **93，非书名英文术语重复保留**：`93_expose_VIIB_sections53_54_stationary_algebras_corollary_en-zh.tex:26,34,42` 的脚注 165、166 已译成“定常/稳定”，但另加了 `（stationary）`、`（stable）`，共 4 处。并非未理解术语；若严格执行本轮“除原题及人名等识别性原文外全文中文”，可删这 4 处英文括注。中译区分本身正确，不能把 stationary 与 stable 合并。

未发现其他明确的内容漏译、否定反转、量词/假设丢失、公式变量丢失或数学结论误译。未改 radicial 的暂定译法；本范围未出现需要处理的 good/very good 译法。

## 源数学与源重建疑点（不是本轮译错，不自动修正文）

- **71，特征 2 的测试代数**：源与译文在末段均取 `C=k[a]/(a^3)`，并评价 `chi_C(x tensor a)`；但该自然变换定义域为 `L(C) tensor sqrt[p]{0_C}`。当 `p=2` 时，这个代数中 `a^2` 非零，因此所代入的 `a` 不属于 `sqrt[2]{0_C}`。原命题涵盖全部 `p>0`，这一步对 `p=2` 的适用性需要回查法文原文或已有勘误。译文忠实保留了源陈述，不应通过静默加上 `p>2` 修补。

- **78 脚注 148、80 脚注 149、81 脚注 151 的“形式完备化”称呼**：英文本将 `Gr_J(A)` 对应的形式群称为“G 沿 H 的形式完备化”，并以此描述半直积分解。由于这里实际使用的是相伴分次代数，需核对法文术语究竟指形式法锥/法群还是通常的沿闭子概形完备化。译文逐字忠实于英文本，不能将其归为译文遗漏或自行替换对象。

- **继承自源的跨报告引用键**：71 第 17、66 行与 72 第 50 行的本节 `4.3.1` 引用键均为 `sga3:VIIA:4.3.1`；源也如此，按上下文疑应指 VII-B 4.3.1。71 源注另用 `sga3:VIIA:4.2.1` 指本报告的群状元素集合。此处仅记录，遵循保持引用键的要求未改。建议纳入主线程已有全书链接核验。

其他源注已完整译出，且源注中保留的印本公式与英文本所用校正公式均保留；本审校未重判这些源注的数学裁决。

## 覆盖清单与审校快照

以下 SHA-256 仅固定本次读到的译文快照，后续主线程修正会使其改变。

|组件|源行数|译文文件|SHA-256|
|---|---:|---|---|
|70|117|`70_expose_VIIB_section431_group_like_elements_en-zh.tex`|`457f63be4ab9acce5ba246262ced7b2ddc3a24c519f46dba0f10da086bbfc657`|
|71|187|`71_expose_VIIB_section432_no_functorial_campbell_hausdorff_en-zh.tex`|`3af3ff94f2c99e38627181c8ecc3bc5e7159b4e0f89e798456df5a858c192662`|
|72|134|`72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex`|`3f585de53262be51c8bf7efdb0d81fea3126dfad533db50aadc9f07293cfa81f`|
|73|95|`73_expose_VIIB_section442_finite_height_filtration_en-zh.tex`|`3e56c4c327435e9cad83b1fa6610d22ef06053df4aeb2218571745b70378d963`|
|74|257|`74_expose_VIIB_section5_and_50_homogeneous_spaces_hopf_en-zh.tex`|`d191822733748b1cbd8612ed225bdfc623306bbaaf4e329bf216fe2ae9894074`|
|75|157|`75_expose_VIIB_section51_quotient_criterion_en-zh.tex`|`1836b713f97a6a4e58625112d026dc05a035e9471f784c4b8d5ecd50abd7644b`|
|76|98|`76_expose_VIIB_section511_cogroups_of_pairs_en-zh.tex`|`cc4e0cb14ff4a8f52f89d154f95fbd445680c96599c91f30bff84acb4622b62d`|
|77|134|`77_expose_VIIB_section512_graded_profinite_algebras_lemma_en-zh.tex`|`aa993721a8222c0324bf04af20d8b586c0ff7d263ef198a928c412acbc405b7a`|
|78|158|`78_expose_VIIB_section512_filtration_lemma_proof_corollary_en-zh.tex`|`d5fc82af0c3ed7d48f313e4d6b8db13ae5c1887425e3b314b60be3ec3df37f7d`|
|79|109|`79_expose_VIIB_section513_graded_cogroup_splitting_en-zh.tex`|`6e457ac2445dca78972951ae3622d910a4383d40ebebb430a2b23d6649149173`|
|80|128|`80_expose_VIIB_section514_graded_generation_en-zh.tex`|`8e7cb54f4514a8cc82a544fbf40e6a08673bf048b5c326ceec3c172b1e4c62de`|
|81|209|`81_expose_VIIB_section514_proposition51_completion_en-zh.tex`|`39154ffa33c82f4348572ff9dd1a61c24e1868d4ba978afcb4e673101cc94a45`|
|81b|98|`81b_expose_VIIB_section515_filtered_groups_lemma_en-zh.tex`|`163f35ff115bfc54c681bb89c33d1f817ad92035c2a284f0f3471794ed8954da`|
|82|138|`82_expose_VIIB_section52_height_theorem_en-zh.tex`|`259b54b03d22adc42a028404225be379c31904a26d83087f2ce419cb037443b1`|
|83|98|`83_expose_VIIB_section521_reduction_proposition_en-zh.tex`|`1880f3f8b182d364ae402f9f347ecee6f1a33b5c2d84c94ab66490a592bee7d2`|
|84|111|`84_expose_VIIB_section521A_pseudobasis_splittings_en-zh.tex`|`5830f8ff25dde4e828b48fdb741796e3fd061097488634b0734f8a217730e547`|
|85|137|`85_expose_VIIB_section521B_split_filtered_spaces_en-zh.tex`|`9a745b099564f426c00ac0d7f119cdc40d53c03ad4e56bdd154c186232bfcf32`|
|86|65|`86_expose_VIIB_section521C_stationary_filtration_en-zh.tex`|`dafa39b25b587d55a5e281d2959f33824ab7a4a6ce9ae568cddbdb11993e5b93`|
|87|55|`87_expose_VIIB_section522_height_one_case_en-zh.tex`|`1352e437d6e5330deb4c65b37750169b2286f2b1b3d13c5412a799778b4a2e86`|
|88|151|`88_expose_VIIB_section523_finite_height_induction_en-zh.tex`|`25a0d6dd30f573e9731778b7d5c27db9e007dcd532ea22db278cb874abef649e`|
|89|101|`89_expose_VIIB_section524_frobenius_twist_induction_en-zh.tex`|`0268b57308c908214c57f67b911857ac6103ab4e9f31be3dee3f31e62ecb2938`|
|90|99|`90_expose_VIIB_remark524A_finite_height_filtration_en-zh.tex`|`4bc0c63b07073ea7211ae34c4693b5b4fd9e12cd183f409991b2ea880cebf2dd`|
|91|151|`91_expose_VIIB_section525_infinite_height_limit_en-zh.tex`|`56610feeab65c3ed0af01d12b144c91af5f6dc259a700a29e789da6fc69c18af`|
|92|78|`92_expose_VIIB_section526_infinite_completed_tensor_product_en-zh.tex`|`b53e8d6e4f450fd6cc5dbd7be1a46e557a8ad8b693c614bb206326c0070793c1`|
|93|155|`93_expose_VIIB_sections53_54_stationary_algebras_corollary_en-zh.tex`|`18b37f283b5269c45101ddca0bece62695b2e79e63525a64e2736c4f25f7af42`|
|94|183|`94_expose_VIIB_section55_complements_en-zh.tex`|`e1e2007361fed5d73d50c77d98c9c4cbff859ee44ea08fafd35d99349f3944ad`|
|95|164|`95_expose_VIIB_bibliography_en-zh.tex`|`1eec727553c9ca912dc5797774bf091b3941acb816e53d907e5ec36679654f4f`|


## 限制

本次验证依据指定英文可构建重建源与当前中文组件；未逐页重新对照法文 PDF，未浏览外部数学文献，也未重新证明所有定理。原生图代码保持与源一致，验证了输入文件存在；未进行原生图逐像素视觉验收。未编译整书，PDF 级排版及交叉引用最终落点由主线程集成核验。没有修改章节、提交、运行付费 API 或新建子代理。
