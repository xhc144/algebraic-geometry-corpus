# SGA 4 前半部原生中文重建

授权范围与唯一输出目录为 `zh-CN/native-reconstruction/sga4-a/`。分配的是完整出版次序前 10 篇：I、II、III、IV、V、V bis、VI、VII、VIII、IX（全书 20 篇，含 V bis）。X 起属于另一作者。本目录已完成这十篇的全文翻译，含定义、陈述、证明、例子、附录、注释及参考文献，并补回英文工程漏收的两篇序言和前两卷全部索引。它已完成一轮独立法中全文对读，数学疑点按证据订正或明示保留；不声称所有证明均重新证明或全部原扫描均已逐字视觉通校。

底本为仓库内通过发布清单 SHA-256 验证的 `00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip` 内 SGA 4 原生源工程及整合稿。松散 TeX 与 ZIP 内稿的唯一差别是 554 处 CRLF 被改为 LF；正文逐字相同。原文件未改动。精确哈希、闭包和篇目见 `audit/SOURCE_AUDIT.json`。

排版沿用底本 `amsbook.cls`、`smfthm.sty`、罗马篇号、原有语义标签、页边原页码、Xy-pic 原生交换图。封面依照原始法文扫描本第一页的居中标题层次重建，中文采用 Noto 宋体；没有原 PDF 页面、图像公式或页面叠加。Linux Libertine O 与 XITS Math 在此环境缺失，西文改用 Nimbus Roman，数学改用 Latin Modern Math；这是已明示的字体适配，并非原字体复刻。第三方 class/style 未修改。

在本目录运行：

```sh
mkdir -p build
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
```

依赖：XeLaTeX、fontspec、xeCJK、unicode-math、amsmath、Xy-pic、TikZ（arrows.meta、decorations.pathreplacing）、longtable、hyperref、xr-hyper、xcolor、xspace、pifont；Noto Serif/Sans/Mono CJK SC、Nimbus Roman、Latin Modern Math。未打包字体。Nimbus Roman 显式选用 OTF 字体，避免 fontconfig 误选同名 Type1 字体。在非本系统字体目录的环境中，西文字体自动回退到 TeX Live 的显式 Latin Modern OTF；CJK 字体及数学字体仍须安装。

实际覆盖、编译和审校状态以 `PROGRESS.json`、`audit/VALIDATION.json` 为准。源文疑点单列在各节段 `*-review.md`；原文数学不作静默更正。编译通过、源文完整覆盖、逐段语言审校与法文原文数学核对是四件不同的事。

原始扫描本中英文源工程漏收的两篇序言及第一、二卷索引另按原页补译，保留原索引顺序和原书篇节号。各源页边界、逐页核对记录在对应 review 文件；索引引用的篇节号不是中文成品页码。

最终交付为 `main.tex`、`sga4-a.pdf`、`sga4-a-source.zip`；ZIP 内含当前完整 TeX、原生图、class/style、xeCJK 运行依赖与审计记录，可在上述依赖齐备的环境独立编译，无须原始 PDF 或英文源。仅运行源文对照审计脚本时才需要原仓库的英文 ZIP。先前 `sga4-a-I.pdf` 与 `sga4-a-I-source.zip` 是早期第一篇检查点，其状态保留在 `audit/VALIDATION-I-CHECKPOINT.json`，不代表当前修订。

本分册七次明确引向 X–XIX 的引用保留可见篇节文字。五个目标均由完整英文源核实；独立分册内不创建伪标签，也不生成无效本地链接。`support/external-references.tex` 仅对这五个明确目标处理；若整合版已有真实标签，则自动使用原超链接。其余任何未定义引用照常报告。

原文中编号、箭头和残缺引文的疑点未批量“修正”；见各篇审校记录、`audit/REFERENCE_AUDIT.md` 与独立编号复核。`audit/FULL_CHUNK_MAP.json` 给出全部19正文区段的精确底本行界；`tools/check_full_scope.py` 可重现数学片段与结构差异盘点。

2026-10-22用户已明确恢复审校；历史暂停边界见 `PAUSED.md`，当前状态见 `PROGRESS.json`。最终独立源码包已实测两遍编译，463页，与工作目录PDF逐页提取文本完全一致。

本轮续校已完成全分配范围的一轮独立法中逐段对读，详见 `audit/review-20261022/STATUS.md` 与六份分章报告。它们区分完整文字对读、原扫描定点视觉核验和未裁定的原版数学问题。新 `zhreviewnote` 使用单独的“译校”脚注标记，不改变作者和既有编者注的编号。旧的审校记录保留为历史，后续结案以本轮报告为准。
