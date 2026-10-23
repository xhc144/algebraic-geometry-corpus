# 代数几何文献与中文译稿

这里收集 EGA、SGA、FGA、FGA Explained 和 Stacks Project 的原始资料、已有译本及相关源码。本轮新增的中文译稿放在 [zh-CN/native-reconstruction/](zh-CN/native-reconstruction/)，提供可直接阅读的 PDF 和可编辑、可独立编译的 LaTeX 源码。

**下载本轮中文成果：**

- **[全部中文 PDF：9 种书、11 份 PDF，共 4033 页](zh-CN/native-reconstruction/_coord/distribution/AGC-zh-CN-all-PDFs-20261023.zip?raw=true)**
- **[全部原生 LaTeX 源码 ZIP](zh-CN/native-reconstruction/_coord/distribution/AGC-zh-CN-all-sources-20261023.zip?raw=true)**

本轮已交付**中文修订稿、可编译源码和分卷核对记录**，尚未完成出版级人工终校。原书疑点、尚未取得的材料和各册审校边界见下文。仓库为私有，下载时需要登录有访问权限的 GitHub 账号。

## 中文译稿目录

以下是 2026-10-23 保存的本轮成果。表中页数是当前中文 PDF 的实际页数，不是外文原书页数。SGA 3、SGA 4 各拆成两份 PDF 便于阅读；这里的分册边界不等同于原版分卷。

| 书目与分册 | 收入范围 | 页数 | 阅读 PDF | 下载源码 | 编译说明 |
| --- | --- | ---: | --- | --- | --- |
| SGA 3 前半 | I–XII，含 VI-A/B、VII-A/B；所选底本卷首及第一卷索引 | 777 | [PDF](zh-CN/native-reconstruction/sga3-a/sga3-a-zh.pdf) | [ZIP](zh-CN/native-reconstruction/sga3-a/sga3-a-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga3-a/BUILD.md) |
| SGA 3 后半 | XIII–XXVI、导读及索引 | 557 | [PDF](zh-CN/native-reconstruction/sga3-b/SGA3-b-zh.pdf) | [ZIP](zh-CN/native-reconstruction/sga3-b/SGA3-b-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga3-b/BUILD.md) |
| SGA 4 前半 | I–IX，含 V bis；两篇序言及前两卷索引 | 463 | [PDF](zh-CN/native-reconstruction/sga4-a/sga4-a.pdf) | [ZIP](zh-CN/native-reconstruction/sga4-a/sga4-a-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga4-a/BUILD.md) |
| SGA 4 后半 | X–XIX | 298 | [PDF](zh-CN/native-reconstruction/sga4-b/SGA4-b-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga4-b/SGA4-b-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga4-b/BUILD.md) |
| SGA 4½ | 八篇报告及卷首、书目等材料 | 200 | [PDF](zh-CN/native-reconstruction/sga4half/SGA4half-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga4half/SGA4half-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga4half/BUILD.md) |
| SGA 5 | 十篇已出版报告、附录、卷首及索引 | 271 | [PDF](zh-CN/native-reconstruction/sga5/SGA5-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga5/SGA5-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga5/README.md) |
| SGA 6 | 已出版各篇、卷首、索引及出版目录 | 441 | [PDF](zh-CN/native-reconstruction/sga6/build/SGA6-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga6/SGA6-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga6/BUILD.md) |
| SGA 7-I | I、II、VI–IX；原卷导言及目录 | 300 | [PDF](zh-CN/native-reconstruction/sga7-i/sga7-i-zh.pdf) | [ZIP](zh-CN/native-reconstruction/sga7-i/sga7-i-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga7-i/BUILD.md) |
| SGA 7-II | X–XXII；另有明确注明的译校补充 | 289 | [PDF](zh-CN/native-reconstruction/sga7-ii/SGA7-II-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/sga7-ii/SGA7-II-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/sga7-ii/BUILD.md) |
| FGA | 前言、八篇报告、书目、补记与勘误 | 124 | [PDF](zh-CN/native-reconstruction/fga/outputs/FGA-zh-working.pdf) | [ZIP](zh-CN/native-reconstruction/fga/outputs/FGA-zh-working-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/fga/BUILD.md) |
| FGA Explained | 第 1–9 章、附录 A/B、卷首、书目及索引 | 313 | [PDF](zh-CN/native-reconstruction/fga-explained/FGA-explained-zh-CN.pdf) | [ZIP](zh-CN/native-reconstruction/fga-explained/FGA-explained-zh-CN-source.zip?raw=true) | [说明](zh-CN/native-reconstruction/fga-explained/BUILD.md) |

