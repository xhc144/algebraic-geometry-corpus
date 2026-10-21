# 代数几何原始文献合集 · EGA / SGA / FGA / FGA Explained / Stacks Project

本仓库是「现代代数几何中文全集」编撰工程的**原文底本库**：按系列收录格罗滕迪克（Grothendieck）学派的经典文献原件 PDF，
并附书目对照、文件校验清单与各卷次的定位说明，作为翻译、注释与教学整理的底本。

## 五套书的定位

| 简称 | 原文书名 | 中文书名 | 性质与角色 |
| --- | --- | --- | --- |
| EGA | Éléments de géométrie algébrique | 《代数几何学原理》 | 系统建立现代代数几何基础的专著，原计划未全部完成 |
| SGA | Séminaire de Géométrie Algébrique du Bois-Marie | 《博瓦马里代数几何讨论班》 | 格罗滕迪克主持的研究讨论班文集，分多个专题 |
| FGA | Fondements de la Géométrie Algébrique | 《代数几何基础》 | 格罗滕迪克关于代数几何基础问题的研究报告合集 |
| FGA Explained | Fundamental Algebraic Geometry: Grothendieck's FGA Explained | 《基础代数几何：格罗滕迪克 FGA 详解》 | 后人对 FGA 相关理论的系统讲解与证明补充 |
| Stacks Project | The Stacks Project | 《代数叠项目》（通常保留英文名） | 不断更新的现代代数几何大型参考书 |

前三套是原著主体；FGA Explained 与 Stacks Project 主要用于补充、整理与扩展理论。

## 中文译本现状（截至 2026-10）

| 系列 | 官方出版中译本 | 非官方 / 社区译本 | 本库收录 |
| --- | --- | --- | --- |
| EGA | **有**：《代数几何学原理》，周健译，高等教育出版社，2018–2025 出版 I–IV 共 8 册 | 另有 I–III 的非官方 AI 译（Zenodo 22907053） | **是**：官方 7 册见 zh-CN/official/（缺 IV 第三部分）；非官方见 zh-CN/EGA/ |
| SGA | 无 | 极少：SGA 1 有个人零散翻译（网络文章），其余无系统译本 | 否 |
| FGA | 无 | 未见公开中译 | 否 |
| FGA Explained | 无 | 未见公开中译（2019 年国内版为英文影印本，不是翻译） | 否 |
| Stacks Project | 原版本身即开放英文版 | **有**：116 章简体中文全译（Zenodo 22865712，2026-09-21，GFDL-1.2-or-later，AI 翻译） | **是**：整包收录于 zh-CN/Stacks/；另有较早的单文件译本 Stacks-Project-zh-CN.pdf |

**结论**：EGA 有高等教育出版社的正式中译本（周健译），这是目前唯一一套官方中文版；
SGA、FGA、FGA Explained 至今没有正式中译本，只有零散社区译稿与 AI 译本。
community 译本可作参考，但不能替代正式译本。

## 版本说明：哪些是「最新版」

| 系列 | 版本性质 | 本库所收版本 |
| --- | --- | --- |
| EGA | 历史定本（原著未按计划完成，无后续修订） | I：1971 年第 2 版（Grundlehren 166）；II–IV：IHES 原刊 1961–1967 |
| SGA | 历史定本（各卷为独立讨论班记录） | Springer LNM 原版；SGA 4 采用 2008 年 Springer 重排版 |
| FGA | 历史定本 | 1962 年汇辑本 |
| FGA Explained | 2005 年定本 | AMS 2005（2019 年影印） |
| Stacks Project | **持续更新**，官网随编译刷新 | Stacks-Project-2026-07-14.pdf（Version ed88ff78，7654 页）＝官网当前最新；另存 2023 年版作对照 |

只有 Stacks Project 存在「最新版」概念，其余四套均已定型。Stacks 官网下载地址为
stacks.math.columbia.edu/download/book.pdf，需要跟进更新时重新下载即可。

