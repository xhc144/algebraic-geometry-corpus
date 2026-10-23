# 代数几何文献库

格罗滕迪克学派代数几何基础文献的整理库。这里收录 **EGA、SGA、FGA、FGA Explained 与 Stacks Project** 的原书 PDF、已出版和社区的中英文译本及 LaTeX 源码、相关讲义与预印本，以及本库新译的 SGA 3–7、FGA、FGA Explained 中文稿。

仓库为私有，下载文件需要登录有权限的 GitHub 账号。图形化的概览页在 [docs/index.html](docs/index.html)，下载后用浏览器打开。

## 一览

| 书目 | 原典 | 已有中译 | 本库新译 | 英文译本 |
| --- | --- | --- | --- | --- |
| EGA I–IV | 8 册 | 周健译（全）· 社区 I–III | — | 3 个项目 |
| SGA 1 | ✓ | 数译站 · 社区 | — | ✓ |
| SGA 2 | ✓ | 数译站 | — | ✓ |
| SGA 3 | 合卷 | — | 1334 页 | ✓ |
| SGA 4 | 3 卷 | — | 761 页 | ✓ |
| SGA 4½ | ✓ | — | 200 页 | ✓ |
| SGA 5 | ✓ | — | 271 页 | ✓ |
| SGA 6 | ✓ | — | 441 页 | ✓ |
| SGA 7 | 2 卷 | — | 589 页 | ✓ |
| FGA | ✓ | — | 124 页 | 源码 |
| FGA Explained | 英文原著 | — | 313 页 | 原文即英文 |
| Stacks Project | 2 版 | 社区全译 116 章 | — | 原文即英文 |

## 目录结构

| 目录 | 内容 |
| --- | --- |
| [EGA/](EGA/)、[SGA/](SGA/)、[FGA/](FGA/)、[Stacks/](Stacks/) | 原典 PDF |
| [zh-CN/official/](zh-CN/official/) | 周健译《代数几何学原理》（高等教育出版社，7 册）；另有一份 SGA 1 社区译本 |
| [zh-CN/EGA/](zh-CN/EGA/)、[zh-CN/Stacks/](zh-CN/Stacks/) | Zenodo 社区中译：EGA I–III、Stacks Project 116 章，均含 LaTeX |
| [zh-CN/native-reconstruction/](zh-CN/native-reconstruction/) | 本库新译：SGA 3–7、FGA、FGA Explained 的 PDF、LaTeX 与审校记录 |
| [en/](en/) | 英文译本与源码 |
| [extra/](extra/) | 参考资料：SGA 历史扫描、英文读者版、讲义、预印本、其他中译 |
| [翻译工作流/](翻译工作流/) | 翻译提示词与原则 |
| [docs/](docs/) | 仓库概览页 |

## 原典

年份指原著出版年，页数为 PDF 文件页数。具体文件可能是重排本、影印本或某一时间点的下载版本；SGA 3 合卷含后期重排材料，不是 1970 年印本的逐页扫描。

### EGA《代数几何学原理》

A. Grothendieck、J. Dieudonné 著。

| 卷次 | 书名 | 出版 | 页数 |
| --- | --- | --- | ---: |
| [EGA I](EGA/EGA-1-Le-langage-des-schemas.pdf) | Le langage des schémas<br>概形的语言 | 1971 第 2 版 · Springer Grundlehren 166 | 474 |
| [EGA II](EGA/EGA-2-Etude-globale-elementaire.pdf) | Étude globale élémentaire de quelques classes de morphismes<br>若干态射类的整体初等研究 | 1961 · Publ. Math. IHÉS 8 | 219 |
| [EGA III.1](EGA/EGA-3-1-Etude-cohomologique-1.pdf) | Étude cohomologique des faisceaux cohérents I<br>凝聚层的上同调研究（一） | 1961 · Publ. Math. IHÉS 11 | 249 |
| [EGA III.2](EGA/EGA-3-2-Etude-cohomologique-2.pdf) | Étude cohomologique des faisceaux cohérents II<br>凝聚层的上同调研究（二） | 1963 · Publ. Math. IHÉS 17 | 90 |
| [EGA IV.1](EGA/EGA-4-1-Etude-locale-1.pdf) | Étude locale des schémas et des morphismes de schémas I<br>概形与态射的局部性质（一） | 1964 · Publ. Math. IHÉS 20 | 258 |
| [EGA IV.2](EGA/EGA-4-2-Etude-locale-2.pdf) | 同上 II<br>概形与态射的局部性质（二） | 1965 · Publ. Math. IHÉS 24 | 228 |
| [EGA IV.3](EGA/EGA-4-3-Etude-locale-3.pdf) | 同上 III<br>概形与态射的局部性质（三） | 1966 · Publ. Math. IHÉS 28 | 254 |
| [EGA IV.4](EGA/EGA-4-4-Etude-locale-4.pdf) | 同上 IV<br>概形与态射的局部性质（四） | 1967 · Publ. Math. IHÉS 32 | 360 |

