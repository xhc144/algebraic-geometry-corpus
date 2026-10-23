# 第 III 篇组件 24–32 独立审校

2026-10-23。只读对照固定英文重建源与旧中文稿，没有修改译文、图文件、源文或 SOURCE_ISSUES.md。

## 实际覆盖

已逐段完整通读以下 9 个组件的英文与中文：

|完整源 stem（中文位于 chapters/<stem>-zh.tex）|范围|
|---|---|
|24_expose_III_s3_infinitesimal_group_structures|§3 全部，3.1–3.10、证明、注及全部脚注|
|25_expose_III_s41_s44_closed_subgroups|§4 篇首、4.1–4.4.1 全部|
|26_expose_III_s450_s47_lci_koszul|4.5.0–4.7，含 Koszul 复形、反例及来源说明|
|27_expose_III_s480_s410_obstruction_factorization|4.8.0–4.10，含全部三项陈述与补出的验证、两则底本记号说明|
|28_expose_III_s411_s4161_functorial_obstructions|4.11–4.16.1 全部，包括函子性、仿射显式计算、4.15 的正文与脚注两种证明|
|29_expose_III_s417_s422_subgroup_obstruction|4.17–4.22 全部，包括余循环及符号约定的证明|
|30_expose_III_s423_s430_conjugacy_coboundaries|4.23–4.30 及最后的商函子讨论|
|31_expose_III_s431_s4351_conjugacy_smooth|4.31–4.35.1 全部|
|32_expose_III_s436_s438_bibliography|4.36–4.38 全部、a)–g) 的几何解释、1)–5) 的态射解释及全部四项书目|

正文全部脚注、编者说明、来源说明均与源对应。逐件核对并保留 source locator：9 件合计 47 段 `% Source page:` 页码说明与源相同；头部来源范围亦保留，25/26 仅将旧“图像”说明调整成实际原生图说明。

另实际读取正文引用的全部 32 个原生图 TeX（diagram_031–diagram_062），检查对象、箭头、标签及上下文；译稿的 figures/exp3 对应文件与英文源 native_diagrams/exp3 文件逐字相同，路径变换正确，没有缺失图依赖。图中 `can.`、`surj.` 等源缩写亦原样保留。结构辅助检查显示引用/标签键及次数、脚注命令与环境起止均守恒；上述结论来自全文阅读，未以守恒检查替代内容审校。

## 交主线程处理的明确用语问题

未发现明确的整段缺译、条件/否定翻转或新增变量遗漏。以下两项违背现有 terminology.csv 的统一用语，建议局部修正，不重翻正文。

|位置|现文|建议|依据|
|---|---|---|---|
|24_expose_III_s3_infinitesimal_group_structures-zh.tex:264，注 3.5.1|`则得到一个上闭链 δ(μ,μ′)∈Z²(X₀,L₀)`|`则得到一个余循环……`|源词 cocycle；terminology.csv 明定 cocycle=余循环。该集合为 Z²，勿改成余链或余边界。|
|32_expose_III_s436_s438_bibliography-zh.tex:380，[Fr64] 题名|`Abel 范畴〔Abelian categories〕`|`阿贝尔范畴〔Abelian categories〕`|terminology.csv 明定 abelian category=阿贝尔范畴。人名 P. Freyd、出版社 Harper and Row 与原题均照旧。|

源注释仍采用英文（头部 provenance、`Source page` 标签以及图文件的 PRELIMINARY/LEAD_VERIFY 说明），完整保留而未缺译/删除。若最终工程要求连源码注释也全部中文化，须另在来源注释整理流程处理；这些并非正文残留。

## 源文疑点与限制

已完整阅读 audit/SOURCE_ISSUES.md 中第 III 篇记录。以下既存疑点在本轮逐段对照中确认同样存在于英文源，不能判为中文误译：24 的 3.5 证明末项链接；26 的 4.6.5 条件自指键；27–29 的局部完全交条件表述、4.19 的 π/μ 混用、4.20 的 4.8(iii) 引用、4.22 的对偶模底环；30 的 4.38(5) 链接；31 的 SGA1 跨书链接及 4.33 两个 E 的记号；32 的 4.38(d) 编者脚注把群自同构函子的 Lie 代数与 Lie 代数导子等同。尤其最后一项已有特征 p 的反例提醒，应继续作为高优先级源疑点保留。

本轮补充一处可直接定位的源文字疑点：29 的 §4.18 说诱导运算 μ_Y 模 J 约化为“X_J 上的群运算”；μ_Y 的定义域是 Y×Y，按上下文目标应当是 Y_J 上的群运算。英文与中文均写 X_J，故未在译文中擅改，宜与法文权威核对。

没有逐式独立重证全部数学，没有重新对照新版法文 PDF，也没有编译或作 PDF 视觉终验。原生图中继承的 PRELIMINARY/LEAD_VERIFY 注释仍在；本次核验是英文原生图与中文原生图/正文之间的对应，不把它称为与法文扫描图逐一认证。
