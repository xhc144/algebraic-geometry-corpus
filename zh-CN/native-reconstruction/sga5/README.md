# SGA 5 简体中文原生重建

状态：翻译及核验进行中，不是已完成或经过独立数学审校的定本。各章实际覆盖范围见 `qa/*-translation-status.json`。所有文件局限于本目录，原文和已有中文译本不作修改。

底本为指定英文 `06_SGA5_EN_COMPLETE_PUBLISHED_CONTENT_READER.tex`；SHA-256 和 ZIP 清单核验结果见 `source-audit/provenance.json`。SGA 5 松散 TeX 与经验证 ZIP 内主文件逐字节相同。另发现英文 reader 缺少原版卷首材料，`00-frontmatter.tex` 因而依据只读法文原版 PDF 第 2–11 页补充原生重建，未使用页面叠图。原导言的 VII/VIII 笔误、交换迹措辞、XIV=XV 历史编号均不暗改。

封面沿用本书 LNM 589 的文字层次、两道横线和留白关系，中文正文保留各报告自己的层次、编号、定义证明边界；纸张扩大到 A4 以容纳中文及原生交换图。未采用其他书的统一模板，也未复制出版社图标。原书原版目录页码与本译稿重新生成的目录分别呈现。

## 构建

在本目录运行 `./build.sh`。需要 XeLaTeX、TeX Live 的 ctex/fontspec、AMS、TikZ/tikz-cd、hyperref、enumitem、microtype、ulem，以及系统字体 Noto Serif/Sans CJK SC、Latin Modern。不捆绑字体。全部公式、文字、交换图均为原生 TeX/TikZ；本工程不读取原版 PDF。

源内容完整性、译文校对、数学核验、真实编译和视觉检查分开记录。编译通过不构成全书数学或翻译质量认证。疑似继承错误保持可追溯记录，不以编译成功掩盖。