### SGA《博瓦马里代数几何讨论班》

| 卷次 | 书名 | 作者 | 出版 | 页数 |
| --- | --- | --- | --- | ---: |
| [SGA 1](SGA/SGA-1-Revetements-etales-et-groupe-fondamental.pdf) | Revêtements étales et groupe fondamental<br>平展覆盖与基本群 | Grothendieck | 1971 · LNM 224 | 469 |
| [SGA 2](SGA/SGA-2-Cohomologie-locale-des-faisceaux-coherents.pdf) | Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz<br>凝聚层的局部上同调与 Lefschetz 定理 | Grothendieck | 1968 · North-Holland | 148 |
| [SGA 3](SGA/SGA-3-Schemas-en-groupes.pdf) | Schémas en groupes I–III<br>群概形 | Demazure、Grothendieck | 1970 · LNM 151–153 | 1371 |
| [SGA 4.1](SGA/SGA-4-1-Theorie-des-topos-1.pdf) | Théorie des topos et cohomologie étale des schémas, tome 1<br>拓扑斯理论与概形的平展上同调（一） | Artin、Grothendieck、Verdier | 1972 · LNM 269 | 334 |
| [SGA 4.2](SGA/SGA-4-2-Theorie-des-topos-2.pdf) | 同上，tome 2<br>拓扑斯理论与概形的平展上同调（二） | 同上 | 1972 · LNM 270 | 290 |
| [SGA 4.3](SGA/SGA-4-3-Theorie-des-topos-3.pdf) | 同上，tome 3<br>拓扑斯理论与概形的平展上同调（三） | 同上 | 1973 · LNM 305 | 423 |
| [SGA 4½](SGA/SGA-4-5-Cohomologie-etale.pdf) | Cohomologie étale<br>平展上同调 | Deligne | 1977 · LNM 569 | 317 |
| [SGA 5](SGA/SGA-5-Cohomologie-l-adique-et-fonctions-L.pdf) | Cohomologie ℓ-adique et fonctions L<br>ℓ 进上同调与 L 函数 | Grothendieck | 1977 · LNM 589 | 495 |
| [SGA 6](SGA/SGA-6-Theorie-des-intersections.pdf) | Théorie des intersections et théorème de Riemann–Roch<br>相交理论与 Riemann–Roch 定理 | Berthelot、Grothendieck、Illusie | 1971 · LNM 225 | 720 |
| [SGA 7 I](SGA/SGA-7-1-Groupes-de-monodromie.pdf) | Groupes de monodromie en géométrie algébrique I<br>代数几何中的单值群（一） | Grothendieck | 1972 · LNM 288 | 446 |
| [SGA 7 II](SGA/SGA-7-2-Groupes-de-monodromie-2.pdf) | 同上 II<br>代数几何中的单值群（二） | Deligne、Katz | 1973 · LNM 340 | 448 |

### FGA 与 FGA Explained

| 书目 | 书名 | 作者 | 出版 | 页数 |
| --- | --- | --- | --- | ---: |
| [FGA](FGA/FGA-Fondements-de-la-geometrie-algebrique.pdf) | Fondements de la géométrie algébrique<br>代数几何基础 | Grothendieck | 1962 · Séminaire Bourbaki 1957–1962 汇辑 | 208 |
| [FGA Explained](FGA/FGA-Explained-Fantechi-AMS-2005.pdf) | Fundamental Algebraic Geometry: Grothendieck's FGA Explained<br>基础代数几何：FGA 详解 | Fantechi、Göttsche、Illusie、Kleiman、Nitsure、Vistoli | 2005 · AMS SURV 123 | 354 |

