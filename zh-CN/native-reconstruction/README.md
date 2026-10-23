# 中文原生重建工作区

当前状态：用户于2026-10-22 23:42 UTC明确恢复本轮项目。协调者仅维护FGA、_coord及本索引，其余十个工作区由原作者续作。以下目录为独立作者工作区，不能据目录存在推定已完成。各书保留自身版式；既有中文译本与原始源文件不改动。

原始底本盘点起点：`e76d5fc9c6f38bfa611da5d1b684b622f60e379c`。分工及源校验见 [_coord/WORK_MAP.json](_coord/WORK_MAP.json)。

| 工作区 | 书目 | 范围 | 状态 |
|---|---|---|---|
| `sga3-a/` | SGA 3 | I, II, III, IV, V, VI-A, VI-B, VII-A, VII-B, VIII, IX, X, XI, XII | 原作者续作；新交付待回执 |
| `sga3-b/` | SGA 3 | XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX, XXI, XXII, XXIII, XXIV, XXV, XXVI | 已整合main；557页；完整英文源组件对读，原本／外引疑点保留 |
| `sga4-a/` | SGA 4 | I, II, III, IV, V, V-bis, VI, VII, VIII, IX | 已整合main；463页；法中全文对读，原书残引保留 |
| `sga4-b/` | SGA 4 | X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX | 已整合main；298页；英文源全范围对读，原著疑点保留 |
| `sga4half/` | SGA 4½ | I, II, III, IV, V, VI, VII, VIII | 已整合main；200页；317页法文对读，原著疑点保留 |
| `sga5/` | SGA 5 | I, III, III-B, V, VI, VII, VIII, X, XII, XV | 已整合验收记录；271页合格译文原字节保留 |
| `sga6/` | SGA 6 | 0, RRR-appendix, I, II, III, IV, V, VI, VII, VIII, IX, X, XII, XIII, XIV | 原作者续作；已核实远端424页快照 |
| `sga7-i/` | SGA 7-I | I, II, VI, VII, VIII, IX | 已整合main；297页；完整英文组件对读，原卷导言仍缺 |
| `sga7-ii/` | SGA 7-II | X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX, XXI, XXII | 已整合main；289页；原Leitfaden关系图仍缺 |
| `fga-explained/` | FGA Explained | 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, bibliography, index | 已整合main；313页；354页底本对读及索引核验 |
| `fga/` | FGA | foreword, 1, 2, 3.I, 3.II, 3.III, 3.IV, 3.V, 3.VI, bibliography | 124页修订稿在协调分支；VI脚注正文缺口保留 |

SGA 3/4 的 a/b 分割按已出版 exposé 有序列表的中点；a 管卷首，b 管卷末。全局索引及本协调目录由协调者独占维护。

FGA 由协调者负责；其余十个作者目录由父线程启动的任务独占。未完成稿必须明确标注。

## 可检查的工作稿与待审队列

- [FGA：前言及全八篇报告，124页中文修订稿](fga/outputs/FGA-zh-working.pdf)，另有[单文件TeX](fga/outputs/FGA-zh-working-standalone.tex)和[原生源码ZIP](fga/outputs/FGA-zh-working-source.zip)。实际合卷编译及独立包重建状态见[FGA记录](fga/PROGRESS.json)；本轮独立模型对照已覆盖八篇全部源页，并完成订正回读；原刊疑误及VI脚注正文缺口仍保留，未作专业人工审定。
- 各SGA与FGA Explained检查点、固定提交、原本覆盖风险和独立审查状态统一见[_coord/REVIEW_QUEUE.json](_coord/REVIEW_QUEUE.json)与[来源风险](_coord/COVERAGE_RISKS.json)。已有全篇初稿不代表最终审定；有些检查点仍在作者分支，保留至复核整合，不改写历史。
- SGA3-a早期检查点及SGA7-II的独立重建/源文发现，见[_coord/reviews/](_coord/reviews/)。这些报告明确限制了审查范围。

当前恢复差距表见 [_coord/RESUME_INVENTORY.json](_coord/RESUME_INVENTORY.json)。[_coord/PAUSED.md](_coord/PAUSED.md)及其JSON保留为2026-10-21历史暂停记录，不代表当前状态。SGA6的424页快照已核实保存到恢复分支`translation/sga6-resume-20261022`（6ce4142），原作者仍在补缺；394页是历史稿。

2026-10-23已正常整合main的恢复交付：SGA5（271页）、SGA4½（200页）、SGA3-b（557页）、SGA4-a（463页）、SGA4-b（298页）、SGA7-I（297页）、SGA7-II（289页）、FGA Explained（313页）。每卷原文覆盖、实际独立包重建及保留缺项见恢复总表和协调验收记录；不据编译成功宣称全部原著证明已重验。FGA修订稿在独立分支，交父线程合入。

当前逐卷已保存范围、审校口径与剩余缺项见[_coord/RESUMED_STATUS.md](_coord/RESUMED_STATUS.md)。历史暂停表不作当前完成状态依据。