FGA 另有 [单文件 LaTeX](zh-CN/native-reconstruction/fga/outputs/FGA-zh-working-standalone.tex)，便于单独编辑。各书沿用各自的封面和标题层级，中文文字、公式及重绘图形保存在原生 LaTeX 中，不用原书 PDF 页面贴图替代排版。

上表就是本轮交付范围。**EGA V 遗稿、后续补编和跨书综合版均不在已交付名单中。** [翻译工作流](翻译工作流/)存放方法与提示词，不能据此认定相应成品已经完成。

## 稿件状态与已知缺口

各册已有真实编译和独立源码包重建记录，也经过模型辅助的独立内容核对。但各册核对底本与覆盖程度不同：部分已做法中全文对照，部分主要对照英文重建底本；不能把整套称为已完成法文逐句终校，更不能把编译通过当作全部数学证明正确的保证。

仍有三类原始材料缺口：

- **SGA 3：2011 年现代再版新增卷首。** 第一卷的编者序、导读及其书目、Michel Demazure 再版序尚未取得正文。这里缺的是现代再版增补，**1970 年原告示与原导言已经译入**。编辑站目录的页标与正式成书分页也须区别，详见[版次及原件核验](zh-CN/native-reconstruction/_coord/reviews/sga3-tome1-edition-frontmatter-20261023.md)。
- **SGA 7-II：原 Leitfaden 关系图。** 现有译稿尚未补入该图；历史 EGA V 引文也仍有未闭合之处。
- **FGA：VI §0 标题脚注 (1) 的正文。** 在已检查的原件及官方勘误中尚未定位，译稿保留说明，没有猜写正文。

此外，各卷仍有原著数学疑点或不完整引文。能够确认的译文错误已经订正；尚不能裁定的内容保留原读法并作说明。SGA 3 前半另有三处引文标为待核。SGA 6 的 XI 篇历史上未写成、未出版，不列为“已译”，也不补造一篇。

详细范围见[逐卷审校与缺口表](zh-CN/native-reconstruction/_coord/RESUMED_STATUS.md)；原件、引用、编译及页面检查的证据见[审核记录](zh-CN/native-reconstruction/_coord/reviews/)。各册已核对的范围、仍待核对的内容和实际编译结果均有记录。

## 阅读、下载与编译

1. **只想读书**：点击表内 PDF 预览；下载可用文件页的下载按钮，或直接下载顶部的全部 PDF ZIP。
2. **需要修改文字或公式**：下载对应源码 ZIP 并解压。全部源码 ZIP 按 `books/` 分书存放，进入所选书的主文件目录即可；各册不依赖原始外文 PDF 来排版。
3. **需要重新生成 PDF**：先打开表内该册的“编译说明”，安装其列明的 TeX 宏包和系统字体，再执行该册命令。各书依赖、主文件名和编译轮次不同，不共用一个构建命令；字体文件没有随包捆绑。

例如，SGA 4 前半使用 XeLaTeX，需 Noto Serif/Sans/Mono CJK SC 等字体及[该册说明](zh-CN/native-reconstruction/sga4-a/BUILD.md)列出的宏包。进入解压后含 `main.tex` 的目录，执行：

```sh
mkdir -p build
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
```

该例生成 `build/main.pdf`。FGA 等使用书目的工程还有不同步骤，请按各册说明操作。

汇总包内附逐文件校验表；外部字节数及 SHA-256 见[下载与校验说明](zh-CN/native-reconstruction/_coord/distribution/README.md)。

## 仓库中的几类资料

| 类别 | 存放位置 | 如何理解 |
| --- | --- | --- |
| 原始资料 | [EGA/](EGA/)、[SGA/](SGA/)、[FGA/](FGA/)、[Stacks/](Stacks/) | 收录的法文、英文原件或历史版本；并非都属于同一版次，也并非都有可编辑源码 |
| 已有出版或社区译本 | [zh-CN/official/](zh-CN/official/)、[zh-CN/EGA/](zh-CN/EGA/)、[zh-CN/Stacks/](zh-CN/Stacks/)、[数译中译](extra/数译中译/)、[译馆](extra/译馆-PKU/) | 本轮开始前已有的独立译本，保留原文件和各自说明 |
| 本轮原生中文译稿 | [zh-CN/native-reconstruction/](zh-CN/native-reconstruction/) | 上表 9 种书的 PDF、LaTeX 与审核记录 |
| 英文译本与源码 | [en/](en/)、[SGA 英文读者版](extra/SGA-English-Zenodo/) | 翻译对照材料；部分尚未定稿，不能仅凭英文文件名认定法文原件已完整覆盖 |
| 参考与方法资料 | [extra/](extra/)、[翻译工作流/](翻译工作流/) | 讲义、预印本、原版扫描档案和工作方法，不能与本轮交付成品混为一谈 |