### Stacks Project《代数叠项目》

A. J. de Jong 等编写、持续更新的在线参考书。

| 版本 | 文件 | 页数 |
| --- | --- | ---: |
| 2023 版 | [Stacks-Project.pdf](Stacks/Stacks-Project.pdf) | 7586 |
| 官网 2026-07-14 编译版（ed88ff78） | [Stacks-Project-2026-07-14.pdf](Stacks/Stacks-Project-2026-07-14.pdf) | 7654 |
| 中文社区版 | [Stacks-Project-zh-CN.pdf](Stacks/Stacks-Project-zh-CN.pdf) | 8440 |

## 中文译本

### 已出版与社区译本

**周健译《代数几何学原理》**，高等教育出版社，存于 [zh-CN/official/](zh-CN/official/)：

| 卷次 | 书名 | 出版年 | 页数 |
| --- | --- | --- | ---: |
| [EGA I](zh-CN/official/EGA-I-概形语言-周健译.pdf) | 概形语言 | 2018 | 261 |
| [EGA II](zh-CN/official/EGA-II-几类态射的整体性质-周健译.pdf) | 几类态射的整体性质 | 2019 | 243 |
| [EGA III](zh-CN/official/EGA-III-凝聚层的上同调-周健译.pdf) | 凝聚层的上同调 | 2021 | 285 |
| [EGA IV-1](zh-CN/official/EGA-IV-1-概形与态射的局部性质-周健译.pdf) | 概形与态射的局部性质（一） | 2022 | 291 |
| [EGA IV-2](zh-CN/official/EGA-IV-2-概形与态射的局部性质-周健译.pdf) | 概形与态射的局部性质（二） | 2023 | 264 |
| [EGA IV-3](zh-CN/official/EGA-IV-3-概形与态射的局部性质-周健译.pdf) | 概形与态射的局部性质（三） | 2024 | 286 |
| [EGA IV-4](zh-CN/official/EGA-IV-4-概形与态射的局部性质-周健译.pdf) | 概形与态射的局部性质（四） | 2025 | 386 |

**社区译本：**

| 译本 | 范围 | 来源 | 位置 |
| --- | --- | --- | --- |
| EGA I–III 简体中文版 | EGA I、II、III-1、III-2，PDF、单文件 LaTeX 与源码 ZIP | Zenodo | [zh-CN/EGA/](zh-CN/EGA/) |
| Stacks Project 中文 | 116 章，PDF、LaTeX 与源码 | Zenodo | [zh-CN/Stacks/](zh-CN/Stacks/) |
| SGA 1、SGA 2 | 数译站 v2，257 页、176 页 | 数译站 | [extra/数译中译/](extra/数译中译/) |
| SGA 1 | 另一份社区译本，255 页 | 社区 | [zh-CN/official/](zh-CN/official/SGA-1-平展覆盖与基本群-中译.pdf) |

`official/` 目录名不表示其中的 SGA 1 是出版社正式译本。

### 本库新译

2026 年 10 月完成的中文译稿，补上此前没有中文的 SGA 3–7、FGA 与 FGA Explained：9 部书、11 份 PDF、共 4033 页，每份都附可独立编译的 LaTeX 源码。

下载全部：[PDF 汇总包](zh-CN/native-reconstruction/_coord/distribution/AGC-zh-CN-all-PDFs-20261023.zip?raw=true) · [LaTeX 源码汇总包](zh-CN/native-reconstruction/_coord/distribution/AGC-zh-CN-all-sources-20261023.zip?raw=true)（[校验值](zh-CN/native-reconstruction/_coord/distribution/README.md)）