## 目录结构

```
EGA/    Éléments de géométrie algébrique I–IV（法文原版）
SGA/    Séminaire de Géométrie Algébrique du Bois-Marie 1 / 2 / 3 / 4（三卷）/ 4½ / 5 / 6 / 7（两卷）（法文原版）
FGA/    Fondements de la géométrie algébrique 与 FGA Explained
Stacks/ The Stacks Project（英文原版 + 中文译本）
zh-CN/  中文译本：official/ 高教社周健译《代数几何学原理》；EGA/、Stacks/ 为社区译本原始发布包
en/     英文译本与工作版：EGA、SGA、FGA 的英文 PDF、LaTeX 源码与可复现构建工程
```

## 文件清单

### EGA — 《代数几何学原理》

| 卷次 | 原文书名 | 中文书名 | 作者 | 年份 | 出版 | 文件 | 大小 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EGA I | Le langage des schémas | 概形的语言 | A. Grothendieck, J. Dieudonné | 1971（第2版） | Springer, Grundlehren 166 | [EGA-1-Le-langage-des-schemas.pdf](EGA/EGA-1-Le-langage-des-schemas.pdf) | 18.1 MB |
| EGA II | Étude globale élémentaire de quelques classes de morphismes | 若干态射类的整体初等研究 | A. Grothendieck, J. Dieudonné | 1961 | Publ. Math. IHES 8 | [EGA-2-Etude-globale-elementaire.pdf](EGA/EGA-2-Etude-globale-elementaire.pdf) | 26.2 MB |
| EGA III.1 | Étude cohomologique des faisceaux cohérents (Première partie) | 凝聚层的上同调研究（第一部分） | A. Grothendieck, J. Dieudonné | 1961 | Publ. Math. IHES 11 | [EGA-3-1-Etude-cohomologique-1.pdf](EGA/EGA-3-1-Etude-cohomologique-1.pdf) | 8.1 MB |
| EGA III.2 | Étude cohomologique des faisceaux cohérents (Seconde partie) | 凝聚层的上同调研究（第二部分） | A. Grothendieck, J. Dieudonné | 1963 | Publ. Math. IHES 17 | [EGA-3-2-Etude-cohomologique-2.pdf](EGA/EGA-3-2-Etude-cohomologique-2.pdf) | 10.4 MB |
| EGA IV.1 | Étude locale des schémas et des morphismes de schémas (Première partie) | 概形与态射的局部性质（第一部分） | A. Grothendieck, J. Dieudonné | 1964 | Publ. Math. IHES 20 | [EGA-4-1-Etude-locale-1.pdf](EGA/EGA-4-1-Etude-locale-1.pdf) | 30.5 MB |
| EGA IV.2 | Étude locale des schémas et des morphismes de schémas (Seconde partie) | 概形与态射的局部性质（第二部分） | A. Grothendieck, J. Dieudonné | 1965 | Publ. Math. IHES 24 | [EGA-4-2-Etude-locale-2.pdf](EGA/EGA-4-2-Etude-locale-2.pdf) | 30.3 MB |
| EGA IV.3 | Étude locale des schémas et des morphismes de schémas (Troisième partie) | 概形与态射的局部性质（第三部分） | A. Grothendieck, J. Dieudonné | 1966 | Publ. Math. IHES 28 | [EGA-4-3-Etude-locale-3.pdf](EGA/EGA-4-3-Etude-locale-3.pdf) | 15.7 MB |
| EGA IV.4 | Étude locale des schémas et des morphismes de schémas (Quatrième partie) | 概形与态射的局部性质（第四部分） | A. Grothendieck, J. Dieudonné | 1967 | Publ. Math. IHES 32 | [EGA-4-4-Etude-locale-4.pdf](EGA/EGA-4-4-Etude-locale-4.pdf) | 47.5 MB |

### SGA — 《博瓦马里代数几何讨论班》

