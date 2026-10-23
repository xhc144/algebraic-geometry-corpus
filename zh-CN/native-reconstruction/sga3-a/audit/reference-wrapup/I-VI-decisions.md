# INTRO 至 VI-B 已报告引用错链收尾决策

此表只定位既有 SOURCE_ISSUES 与历史报告的错链，供主线程统一编辑；没有修改正文、main 或 preamble。JSON 中 `items` 每次调用分别记录文件、行、旧键、完整第二参数、上下文、决策与证据；同键不同语义不作全局替换。

决策统计：{'replace_key': 37, 'external': 39, 'retain': 21, 'pending': 3}。另有两处实际命令为 hyperref，及一处没有链接的源文疑点，单独列出。

## 逐次调用

| 文件:行 | 原键 | 完整可见第二参数 | 决策/新键 | 理由 |
|---|---|---|---|---|
| chapters/00_introduction-zh.tex:23 | `sga3:intro:section:5` | `第~5~节` | replace_key → `sec:sga3-VIB-5` | 编者告示明确 VI-B 第5节；当前旧键为导言§5。 |
| chapters/03_expose_I_s18_s22_pp010_015-zh.tex:138 | `sga3:i:proposition:1:4:1` | `(1)` | replace_key → `sga3:i:subsection:1-8:equation:1` | I§1.8 紧前已有带 tag(1)/(2)/(3) 的 equation 标签，结合三式推导纤维积。 |
| chapters/03_expose_I_s18_s22_pp010_015-zh.tex:138 | `sga3:i:section:2` | `(2)` | replace_key → `sga3:i:subsection:1-8:equation:2` | I§1.8 紧前已有带 tag(1)/(2)/(3) 的 equation 标签，结合三式推导纤维积。 |
| chapters/03_expose_I_s18_s22_pp010_015-zh.tex:139 | `sga3:i:section:3` | `(3)` | replace_key → `sga3:i:subsection:1-8:equation:3` | I§1.8 紧前已有带 tag(1)/(2)/(3) 的 equation 标签，结合三式推导纤维积。 |
| chapters/06_expose_I_s41_s43_basic_scheme_groups-zh.tex:211 | `sga3:i:subsection:1-3` | `1.3` | replace_key → `sga3:ii:remark:1-3` | I§4.3.2 文字明确 II,1.3；II注1.3讨论模值Y-函子。 |
| chapters/07_expose_I_s44_s47_scheme_groups-zh.tex:499 | `sga3:ii:section:2` | `第 2 节` | external | 脚注明引 [DG], II, §2,1.1；两段号码均属外部[DG]，不是SGA3 II§2或I1.1。 |
| chapters/07_expose_I_s44_s47_scheme_groups-zh.tex:500 | `sga3:i:subsection:1-1` | `1.1` | external | 脚注明引 [DG], II, §2,1.1；两段号码均属外部[DG]，不是SGA3 II§2或I1.1。 |
| chapters/07_expose_I_s44_s47_scheme_groups-zh.tex:669 | `sga3:i:subsection:1-3` | `第 1.3 节` | external | 脚注明引 [Se68] §1.3。 |
| chapters/08_expose_I_s5_group_cohomology-zh.tex:435 | `sga3:i:subsection:2-3` | `2.3` | external | 同上承接前句[Gr57]关于卫星函子/导出函子的文献引用，指该外部文献2.3。 |
| chapters/08_expose_I_s5_group_cohomology-zh.tex:515 | `sga3:i:subsection:4-2` | `4.2` | external | 编者脚注明引[Ja03]第一部分4.2。 |
| chapters/08_expose_I_s5_group_cohomology-zh.tex:517 | `sga3:i:subsection:2-1` | `2.1` | external | 同上承接[Ja03]，指该书2.1。 |
| chapters/12_expose_II_s41_s44_lie_algebras-zh.tex:848 | `sga3:ii:section:6` | `(6)` | replace_key → `sga3:ii:subsection:4-3-2:equation:6` | 本段明确指4.3.2中局部式号，现有对应tag及equation标签；不能跳本篇§5/§6。 |
| chapters/12_expose_II_s41_s44_lie_algebras-zh.tex:974 | `sga3:ii:section:5` | `(5)` | replace_key → `sga3:ii:subsection:4-3-2:equation:5` | 本段明确指4.3.2中局部式号，现有对应tag及equation标签；不能跳本篇§5/§6。 |
| chapters/19_expose_III_s07bis_s010_group_actions-zh.tex:105 | `sga3:iii:theorem:3-5` | `定理~3.5` | external | 原句明确[DG70] II.4定理3.5的证明，属外部书目。 |
| chapters/19_expose_III_s07bis_s010_group_actions-zh.tex:113 | `sga3:iii:corollary:3-10` | `引理~3.10` | replace_key → `sga3:ii:lemma:3-10` | 紧前文字明确“第II篇的引理3.10”；II引理3.10为H对象中H对象的Eckmann–Hilton结论。 |
| chapters/23_expose_III_s2_infinitesimal_group_morphisms-zh.tex:472 | `sga3:iii:theorem:2-1` | `2.1` | replace_key → `sga3:ii:definition:2-1` | 注2.10在对偶数概形I_{S0}后明写II,2.1；II定义2.1定义I_S(M)。同文件其它III定理2.1引用不动。 |
| chapters/24_expose_III_s3_infinitesimal_group_structures-zh.tex:250 | `sga3:iii:proposition:3-3` | `3.3` | retain | 邻近3.3本身的调用确为辅助命题，不能随错误的(i)/(ii)批量改。 |
| chapters/24_expose_III_s3_infinitesimal_group_structures-zh.tex:251 | `sga3:iii:proposition:3-3:item:i` | `(i)` | replace_key → `sga3:iii:theorem:3-5:item:i` | 处于定理3.5证明结尾，刚证明本定理(i)/(ii)；3.3为引用的辅助命题。 |
| chapters/24_expose_III_s3_infinitesimal_group_structures-zh.tex:252 | `sga3:iii:proposition:3-3:item:ii` | `(ii)` | replace_key → `sga3:iii:theorem:3-5:item:ii` | 处于定理3.5证明结尾，刚证明本定理(i)/(ii)；3.3为引用的辅助命题。 |
| chapters/26_expose_III_s450_s47_lci_koszul-zh.tex:367 | `sga3:iii:proposition:4-6-5:item:a` | `(a)` | replace_key → `sga3:iii:proposition:4-5:item:a` | 4.6.5陈述说4.5(i)中的条件(a)/(b)成立；条件定义在4.5(i)的内层枚举，不是自指4.6.5的结论。 |
| chapters/26_expose_III_s450_s47_lci_koszul-zh.tex:372 | `sga3:iii:proposition:4-6-5:item:b` | `(b)` | replace_key → `sga3:iii:proposition:4-5:item:b` | 4.6.5陈述说4.5(i)中的条件(a)/(b)成立；条件定义在4.5(i)的内层枚举，不是自指4.6.5的结论。 |
| chapters/26_expose_III_s450_s47_lci_koszul-zh.tex:377 | `sga3:iii:proposition:4-6-5:item:a` | `(a)` | retain | 证明段开头(a)确指本命题4.6.5(a)，应保留，不能按旧键全文件替换。 |
| chapters/29_expose_III_s417_s422_subgroup_obstruction-zh.tex:323 | `sga3:iii:proposition:4-8:item:iii` | `4.8(iii)` | pending | SOURCE_ISSUES仅提出原文4.8(iii)可能应为(ii)，可见文字与当前键一致；涉及原文编号疑点，不能只改链接并保持矛盾的显示文字。 |
| chapters/30_expose_III_s423_s430_conjugacy_coboundaries-zh.tex:175 | `sga3:iii:paragraph:4-20:equation:5` | `(5)` | replace_key → `sga3:iii:paragraph:4-38:item:5` | 脚注说将在4.38(4)及(5)中用到；(5)是4.38的第5项，不是4.20的式(5)，已有4.38:item:5锚点。 |
| chapters/31_expose_III_s431_s4351_conjugacy_smooth-zh.tex:175 | `sga3:ii:definition:4-10` | `4.10` | external | 原句明确SGA1, II,4.10；应取消错内部链接，保留显示4.10。 |
| chapters/IV/03_expose_IV_s3-zh.tex:728 | `sga3:iv:para:3:4:4` | `3.4.4` | pending | 既有报告认为3.5.2(i)⇒(ii)应引基变换命题3.4.5，但当前显示3.4.4本身即源文；本轮不得改显示编号，故不擅自换成与显示矛盾的键。 |
| chapters/IV/19_expose_IV_s47-zh.tex:51 | `sga3:iv:proposition:5:3:1` | `5.3.1` | replace_key → `par:sga3-VIA-5.3.1` | 开头脚注明确另见VI_A,5.3.1；正确目标为VI-A的对应段。 |
| chapters/IV/20_expose_IV_s5-zh.tex:332 | `sga3:iv:proposition:5:2:8` | `前一命题` | replace_key → `sga3:iv:proposition:5:2:7` | 在5.2.8证明中“前一命题的对应”指5.2.7的子群对应，非自指5.2.8。 |
| chapters/V/20_expose_V_localp28_31_sections7_9_en-zh.tex:244 | `sga3:viii:corollary:4:4` | `4.4` | external | 上下文明引SGA1 VIII的下降结果；本书SGA3 VIII同号条目不是目标。 |
| chapters/V/20_expose_V_localp28_31_sections7_9_en-zh.tex:255 | `sga3:viii:examples:6:5` | `6.5` | external | 上下文明引SGA1 VIII的下降结果；本书SGA3 VIII同号条目不是目标。 |
| chapters/V/20_expose_V_localp28_31_sections7_9_en-zh.tex:259 | `sga3:viii:corollary:5:7` | `5.7` | external | 上下文明引SGA1 VIII的下降结果；本书SGA3 VIII同号条目不是目标。 |
| chapters/VI-A/02_expose_VIA_examples132_through_cor241_en-zh.tex:320 | `prop:sga3-VIB-2.1` | `2.1` | replace_key → `par:sga3-VIA-2.1` | 本篇上下文沿用G′、G⁰的记号及约化群结构，分别由紧前本篇2.1/2.2定义和讨论，并无VI-B跨篇指示。 |
| chapters/VI-A/02_expose_VIA_examples132_through_cor241_en-zh.tex:402 | `prop:sga3-VIB-2.2` | `2.2` | replace_key → `par:sga3-VIA-2.2` | 本篇上下文沿用G′、G⁰的记号及约化群结构，分别由紧前本篇2.1/2.2定义和讨论，并无VI-B跨篇指示。 |
| chapters/VI-A/06_expose_VIA_theorem265_through_remark267_loop2_r1_en-zh.tex:152 | `prop:sga3-VIA-2.6.1:item:iii` | `(iii)` | replace_key → `prop:sga3-VIA-2.6.6:item:iii` | 本段正在证明2.6.6(ii),(iii)第二断言；紧前明确已证明其第一断言，故“先证明(iii)第二断言”仍指2.6.6。 |
| chapters/VI-A/09_expose_VIA_section322_induction_en-zh.tex:19 | `par:sga3-VIB-8.1` | `定理~V.8.1` | replace_key → `thm:sga3-V-8.1` | 显示明确“定理V.8.1”，V现有定理8.1给群胚平坦取商。 |
| chapters/VI-A/12_expose_VIA_section33_theorems_corollary_loop2_r1_en-zh.tex:18 | `sec:sga3-VIA-4` | `定理~4` | external | 脚注明引Anantharaman [An73]定理4；不是本篇第4节。 |
| chapters/VI-A/12_expose_VIA_section33_theorems_corollary_loop2_r1_en-zh.tex:21 | `prop:sga3-VIB-7.1` | `7.1` | external | 前后两处同指[DG70] III.2,7.1，属外部文献；两次调用均应拆除错内部链接。 |
| chapters/VI-A/12_expose_VIA_section33_theorems_corollary_loop2_r1_en-zh.tex:39 | `prop:sga3-VIB-7.1` | `7.1` | external | 前后两处同指[DG70] III.2,7.1，属外部文献；两次调用均应拆除错内部链接。 |
| chapters/VI-A/17_expose_VIA_par45_46_base_change_en-zh.tex:21 | `par:sga3-VIA-4.6` | `4.6` | external | 原句明确SGA1 VIII (3.1,4.6,5.4)，属跨书外引。 |
| chapters/VI-A/17_expose_VIA_par45_46_base_change_en-zh.tex:34 | `lem:sga3-VIA-6.1` | `引理~6.1` | replace_key → `lem:sga3-V-6.1` | 文字明确本节对第V篇引理6.1及§9(a)作说明。 |
| chapters/VI-A/21_expose_VIA_par53_correspondences_en-zh.tex:16 | `sga3:iv:proposition:5:2:7` | `第~IV~篇 5.2.7` | retain | 同句第一个IV5.2.7明确正确，保留。 |
| chapters/VI-A/21_expose_VIA_par53_correspondences_en-zh.tex:17 | `par:sga3-VIA-5.3.1` | `5.3.1` | replace_key → `sga3:iv:proposition:5:3:1` | 段首说明回顾第IV篇；“IV5.2.7及5.3.1的陈述”应同属IV，VI-A当前5.3.1是转述本身。 |
| chapters/VI-A/22_expose_VIA_par54_abelian_categories_loop2_r1_en-zh.tex:18 | `prop:sga3-VIB-5.2` | `5.2` | replace_key → `par:sga3-VIA-5.2` | 商群N\G的存在及结构沿用本篇3.3.2和5.2；本篇5.2紧前讨论子群商结构，VIB5.2是分离性命题。 |
| chapters/VI-A/22_expose_VIA_par54_abelian_categories_loop2_r1_en-zh.tex:140 | `prop:sga3-VIB-7.4` | `7.4` | external | 括号明确[DG70] §III.3,7.4，是外部引文。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:10 | `prop:sga3-V-3.1` | `3.1` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:11 | `thm:sga3-VIA-3.2` | `3.2` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:12 | `sga3:VIA:0.1` | `0.1` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:36 | `par:sga3-VIA-3.3` | `3.3` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:97 | `prop:sga3-VIB-2.7` | `2.7` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:100 | `prop:sga3-VIB-2.7:item:i` | `(i)` | replace_key → `cor:sga3-VIA-6.6:item:i` | 这是本段推论6.6的证明，结尾“这就证明(i)，断言(ii)…”指本推论两项，与上一句外部[BAC]§2.7无关。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:101 | `prop:sga3-VIB-2.7:item:ii` | `(ii)` | replace_key → `cor:sga3-VIA-6.6:item:ii` | 这是本段推论6.6的证明，结尾“这就证明(i)，断言(ii)…”指本推论两项，与上一句外部[BAC]§2.7无关。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:182 | `par:sga3-VIA-1.1` | `定理~1.1` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:194 | `prop:sga3-VIB-3.7` | `3.7` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-B/37_expose_VIB_prop311_section4_prop41_en-zh.tex:11 | `par:sga3-VIB-5.6` | `5.6` | replace_key → `par:sga3-VIA-5.6` | 脚注明写比较VI_A,5.6；VI-A5.6讨论同样的平坦性/单位连通分支。 |
| chapters/VI-B/37_expose_VIB_prop311_section4_prop41_en-zh.tex:20 | `cor:sga3-VIB-1.3.2` | `1.3.2` | retain | 两次1.3.2确为本篇连通分支像的推论；与VI-A5.6误链不同。 |
| chapters/VI-B/37_expose_VIB_prop311_section4_prop41_en-zh.tex:26 | `cor:sga3-VIB-1.3.2` | `1.3.2` | retain | 两次1.3.2确为本篇连通分支像的推论；与VI-A5.6误链不同。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:51 | `concl:sga3-VIB-4.2-iii` | `(iii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:58 | `prop:sga3-VIB-4.2:item:i` | `(i)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:60 | `prop:sga3-VIB-4.2:item:i` | `(i)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:61 | `prop:sga3-VIB-4.2:item:ii` | `(ii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:87 | `prop:sga3-VIB-4.1:item:i` | `(i)` | replace_key → `prop:sga3-VIB-4.2:item:i` | 命题4.2内部证明(i)⇒(ii)、(iii)⇒(i)，对应4.2自己的三条件；4.1是辅助半连续性命题。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:88 | `prop:sga3-VIB-4.1:item:ii` | `(ii)` | replace_key → `prop:sga3-VIB-4.2:item:ii` | 命题4.2内部证明(i)⇒(ii)、(iii)⇒(i)，对应4.2自己的三条件；4.1是辅助半连续性命题。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:90 | `concl:sga3-VIB-4.2-iii` | `(iii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:91 | `prop:sga3-VIB-4.1:item:i` | `(i)` | replace_key → `prop:sga3-VIB-4.2:item:i` | 命题4.2内部证明(i)⇒(ii)、(iii)⇒(i)，对应4.2自己的三条件；4.1是辅助半连续性命题。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:92 | `prop:sga3-VIB-4.2:item:ii` | `(ii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:93 | `concl:sga3-VIB-4.2-iii` | `(iii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:128 | `prop:sga3-VIB-4.2:item:ii` | `(ii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:137 | `prop:sga3-VIB-4.2:item:ii` | `(ii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:138 | `concl:sga3-VIB-4.2-iii` | `(iii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:141 | `prop:sga3-VIB-4.2:item:ii` | `(ii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:142 | `prop:sga3-VIB-4.2:item:i` | `(i)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:143 | `prop:sga3-VIB-4.2:item:ii` | `(ii)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:144 | `prop:sga3-VIB-4.2:item:i` | `(i)` | retain | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/39_expose_VIB_cor43_cor44_en-zh.tex:82 | `cor:sga3-VIB-1.3.1` | `1.3.1` | retain | 单独的1.3.1确用于纤维平滑，当前正确；只改随后同旧编号衍生的(ii)错链。 |
| chapters/VI-B/39_expose_VIB_cor43_cor44_en-zh.tex:85 | `cor:sga3-VIB-1.3.1:item:ii` | `(ii)` | replace_key → `cor:sga3-VIB-4.4:item:ii` | 4.4证明段明确证明本推论(ii)⇒(iv)；上一句1.3.1为辅助结论。 |
| chapters/VI-B/39_expose_VIB_cor43_cor44_en-zh.tex:114 | `prop:sga3-VIB-4.2:item:ii` | `(ii)` | replace_key → `cor:sga3-VIB-4.4:item:ii` | 本段末要在S约化时由本推论(ii)–(iv)推出G⁰平滑；不是4.2(ii)。 |
| chapters/VI-B/39_expose_VIB_cor43_cor44_en-zh.tex:114 | `thm:sga3-VIB-3.10:item:iv` | `(iv)` | replace_key → `cor:sga3-VIB-4.4:item:iv` | 同一范围(ii)–(iv)指本推论4.4条件(iv)，3.10仅前文说明构造方法。 |
| chapters/VI-B/40_expose_VIB_section5_through_rem541_loop2_r1_en-zh.tex:124 | `concl:sga3-VIA-2.5.4-ii` | `(ii)` | replace_key → `cor:sga3-VIB-5.4:item:ii` | 本段是推论5.4证明(ii)即拟紧性；上句VI-A2.5.4只是纤维不可约性的辅助引用。 |
| chapters/VI-B/41_expose_VIB_cor55_through_lemma560_loop2_r1_en-zh.tex:17 | `prop:sga3-VIB-2.5` | `2.5` | external | 脚注明引[Ray70a] VI,2.5，属外部文献。 |
| chapters/VI-B/53_expose_VIB_theorem623_en-zh.tex:31 | `concl:sga3-VIB-6.2.3-i` | `(ii)` | replace_key → `concl:sga3-VIB-6.2.3-ii` | 两次显示(ii)分别在编者注及证明第二项，已有本定理(ii)标签，旧键落(i)。 |
| chapters/VI-B/53_expose_VIB_theorem623_en-zh.tex:128 | `concl:sga3-VIB-6.2.3-i` | `(ii)` | replace_key → `concl:sga3-VIB-6.2.3-ii` | 两次显示(ii)分别在编者注及证明第二项，已有本定理(ii)标签，旧键落(i)。 |
| chapters/VI-B/56_expose_VIB_rem63_through_def65_en-zh.tex:137 | `prop:sga3-VIB-6.2` | `6.2` | pending | 主键确指命题6.2，但visible参数仅6.2，后接(iv)在宏外；既有疑点是原文6.2无(iv)，不能猜应改哪一条或仅换主键。 |
| chapters/VI-B/56_expose_VIB_rem63_through_def65_en-zh.tex:152 | `cor:sga3-VIB-1.4.2:item:ii` | `(ii)` | replace_key → `def:sga3-VIB-6.5:item:ii` | 定义6.5后的N.B.说上述(ii)的闭浸入假设满足；1.4.2为提供该事实的辅助推论，不是被满足的假设。 |
| chapters/VI-B/61_expose_VIB_def66_through_par69_en-zh.tex:71 | `cor:sga3-VIA-3.3.3` | `3.3.3` | external | 原句明引[RG71] I,3.3.3定义纯概形，属外部。 |
| chapters/VI-B/64_expose_VIB_def722_through_cor73_en-zh.tex:298 | `concl:sga3-VIB-7.3-iv` | `(v)` | replace_key → `concl:sga3-VIB-7.3-v` | 证明“最后(v)”指本推论7.3(v)，已有正确标签；旧键落(iv)。 |
| chapters/VI-B/82_expose_VIB_section11_through_prop1131_loop2_r1_en-zh.tex:255 | `sga3:VIIB:3.2:prop` | `3.2` | external | 编者注[Ray70a] VII,3.2是外部文献第VII章，不是SGA3 VII-B。 |
| chapters/VI-B/84_expose_VIB_def1180_through_cor1110_loop2_r1_en-zh.tex:322 | `lem:sga3-VIA-2.5.1` | `2.5.1` | external | 正文和注116明引[RG71] II,2.5.1/2.5.2，及[Gr73]对该外部引文的勘误；不是VI-A的同号引理。 |
| chapters/VI-B/84_expose_VIB_def1180_through_cor1110_loop2_r1_en-zh.tex:323 | `lem:sga3-VIA-2.5.1` | `2.5.1` | external | 正文和注116明引[RG71] II,2.5.1/2.5.2，及[Gr73]对该外部引文的勘误；不是VI-A的同号引理。 |
| chapters/VI-B/84_expose_VIB_def1180_through_cor1110_loop2_r1_en-zh.tex:323 | `prop:sga3-VIA-2.5.2` | `2.5.2` | external | 正文和注116明引[RG71] II,2.5.1/2.5.2，及[Gr73]对该外部引文的勘误；不是VI-A的同号引理。 |
| chapters/VI-B/85_expose_VIB_prop1110bis_through_rem11111_loop2_r1_en-zh.tex:21 | `lem:sga3-VIB-1.5` | `1.5` | external | 注119分别明引[Th87]1.4–1.5和[Kn71]III定理1.1，属外部。 |
| chapters/VI-B/85_expose_VIB_prop1110bis_through_rem11111_loop2_r1_en-zh.tex:21 | `par:sga3-VIB-1.1` | `1.1` | external | 注119分别明引[Th87]1.4–1.5和[Kn71]III定理1.1，属外部。 |
| chapters/VI-B/85_expose_VIB_prop1110bis_through_rem11111_loop2_r1_en-zh.tex:21 | `prop:sga3-VIB-1.4` | `1.4` | external | 注119分别明引[Th87]1.4–1.5和[Kn71]III定理1.1，属外部。 |
| chapters/VI-B/85_expose_VIB_prop1110bis_through_rem11111_loop2_r1_en-zh.tex:33 | `sga3:i:section:6` | `第 I 篇，第 6 节` | retain | 文字明写参见第I篇§6，解释G等变模，确为SGA3内部引用。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:220 | `prop:sga3-VIB-2.1` | `2.1` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:226 | `def:sga3-VIB-3.1` | `定理~3.1` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:323 | `def:sga3-VIB-3.1` | `定理~3.1` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:362 | `def:sga3-VIB-3.1` | `定理~3.1` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:362 | `prop:sga3-VIB-2.5` | `2.5` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:362 | `rem:sga3-VIB-3.2` | `推论~3.2` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:365 | `prop:sga3-VIB-2.5` | `2.5` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |


## 无现成锚点的精确插入建议

- chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:44：在本推论对应item的可见(i)/(ii)前加入唯一行内锚点；不改原编号。 建议 `\SGAInlineRefTarget{cor:sga3-VIA-6.6:item:i}`。原行 `\item[\textup{(i)}] 若 \(f\) 概形占优, 则它忠实平坦.`。
- chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:45：在本推论对应item的可见(i)/(ii)前加入唯一行内锚点；不改原编号。 建议 `\SGAInlineRefTarget{cor:sga3-VIA-6.6:item:ii}`。原行 `\item[\textup{(ii)}] 特别地, 若 \(H\) 仿射, 且态射`。
- chapters/VI-B/40_expose_VIB_section5_through_rem541_loop2_r1_en-zh.tex:99：在推论5.4的(ii)可见编号前加唯一行内锚点。 建议 `\SGAInlineRefTarget{cor:sga3-VIB-5.4:item:ii}`。原行 `\item[\textup{(ii)}] \emph{若 \(X\) 有一个在 \(S\) 上拟紧的开集`。
- chapters/VI-B/56_expose_VIB_rem63_through_def65_en-zh.tex:138：只在定义6.5的(ii)对应item（后文为连通正规化子定义）编号前加锚点。 建议 `\SGAInlineRefTarget{def:sga3-VIB-6.5:item:ii}`。原行 `\item[\textup{(ii)}]`。


## 非 SGARefLink 与普通文本

- chapters/VI-B/41_expose_VIB_cor55_through_lemma560_loop2_r1_en-zh.tex:23：`\hyperref[note:sga3-VIB-35]{注 35}`；replace_key → `note:sga3-VIA-35`。脚注明确VI_A中的编者注35；VIB注35是另一反例，与该处拟射影结果无关。
- chapters/VI-B/88_expose_VIB_rem11185_through_section12_end_loop2_r1_en-zh.tex:102：`\hyperref[thm:sga3-VIB-12.2-ii]{\textup{(ii)}}`；pending。原文显示(ii)，但用于N′不变性，既有报告认为应由(iii)特征性得到；这是源显示编号疑点，未获改文字授权，不能仅换键。
- chapters/V/02_expose_V_pp256_260_en-zh.tex:57：现文为普通文本，无SGARefLink或hyperref可修；篇号疑点不能通过改内部键解决。


## 已正常的情况与边界

- VI-B83的已见I篇定义/命题及本篇11.*调用没有发现所报告外部RG71/Th87/Kn71错链；这批外部错链实际位于82、84、85，不能把整个82–85全删。
- VI-B38已有4.2各项调用保留，仅3次4.1项键需改；VI-B39独立1.3.1调用保留。
- 决策external只取消这一次错误内部包装，完整保留visible_tex及相邻文献文字，不替换成书目条目链接冒充精确外部节号。


## 实际法文核验覆盖

本轮未打开任何法文 PDF 页面；不新增“法文逐页终校”覆盖。既有报告明确记录的法文局部核对如下。英文逐段对照与当前标签/上下文核验不计作法文终校。

| 历史物理页 | 印刷页 | 实际记录的事项 |
|---|---|---|
| 55 | 43 | I6.5.3 第三项转置t及Lambda/varphi；SOURCE_ISSUES明确记载 |
| 54 | 未明确记载 | I6.5.3反变箭头方向；SOURCE_ISSUES明确记载 |
| 未明确记载 | 未明确记载 | I6.6只写“旧法文同页”，不能推补精确页码 |

所用历史法文参照为1371页库内扫描本，非新版Polo–Gille各篇权威PDF。以上仅为局部核对，不能声称I–VI-B整页逐字终校或新版全文校勘完成。所有 pending 保留原文，未猜改显示文字或数学。

## 主线程最终有界补充

原清单的待核策略不构成修改授权限制。主线程按父任务要求仅对这7个已列疑点核对现存目标：III4.8等式来自(ii)、IV基变换结果来自3.4.5、VI-B12.2中反仿射核的特征性来自(iii)、V自由作用判据来自IV3.2.1；四项均可唯一确认，最终改正显示引用并记录旧文。其余3项保留待核。最终处置及完整证据以APPLIED.json/.md为准，前表为最初决策快照。
