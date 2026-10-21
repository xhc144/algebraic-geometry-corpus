# SGA 5 简体中文原生重建

状态：指定底本中十篇已出版报告、全部证明与附录、两套索引的简体中文首译已完整覆盖；另补齐法文原版卷首材料。逐篇独立代理对译审阅已完成，修订记录见 `qa/`。这仍是待进一步数学校勘的译稿，不是人工认证定本。底本自身的公式/引用疑点未被编译成功所消除。详见 `SOURCE_COVERAGE.tsv` 和 `qa/FINAL_STATUS.json`。

底本为指定英文 `06_SGA5_EN_COMPLETE_PUBLISHED_CONTENT_READER.tex`；SHA-256 和 ZIP 清单核验结果见 `source-audit/provenance.json`。SGA 5 松散 TeX 与经验证 ZIP 内主文件逐字节相同。另发现英文 reader 缺少原版卷首材料，`00-frontmatter.tex` 因而依据只读法文原版 PDF 第 2–11 页补充原生重建，未使用页面叠图。原导言的 VII/VIII 笔误、交换迹措辞、XIV=XV 历史编号均不暗改。

封面沿用本书 LNM 589 的文字层次、两道横线和留白关系，中文正文保留各报告自己的层次、编号、定义证明边界；纸张扩大到 A4 以容纳中文及原生交换图。未采用其他书的统一模板，也未复制出版社图标。原书原版目录页码与本译稿重新生成的目录分别呈现。

## 构建

在本目录运行 `./build.sh`。需要 XeLaTeX、TeX Live 的 fontspec、AMS、TikZ/tikz-cd、hyperref、enumitem、microtype、ulem，以及系统字体 Noto Serif/Sans CJK SC、Latin Modern。不捆绑字体。为适配本环境所需的 ctex、xeCJK、zhnumber 和 ulem 官方标准运行宏已随 `texmf/` 提供，构建脚本自动使用相对目录，无外部临时路径依赖。全部公式、文字、交换图均为原生 TeX/TikZ；本工程不读取原版 PDF。

源内容完整性、译文校对、数学核验、真实编译和视觉检查分开记录。编译通过不构成全书数学或翻译质量认证。疑似继承错误保持可追溯记录，不以编译成功掩盖。


独立源码包为 `SGA5-zh-CN-source.zip`，其中的 `SOURCE_BUNDLE_MANIFEST.sha256` 校验全部源码成员；顶层 `SHA256SUMS` 校验最终 TeX/PDF/ZIP。源码包不依赖原版或英文 PDF。`figures/README.md` 说明原生图的位置。