| 卷次 | 原文书名 | 中文书名 | 作者 | 年份 | 出版 | 文件 | 大小 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SGA 1 | Revêtements étales et groupe fondamental | 平展覆盖与基本群 | A. Grothendieck (ed.) | 1971 | Springer LNM 224 | [SGA-1-Revetements-etales-et-groupe-fondamental.pdf](SGA/SGA-1-Revetements-etales-et-groupe-fondamental.pdf) | 10.7 MB |
| SGA 2 | Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux | 凝聚层的局部上同调与局部和整体 Lefschetz 定理 | A. Grothendieck | 1968 | North-Holland / Adv. Stud. Pure Math. 2 | [SGA-2-Cohomologie-locale-des-faisceaux-coherents.pdf](SGA/SGA-2-Cohomologie-locale-des-faisceaux-coherents.pdf) | 6.8 MB |
| SGA 3 | Schémas en groupes I–III | 群概形 I–III | M. Demazure, A. Grothendieck (eds.) | 1970 | Springer LNM 151–153（合卷） | [SGA-3-Schemas-en-groupes.pdf](SGA/SGA-3-Schemas-en-groupes.pdf) | 14.8 MB |
| SGA 4.1 | Théorie des topos et cohomologie étale des schémas, tome 1 | 拓扑斯理论与概形的平展上同调（第 1 卷） | M. Artin, A. Grothendieck, J.-L. Verdier | 1972/2008 | Springer LNM 269 | [SGA-4-1-Theorie-des-topos-1.pdf](SGA/SGA-4-1-Theorie-des-topos-1.pdf) | 2.4 MB |
| SGA 4.2 | Théorie des topos et cohomologie étale des schémas, tome 2 | 拓扑斯理论与概形的平展上同调（第 2 卷） | M. Artin, A. Grothendieck, J.-L. Verdier | 1972/2008 | Springer LNM 270 | [SGA-4-2-Theorie-des-topos-2.pdf](SGA/SGA-4-2-Theorie-des-topos-2.pdf) | 2.3 MB |
| SGA 4.3 | Théorie des topos et cohomologie étale des schémas, tome 3 | 拓扑斯理论与概形的平展上同调（第 3 卷） | M. Artin, A. Grothendieck, J.-L. Verdier | 1973/2008 | Springer LNM 305 | [SGA-4-3-Theorie-des-topos-3.pdf](SGA/SGA-4-3-Theorie-des-topos-3.pdf) | 3.3 MB |
| SGA 4½ | Cohomologie étale | 平展上同调 | P. Deligne | 1977 | Springer LNM 569 | [SGA-4-5-Cohomologie-etale.pdf](SGA/SGA-4-5-Cohomologie-etale.pdf) | 5.8 MB |
| SGA 5 | Cohomologie ℓ-adique et fonctions L | ℓ 进上同调与 L 函数 | A. Grothendieck (ed.) | 1977 | Springer LNM 589 | [SGA-5-Cohomologie-l-adique-et-fonctions-L.pdf](SGA/SGA-5-Cohomologie-l-adique-et-fonctions-L.pdf) | 5.8 MB |
| SGA 6 | Théorie des intersections et théorème de Riemann-Roch | 相交理论与 Riemann–Roch 定理 | P. Berthelot, A. Grothendieck, L. Illusie | 1971 | Springer LNM 225 | [SGA-6-Theorie-des-intersections.pdf](SGA/SGA-6-Theorie-des-intersections.pdf) | 25.6 MB |
| SGA 7 I | Groupes de monodromie en géométrie algébrique (SGA 7 I) | 代数几何中的单值群（I） | A. Grothendieck (ed.) | 1972 | Springer LNM 288 | [SGA-7-1-Groupes-de-monodromie.pdf](SGA/SGA-7-1-Groupes-de-monodromie.pdf) | 8.4 MB |
| SGA 7 II | Groupes de monodromie en géométrie algébrique (SGA 7 II) | 代数几何中的单值群（II） | P. Deligne, N. Katz | 1973 | Springer LNM 340 | [SGA-7-2-Groupes-de-monodromie-2.pdf](SGA/SGA-7-2-Groupes-de-monodromie-2.pdf) | 8.2 MB |

