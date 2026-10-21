# 代数几何原始文献合集 · EGA / SGA / FGA / FGA Explained / Stacks Project

「现代代数几何中文全集」编撰工程的底本库：格罗滕迪克学派的原始文献、官方与社区中文译本、
英文工作版与 LaTeX 源码，按来源分层存放，附书目对照与逐文件校验。

当前规模：1042 个文件，约 1540.6 MB。

## 快速导航

| 想要 | 去这里 |
| --- | --- |
| 法文原著 | EGA/、SGA/、FGA/ |
| 官方中文版（周健译，高教社） | zh-CN/official/ |
| 社区中文译本 | zh-CN/EGA/、zh-CN/Stacks/、extra/数译中译/、extra/译馆-PKU/ |
| 英文译本与 LaTeX 源码 | en/、extra/SGA-English-Zenodo/ |
| 增补与参考 | extra/ |
| 逐文件校验 | MANIFEST.sha256 |

## 五套书的分工

| 简称 | 原文书名 | 中文书名 | 性质与角色 |
| --- | --- | --- | --- |
| EGA | Éléments de géométrie algébrique | 《代数几何学原理》 | 系统建立现代代数几何基础的专著，原计划未全部完成 |
| SGA | Séminaire de Géométrie Algébrique du Bois-Marie | 《博瓦马里代数几何讨论班》 | 格罗滕迪克主持的研究讨论班文集，分多个专题 |
| FGA | Fondements de la Géométrie Algébrique | 《代数几何基础》 | 格罗滕迪克关于基础问题的研究报告合集 |
| FGA Explained | Fundamental Algebraic Geometry | 《基础代数几何：FGA 详解》 | 后人的系统讲解与证明补充 |
| Stacks Project | The Stacks Project | 《代数叠项目》 | 持续更新的现代参考书 |

前四套是编撰主体（EGA、SGA、FGA 为原著，FGA Explained 为补证），Stacks Project 负责扩展与查证。

## 目录结构

~~~
EGA/  SGA/  FGA/  Stacks/    原著：法文原版与英文原版 PDF
zh-CN/
  official/                   周健译《代数几何学原理》官方中文版 8 册
  EGA/  Stacks/               社区中文译本的原始发布包（含 LaTeX 源码与 QA 文件）
en/                           英文译本与可复现 LaTeX 工程
extra/
  SGA-archive/                SGA 原版扫描档案（wstein.org，12 卷）
  SGA-English-Zenodo/         SGA 英文读者版（Zenodo）
  jcreinhold-sga/             SGA 英译仓库源码
  数译中译/                    数译站社区中译（SGA 1/2、Vakil、Milne、Hartshorne、Alper）
  译馆-PKU/                    译馆（北大）经典文献中译
  Conrad/  arXiv/             讲义与预印本
~~~

## 原著

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

## 中文译本

### 官方：高等教育出版社 · 周健译

目前唯一一套正式出版的中文译本，2018–2025 年出齐 EGA I–IV 共 8 册。

| 卷次 | 书名 | 出版年 | 页数 | 文件 |
| --- | --- | --- | --- | --- |
| EGA I | 概形语言 | 2018 | 261 | [EGA-I-概形语言-周健译.pdf](zh-CN/official/EGA-I-概形语言-周健译.pdf) |
| EGA II | 几类态射的整体性质 | 2019 | 243 | [EGA-II-几类态射的整体性质-周健译.pdf](zh-CN/official/EGA-II-几类态射的整体性质-周健译.pdf) |
| EGA IV-1 | 概形与态射的局部性质（一） | 2022 | 291 | [EGA-IV-1-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-1-概形与态射的局部性质-周健译.pdf) |
| EGA IV-2 | 概形与态射的局部性质（二） | 2023 | 264 | [EGA-IV-2-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-2-概形与态射的局部性质-周健译.pdf) |
| EGA IV-4 | 概形与态射的局部性质（四） | 2025 | 386 | [EGA-IV-4-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-4-概形与态射的局部性质-周健译.pdf) |
| SGA 1 | 平展覆盖与基本群（社区中译） | — | 255 | [SGA-1-平展覆盖与基本群-中译.pdf](zh-CN/official/SGA-1-平展覆盖与基本群-中译.pdf) |
| EGA III | 凝聚层的上同调 | 2021 | 285 | [EGA-III-凝聚层的上同调-周健译.pdf](zh-CN/official/EGA-III-凝聚层的上同调-周健译.pdf) |
| EGA IV-3 | 概形与态射的局部性质（三） | 2024 | 286 | [EGA-IV-3-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-3-概形与态射的局部性质-周健译.pdf) |

