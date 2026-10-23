# 第 VIII 篇独立内容审校

审校范围：按 `inputs/VIII/body.tex` 的实际输入顺序完整对照八个源组件与 `chapters/VIII/` 对应译文，2676 源行。审校包括全部定义、假设与量词、否定、陈述与证明、48 个脚注、源注、4 个内嵌 tikzcd 及末尾书目。未修改第 VIII 篇译文。本报告是内容对照审校，非编译验收。

## 覆盖记录

|顺序|源组件 stem（译文加 -zh.tex）|源行|脚注|tikzcd|
|---|---|---:|---:|---:|
|1|01_expose_VIII_opening_through_corollary_1_3|238|4|0|
|2|02_expose_VIII_corollary_1_4_through_remark_1_7_4|324|7|2|
|3|01_expose_VIII_s2_s4_pp007_013|648|6|0|
|4|03_expose_VIII_section4_continuation_p14|51|0|1|
|5|05_expose_VIII_section5_en|290|5|0|
|6|06_expose_VIII_section6_en|533|11|0|
|7|05_expose_VIII_section7_part1|271|11|0|
|8|06_expose_VIII_section7_part2_and_bibliography|321|4|1|

逐段通读后，未发现改变数学结论的明确误译、漏译、变量丢失或量词/否定颠倒。以下为需要修正的术语和未译定位注释。

## 明确问题

### R1：transporter 术语未采用本书统一译名

- 文件：`chapters/VIII/06_expose_VIII_section6_en-zh.tex`，例 6.5(e)，第 184、186、192、195 行。
- 现文：“将 \(Y\) 输送到 \(Z\) 中的输送子”“严格输送子”（共五处术语出现）。
- 建议：术语统一为“传送子”“严格传送子”；相邻动词可相应写“将……传送到……”。
- 理由：源文 transporter / strict transporter；本项目明确采用“传送子”。该处包含普通传送子、严格传送子及正规化子的定义，宜保持一致。

### R2：identity component 的译名不完整

- 文件：`chapters/VIII/06_expose_VIII_section7_part2_and_bibliography-zh.tex`，注 7.10 后、引理 7.11 前，第 138 行。
- 现文：“其像包含单位分支 \((H_0)^0\)。”
- 建议：“其像包含单位连通分支 \((H_0)^0\)。”
- 理由：源文 identity component；本项目指定译名“单位连通分支”。数学记号原样保留。

### R3：页码定位与一处源稿说明注释仍为英文

- 文件：顺序 1、2、3、7、8 中全部 `% Source page:` 注释；另顺序 8 第 96–97 行 `% The authority prints ...` 注释。
- 现文举例：`% Source page: Exp8 component-local p. 30; complete-reader p. 646.`；`% The authority prints _{p^\nu}H over S_n here; the base-changed family ...`。
- 建议：仅翻译说明文字，原页码和公式照留，如“源页码：第 VIII 篇组件内第 30 页；完整合阅本第 646 页”；后者译为“权威源此处印作……；此处讨论的基变换族是……”。
- 理由：本任务要求定位说明与源注完整中文化。这些是非排印注释，不影响当前正文数学内容，但尚未满足完整中文化要求。

## 源稿已有疑点（不归为译错，不在译文自行改键）

1. 顺序 2 的注 1.7.4 附近引用 SGA 1, VIII, 2.1，源键为 `sga3:viii:proposition:2:1`，看似链接到本书 VIII 2.1，而非 SGA 1。译文忠实保留。
2. 顺序 7 的编者脚注引用 VI_A, Theorems 3.2，及稍后正文引用 VI_A, 3.2，源键均为 `sga3:viii:corollary:3:2`；同组件引用 VI_B, 4.3 的键为 `sga3:viii:corollary:4:3`。篇名与目标键前缀不符。译文保留了源键；应由集成者核对真实目标后修复，不能算作译者漏改。
3. 顺序 8 关于 XVI, 1.1(a),(b) 的末尾说明，其 (b) 链接键为 `sga3:viii:proposition:7:9:item:b`。同样为源稿目标可疑，译文忠实保留。

## 辅助守恒检查与限度

全部八对文件的 label/ref/hyperref/SGARef 键序列、环境序列、脚注数一致；4 个 tikzcd 块与源逐字一致。去除注释与转义括号后，全部源译花括号平衡为零。公式差异逐项核对，只涉及公式内 for/and/such that 等说明文字中文化，以及源文 étale 中单独的 \(\acute{e}\) 字形并入“平展”；未见数学内容丢失。书目题名已采用中文与〔原题〕并列，人名与刊名保留。检查证据保存在 `/tmp/viii-integrity-review.json`、`/tmp/viii-integrity-review.txt`，对照读取工具为 `/tmp/viii_review_pair.py`。这些机械检查仅佐证完整通读，不能替代数学审校；未在本审校中独立重证原书各命题，未执行全卷编译。
