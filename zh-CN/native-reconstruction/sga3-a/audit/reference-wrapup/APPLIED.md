# 已报告语义错链：最终逐项处置

Bounded repair of previously reported semantic wrong-links, plus explicitly identified adjacent same-kind references; not a new full-book review.

原行号据基线 `ea116c5f61fcfa9c499922abdb7be5622c71bfb3`；新增锚点会移动后续行。实际调用、完整显示参数及证据见 APPLIED.json。

{'replace_key': 140, 'external': 47, 'retain': 53, 'replace_plain_citation': 5, 'pending': 3}

| 原文件:行 | 原引用/键 | 处置/新目标 | 依据 |
|---|---|---|---|
| chapters/00_introduction-zh.tex:23 | `第~5~节` / `sga3:intro:section:5` | replace_key → `sec:sga3-VIB-5` | 编者告示明确 VI-B 第5节；当前旧键为导言§5。 |
| chapters/03_expose_I_s18_s22_pp010_015-zh.tex:138 | `(1)` / `sga3:i:proposition:1:4:1` | replace_key → `sga3:i:subsection:1-8:equation:1` | I§1.8 紧前已有带 tag(1)/(2)/(3) 的 equation 标签，结合三式推导纤维积。 |
| chapters/03_expose_I_s18_s22_pp010_015-zh.tex:138 | `(2)` / `sga3:i:section:2` | replace_key → `sga3:i:subsection:1-8:equation:2` | I§1.8 紧前已有带 tag(1)/(2)/(3) 的 equation 标签，结合三式推导纤维积。 |
| chapters/03_expose_I_s18_s22_pp010_015-zh.tex:139 | `(3)` / `sga3:i:section:3` | replace_key → `sga3:i:subsection:1-8:equation:3` | I§1.8 紧前已有带 tag(1)/(2)/(3) 的 equation 标签，结合三式推导纤维积。 |
| chapters/06_expose_I_s41_s43_basic_scheme_groups-zh.tex:211 | `1.3` / `sga3:i:subsection:1-3` | replace_key → `sga3:ii:remark:1-3` | I§4.3.2 文字明确 II,1.3；II注1.3讨论模值Y-函子。 |
| chapters/07_expose_I_s44_s47_scheme_groups-zh.tex:499 | `第 2 节` / `sga3:ii:section:2` | external | 脚注明引 [DG], II, §2,1.1；两段号码均属外部[DG]，不是SGA3 II§2或I1.1。 |
| chapters/07_expose_I_s44_s47_scheme_groups-zh.tex:500 | `1.1` / `sga3:i:subsection:1-1` | external | 脚注明引 [DG], II, §2,1.1；两段号码均属外部[DG]，不是SGA3 II§2或I1.1。 |
| chapters/07_expose_I_s44_s47_scheme_groups-zh.tex:669 | `第 1.3 节` / `sga3:i:subsection:1-3` | external | 脚注明引 [Se68] §1.3。 |
| chapters/08_expose_I_s5_group_cohomology-zh.tex:435 | `2.3` / `sga3:i:subsection:2-3` | external | 同上承接前句[Gr57]关于卫星函子/导出函子的文献引用，指该外部文献2.3。 |
| chapters/08_expose_I_s5_group_cohomology-zh.tex:515 | `4.2` / `sga3:i:subsection:4-2` | external | 编者脚注明引[Ja03]第一部分4.2。 |
| chapters/08_expose_I_s5_group_cohomology-zh.tex:517 | `2.1` / `sga3:i:subsection:2-1` | external | 同上承接[Ja03]，指该书2.1。 |
| chapters/12_expose_II_s41_s44_lie_algebras-zh.tex:848 | `(6)` / `sga3:ii:section:6` | replace_key → `sga3:ii:subsection:4-3-2:equation:6` | 本段明确指4.3.2中局部式号，现有对应tag及equation标签；不能跳本篇§5/§6。 |
| chapters/12_expose_II_s41_s44_lie_algebras-zh.tex:974 | `(5)` / `sga3:ii:section:5` | replace_key → `sga3:ii:subsection:4-3-2:equation:5` | 本段明确指4.3.2中局部式号，现有对应tag及equation标签；不能跳本篇§5/§6。 |
| chapters/19_expose_III_s07bis_s010_group_actions-zh.tex:105 | `定理~3.5` / `sga3:iii:theorem:3-5` | external | 原句明确[DG70] II.4定理3.5的证明，属外部书目。 |
| chapters/19_expose_III_s07bis_s010_group_actions-zh.tex:113 | `引理~3.10` / `sga3:iii:corollary:3-10` | replace_key → `sga3:ii:lemma:3-10` | 紧前文字明确“第II篇的引理3.10”；II引理3.10为H对象中H对象的Eckmann–Hilton结论。 |
| chapters/23_expose_III_s2_infinitesimal_group_morphisms-zh.tex:472 | `2.1` / `sga3:iii:theorem:2-1` | replace_key → `sga3:ii:definition:2-1` | 注2.10在对偶数概形I_{S0}后明写II,2.1；II定义2.1定义I_S(M)。同文件其它III定理2.1引用不动。 |
| chapters/24_expose_III_s3_infinitesimal_group_structures-zh.tex:250 | `3.3` / `sga3:iii:proposition:3-3` | retain → `sga3:iii:proposition:3-3` | 邻近3.3本身的调用确为辅助命题，不能随错误的(i)/(ii)批量改。 |
| chapters/24_expose_III_s3_infinitesimal_group_structures-zh.tex:251 | `(i)` / `sga3:iii:proposition:3-3:item:i` | replace_key → `sga3:iii:theorem:3-5:item:i` | 处于定理3.5证明结尾，刚证明本定理(i)/(ii)；3.3为引用的辅助命题。 |
| chapters/24_expose_III_s3_infinitesimal_group_structures-zh.tex:252 | `(ii)` / `sga3:iii:proposition:3-3:item:ii` | replace_key → `sga3:iii:theorem:3-5:item:ii` | 处于定理3.5证明结尾，刚证明本定理(i)/(ii)；3.3为引用的辅助命题。 |
| chapters/26_expose_III_s450_s47_lci_koszul-zh.tex:367 | `(a)` / `sga3:iii:proposition:4-6-5:item:a` | replace_key → `sga3:iii:proposition:4-5:item:a` | 4.6.5陈述说4.5(i)中的条件(a)/(b)成立；条件定义在4.5(i)的内层枚举，不是自指4.6.5的结论。 |
| chapters/26_expose_III_s450_s47_lci_koszul-zh.tex:372 | `(b)` / `sga3:iii:proposition:4-6-5:item:b` | replace_key → `sga3:iii:proposition:4-5:item:b` | 4.6.5陈述说4.5(i)中的条件(a)/(b)成立；条件定义在4.5(i)的内层枚举，不是自指4.6.5的结论。 |
| chapters/26_expose_III_s450_s47_lci_koszul-zh.tex:377 | `(a)` / `sga3:iii:proposition:4-6-5:item:a` | retain → `sga3:iii:proposition:4-6-5:item:a` | 证明段开头(a)确指本命题4.6.5(a)，应保留，不能按旧键全文件替换。 |
| chapters/29_expose_III_s417_s422_subgroup_obstruction-zh.tex:323 | `4.8(iii)` / `sga3:iii:proposition:4-8:item:iii` | replace_plain_citation → `sga3:iii:proposition:4-8:item:ii` | III 4.8(ii)的式(**)明确给出c(X,Y,i′)=u(d(Y,Y′))；(iii)讨论法模的微分D，与此所引等式不同。故可从现存陈述唯一确认应引(ii)。 |
| chapters/30_expose_III_s423_s430_conjugacy_coboundaries-zh.tex:175 | `(5)` / `sga3:iii:paragraph:4-20:equation:5` | replace_key → `sga3:iii:paragraph:4-38:item:5` | 脚注说将在4.38(4)及(5)中用到；(5)是4.38的第5项，不是4.20的式(5)，已有4.38:item:5锚点。 |
| chapters/31_expose_III_s431_s4351_conjugacy_smooth-zh.tex:175 | `4.10` / `sga3:ii:definition:4-10` | external | 原句明确SGA1, II,4.10；应取消错内部链接，保留显示4.10。 |
| chapters/IV/03_expose_IV_s3-zh.tex:728 | `3.4.4` / `sga3:iv:para:3:4:4` | replace_plain_citation → `sga3:iv:proposition:3:4:5` | IV 3.4.5明确陈述(M)有效商与基变换相容，恰为3.5.2(i)⇒(ii)；紧前705行构造下降数据也明引3.4.5。3.4.4仅定义自由群作用，故可唯一确认编号应为3.4.5。 |
| chapters/IV/19_expose_IV_s47-zh.tex:51 | `5.3.1` / `sga3:iv:proposition:5:3:1` | replace_key → `par:sga3-VIA-5.3.1` | 开头脚注明确另见VI_A,5.3.1；正确目标为VI-A的对应段。 |
| chapters/IV/20_expose_IV_s5-zh.tex:332 | `前一命题` / `sga3:iv:proposition:5:2:8` | replace_key → `sga3:iv:proposition:5:2:7` | 在5.2.8证明中“前一命题的对应”指5.2.7的子群对应，非自指5.2.8。 |
| chapters/V/20_expose_V_localp28_31_sections7_9_en-zh.tex:244 | `4.4` / `sga3:viii:corollary:4:4` | external | 上下文明引SGA1 VIII的下降结果；本书SGA3 VIII同号条目不是目标。 |
| chapters/V/20_expose_V_localp28_31_sections7_9_en-zh.tex:255 | `6.5` / `sga3:viii:examples:6:5` | external | 上下文明引SGA1 VIII的下降结果；本书SGA3 VIII同号条目不是目标。 |
| chapters/V/20_expose_V_localp28_31_sections7_9_en-zh.tex:259 | `5.7` / `sga3:viii:corollary:5:7` | external | 上下文明引SGA1 VIII的下降结果；本书SGA3 VIII同号条目不是目标。 |
| chapters/VI-A/02_expose_VIA_examples132_through_cor241_en-zh.tex:320 | `2.1` / `prop:sga3-VIB-2.1` | replace_key → `par:sga3-VIA-2.1` | 本篇上下文沿用G′、G⁰的记号及约化群结构，分别由紧前本篇2.1/2.2定义和讨论，并无VI-B跨篇指示。 |
| chapters/VI-A/02_expose_VIA_examples132_through_cor241_en-zh.tex:402 | `2.2` / `prop:sga3-VIB-2.2` | replace_key → `par:sga3-VIA-2.2` | 本篇上下文沿用G′、G⁰的记号及约化群结构，分别由紧前本篇2.1/2.2定义和讨论，并无VI-B跨篇指示。 |
| chapters/VI-A/06_expose_VIA_theorem265_through_remark267_loop2_r1_en-zh.tex:152 | `(iii)` / `prop:sga3-VIA-2.6.1:item:iii` | replace_key → `prop:sga3-VIA-2.6.6:item:iii` | 本段正在证明2.6.6(ii),(iii)第二断言；紧前明确已证明其第一断言，故“先证明(iii)第二断言”仍指2.6.6。 |
| chapters/VI-A/09_expose_VIA_section322_induction_en-zh.tex:19 | `定理~V.8.1` / `par:sga3-VIB-8.1` | replace_key → `thm:sga3-V-8.1` | 显示明确“定理V.8.1”，V现有定理8.1给群胚平坦取商。 |
| chapters/VI-A/12_expose_VIA_section33_theorems_corollary_loop2_r1_en-zh.tex:18 | `定理~4` / `sec:sga3-VIA-4` | external | 脚注明引Anantharaman [An73]定理4；不是本篇第4节。 |
| chapters/VI-A/12_expose_VIA_section33_theorems_corollary_loop2_r1_en-zh.tex:21 | `7.1` / `prop:sga3-VIB-7.1` | external | 前后两处同指[DG70] III.2,7.1，属外部文献；两次调用均应拆除错内部链接。 |
| chapters/VI-A/12_expose_VIA_section33_theorems_corollary_loop2_r1_en-zh.tex:39 | `7.1` / `prop:sga3-VIB-7.1` | external | 前后两处同指[DG70] III.2,7.1，属外部文献；两次调用均应拆除错内部链接。 |
| chapters/VI-A/17_expose_VIA_par45_46_base_change_en-zh.tex:21 | `4.6` / `par:sga3-VIA-4.6` | external | 原句明确SGA1 VIII (3.1,4.6,5.4)，属跨书外引。 |
| chapters/VI-A/17_expose_VIA_par45_46_base_change_en-zh.tex:34 | `引理~6.1` / `lem:sga3-VIA-6.1` | replace_key → `lem:sga3-V-6.1` | 文字明确本节对第V篇引理6.1及§9(a)作说明。 |
| chapters/VI-A/21_expose_VIA_par53_correspondences_en-zh.tex:16 | `第~IV~篇 5.2.7` / `sga3:iv:proposition:5:2:7` | retain → `sga3:iv:proposition:5:2:7` | 同句第一个IV5.2.7明确正确，保留。 |
| chapters/VI-A/21_expose_VIA_par53_correspondences_en-zh.tex:17 | `5.3.1` / `par:sga3-VIA-5.3.1` | replace_key → `sga3:iv:proposition:5:3:1` | 段首说明回顾第IV篇；“IV5.2.7及5.3.1的陈述”应同属IV，VI-A当前5.3.1是转述本身。 |
| chapters/VI-A/22_expose_VIA_par54_abelian_categories_loop2_r1_en-zh.tex:18 | `5.2` / `prop:sga3-VIB-5.2` | replace_key → `par:sga3-VIA-5.2` | 商群N\G的存在及结构沿用本篇3.3.2和5.2；本篇5.2紧前讨论子群商结构，VIB5.2是分离性命题。 |
| chapters/VI-A/22_expose_VIA_par54_abelian_categories_loop2_r1_en-zh.tex:140 | `7.4` / `prop:sga3-VIB-7.4` | external | 括号明确[DG70] §III.3,7.4，是外部引文。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:10 | `3.1` / `prop:sga3-V-3.1` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:11 | `3.2` / `thm:sga3-VIA-3.2` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:12 | `0.1` / `sga3:VIA:0.1` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:36 | `3.3` / `par:sga3-VIA-3.3` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:97 | `2.7` / `prop:sga3-VIB-2.7` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:100 | `(i)` / `prop:sga3-VIB-2.7:item:i` | replace_key → `cor:sga3-VIA-6.6:item:i` | 这是本段推论6.6的证明，结尾“这就证明(i)，断言(ii)…”指本推论两项，与上一句外部[BAC]§2.7无关。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:101 | `(ii)` / `prop:sga3-VIB-2.7:item:ii` | replace_key → `cor:sga3-VIA-6.6:item:ii` | 这是本段推论6.6的证明，结尾“这就证明(i)，断言(ii)…”指本推论两项，与上一句外部[BAC]§2.7无关。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:182 | `定理~1.1` / `par:sga3-VIA-1.1` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-A/25_expose_VIA_theorem65_through_bibliography_loop2_r1_en-zh.tex:194 | `3.7` / `prop:sga3-VIB-3.7` | external | 该次上下文明确[Per75]V、[Per76]、[BAC]I§2.7或[DG70]II.6；均为所引外部文献的节/定理号，完整上下文见context。 |
| chapters/VI-B/37_expose_VIB_prop311_section4_prop41_en-zh.tex:11 | `5.6` / `par:sga3-VIB-5.6` | replace_key → `par:sga3-VIA-5.6` | 脚注明写比较VI_A,5.6；VI-A5.6讨论同样的平坦性/单位连通分支。 |
| chapters/VI-B/37_expose_VIB_prop311_section4_prop41_en-zh.tex:20 | `1.3.2` / `cor:sga3-VIB-1.3.2` | retain → `cor:sga3-VIB-1.3.2` | 两次1.3.2确为本篇连通分支像的推论；与VI-A5.6误链不同。 |
| chapters/VI-B/37_expose_VIB_prop311_section4_prop41_en-zh.tex:26 | `1.3.2` / `cor:sga3-VIB-1.3.2` | retain → `cor:sga3-VIB-1.3.2` | 两次1.3.2确为本篇连通分支像的推论；与VI-A5.6误链不同。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:51 | `(iii)` / `concl:sga3-VIB-4.2-iii` | retain → `concl:sga3-VIB-4.2-iii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:58 | `(i)` / `prop:sga3-VIB-4.2:item:i` | retain → `prop:sga3-VIB-4.2:item:i` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:60 | `(i)` / `prop:sga3-VIB-4.2:item:i` | retain → `prop:sga3-VIB-4.2:item:i` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:61 | `(ii)` / `prop:sga3-VIB-4.2:item:ii` | retain → `prop:sga3-VIB-4.2:item:ii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:87 | `(i)` / `prop:sga3-VIB-4.1:item:i` | replace_key → `prop:sga3-VIB-4.2:item:i` | 命题4.2内部证明(i)⇒(ii)、(iii)⇒(i)，对应4.2自己的三条件；4.1是辅助半连续性命题。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:88 | `(ii)` / `prop:sga3-VIB-4.1:item:ii` | replace_key → `prop:sga3-VIB-4.2:item:ii` | 命题4.2内部证明(i)⇒(ii)、(iii)⇒(i)，对应4.2自己的三条件；4.1是辅助半连续性命题。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:90 | `(iii)` / `concl:sga3-VIB-4.2-iii` | retain → `concl:sga3-VIB-4.2-iii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:91 | `(i)` / `prop:sga3-VIB-4.1:item:i` | replace_key → `prop:sga3-VIB-4.2:item:i` | 命题4.2内部证明(i)⇒(ii)、(iii)⇒(i)，对应4.2自己的三条件；4.1是辅助半连续性命题。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:92 | `(ii)` / `prop:sga3-VIB-4.2:item:ii` | retain → `prop:sga3-VIB-4.2:item:ii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:93 | `(iii)` / `concl:sga3-VIB-4.2-iii` | retain → `concl:sga3-VIB-4.2-iii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:128 | `(ii)` / `prop:sga3-VIB-4.2:item:ii` | retain → `prop:sga3-VIB-4.2:item:ii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:137 | `(ii)` / `prop:sga3-VIB-4.2:item:ii` | retain → `prop:sga3-VIB-4.2:item:ii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:138 | `(iii)` / `concl:sga3-VIB-4.2-iii` | retain → `concl:sga3-VIB-4.2-iii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:141 | `(ii)` / `prop:sga3-VIB-4.2:item:ii` | retain → `prop:sga3-VIB-4.2:item:ii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:142 | `(i)` / `prop:sga3-VIB-4.2:item:i` | retain → `prop:sga3-VIB-4.2:item:i` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:143 | `(ii)` / `prop:sga3-VIB-4.2:item:ii` | retain → `prop:sga3-VIB-4.2:item:ii` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/38_expose_VIB_prop42_en-zh.tex:144 | `(i)` / `prop:sga3-VIB-4.2:item:i` | retain → `prop:sga3-VIB-4.2:item:i` | 该次已经正确指4.2自身条件，保留；不能把本组件所有条件引用一律判错。 |
| chapters/VI-B/39_expose_VIB_cor43_cor44_en-zh.tex:82 | `1.3.1` / `cor:sga3-VIB-1.3.1` | retain → `cor:sga3-VIB-1.3.1` | 单独的1.3.1确用于纤维平滑，当前正确；只改随后同旧编号衍生的(ii)错链。 |
| chapters/VI-B/39_expose_VIB_cor43_cor44_en-zh.tex:85 | `(ii)` / `cor:sga3-VIB-1.3.1:item:ii` | replace_key → `cor:sga3-VIB-4.4:item:ii` | 4.4证明段明确证明本推论(ii)⇒(iv)；上一句1.3.1为辅助结论。 |
| chapters/VI-B/39_expose_VIB_cor43_cor44_en-zh.tex:114 | `(ii)` / `prop:sga3-VIB-4.2:item:ii` | replace_key → `cor:sga3-VIB-4.4:item:ii` | 本段末要在S约化时由本推论(ii)–(iv)推出G⁰平滑；不是4.2(ii)。 |
| chapters/VI-B/39_expose_VIB_cor43_cor44_en-zh.tex:114 | `(iv)` / `thm:sga3-VIB-3.10:item:iv` | replace_key → `cor:sga3-VIB-4.4:item:iv` | 同一范围(ii)–(iv)指本推论4.4条件(iv)，3.10仅前文说明构造方法。 |
| chapters/VI-B/40_expose_VIB_section5_through_rem541_loop2_r1_en-zh.tex:124 | `(ii)` / `concl:sga3-VIA-2.5.4-ii` | replace_key → `cor:sga3-VIB-5.4:item:ii` | 本段是推论5.4证明(ii)即拟紧性；上句VI-A2.5.4只是纤维不可约性的辅助引用。 |
| chapters/VI-B/41_expose_VIB_cor55_through_lemma560_loop2_r1_en-zh.tex:17 | `2.5` / `prop:sga3-VIB-2.5` | external | 脚注明引[Ray70a] VI,2.5，属外部文献。 |
| chapters/VI-B/41_expose_VIB_cor55_through_lemma560_loop2_r1_en-zh.tex:23 | `注 35` / `note:sga3-VIB-35` | replace_key → `note:sga3-VIA-35` | 脚注明确VI_A中的编者注35；VIB注35是另一反例，与该处拟射影结果无关。 |
| chapters/VI-B/53_expose_VIB_theorem623_en-zh.tex:31 | `(ii)` / `concl:sga3-VIB-6.2.3-i` | replace_key → `concl:sga3-VIB-6.2.3-ii` | 两次显示(ii)分别在编者注及证明第二项，已有本定理(ii)标签，旧键落(i)。 |
| chapters/VI-B/53_expose_VIB_theorem623_en-zh.tex:128 | `(ii)` / `concl:sga3-VIB-6.2.3-i` | replace_key → `concl:sga3-VIB-6.2.3-ii` | 两次显示(ii)分别在编者注及证明第二项，已有本定理(ii)标签，旧键落(i)。 |
| chapters/VI-B/56_expose_VIB_rem63_through_def65_en-zh.tex:137 | `6.2` / `prop:sga3-VIB-6.2` | pending | 主键确指命题6.2，但visible参数仅6.2，后接(iv)在宏外；既有疑点是原文6.2无(iv)，不能猜应改哪一条或仅换主键。 |
| chapters/VI-B/56_expose_VIB_rem63_through_def65_en-zh.tex:152 | `(ii)` / `cor:sga3-VIB-1.4.2:item:ii` | replace_key → `def:sga3-VIB-6.5:item:ii` | 定义6.5后的N.B.说上述(ii)的闭浸入假设满足；1.4.2为提供该事实的辅助推论，不是被满足的假设。 |
| chapters/VI-B/61_expose_VIB_def66_through_par69_en-zh.tex:71 | `3.3.3` / `cor:sga3-VIA-3.3.3` | external | 原句明引[RG71] I,3.3.3定义纯概形，属外部。 |
| chapters/VI-B/64_expose_VIB_def722_through_cor73_en-zh.tex:298 | `(v)` / `concl:sga3-VIB-7.3-iv` | replace_key → `concl:sga3-VIB-7.3-v` | 证明“最后(v)”指本推论7.3(v)，已有正确标签；旧键落(iv)。 |
| chapters/VI-B/82_expose_VIB_section11_through_prop1131_loop2_r1_en-zh.tex:255 | `3.2` / `sga3:VIIB:3.2:prop` | external | 编者注[Ray70a] VII,3.2是外部文献第VII章，不是SGA3 VII-B。 |
| chapters/VI-B/84_expose_VIB_def1180_through_cor1110_loop2_r1_en-zh.tex:322 | `2.5.1` / `lem:sga3-VIA-2.5.1` | external | 正文和注116明引[RG71] II,2.5.1/2.5.2，及[Gr73]对该外部引文的勘误；不是VI-A的同号引理。 |
| chapters/VI-B/84_expose_VIB_def1180_through_cor1110_loop2_r1_en-zh.tex:323 | `2.5.1` / `lem:sga3-VIA-2.5.1` | external | 正文和注116明引[RG71] II,2.5.1/2.5.2，及[Gr73]对该外部引文的勘误；不是VI-A的同号引理。 |
| chapters/VI-B/84_expose_VIB_def1180_through_cor1110_loop2_r1_en-zh.tex:323 | `2.5.2` / `prop:sga3-VIA-2.5.2` | external | 正文和注116明引[RG71] II,2.5.1/2.5.2，及[Gr73]对该外部引文的勘误；不是VI-A的同号引理。 |
| chapters/VI-B/85_expose_VIB_prop1110bis_through_rem11111_loop2_r1_en-zh.tex:21 | `1.5` / `lem:sga3-VIB-1.5` | external | 注119分别明引[Th87]1.4–1.5和[Kn71]III定理1.1，属外部。 |
| chapters/VI-B/85_expose_VIB_prop1110bis_through_rem11111_loop2_r1_en-zh.tex:21 | `1.1` / `par:sga3-VIB-1.1` | external | 注119分别明引[Th87]1.4–1.5和[Kn71]III定理1.1，属外部。 |
| chapters/VI-B/85_expose_VIB_prop1110bis_through_rem11111_loop2_r1_en-zh.tex:21 | `1.4` / `prop:sga3-VIB-1.4` | external | 注119分别明引[Th87]1.4–1.5和[Kn71]III定理1.1，属外部。 |
| chapters/VI-B/85_expose_VIB_prop1110bis_through_rem11111_loop2_r1_en-zh.tex:33 | `第 I 篇，第 6 节` / `sga3:i:section:6` | retain → `sga3:i:section:6` | 文字明写参见第I篇§6，解释G等变模，确为SGA3内部引用。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:220 | `2.1` / `prop:sga3-VIB-2.1` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:226 | `定理~3.1` / `def:sga3-VIB-3.1` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:323 | `定理~3.1` / `def:sga3-VIB-3.1` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:362 | `定理~3.1` / `def:sga3-VIB-3.1` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:362 | `2.5` / `prop:sga3-VIB-2.5` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:362 | `推论~3.2` / `rem:sga3-VIB-3.2` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/89_expose_VIB_section13_through_bibliography_loop2_r1_en-zh.tex:365 | `2.5` / `prop:sga3-VIB-2.5` | external | 对应定义13.4、13.5前述及13.6(a)/(b)/13.7前的[Th87]/“该文”引用，指Thomason外部文献，不是VI-B同号条目。 |
| chapters/VI-B/88_expose_VIB_rem11185_through_section12_end_loop2_r1_en-zh.tex:102 | `\textup{(ii)}` / `thm:sga3-VIB-12.2-ii` | replace_plain_citation → `thm:sga3-VIB-12.2-iii` | 12.2(iii)断言反仿射核为特征子群，应用于N使N′为N的特征子群；结合N在G中特征，得到N′在G中不变。12.2(ii)仅给仿射化同构，故此引用的正确分项可从紧前证明确认是(iii)。 |
| chapters/V/02_expose_V_pp256_260_en-zh.tex:57 | `参见第 III 篇, 3.2.1` / `` | replace_plain_citation → `sga3:iv:definition:3:2:1` | IV定义3.2.1明确把自由作用等价定义为G×X→X×X单态射，正是V此脚注的断言。III没有3.2.1，故从现有定义可唯一确认篇号III应为IV。 |
| chapters/VII-A/01_expose_VIIA_par13_through_par15_en-zh.tex:215 | `1.3` / `sga3:VIIB:1.3.prop` | replace_key → `sga3:VIIA:1.3` | 本篇相应编号与所述内容一致：1.3；非 VII-B 同号条目。 |
| chapters/VII-A/01_expose_VIIA_par13_through_par15_en-zh.tex:249 | `1.3` / `sga3:VIIB:1.3.prop` | replace_key → `sga3:VIIA:1.3` | 本篇相应编号与所述内容一致：1.3；非 VII-B 同号条目。 |
| chapters/VII-A/01_expose_VIIA_par13_through_par15_en-zh.tex:271 | `1.3` / `sga3:VIIB:1.3.prop` | replace_key → `sga3:VIIA:1.3` | 本篇相应编号与所述内容一致：1.3；非 VII-B 同号条目。 |
| chapters/VII-A/02_expose_VIIA_section2_invariant_differential_operators_en-zh.tex:122 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:2.3-invariance-lemma:item:ii` | 所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/02_expose_VIIA_section2_invariant_differential_operators_en-zh.tex:146 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:2.3-invariance-lemma:item:ii` | 所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/02_expose_VIIA_section2_invariant_differential_operators_en-zh.tex:177 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:2.4:item:ii` | 补核更正：本条位于定理2.4的编者脚注，明确说补入断言(ii)；现有2.4:item:ii位于同一定理左不变算子断言，不能指2.3引理。 |
| chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:19 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:3.1:item:i` | 所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:29 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:3.1:item:i` | 所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:33 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:3.1:item:ii` | 所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:481 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:3.1:item:i` | 所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/03_expose_VIIA_section3_coalgebras_cartier_en-zh.tex:481 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:3.1:item:ii` | 所指是紧邻的本地定义/引理条款，5.1公式不相干。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/05_expose_VIIA_par413_through_par414_en-zh.tex:141 | `3.1` / `sga3:VIIB:3.1:lemma` | replace_key → `sga3:VIIA:3.1` | 本篇相应编号与所述内容一致：3.1；非 VII-B 同号条目。 |
| chapters/VII-A/08_expose_VIIA_section5_restricted_p_lie_51_52_en-zh.tex:130 | `3.2` / `sga3:VIIB:3.2:prop` | external | 脚注明指 [DG70] III.7,3.2，外部书目，保留显示文字不点击。 |
| chapters/VII-A/08_expose_VIIA_section5_restricted_p_lie_51_52_en-zh.tex:217 | `5.1` / `sga3:VIIB:5.1:proposition` | replace_key → `sga3:VIIA:5.1` | 本篇相应编号与所述内容一致：5.1；非 VII-B 同号条目。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:20 | `5.2` / `sga3:VIIB:5.2:theorem` | replace_key → `sga3:VIIA:5.2` | 相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:82 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | retain | 前紧连“公式5.1”，现有目标为5.1 Jacobson第一公式，正常。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:82 | `5.2` / `sga3:VIIB:5.2:theorem` | replace_key → `sga3:VIIA:5.2` | 相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:82 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:5.2:condition:i` | 紧连5.2，应指5.2的(i)，而现键指5.1第一公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:105 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | retain | 此调用紧连5.1，指Jacobson第二公式，目标正确。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:105 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:5.2:condition:ii` | 紧连5.2，应指5.2条件(ii)而非5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:125 | `5.2` / `sga3:VIIB:5.2:theorem` | replace_key → `sga3:VIIA:5.2` | 相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:125 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:5.2:condition:i` | 本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:126 | `(0)` / `sga3:VIIB:0` | replace_key → `sga3:VIIA:5.2:condition:0` | 当前句连引5.2的(i)、(0)、(ii)，此处(0)唯一对应5.2齐次性条件。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:126 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:5.2:condition:ii` | 本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:186 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | retain | 本处直接使用5.1的Jacobson第二公式，现有公式键可保留。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:206 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:5.2:condition:i` | 本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:212 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | retain | 紧连“Jacobson第二个公式5.1”，现键正确。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:213 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:5.2:condition:ii` | 本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:213 | `5.2` / `sga3:VIIB:5.2:theorem` | replace_key → `sga3:VIIA:5.2` | 相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:343 | `5.2` / `sga3:VIIB:5.2:theorem` | replace_key → `sga3:VIIA:5.2` | 相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。 |
| chapters/VII-A/09_expose_VIIA_section53_restricted_enveloping_en-zh.tex:343 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:5.2:condition:ii` | 本段明确引用5.2定义条件，而非5.1 Jacobson公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。这是5.2定义陈列数学中的条件编号，采用SGAInlineEquationTarget。 |
| chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:120 | `3.2` / `sga3:VIIB:3.2:prop` | replace_key → `sga3:VIIA:3.2` | 此处定义群余代数，VII-A3.2正是该定义；VII-B3.2是指数映射命题。 |
| chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:139 | `5.1` / `sga3:VIIB:5.1:proposition` | replace_key → `sga3:VIIA:5.1` | 本篇相应编号与所述内容一致：5.1；非 VII-B 同号条目。 |
| chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:139 | `5.2` / `sga3:VIIB:5.2:theorem` | replace_key → `sga3:VIIA:5.2` | 相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。 |
| chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:305 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:5.5.3:item:i` | 5.5.3证明中的本地(i)/(ii)，已存在精确分项标签。 |
| chapters/VII-A/10_expose_VIIA_section54_55_coalgebra_group_en-zh.tex:305 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:5.5.3:item:ii` | 5.5.3证明中的本地(i)/(ii)，已存在精确分项标签。 |
| chapters/VII-A/11_expose_VIIA_section6_p_lie_group_scheme_en-zh.tex:29 | `2.5` / `sga3:VIIB:2.5:proposition` | replace_key → `sga3:VIIA:2.5-proposition` | 本篇相应编号与所述内容一致：2.5；非 VII-B 同号条目。 |
| chapters/VII-A/11_expose_VIIA_section6_p_lie_group_scheme_en-zh.tex:29 | `5.2` / `sga3:VIIB:5.2:theorem` | replace_key → `sga3:VIIA:5.2` | 相邻文字讨论受限 p-Lie 代数定义、符号 p 次幂条件，目标为本篇5.2。 |
| chapters/VII-A/11_expose_VIIA_section6_p_lie_group_scheme_en-zh.tex:41 | `2.5` / `sga3:VIIB:2.5:proposition` | replace_key → `sga3:VIIA:2.5-proposition` | 本篇相应编号与所述内容一致：2.5；非 VII-B 同号条目。 |
| chapters/VII-A/11_expose_VIIA_section6_p_lie_group_scheme_en-zh.tex:45 | `2.5` / `sga3:VIIB:2.5:proposition` | replace_key → `sga3:VIIA:2.5-proposition` | 本篇相应编号与所述内容一致：2.5；非 VII-B 同号条目。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:162 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:7.2:item:ii` | 当前证明7.2的(ii)情形，已存在精确标签。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:280 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:7.2:item:i` | 当前证明7.2的(i)情形。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:280 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:7.2:item:ii` | 当前证明7.2的(ii)情形，已存在精确标签。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:318 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:7.2:item:i` | 当前证明7.2的(i)情形。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:331 | `11.6.1` / `prop:sga3-VIB-11.6.1` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:339 | `11.6.1` / `prop:sga3-VIB-11.6.1` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:455 | `2.5` / `sga3:VIIB:2.5:proposition` | replace_key → `sga3:VIIA:2.5-proposition` | 本篇相应编号与所述内容一致：2.5；非 VII-B 同号条目。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:520 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:7.4-theorem:item:i` | 7.4.1证明的本地条件，7.4定理对应分项。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:520 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:5.5.3:item:i` | 紧连5.5.3，应指该定理(i)/(ii)，该精确标签已存在。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:520 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:7.4-theorem:item:i` | 7.4.1证明的本地条件，7.4定理对应分项。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:520 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:7.4-theorem:item:ii` | 7.4.1证明的本地条件(ii)。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。该(ii)实际为仿射性、omega局部自由有限型及截断对称代数结构，前轮near的简写不准确，本轮已以原行495核清。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:526 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:5.5.3:item:ii` | 紧连5.5.3，应指该定理(i)/(ii)，该精确标签已存在。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:546 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:7.4-theorem:item:i` | 7.4.1证明的本地条件，7.4定理对应分项。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:546 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:7.4-theorem:item:ii` | 7.4.1证明的本地条件(ii)。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。该(ii)实际为仿射性、omega局部自由有限型及截断对称代数结构，前轮near的简写不准确，本轮已以原行495核清。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:602 | `(71)` / `sga3:VIIB:nde:71` | pending | 当前引“编者注(71)”但现有VIIB nde71属于1.5形式平滑代数，与本处7.4证明无关；未能由现存标签唯一定位本篇所需脚注。保留(71)不点击。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:610 | `5.2` / `sga3:VIIB:5.2:theorem` | external | 显式 [BAC] II §5.2 定理1/推论2，为 Bourbaki 外部文献，不能指本书 VII-B；保留完整文字不点击。 |
| chapters/VII-A/12_expose_VIIA_section7_radicial_height1_en-zh.tex:636 | `2.8` / `sga3:VIIB:2.8` | external | 显式 [BAC] I §2.8 引理9，外部文献；保留文字不点击。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:96 | `5.2` / `sga3:VIIB:5.2:theorem` | replace_key → `par:sga3-VIA-5.2` | 同一脚注明指 VIA 3.2 和 5.2；VI-A5.2 讨论正规子群商。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140 | `9.2` / `prop:sga3-VIB-9.2` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140 | `(vii)` / `concl:sga3-VIB-9.2-vii` | retain | 前缀VIB9.2及(vii)明确为外引，用于后面的(i)⇔(ii)；这一个不是当前局部(iii)，保留。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIA:8.2:item:i` | 8.2证明中的本地条件，非5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:8.2:item:ii` | 8.2证明中的本地条件，非5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:140 | `(iii)` / `concl:sga3-VIB-9.2-iii` | replace_key → `sga3:VIIA:8.2:item:iii` | 此处是8.2本地条件间蕴含，后接本地(iv)/(v)及Frobenius正合行图，不是VIB9.2的条件。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:142 | `(ii)` / `concl:sga3-VIB-9.2-ii` | replace_key → `sga3:VIIA:8.2:item:ii` | 此处是8.2本地条件间蕴含，后接本地(iv)/(v)及Frobenius正合行图，不是VIB9.2的条件。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:142 | `(iii)` / `concl:sga3-VIB-9.2-iii` | replace_key → `sga3:VIIA:8.2:item:iii` | 此处是8.2本地条件间蕴含，后接本地(iv)/(v)及Frobenius正合行图，不是VIB9.2的条件。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:189 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:8.3.1:item:ii` | 本地8.3.1的(ii)，不是5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:198 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIA:8.3.1:item:ii` | 本地8.3.1的(ii)，不是5.1公式。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-A/13_expose_VIIA_section8_base_field_81_83_en-zh.tex:198 | `1.3` / `prop:sga3-VIB-1.3` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:34 | `1.3` / `prop:sga3-VIB-1.3` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:105 | `8.4` / `sga3:VIIA:8.4` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:105 | `8.5` / `sga3:VIIA:8.5` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:105 | `引理~5` / `sga3:VIIA:5` | external | 脚注明指 [TO70] 引理5，非本书第5节；保留文字不点击。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:107 | `8.5` / `sga3:VIIA:8.5` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:132 | `7.0` / `sga3:VIIA:7.0` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:136 | `1.6.1` / `cor:sga3-VIB-1.6.1` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:136 | `3.3.1` / `sga3:VIIA:3.3.1` | replace_key → `sga3:VIIB:3.3.1` | 当前明确写VIIB3.3.1，故先修篇别到现有同号标签；引用是否充分不是本次链接判断。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:143 | `7.4` / `sga3:VIIA:7.4` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:143 | `5.3.3` / `sga3:VIIA:5.3.3` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:211 | `1.3.6` / `sga3:VIIB:1.3.6` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:230 | `4.3` / `sga3:VIIA:4.3` | replace_key → `sga3:VIIB:4.3` | 当前句明指VIIB4.3，讨论受限包络代数滤过；VII-A4.3是Verschiebung。 |
| chapters/VII-A/14_expose_VIIA_section84_85_bibliography_en-zh.tex:291 | `8.5` / `sga3:VIIA:8.5` | retain | 篇别、可见编号与附近明确引用相符，当前目标存在；不因跨篇前缀自动改动。 |
| chapters/VII-B/51_expose_VIIB_section26_lie_algebra_opening_en-zh.tex:82 | `2.1` / `sga3:VIIA:2.1` | replace_key → `sga3:VIIB:2.1` | 当前用形式群仿射代数的增广余乘法公式，VIIB2.1定义该结构；VII-A2.1仅原点偏差。 |
| chapters/VII-B/51_expose_VIIB_section26_lie_algebra_opening_en-zh.tex:82 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:2.1:item:ii` | 紧连2.1并使用增广恒等式，所指为VIIB2.1(ii)。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:19 | `3.2.2` / `sga3:VIIA:3.2.2` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:19 | `2.2` / `sga3:VIIA:2.2` | replace_key → `sga3:VIIB:2.2` | 此处由双代数用Spf*构造形式群，VIIB2.2为此定义；VII-A2.2是平移偏差。 |
| chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:31 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:2.6.2:prop:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:2.6.2:prop:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:31 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:2.6.2:prop:item:ii` | 本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:70 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:2.6.2:prop:item:ii` | 本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/52_expose_VIIB_section262_enveloping_formal_group_en-zh.tex:97 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:2.6.2:prop:item:ii` | 本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en-zh.tex:176 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:2.9.1:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:2.9.1:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en-zh.tex:177 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:2.9.1:item:ii` | 本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en-zh.tex:202 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:2.9.1:item:ii` | 本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/58_expose_VIIB_section32_exponential_logarithm_en-zh.tex:37 | `2.2` / `sga3:VIIA:2.2` | replace_key → `sga3:VIIB:2.2` | 此处由双代数用Spf*构造形式群，VIIB2.2为此定义；VII-A2.2是平移偏差。 |
| chapters/VII-B/58_expose_VIIB_section32_exponential_logarithm_en-zh.tex:37 | `3.2.3` / `sga3:VIIA:3.2.3` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/58_expose_VIIB_section32_exponential_logarithm_en-zh.tex:141 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:3.2:prop:item:ii` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.2:prop:item:ii；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:39 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:40 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:ii` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:82 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:84 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:ii` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:117 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:126 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:126 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:ii` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:158 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:158 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:ii` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:179 | `7.4` / `sga3:VIIA:7.4` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/60_expose_VIIB_section33_cartier_theorem_en-zh.tex:202 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/61_expose_VIIB_section331_smoothness_corollary_en-zh.tex:45 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:3.3:cartier-theorem:item:ii` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.3:cartier-theorem:item:ii；5.1公式键跨错到VII-A。 |
| chapters/VII-B/62_expose_VIIB_section332_lie_formal_group_equivalence_en-zh.tex:32 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:3.2:prop:item:ii` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.2:prop:item:ii；5.1公式键跨错到VII-A。 |
| chapters/VII-B/62_expose_VIIB_section332_lie_formal_group_equivalence_en-zh.tex:41 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:VIIB:3.2:prop:item:ii` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:3.2:prop:item:ii；5.1公式键跨错到VII-A。 |
| chapters/VII-B/67_expose_VIIB_sections42_421_restricted_enveloping_group_en-zh.tex:14 | `2.3` / `sga3:VIIA:2.3` | replace_key → `sga3:VIIB:2.3` | 此处Lie(G)作为H(G)本原元素子代数使用VIIB2.3；VII-A2.3是右不变偏差。 |
| chapters/VII-B/67_expose_VIIB_sections42_421_restricted_enveloping_group_en-zh.tex:41 | `5.3` / `sga3:VIIA:5.3` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/67_expose_VIIB_sections42_421_restricted_enveloping_group_en-zh.tex:41 | `5.4` / `sga3:vii:corollary:5-4` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/67_expose_VIIB_sections42_421_restricted_enveloping_group_en-zh.tex:41 | `2.2` / `sga3:VIIA:2.2` | replace_key → `sga3:VIIB:2.2` | 此处由双代数用Spf*构造形式群，VIIB2.2为此定义；VII-A2.2是平移偏差。 |
| chapters/VII-B/68_expose_VIIB_section422_restricted_universal_property_en-zh.tex:15 | `5.3.3` / `sga3:VIIA:5.3.3` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/68_expose_VIIB_section422_restricted_universal_property_en-zh.tex:15 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:VIIB:2.6.2:prop:item:i` | 根据本段定理/命题的陈述和证明标题，此处明确指sga3:VIIB:2.6.2:prop:item:i；5.1公式键跨错到VII-A。 |
| chapters/VII-B/68_expose_VIIB_section422_restricted_universal_property_en-zh.tex:23 | `3.2.3` / `sga3:VIIA:3.2.3` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/68_expose_VIIB_section422_restricted_universal_property_en-zh.tex:23 | `5.5.3` / `sga3:VIIA:5.5.3` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/71_expose_VIIB_section432_no_functorial_campbell_hausdorff_en-zh.tex:17 | `4.3.1` / `sga3:VIIA:4.3.1` | replace_key → `sga3:VIIB:4.3.1` | 当前处讨论VIIB4.3.1中群状元素参数化，VII-A4.3.1为Verschiebung常群例。 |
| chapters/VII-B/71_expose_VIIB_section432_no_functorial_campbell_hausdorff_en-zh.tex:46 | `4.2.1` / `sga3:VIIA:4.2.1` | replace_key → `sga3:VIIB:4.2.1` | 源注明确指本讲4.2.1的群状元素集合，VIIB4.2.1定义G_p。 |
| chapters/VII-B/71_expose_VIIB_section432_no_functorial_campbell_hausdorff_en-zh.tex:66 | `4.3.1` / `sga3:VIIA:4.3.1` | replace_key → `sga3:VIIB:4.3.1` | 当前处讨论VIIB4.3.1中群状元素参数化，VII-A4.3.1为Verschiebung常群例。 |
| chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:28 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:viib:subsection:4-4:item:i` | 本地命题/定理(i)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:28 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:viib:subsection:4-4:item:ii` | 本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:50 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:viib:subsection:4-4:item:i` | 本地命题/定理(i)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:50 | `(ii)` / `sga3:vii:paragraph:5-1:equation:ii` | replace_key → `sga3:viib:subsection:4-4:item:ii` | 本地命题/定理(ii)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:50 | `4.3.1` / `sga3:VIIA:4.3.1` | replace_key → `sga3:VIIB:4.3.1` | 当前处讨论VIIB4.3.1中群状元素参数化，VII-A4.3.1为Verschiebung常群例。 |
| chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:57 | `7.4.1` / `sga3:VIIA:7.4.1` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:79 | `(i)` / `sga3:vii:paragraph:5-1:equation:i` | replace_key → `sga3:viib:subsection:4-4:item:i` | 本地命题/定理(i)分项唯一，但该项尚未设锚点。补核已唯一定位：在insert_target指定原行内、可见编号前插入所列宏；target_line_after_insertion给出整行精确结果（仅添锚点，原文字不变）。采用SGAInlineRefTarget。 |
| chapters/VII-B/72_expose_VIIB_sections44_441_height_one_groups_en-zh.tex:102 | `5.5.3` / `sga3:VIIA:5.5.3` | retain | 附近明确写VII-A并涉及相应包络代数/本原元素/Cartier定理；当前目标编号存在，不应批量替换。 |
| chapters/VIII/02_expose_VIII_corollary_1_4_through_remark_1_7_4-zh.tex:196 | `2.1` / `sga3:viii:proposition:2:1` | external | 显式SGA 1 VIII 2.1：仿射概形有效下降，不是本书可对角化群的VIII 2.1。 |
| chapters/VIII/02_expose_VIII_corollary_1_4_through_remark_1_7_4-zh.tex:196 | `5.6` / `sga3:viii:corollary:5:6` | replace_key → `sga3:x:theorem:5-6` | 同一脚注的X 5.4–5.6；X定理5.6即拟等平凡群的有效下降。 |
| chapters/VIII/05_expose_VIII_section7_part1-zh.tex:15 | `定理 3.2` / `sga3:viii:corollary:3:2` | replace_key → `thm:sga3-VIA-3.2` | 明引VI-A定理3.2：平坦正规子群的商存在。 |
| chapters/VIII/05_expose_VIII_section7_part1-zh.tex:96 | `3.2` / `sga3:viii:corollary:3:2` | replace_key → `thm:sga3-VIA-3.2` | 明引VI-A 3.2，构造H_n/G_n；非本篇3.2。 |
| chapters/VIII/05_expose_VIII_section7_part1-zh.tex:75 | `4.3` / `sga3:viii:corollary:4:3` | replace_key → `cor:sga3-VIB-4.3` | 明引VI-B 4.3：平坦群概形纤维维数恒定。 |
| chapters/VIII/05_expose_VIII_section7_part1-zh.tex:73 | `5.7` / `sga3:viii:corollary:5:7` | external | 同一已报附录段明引SGA 1 I 5.7，纤维上开浸入判据；非本篇VIII 5.7。 |
| chapters/VIII/06_expose_VIII_section7_part2_and_bibliography-zh.tex:136 | `(b)` / `sga3:viii:proposition:7:9:item:b` | external → `sga3:xvi:subsection:1:1` | 明引后篇XVI 1.1(b)，英文XVI源有该例但无(b)标签；超出本目录范围，保留文字不跳转。 |
| chapters/VIII/06_expose_VIII_section7_part2_and_bibliography-zh.tex:156 | `(b)` / `sga3:viii:proposition:7:9:item:b` | retain | 此处确为本篇7.9(b)假设，不可与136行同键的XVI例(b)一并改动。 |
| chapters/IX/02_expose_IX_sections_2_3-zh.tex:44 | `VIII~2.1` / `sga3:viii:proposition:2:1` | retain | 乘法型群性质由可对角化群性质下降，此处确引本书VIII 2.1。 |
| chapters/IX/02_expose_IX_sections_2_3-zh.tex:63 | `VIII~2.1` / `sga3:viii:proposition:2:1` | external | 明引SGA 1 VIII 2.1，仿射概形有效下降。 |
| chapters/IX/02_expose_IX_sections_2_3-zh.tex:166 | `3.2(b)` / `sga3:ix:theorem:3:2:item:b` | replace_key → `sga3:viii:corollary:3:2:item:b:01` | 承前VIII 1.5，字符群满射对应闭浸入是VIII 3.2(b)；旧键误锚在IX 3.6 bis(b)。 |
| chapters/IX/02_expose_IX_sections_2_3-zh.tex:186 | `5.3` / `sga3:ix:corollary:5:3` | replace_key → `sga3:i:subsection:5-3` | 同上所指为第I篇5.3的Hochschild上同调复形；本篇IX 5.3是中心同态相等的开闭性。 |
| chapters/IX/03_expose_IX_sections_4_5-zh.tex:656 | `5.3` / `sga3:ix:corollary:5:3` | retain | 此处应用中心同态相等的开闭性，确为本篇IX 5.3。 |
| chapters/IX/03_expose_IX_sections_4_5-zh.tex:661 | `2.4` / `sga3:ix:corollary:2:4` | replace_key → `prop:sga3-VIA-2.4` | 显式VI-A 2.4，域上局部有限型连通群几何连通；IX 2.4为关系的图浸入，不相关。 |
| chapters/IX/03_expose_IX_sections_4_5-zh.tex:666 | `2.4` / `sga3:ix:corollary:2:4` | replace_key → `prop:sga3-VIA-2.4` | 显式VI-A 2.4，域上局部有限型连通群几何连通；IX 2.4为关系的图浸入，不相关。 |
| chapters/XI/09_expose_XI_section_4-zh.tex:94 | `3.7` / `sga3:xi:proposition:3:7` | pending | 源段承接IX 3.6 bis的提升及共轭，却引3.7；IX明注无3.7，现键XI 3.7是可表性判据且与此论断无关。具体原始目标未能确认，保留3.7并标待核。 |
| chapters/XI/05_expose_XI_section_2-zh.tex:37 | `因此由第八讲，3.6，存在元素` / `` | replace_plain_citation → `sga3:ix:theorem:3:6` | IX定理3.6正是乘法型群到平滑群的同态提升及模幂零理想共轭；XI 2.4同一论证已正确明引IX 3.6。VIII不存在3.6。旧引用纯文字而非超链接。 |
