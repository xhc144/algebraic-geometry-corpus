# 源范围闭合独立输入清单审计

快照：2026-10-23T00:15:56.816304+00:00。仅写审计文件，未修改正文、图或主文件。固定 ZIP SHA-256：`19e19e7226756315a86c21cf575ccbb300fab3a381289dc1f8669cfc3a3382a7`。

## 方法与结论

从固定源 cumulative master 的正文切换指令独立抽取单元顺序，再递归展开各 `body.tex` 的 `input`。IV 的整篇聚合文件继续展开为叶组件；V 的条件输入按固定源文件实际存在展开。未使用既有 coverage 数字作为预计清单。逐组件 source→译稿→main 位置及依赖详见同名 JSON。

预计 **295** 个叶组件；现有译稿 **294** 个；当前 main 唯一且按源顺序接入 **273** 个，另 **21** 个文件待集成、**1** 个文件缺失。没有多余或重复的正文 main 输入。

| 单元 | 源叶组件 | 译稿存在 | main 接入 | 待集成 | 缺失 |
|---|---:|---:|---:|---:|---:|
| INTRO | 1 | 1 | 1 | 0 | 0 |
| I | 9 | 9 | 9 | 0 | 0 |
| II | 5 | 5 | 5 | 0 | 0 |
| III | 18 | 18 | 18 | 0 | 0 |
| IV | 20 | 20 | 20 | 0 | 0 |
| V | 24 | 24 | 24 | 0 | 0 |
| VI | 90 | 90 | 90 | 0 | 0 |
| VII | 97 | 97 | 97 | 0 | 0 |
| TOMEI_INDEX | 1 | 1 | 1 | 0 | 0 |
| VIII | 8 | 8 | 8 | 0 | 0 |
| IX | 5 | 5 | 0 | 5 | 0 |
| X | 3 | 2 | 0 | 2 | 1 |
| XI | 11 | 11 | 0 | 11 | 0 |
| XII | 3 | 3 | 0 | 3 | 0 |


VI 分项为 VI-A 26、VI-B 64；VII 分项为 VII-A 15、VII-B 82。以上数目均来自实际输入，而非按文件数字前缀猜测。

## 特别核对

- **VIII 委托目录**：源的 `delegated_sections2_4` 一件、`delegated_sections5_6` 两件均找到中文同完整 stem 文件，并按源次序接入。中文扁平化到 `chapters/VIII` 不构成缺失；完整路径映射在 JSON。
- **VII-B81b**：源和中文 main 均明确在 81 后、82 前接入 `81b_expose_VIIB_section515_filtered_groups_lemma_en`。VII 共 97 个叶组件，不能按 00–95 得出 96。
- **IV17**：源 `33_expose_IV_complete.tex` 明确在 16 后直接输入 18；20 个源叶组件全部接入。没有 IV17 是源清单本身的情况，不能补造。
- **XII 篇题**：源 cumulative master 第 299–307 行在三个组件之前另有完整篇题、目录项与作者。题名为 “Maximal Tori, the Weyl Group, Cartan Subgroups, and the Reductive Center”，作者 A. Grothendieck。`body.tex` 的 “Maximal Tori and the Weyl Group” 只是缩略页眉，不能代替完整篇题。当前 XII 未接入 main，完整篇题与作者列为集成义务。
- **卷 I 索引**：单独从 `TOMEI_INDEX/body.tex` 展开，唯一源条目组件已接入；主文件中的篇题、页码说明、双栏包装也存在。

## 脚注、书目与图依赖

全 295 件源组件记录脚注命令：`footnote` 1176、`footnotetext` 18、`footnotemark` 33。已有的 294 件译稿逐件命令种类和数量一致；缺失的 X03 不计为译稿通过。记录源书目带标签 `item` 119 项、`bibitem` 6 项；已有译稿的书目标题存在性、条目标识及顺序一致。此为结构清单核对，不是书目正文终审。

源和现有译稿均解析出 333 次图/文件依赖调用；固定源依赖均存在，中文依赖均存在，按组件归一文件名与顺序一致。对 V 的 `SGAThreeDiagram`/`SGAThreeNativeInput` 按源 master 实际宏展开路径规则处理，避免把历史 PNG 名称参数错算成缺失的位图。JSON 保留原命令、参数、有效路径及解析结果。

## 待集成与后续回归

当前唯一缺失译稿：`chapters/X/03_expose_X_sections7_9_bibliography-zh.tex`。IX 五件、X 已有两件、XI 十一件、XII 三件目前均未在 main 输入；此处记录的是快照状态，不能据“文件已存在”称已经收卷。待主流程通知全部 main assembled 后，须重新抽取实际 main 输入，复核遗漏、重复、顺序、XII master 级篇题/作者及所有依赖。

## 核验限制

- 本轮为输入清单和依赖审计，不判断译文完整性或数学正确性。
- 脚注仅核对命令种类与数量，书目核对标题存在性、条目标识/顺序与bibitem键，不重审条目正文。
- 图依赖核对字面路径解析、存在性与归一文件名顺序，不作图数学复证或像素审查。
- 源V的IfFileExists分支按固定源所有被请求组件实际存在展开；不把fallback pending标题计为正文。
- 当前快照主文件只集成至VIII；IX–XII不可称已收卷，需待main assembled再回归。
