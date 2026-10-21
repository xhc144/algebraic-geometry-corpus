# SGA 4 前半部原生中文重建

授权范围与唯一输出目录为 `zh-CN/native-reconstruction/sga4-a/`。分配的是完整出版次序前 10 篇：I、II、III、IV、V、V bis、VI、VII、VIII、IX（全书 20 篇，含 V bis）。X 起属于另一作者。本目录仅是正在翻译的工作稿；不得因存在 PDF 或 ZIP 而认定十篇已完成。

底本为仓库内通过发布清单 SHA-256 验证的 `00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip` 内 SGA 4 原生源工程及整合稿。松散 TeX 与 ZIP 内稿的唯一差别是 554 处 CRLF 被改为 LF；正文逐字相同。原文件未改动。精确哈希、闭包和篇目见 `audit/SOURCE_AUDIT.json`。

排版沿用底本 `amsbook.cls`、`smfthm.sty`、罗马篇号、原有语义标签、页边原页码、Xy-pic 原生交换图。封面依照原始法文扫描本第一页的居中标题层次重建，中文采用 Noto 宋体；没有原 PDF 页面、图像公式或页面叠加。Linux Libertine O 与 XITS Math 在此环境缺失，西文改用 Nimbus Roman，数学改用 Latin Modern Math；这是已明示的字体适配，并非原字体复刻。第三方 class/style 未修改。

在本目录运行：

```sh
mkdir -p build
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
```

依赖：XeLaTeX、fontspec、xeCJK、unicode-math、amsmath、Xy-pic、hyperref、xr-hyper、xcolor、xspace、pifont；Noto Serif/Sans/Mono CJK SC、Nimbus Roman、Latin Modern Math。未打包字体。`support/preamble-zh.tex` 中 Nimbus Roman 使用此环境的标准字体目录；其他系统可改为已安装的同名字体定位方式。

实际覆盖、编译和审校状态以 `PROGRESS.json`、`audit/VALIDATION.json` 为准。源文疑点单列在各节段 `*-review.md`；原文数学不作静默更正。编译通过、源文完整覆盖、逐段语言审校与法文原文数学核对是四件不同的事。
