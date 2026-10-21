# SGA 5 简体中文原生重建

状态：指定底本中十篇已出版报告、全部证明与附录、两套索引及法文原版卷首材料已完整翻译。本轮又完成有明确边界的独立内容复核：64项既有疑点、18项新增发现，共82项均有法文原页依据和裁定；已修正可确定的错误，修订后82项再次验收。PDF末尾的“校勘说明”保留原读法和依据。详见 `SOURCE_COVERAGE.tsv`、`qa/FINAL_STATUS.json` 及 `qa/content-verification-20261021/`。

四处原文疑义仍明确保留范围：I 2.1证明的失效引文、III B 6.15额外的平凡作用假设、XII (6.4.7)对任意分歧覆盖的论证、导言对偶概述的(I,VII)编号。没有把这些事项称为已证明，也没有据此虚构缺文。这是独立代理检查的译稿，不是专业人工审定；全文源译忠实度检查与针对疑点的法文核对，也不等同于逐句校勘整部法文本。

底本为指定英文 `06_SGA5_EN_COMPLETE_PUBLISHED_CONTENT_READER.tex`；SHA-256 和 ZIP 清单核验结果见 `source-audit/provenance.json`。SGA 5 松散 TeX 与经验证 ZIP 内主文件逐字节相同。英文 reader 缺少的原版卷首材料，依据只读法文原版 PDF 第2–11页补充原生重建，未使用页面叠图。导言、正文及索引的校订均在校勘说明中记录；XIV=XV等历史编号另作解释。原版和英文本均未改动。

封面沿用本书 LNM 589 的文字层次、两道横线和留白关系，中文正文保留各报告自己的层次、编号、定义证明边界；纸张扩大到 A4 以容纳中文及原生交换图。未采用其他书的统一模板，也未复制出版社图标。原书原版目录页码与本译稿重新生成的目录分别呈现。

## 构建

在本目录运行 `./build.sh`。需要 XeLaTeX、TeX Live 的 fontspec、AMS、TikZ/tikz-cd、hyperref、enumitem、microtype、ulem，以及系统字体 Noto Serif/Sans CJK SC、Latin Modern。不捆绑字体。为适配本环境所需的 ctex、xeCJK、zhnumber 和 ulem 官方标准运行宏已随 `texmf/` 提供，构建脚本自动使用相对目录，无外部临时路径依赖。全部公式、文字、交换图均为原生 TeX/TikZ；本工程不读取原版 PDF。

源内容完整性、译文校对、数学核验、真实编译和视觉检查分开记录。`adjudication-ledger.json`汇集全部裁定和精确补丁，`application-verification.json`验证所有正文改动均能还原为已审阅的初稿哈希；原公式编号和环境序列保持。`tools/verify_collation.py`可在独立源码包中复核这一点。`prepare_collation.py`只生成裁定汇总和附记；`apply_collation.py`用于初稿快照，默认仅试运行，已应用的稿件无需重跑。


当前PDF为271页，三遍XeLaTeX编译通过；全部页面已渲染并查看缩略总览，另放大检查22页（包括全部7页校勘附记）。缺字、溢出、未定义引用均为0；保留3条rsfs字体尺寸替代提示和4条Underfull段落间距提示。独立解压构建的每页文字、字词位置及渲染像素与主构建相同，证据见`qa/clean-replay.json`。

独立源码包为 `SGA5-zh-CN-source.zip`，其中的 `SOURCE_BUNDLE_MANIFEST.sha256` 校验全部源码成员；顶层 `SHA256SUMS` 校验最终 TeX/PDF/ZIP。`FINAL_ARCHIVE_VERIFICATION.json`在包外记录最终ZIP哈希、全部成员验证和编译输入与独立复建的一致性，避免归档自引用。使用保留Unix权限的解压工具后运行`./build.sh`；若解压工具丢失执行权限，可运行`bash build.sh`。源码包不依赖原版或英文 PDF。`figures/README.md` 说明原生图的位置。