[原资料格式对照表](译本对照表.md)和[文件目录数据](catalog.json)保留了早期收录盘点；其中的旧覆盖率、文件数量和“没有中译”等状态没有包含本轮全部新增成果，当前中文交付以上表为准。

## 主要书目的关系

| 简称 | 原文书名 | 中文书名 | 性质与角色 |
| --- | --- | --- | --- |
| EGA | Éléments de géométrie algébrique | 《代数几何学原理》 | 系统建立现代代数几何基础的专著，原计划未全部完成 |
| SGA | Séminaire de Géométrie Algébrique du Bois-Marie | 《博瓦马里代数几何讨论班》 | 格罗滕迪克主持的研究讨论班文集，分多个专题 |
| FGA | Fondements de la Géométrie Algébrique | 《代数几何基础》 | 格罗滕迪克关于基础问题的研究报告合集 |
| FGA Explained | Fundamental Algebraic Geometry | 《基础代数几何：FGA 详解》 | 后人的系统讲解与证明补充 |
| Stacks Project | The Stacks Project | 《代数叠项目》 | 持续更新的现代参考书 |

这些书侧重点不同，原著、后人的讲解和持续更新的参考书分别保留，便于互相查证。收录 Stacks Project 不表示本轮对它重新翻译或更新。

## 原始资料索引

以下保留原有书目、原件链接及版本说明。年份主要指原著出版年；具体文件可能是重排版、影印本或某个时间点的下载版本。SGA 3 合卷尤其不能直接视为 1970 年印本的逐页扫描。

<details>
<summary>展开 EGA、SGA、FGA、FGA Explained 与 Stacks 的原件目录</summary>

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
| SGA 3 | Schémas en groupes I–III | 群概形 I–III | M. Demazure, A. Grothendieck (eds.) | 1970 | 对应 Springer LNM 151–153；合卷含后期重排材料 | [SGA-3-Schemas-en-groupes.pdf](SGA/SGA-3-Schemas-en-groupes.pdf) | 14.8 MB |
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
| Stacks Project（收录的官网版本） | The Stacks Project — official current build | 代数叠项目（官网 2026-07-14 编译版） | A. J. de Jong et al. | 2026-07-14（Version ed88ff78） | stacks.math.columbia.edu/download/book.pdf | [Stacks-Project-2026-07-14.pdf](Stacks/Stacks-Project-2026-07-14.pdf) | 36.6 MB |

</details>

## 已有中文译本与参考译本

### EGA：周健译、高等教育出版社版本

现有文件存于 [zh-CN/official/](zh-CN/official/)。下表按仓库实际文件列出，不将原著分册数与中文 PDF 文件数混为一谈。

| 卷次 | 书名 | 出版年 | 页数 | 文件 |
| --- | --- | --- | --- | --- |
| EGA I | 概形语言 | 2018 | 261 | [EGA-I-概形语言-周健译.pdf](zh-CN/official/EGA-I-概形语言-周健译.pdf) |
| EGA II | 几类态射的整体性质 | 2019 | 243 | [EGA-II-几类态射的整体性质-周健译.pdf](zh-CN/official/EGA-II-几类态射的整体性质-周健译.pdf) |
| EGA IV-1 | 概形与态射的局部性质（一） | 2022 | 291 | [EGA-IV-1-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-1-概形与态射的局部性质-周健译.pdf) |
| EGA IV-2 | 概形与态射的局部性质（二） | 2023 | 264 | [EGA-IV-2-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-2-概形与态射的局部性质-周健译.pdf) |
| EGA IV-4 | 概形与态射的局部性质（四） | 2025 | 386 | [EGA-IV-4-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-4-概形与态射的局部性质-周健译.pdf) |
| EGA III | 凝聚层的上同调 | 2021 | 285 | [EGA-III-凝聚层的上同调-周健译.pdf](zh-CN/official/EGA-III-凝聚层的上同调-周健译.pdf) |
| EGA IV-3 | 概形与态射的局部性质（三） | 2024 | 286 | [EGA-IV-3-概形与态射的局部性质-周健译.pdf](zh-CN/official/EGA-IV-3-概形与态射的局部性质-周健译.pdf) |

`official/` 中另存一份 [SGA 1 社区译本](zh-CN/official/SGA-1-平展覆盖与基本群-中译.pdf)；目录名称不表示它是出版社正式中译。