| 书目 | 范围 | 页数 | PDF | 源码 | 编译 |
| --- | --- | ---: | --- | --- | --- |
| SGA 3 前半 | I–XII，含卷首与第一卷索引 | 777 | [PDF](zh-CN/native-reconstruction/sga3-a/sga3-a-zh.pdf) | [ZIP](zh-CN/native-reconstruction/sga3-a/sga3-a-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga3-a/BUILD.md) |
| SGA 3 后半 | XIII–XXVI，含导读与索引 | 557 | [PDF](zh-CN/native-reconstruction/sga3-b/SGA3-b-zh.pdf) | [ZIP](zh-CN/native-reconstruction/sga3-b/SGA3-b-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga3-b/BUILD.md) |
| SGA 4 前半 | I–IX、V bis，含两篇序言与索引 | 463 | [PDF](zh-CN/native-reconstruction/sga4-a/sga4-a.pdf) | [ZIP](zh-CN/native-reconstruction/sga4-a/sga4-a-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga4-a/BUILD.md) |
| SGA 4 后半 | X–XIX | 298 | [PDF](zh-CN/native-reconstruction/sga4-b/SGA4-b-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga4-b/SGA4-b-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga4-b/BUILD.md) |
| SGA 4½ | 八篇报告及卷首、书目 | 200 | [PDF](zh-CN/native-reconstruction/sga4half/SGA4half-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga4half/SGA4half-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga4half/BUILD.md) |
| SGA 5 | 十篇报告、附录、卷首及索引 | 271 | [PDF](zh-CN/native-reconstruction/sga5/SGA5-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga5/SGA5-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga5/README.md) |
| SGA 6 | 已出版各篇、卷首及索引 | 441 | [PDF](zh-CN/native-reconstruction/sga6/build/SGA6-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga6/SGA6-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga6/BUILD.md) |
| SGA 7 I | I、II、VI–IX，含导言及目录 | 300 | [PDF](zh-CN/native-reconstruction/sga7-i/sga7-i-zh.pdf) | [ZIP](zh-CN/native-reconstruction/sga7-i/sga7-i-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga7-i/BUILD.md) |
| SGA 7 II | X–XXII | 289 | [PDF](zh-CN/native-reconstruction/sga7-ii/SGA7-II-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga7-ii/SGA7-II-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga7-ii/BUILD.md) |
| FGA | 前言、八篇报告、书目与勘误 | 124 | [PDF](zh-CN/native-reconstruction/fga/outputs/FGA-zh-working.pdf) | [ZIP](zh-CN/native-reconstruction/fga/outputs/FGA-zh-working-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/fga/BUILD.md) |
| FGA Explained | 第 1–9 章、附录 A/B、书目及索引 | 313 | [PDF](zh-CN/native-reconstruction/fga-explained/FGA-explained-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/fga-explained/FGA-explained-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/fga-explained/BUILD.md) |

**状态：** 这些是修订稿。各卷都已实际编译，并做过模型辅助的源文核对，但还没有经过出版级人工终校。目前缺三处原件材料：SGA 3 2011 年再版新增的卷首、SGA 7 II 原书的 Leitfaden 关系图、FGA VI §0 脚注 (1) 的正文。逐卷范围和缺项见[状态表](zh-CN/native-reconstruction/_coord/RESUMED_STATUS.md)，审校证据见 [reviews/](zh-CN/native-reconstruction/_coord/reviews/)。

**编译：** 各卷依赖不同，请按表中“说明”操作。多数使用 XeLaTeX 和 Noto CJK 字体，字体不随源码包附带。

### 其他代数几何中译

| 原著 | 中译 | 译者 / 来源 | 页数 |
| --- | --- | --- | ---: |
| Vakil, *The Rising Sea* | 上升之海（繁体） | 遠征的小象 / 数译站 | 1010 |
| Hartshorne, *Algebraic Geometry* | 代数几何 | Tzuchien / 数译站 | 408 |
| Milne, *Algebraic Geometry* | 代数几何（未完成） | 鸡煲老公 / 数译站 | 353 |
| Milne, *Lectures on Étale Cohomology* | 平展上同调讲义 | Fingolfin / 数译站 | 219 |
| Alper, *Stacks and Moduli* | 叠与模空间 | Fingolfin / 数译站 | 601 |
| Bourbaki、Serre、Deligne、Raynaud、吴宝珠 | 6 篇文献中译 | 译馆（北大张锦楠） | — |