### FGA — 《代数几何基础》

| 卷次 | 原文书名 | 中文书名 | 作者 | 年份 | 出版 | 文件 | 大小 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FGA | Fondements de la géométrie algébrique | 代数几何基础 | A. Grothendieck | 1962 | Séminaire Bourbaki 1957–1962 汇辑 | [FGA-Fondements-de-la-geometrie-algebrique.pdf](FGA/FGA-Fondements-de-la-geometrie-algebrique.pdf) | 7.5 MB |
| FGA Explained | Fundamental Algebraic Geometry: Grothendieck's FGA Explained | 基础代数几何：格罗滕迪克 FGA 详解 | B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli | 2005（2019 影印） | AMS Math. Surveys & Monographs 123 | [FGA-Explained-Fantechi-AMS-2005.pdf](FGA/FGA-Explained-Fantechi-AMS-2005.pdf) | 62.5 MB |

### Stacks — 《代数叠项目》

| 卷次 | 原文书名 | 中文书名 | 作者 | 年份 | 出版 | 文件 | 大小 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Stacks Project | The Stacks Project | 代数叠项目 | A. J. de Jong et al. | 2023 | stacks.math.columbia.edu | [Stacks-Project.pdf](Stacks/Stacks-Project.pdf) | 35.5 MB |
| Stacks Project（中文翻译） | The Stacks Project — Chinese translation | 代数叠项目（中文译本） | The Stacks Project Authors | — | 社区译本 | [Stacks-Project-zh-CN.pdf](Stacks/Stacks-Project-zh-CN.pdf) | 33.6 MB |
| Stacks Project（官网最新） | The Stacks Project — official current build | 代数叠项目（官网最新编译版） | A. J. de Jong et al. | 2026-07-14（Version ed88ff78） | stacks.math.columbia.edu/download/book.pdf | [Stacks-Project-2026-07-14.pdf](Stacks/Stacks-Project-2026-07-14.pdf) | 36.6 MB |

## 官方中文译本（高等教育出版社 · 周健译）

这是目前唯一一套正式出版的中文译本：《代数几何学原理》，周健翻译，高等教育出版社出版，
2018 年起陆续出齐 EGA I–IV 共 8 册，最新为 2025 年的 IV 第四部分。

| 卷次 | 书名 | 出版年 | 页数 | 文件 |
| --- | --- | --- | --- | --- |
| EGA I | 概形语言 | 2018 | 261 | [EGA-I-概形语言-周健译.pdf](zh-CN/official/EGA-I-概形语言-周健译.pdf) |
| EGA II | 几类态射的整体性质 | 2019 | 243 | [EGA-II-几类态射的整体性质-周健译.pdf](zh-CN/official/EGA-II-几类态射的整体性质-周健译.pdf) |
| EGA IV 第一部分 | 概形与态射的局部性质（一） | 2022 | 291 | [EGA-IV-1-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-1-概形与态射的局部性质-周健译.pdf) |
| EGA IV 第二部分 | 概形与态射的局部性质（二） | 2023 | 264 | [EGA-IV-2-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-2-概形与态射的局部性质-周健译.pdf) |
| EGA IV 第四部分 | 概形与态射的局部性质（四） | 2025 | 386 | [EGA-IV-4-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-4-概形与态射的局部性质-周健译.pdf) |
| SGA 1 | 平展覆盖与基本群（社区中译） | — | 255 | [SGA-1-平展覆盖与基本群-中译.pdf](zh-CN/official/SGA-1-平展覆盖与基本群-中译.pdf) |
| EGA III | 凝聚层的上同调 | 2021 | 285 | [EGA-III-凝聚层的上同调-周健译.pdf](zh-CN/official/EGA-III-凝聚层的上同调-周健译.pdf) |