| 来源 | 收录内容 | 入口 |
| --- | --- | --- |
| Zenodo 社区发布包 | EGA I–III 非官方中文 PDF、TeX、源码与核对记录 | [EGA 中文目录](zh-CN/EGA/) |
| Zenodo 社区发布包 | Stacks Project 116 章中文译本及源码；保留原发布版本 | [Stacks 中文目录](zh-CN/Stacks/) |
| 数译站 | SGA 1、SGA 2，以及 Vakil、Milne、Hartshorne、Alper 的相关书籍译本 | [数译中译](extra/数译中译/) |
| 译馆（北大张锦楠） | Bourbaki、Serre、Deligne、Raynaud、吴宝珠等文献中译 | [译馆资料](extra/译馆-PKU/) |

这些译本的来源、版次和核对程度各不相同，引用或继续编辑时应阅读其自身说明；本轮没有替换它们。

<details>
<summary>展开相关教材的原有中译索引</summary>

| 原著 | 中译 | 译者 / 来源 | 页数 | 库内文件 |
| --- | --- | --- | --- | --- |
| Vakil《The Rising Sea》 | 上升之海（繁体） | 遠征的小象 / 数译站 | 1010 | extra/数译中译/ |
| Milne《Lectures on Étale Cohomology》 | 平展上同调讲义 | Fingolfin / 数译站 | 219 | extra/数译中译/ |
| Milne《Algebraic Geometry》 | 代数几何（未完成版） | 鸡煲老公 / 数译站 | 353 | extra/数译中译/ |
| Hartshorne《Algebraic Geometry》 | 代数几何 | Tzuchien / 数译站 | 408 | extra/数译中译/ |
| Alper《Stacks and Moduli》 | 叠与模空间 | Fingolfin / 数译站 | 601 | extra/数译中译/ |
| Bourbaki《交换代数》等 6 篇 | 中译 | 译馆（北大张锦楠） | — | extra/译馆-PKU/ |

</details>

## 英文译本、源码与其他参考

| 来源 | 内容 | 目录 |
| --- | --- | --- |
| KokunoYumeto/ega-en | EGA 英文工作版、PDF 和 LaTeX 工程 | [EGA 英文资料](en/KokunoYumeto-ega-en/) |
| KokunoYumeto/sga-en | SGA 英文工作版、读者版和源码 | [SGA 英文资料](en/KokunoYumeto-sga-en/) |
| ryankeleti/ega、jcreinhold/ega | 另两套 EGA 英译及源码 | [ryankeleti](en/ryankeleti-ega/)、[jcreinhold](en/jcreinhold-ega/) |
| Tim Hosgood | SGA、FGA 英译工程 | [SGA](en/thosgood-sga/)、[FGA](en/thosgood-fga/) |
| Zenodo SGA 英文读者版 | 已收录的英文 PDF | [英文读者版](extra/SGA-English-Zenodo/) |
| jcreinhold/sga | SGA 英译的可检索文本工程 | [英文文本](extra/jcreinhold-sga/) |
| SGA 原版扫描档案 | wstein.org 来源的历史扫描 | [扫描档案](extra/SGA-archive/) |
| Brian Conrad | Reductive Group Schemes 讲义 | [Conrad 资料](extra/Conrad/) |
| Vistoli、Nitsure、Kleiman 等 | 相关预印本 | [arXiv 资料](extra/arXiv/) |

[MANIFEST.sha256](MANIFEST.sha256)是原始收录批次的校验清单，不是当前整个仓库的完整性声明。后续新增中文译稿及汇总包使用各自的清单和编译记录。

## 来源、版权与许可

本仓库为私有研究、翻译与编撰资料库。原著、正式出版译本、社区译文及代码分别保留其作者、出版机构和原有许可说明；收录到仓库或能够下载，不代表仓库统一授予这些作品公开传播、再许可或商业使用的权利。

EGA、SGA、FGA 及 FGA Explained 的原著与出版版本涉及 Springer、IHES、North-Holland、AMS 等机构；周健中译版本涉及高等教育出版社。英文与社区工程的许可只适用于其说明中界定的贡献，不能自动延伸到原著或第三方材料。例如：[EGA 英译许可](en/KokunoYumeto-ega-en/LICENSE)、[SGA 英文来源与权利说明](en/KokunoYumeto-sga-en/LICENSE_AND_RIGHTS.md)、[jcreinhold SGA 译文许可](extra/jcreinhold-sga/LICENSE)。Stacks Project 及其中文发布包按各自附带的许可和署名要求使用。