### 社区译本

| 来源 | 内容 | 目录 |
| --- | --- | --- |
| Zenodo 22907053 / 22865712 | EGA I–III 非官方 AI 译（含 TeX 与源码包）；Stacks 116 章中文全译 | zh-CN/EGA/、zh-CN/Stacks/ |
| 数译站 mathtranslations.org | SGA 1、SGA 2、Vakil《上升之海》、Milne 两种、Hartshorne、Alper | extra/数译中译/ |
| 译馆（北大张锦楠） | Bourbaki 交换代数、Serre、Deligne、Raynaud、吴宝珠等经典文献中译 | extra/译馆-PKU/ |

这些社区译本未经同行校订，作为编撰底本必须自行核校。

## 英文译本与 LaTeX 源码

| 来源 | 内容 | 目录 |
| --- | --- | --- |
| KokunoYumeto/ega-en | EGA 0–IV 英文连结版 + 各卷 PDF + 完整 LaTeX + release 资产 | en/KokunoYumeto-ega-en/ |
| KokunoYumeto/sga-en | 4211 页 SGA 英文累积版 + 9 卷 PDF + TeX + 源码 ZIP | en/KokunoYumeto-sga-en/ |
| ryankeleti/ega、jcreinhold/ega | 另外两套 EGA 英译（PDF 与源码） | en/ryankeleti-ega/、en/jcreinhold-ega/ |
| thosgood/sga、thosgood/fga | Tim Hosgood 的 SGA、FGA 英译项目源码 | en/thosgood-sga/、en/thosgood-fga/ |
| Zenodo 21749057 | SGA 1–7 英文读者版（8 个 PDF） | extra/SGA-English-Zenodo/ |
| jcreinhold/sga | SGA 英译的可检索 HTML 工程 | extra/jcreinhold-sga/ |

英文版多为机器辅助或未定稿译本（SGA 6 校对程度尤其不一致），宜作翻译底稿与对照，不宜当权威版本引用。

## 其他资料

| 内容 | 来源 | 目录 |
| --- | --- | --- |
| SGA 原版扫描档案（12 卷） | wstein.org/sga | extra/SGA-archive/ |
| Conrad《SGA 3 讲义》 | Stanford | extra/Conrad/ |
| Vistoli / Nitsure / Kleiman 预印本 | arXiv | extra/arXiv/ |

## 版本说明

| 系列 | 版本性质 | 本库所收 |
| --- | --- | --- |
| EGA | 历史定本 | I：1971 年第 2 版；II–IV：IHES 原刊 |
| SGA | 历史定本 | Springer LNM 原版；SGA 4 用 2008 重排版 |
| FGA | 历史定本 | 1962 年汇辑本 |
| FGA Explained | 2005 年定本 | AMS 2005（2019 影印） |
| Stacks Project | 持续更新 | 官网 2026-07-14 版（ed88ff78，7654 页）＋ 2023 版对照 |

只有 Stacks Project 有「最新版」概念；其余四套已定型。Stacks 官网：stacks.math.columbia.edu/download/book.pdf

## 完整性校验

MANIFEST.sha256 收录全部文件（原著、中文译本、英文源码、增补资料）的 SHA-256 与相对路径：

~~~bash
sha256sum -c MANIFEST.sha256
~~~

## 版权与使用范围

EGA、SGA、FGA 由 Springer、IHES、North-Holland 等出版；FGA Explained 由 AMS 出版；
官方中译版权属高等教育出版社；Stacks Project 以开放许可维护（中文译本为 GFDL-1.2-or-later）。
**本仓库为私有仓库**，仅作个人研究、翻译与编撰参照，不再分发、不用于商业用途。

_清单生成于 2026-10-21 04:06；共 1042 个文件，合计 1540.6 MB。_
