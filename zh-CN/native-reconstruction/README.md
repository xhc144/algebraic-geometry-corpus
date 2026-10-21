# 中文原生重建工作区

当前状态：按用户指令暂停，不自动续写。以下目录为独立作者工作区，不能据目录存在推定已完成。各书保留自身版式；既有中文译本与原始源文件不改动。

冻结起点：`e76d5fc9c6f38bfa611da5d1b684b622f60e379c`。分工及源校验见 [_coord/WORK_MAP.json](_coord/WORK_MAP.json)。

| 工作区 | 书目 | 范围 | 状态 |
|---|---|---|---|
| `sga3-a/` | SGA 3 | I, II, III, IV, V, VI-A, VI-B, VII-A, VII-B, VIII, IX, X, XI, XII | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `sga3-b/` | SGA 3 | XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX, XXI, XXII, XXIII, XXIV, XXV, XXVI | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `sga4-a/` | SGA 4 | I, II, III, IV, V, V-bis, VI, VII, VIII, IX | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `sga4-b/` | SGA 4 | X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `sga4half/` | SGA 4½ | I, II, III, IV, V, VI, VII, VIII | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `sga5/` | SGA 5 | I, III, III-B, V, VI, VII, VIII, X, XII, XV | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `sga6/` | SGA 6 | 0, RRR-appendix, I, II, III, IV, V, VI, VII, VIII, IX, X, XII, XIII, XIV | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `sga7-i/` | SGA 7-I | I, II, VI, VII, VIII, IX | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `sga7-ii/` | SGA 7-II | X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX, XXI, XXII | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `fga-explained/` | FGA Explained | 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, bibliography, index | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |
| `fga/` | FGA | foreword, 1, 2, 3.I, 3.II, 3.III, 3.IV, 3.V, 3.VI, bibliography | 已分配；正文与编译进度由各目录 PROGRESS.json 记载 |

SGA 3/4 的 a/b 分割按已出版 exposé 有序列表的中点；a 管卷首，b 管卷末。全局索引及本协调目录由协调者独占维护。

FGA 由协调者负责；其余十个作者目录由父线程启动的任务独占。未完成稿必须明确标注。

## 可检查的工作稿与待审队列

- [FGA：前言及全八篇报告，124页中文初稿](fga/outputs/FGA-zh-working.pdf)，另有[单文件TeX](fga/outputs/FGA-zh-working-standalone.tex)和[原生源码ZIP](fga/outputs/FGA-zh-working-source.zip)。实际合卷编译及独立包重建状态见[FGA记录](fga/PROGRESS.json)；未完成全书独立数学通校。
- 各SGA与FGA Explained检查点、固定提交、原本覆盖风险和独立审查状态统一见[_coord/REVIEW_QUEUE.json](_coord/REVIEW_QUEUE.json)与[来源风险](_coord/COVERAGE_RISKS.json)。已有全篇初稿不代表最终审定；有些检查点仍在作者分支，保留至复核整合，不改写历史。
- SGA3-a早期检查点及SGA7-II的独立重建/源文发现，见[_coord/reviews/](_coord/reviews/)。这些报告明确限制了审查范围。