数译站译本在 [extra/数译中译/](extra/数译中译/)，译馆译本在 [extra/译馆-PKU/](extra/译馆-PKU/)。

## 英文译本与源码

| 项目 | 内容 | 位置 |
| --- | --- | --- |
| KokunoYumeto/ega-en | EGA 0–IV 英文版，PDF 与 LaTeX | [en/KokunoYumeto-ega-en/](en/KokunoYumeto-ega-en/) |
| KokunoYumeto/sga-en | SGA 1–7 英文读者版，PDF 与 LaTeX | [en/KokunoYumeto-sga-en/](en/KokunoYumeto-sga-en/) |
| jcreinhold/ega | EGA I–IV 及未完成的 EGA V，Markdown（mdBook） | [en/jcreinhold-ega/](en/jcreinhold-ega/) |
| jcreinhold/sga | SGA 1–4，Markdown（mdBook） | [extra/jcreinhold-sga/](extra/jcreinhold-sga/) |
| ryankeleti/ega | EGA 社区英译，LaTeX | [en/ryankeleti-ega/](en/ryankeleti-ega/) |
| thosgood/fga | FGA 英译，forester 源码 | [en/thosgood-fga/](en/thosgood-fga/) |
| thosgood/sga | SGA 1、SGA 6 英译（进行中），forester 源码 | [en/thosgood-sga/](en/thosgood-sga/) |
| Zenodo SGA 英文读者版 | 8 份 PDF：SGA 1–7（不含 4½） | [extra/SGA-English-Zenodo/](extra/SGA-English-Zenodo/) |

部分英文译本尚未定稿，不能仅凭文件名认定已完整覆盖法文原件。

## 参考资料

| 资料 | 说明 | 位置 |
| --- | --- | --- |
| SGA 历史扫描 | 12 卷，来自 wstein.org | [extra/SGA-archive/](extra/SGA-archive/) |
| Conrad, *Reductive Group Schemes* | SGA 3 相关讲义 | [extra/Conrad/](extra/Conrad/) |
| Vistoli, *Notes on Grothendieck topologies, fibered categories and descent theory* | arXiv:math/0412512 | [extra/arXiv/](extra/arXiv/) |
| Illusie、Laszlo、Orgogozo, *Travaux de Gabber* | arXiv:1207.3648 | [extra/arXiv/](extra/arXiv/) |
| SGA 1 重排本 | arXiv:math/0206203 | [extra/arXiv/](extra/arXiv/) |

## 翻译工作流

[翻译工作流/](翻译工作流/) 存放翻译提示词：以英文 LaTeX 为底本逐章译成中文 LaTeX，法文原件用来核对疑难处，术语以周健译 EGA 为准。本库新译的分工、术语和审校记录在 [zh-CN/native-reconstruction/_coord/](zh-CN/native-reconstruction/_coord/)。

## 索引与校验

- [译本对照表.md](译本对照表.md)：每部书有哪些版本、哪些格式，以及中译覆盖情况。
- [catalog.json](catalog.json)：机器可读的目录数据，涵盖原典、出版与社区中译、本库新译、英文项目和参考资料，含页数、字节数与 SHA-256。
- [MANIFEST.sha256](MANIFEST.sha256)：原典、已有译本、英文译本与参考资料目录下全部文件的 SHA-256，可用 `sha256sum -c MANIFEST.sha256` 校验。本库新译不在其中，各卷和汇总包另有清单。

## 来源、版权与许可

本仓库是私有的研究与翻译资料库。原著、出版译本、社区译文和代码的权利归各自作者与出版方，收录在这里不代表授予公开传播、再许可或商业使用的权利。

EGA、SGA、FGA 及 FGA Explained 的原著涉及 Springer、IHÉS、North-Holland、AMS 等机构；周健译本由高等教育出版社出版。英文和社区项目的许可只适用于其说明界定的贡献，例如 [EGA 英译许可](en/KokunoYumeto-ega-en/LICENSE)、[SGA 英文权利说明](en/KokunoYumeto-sga-en/LICENSE_AND_RIGHTS.md)、[jcreinhold SGA 许可](extra/jcreinhold-sga/LICENSE)。Stacks Project 及其中文版按各自附带的许可和署名要求使用。
