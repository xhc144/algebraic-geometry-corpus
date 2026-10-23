# SGA 6 简体中文原生重建工作稿

已完成原书全部可识别内容的原生重建，并完成一轮全卷独立逐页保真对读及排版核验。交付入口为 `main.tex`、`build/SGA6-zh-CN.pdf`（441页）和 `SGA6-zh-CN-source.zip`。第XI讲历史上未写成、未出版，保留原书说明和后续编号；不计作已译，也未补造。准确覆盖及审校边界见 `PROGRESS.json`。

在本目录执行 `sh build.sh`，以禁止shell escape的XeLaTeX编译两遍。需TeX Live2025或兼容环境，安装fontspec、amsmath/mathtools、mathrsfs、tikz-cd、enumitem、longtable/booktabs、hyperref/hyperxmp、microtype，以及Noto Serif/Sans/Mono CJK SC、Latin Modern Roman字体。固定版ctex、xeCJK、zhnumber及LPPL源文件位于 `dependencies/`；字体未捆绑。解包后无需原扫描PDF或联网即可编译。31个本版原生TeX文件及所有依赖均在源码包内。

版式依本书LNM225黑黄封面、开本比例与讲次层级适配中文。正文、数学、图式、丛书题名页、出版说明、196条丛书目录和封底均为原生LaTeX/TikZ；最终PDF没有栅格图像资源。封二被贴纸遮挡部分据同年LNM228原版封二逐行核对恢复，证据见 `audits/R3-PUBLISHER-WITNESS.json`。原始扫描件、既有中文资料及其他作者目录未改。

全部700个原印页（含原印空白690页）、前置材料、参考文献、234项术语及符号索引均已逐页对读，台账见 `audits/R3-ORIGINAL-COVERAGE.json`。原书自身的疑误以相邻译校注说明，未补造假设或证明。一次独立保真审读不等于对原书全部数学论证作出有效性认证，本稿仍称工作稿。

最终合卷和源码ZIP独立解包构建都实际完成两遍、退出0；全部441页的提取文字和108dpi RGB像素逐页一致。两份PDF的二进制哈希因构建元数据不同而不同，不冒称PDF逐字节相同。构建记录见 `audits/R3-REPLAY.json` 与 `R3-REPLAY-PAGEHASHES.json`。最终打包只更新审计/状态元数据；115项冻结TeX、依赖和构建脚本逐字节与实际重编译包相同，核验见 `audits/FINAL_ARTIFACTS.json`。

缺字、未定义控制序列、未定义引用、横纵溢出及越出纸页的文字块均为零。全部1492个英文稳定目标保留；中文1525个目标无重复或悬空引用，已在实际PDF目的地复核。保留5条字体替代/字号提示、12条Underfull提示及3条固定依赖包的名称提示；对应页面均已看图，没有据这些警告声称“零警告”。见 `audits/MECHANICAL.json` 及重编译日志计数。

视觉核验先实际逐页查看442页冻结稿，再复看441页修订版的98个变动页和最后7个变动页；未变页以逐像素相同比对承接真实查看记录。全部431个编号页页脚顺序另作机械核验。已报告的游离标记、标点、孤立标题和图标签拥挤均解决；脚注157在正常行首随“所以”出现，清楚可读，作为非阻断换行观察保留。完整证据链见 `audits/R3-NATIVE-VISUAL-COMPLETION.json`。

用户2026-10-21的暂停及旧424页验证只作历史记录保存在 `PAUSED.md`、`audits/R2-REPLAY.json` 等；项目于2026-10-22获明确恢复。旧394/424/434页审计不能代替当前441页证据。当前无已识别未译原页或访问阻断。父线程负责全局索引与合入，本目录不修改全局文件。

## 当前产物校验

根目录 `DELIVERABLES.sha256` 按当前实际文件字节生成，覆盖主文件、PDF、源码ZIP、进度和覆盖表。它和 `audits/FINAL_ARTIFACTS.json` 是库外层产物记录，不嵌入源码ZIP，以避免ZIP包含自身哈希。源码包仍保留全部冻结编译输入；独立解包编译按上文命令执行。
