# VII-B47–69 独立内容审校

审校日期：2026-10-22。审校者未翻译本范围。审校对象为本项目英文重建底本与相应中文组件，未改动译者文件。本报告区分翻译问题与英文底本疑点；不据下列疑点擅自添加数学条件，不宣称逐式重证。

## 覆盖与限制（已完成）

已完整逐段对照：47–69（23 件），包括定义、量词与否定、命题/定理/证明、脚注、源注及文件头来源定位。另已阅读其中实际引用的原生图 diag_113–122 的数学内容、箭头文字和来源注。未发现已读范围的整段遗漏、假设或否定反译；下面列出实际发现的问题。

66–69 保存后也已完整逐段读完，未发现新增译错、段落遗漏或量词/否定反译。全部 23 件的 292 个 label/ref/inline-target 键出现、43 处脚注及 10 个图输入已比较，源译一致（图路径按要求由 native_diagrams/ 改为 figures/）；环境有序序列一致。这里的结构核对仅为内容审校的辅助证据，不能代替数学证明核验。未重看法文权威 PDF 图像、未逐式重新证明、未编译或作 PDF 视觉审查。

## 明确翻译及本地化问题

行号以本次读取时的中文文件为准；均位于 `chapters/VII-B/`。

| 编号 | 文件、条款、行 | 现文 | 建议 | 理由 |
|---|---|---|---|---|
| T01 | `51_expose_VIIB_section26_lie_algebra_opening_en-zh.tex`，§2.6(b)，49 | `\text{for every \(x\in A\),}` | 改为 `\text{对每个 \(x\in A\)，}`，保留其中变量及条件 | 公式中量词说明仍为英语。 |
| T02 | `54_expose_VIIB_section27_infinitesimal_formal_monoids_en-zh.tex`，§2.7 证明中定义 c₁，91 | `\text{if }x\in U_1^+` | `\text{若 }x\in U_1^+` | 条件说明仍为英语；无需改变数学。 |
| T03 | `55_expose_VIIB_section28_unipotent_group_schemes_en-zh.tex`，§2.8(b) 及平凡模段，30、77 | 两处 `\text{for every }v\in V` | 两处均改为 `\text{对每个 }v\in V` | 量词说明仍为英语。 |
| T04 | `56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en-zh.tex`，不可约定义和局部分量描述，46、89 | 两处 `\text{for every open maximal ideal }` | `\text{对每个开极大理想 }` | 术语及量词说明仍为英语。 |
| T05 | `57_expose_VIIB_section3_and_31_primitives_en-zh.tex`，引理3.1证明，68 | `\text{for every }i` | `\text{对每个 }i` | 量词说明仍为英语。 |
| T06 | `60_expose_VIIB_section33_cartier_theorem_en-zh.tex`，(iii)⇒(i) 证明，152 | “由于 \(G\) 是根式的” | 建议“由于 \(G\) 是根性的（radicial）”或按项目最终选定术语译“纯不可分的（radicial）”；保留底本文义，不擅改为另一个假设 | 英文为 `Since G is radicial`；“根式”通常指 radical expression，不能明确表达概形态射的 radicial 性质。此处词义须与环的 radical（下半句现译“根”）区分。 |
| T07 | `63_expose_VIIB_section333_gamma_lie_algebras_en-zh.tex`，说明 Endₖ(G)(C) 的段落，46 | “即使通常的相容图交换。” | “即，使通常的相容图交换。”或“也就是说，通常的相容图对该态射交换。” | 英文 `that is, for which the usual compatibility diagrams commute` 是解释前述保持余代数结构的条件；现文黏为汉语让步连词“即使”，可能被读成 even if。 |

补充术语建议（非数学错译）：58、60 中 radical 现译“根”，而本项目后续用“根基”；可在总校时决定是否统一为“根基”。未据此判定陈述错误。

## 英文底本疑点：译者忠实保留，不计为译错

| 编号 | 文件、条款 | 底本文字或公式 | 疑点与建议处理 |
|---|---|---|---|
| S01 | `47_expose_VIIB_section25_etale_formal_groups_en.tex`，§2.5 定义 X(κₛ) 后 | `The group Γ acts continuously on every X(ℓ), and hence on X(κ_s).` | ℓ 遍历所有有限子扩张，未限于 Galois 子扩张；一般 γ 将 X(ℓ) 送到 X(γℓ)，未必保持单个 X(ℓ)。极限上的作用是自然的，逐个 X(ℓ) 的断言需核。中文忠实照译，勿直接归责译者。 |
| S02 | `51_expose_VIIB_section26_lie_algebra_opening_en.tex`，§2.6.1 末两式 | `ω_{G'/C}=ω_{G/k}\widehat\otimes_A C`，随后 Hom 中同样下标 A | 上文标准基变换先使用 `\widehat\otimes_k C`；此处下标 A 若是借增广赋予 C 以 A-模结构，应说明该约定。中文逐式保留；宜作为底本下标/约定核对项，不自行替换。 |
| S03 | `56_expose_VIIB_section29_pointed_cocommutative_hopf_algebras_en.tex`，命题2.9.1(i)证明 | 从 `π∘m_G∘(s×s)=π∘s∘m_{G_e}` 后称 `As π is an epimorphism, it follows that s is a group morphism.` | 满态射的一般消去律适用于前复合，不能仅凭此理由消去这里的后复合 π；预期可利用 étale 部分截面的唯一性等结构补足。中文保留了源文逻辑，非翻译错漏。 |
| S04 | `59_expose_VIIB_section321_campbell_hausdorff_en.tex`，Campbell–Hausdorff 总公式后的指标条件 | 第二个大和未出现 pₘ，但随后统一写 `p_m+Σ(p_i+q_i)=ℓ−1` | 对第二个和需要单独总次数约定，或说明其中 pₘ=0；中文完整保留了英文，宜回查权威底本而不静默改公式。 |
| S05 | `63_expose_VIIB_section333_gamma_lie_algebras_en.tex`，证明 End 函子左正合后 | `Thus End_k(G) is left exact and can be treated as a formal k-group.` | End 在复合运算下通常是幺半群，非所有自同态可逆。前文所需仅为其由形式簇表示，Aut 才是形式群。中文“可视为形式 k-群”忠实于英文；建议将此列为底本对象类型问题。 |
| S06 | `65_expose_VIIB_section411_formal_completion_frobenius_en.tex`，§4.1.1 定义 X^(p) 后 | `X^{(p)}=X×_{fr(S)}S` 后称其结构态射为 `fr(S)∘η` | 通常基变换的结构态射是第二投影；`fr(S)∘η` 的定义域是 X。底本随后还采用 `X^{(p)}=X` 的点集记号，须核对是否使用另一个 Frobenius 扭曲约定或省略了标识。中文忠实保留；不得仅凭通常约定改式。 |

另外，51、52、56、58、60–62、67、68 等文件中存在显示文字指向 VIIA 或 `sga3:vii:paragraph:5-1:equation:*` 等与当前条款不相称的链接键；所见中文均保留英文键。这属于来源层引用核对，不作为翻译新增错误，亦未在审校中改键。

## 交付状态

本报告已覆盖全部指定 23 件；共列出 7 项需总校处理的翻译/本地化问题（9 个出现位置），另有独立列出的底本疑点。审校期间未改动任何源文件或中文组件。最终修改由 root 处理；本报告不表示上述问题已修正。