同目录下的《平展覆盖与基本群》是 SGA 1 的社区中译，非官方出版物，单独标注。
**库内缺 EGA IV 第三部分**（2024 年出版）：下载当日额度用尽，待补。

## 英文译本与 LaTeX 工作版

| 系列 | 来源仓库 | 内容 | 目录 |
| --- | --- | --- | --- |
| EGA | KokunoYumeto/ega-en | 连结版英文 EGA 0–IV（14.2 MB PDF）、各卷独立 PDF、完整 LaTeX 源码与 release 资产 | en/KokunoYumeto-ega-en/ |
| EGA | ryankeleti/ega | 业余英译项目：book.pdf 与 ega0–4 分卷 PDF、LaTeX 源码 | en/ryankeleti-ega/ |
| EGA | jcreinhold/ega | 另一套英译源码工程 | en/jcreinhold-ega/ |
| SGA | KokunoYumeto/sga-en | 4211 页英文累积版：合并读者版 + 9 卷 PDF + .tex + 可复现源码 ZIP | en/KokunoYumeto-sga-en/ |
| SGA | thosgood/sga | Tim Hosgood 英译项目源码（主要推进 SGA 1、SGA 6，尚未完成） | en/thosgood-sga/ |
| FGA | thosgood/fga | Tim Hosgood FGA 英译完整初稿源码 | en/thosgood-fga/ |

这些英文版多为机器辅助或未定稿译本：SGA 6 的校对程度不一致，EGA 英文版亦未经独立数学审校，
适合作为翻译底稿与对照，不宜作为权威版本引用。

## 社区中文译本（本库完整收录）

以下两个中译本按 Zenodo 发布**整包搬运**：PDF、LaTeX 源码（.tex）、可编辑源码包（zip），
连同发布方附带的 QA 报告、术语表、清单与校验文件一并保存，未删减、未重新打包。

| 译本 | Zenodo 记录 | 版本 / 日期 | 许可 | 文件数 | 体积 | 目录 |
| --- | --- | --- | --- | --- | --- | --- |
| 《代数几何学原理 I–III》简体中文版 | 22907053 | 2026-09-23 | 未标明（个人非官方译本） | 37 | 11.4 MB | zh-CN/EGA/ |
| Stacks Project 简体中文版（116 章） | 22865712 | 2026-09-21 | GFDL-1.2-or-later | 15 | 132.9 MB | zh-CN/Stacks/ |

关键文件：

- zh-CN/EGA/：01_ega1-zh-hans-cn.pdf、04_ega2-zh-hans-cn.pdf、07_ega3-1-zh-hans-cn.pdf、10_ega3-2-zh-hans-cn.pdf；
  对应 .tex 与 source.zip；另有 TERMINOLOGY.jsonl（术语表）、QA.json（质量报告）、README_zh-Hans-CN.md。
- zh-CN/Stacks/：00_0_..._2026-09-21.pdf（规范化最新版）、00_..._2026-08-30.pdf（前版）；各自 .tex 与 Editable_Source.zip；
  另有 Brauer 译名选择记录与规范化校验证据。源码 zip 内为 121 个分章 .tex 与 BUILD.ps1 构建脚本。

**注意**：两者均为非官方、AI 辅助译文，未获出版方授权或同行校订，作为编撰底本必须自行校核。

## 完整性校验

MANIFEST.sha256 收录每个文件的 SHA-256 与相对路径，可用 sha256sum -c MANIFEST.sha256 校验。

## 版权与使用范围

EGA、SGA、FGA 原文由 Springer、IHES、North-Holland 等出版方发行，FGA Explained 由 AMS 出版；
Stacks Project 由 A. J. de Jong 等人以开放许可维护。**本仓库为私有仓库**，所收文件仅作个人研究、翻译与编撰参照，
不再分发、不用于商业用途。引用请以各出版方的正式版本为准。

_清单生成于 2026-10-21 01:15；共 889 个文件，合计 932.6 MB。_
