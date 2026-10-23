# SGA 6 简体中文原生重建工作稿

当前已恢复原书全部可识别内容，并完成一轮独立逐页保真对读。第 XI 讲历史上未写成、未出版，保留原书说明及后续编号。当前原生合卷为 441 页；最终排版变动页复看及源码 ZIP 独立重编译尚在进行，不能把旧 R2 的验证套用于本稿。现行机器可读状态见 `PROGRESS.json`。

入口为 `main.tex`、`build/SGA6-zh-CN.pdf` 和 `SGA6-zh-CN-source.zip`。在本目录执行 `sh build.sh`，以禁止 shell escape 的 XeLaTeX 编译两遍。需 TeX Live 2025 或兼容环境，安装 fontspec、amsmath/mathtools、mathrsfs、tikz-cd、enumitem、longtable/booktabs、hyperref/hyperxmp、microtype，以及 Noto Serif/Sans/Mono CJK SC、Latin Modern Roman 字体。固定版 ctex、xeCJK、zhnumber 及 LPPL 源文件位于 `dependencies/`；字体未捆绑。解包后无需原扫描 PDF 或联网即可编译。

版式依本书 LNM225 黑黄封面、开本比例与讲次层级适配中文；正文、数学、图式、丛书题名页、出版说明、196 条丛书目录及封底均为原生 LaTeX/TikZ。封二受贴纸遮挡部分据同年 LNM228 的原版封二逐行核对恢复，证据见 `audits/R3-PUBLISHER-WITNESS.json`。没有替换原始扫描件，也没有页面贴图或图像数学。

全部 700 个原印页的对读台账见 `audits/R3-ORIGINAL-COVERAGE.json`；原书印页690为空白。现有中文译本及其他作者目录未改。原书自身的疑误均以可见译校注说明，不补造假设或证明；内容保真审读不等于对全书数学有效性作保证。

当前两遍构建已退出成功，缺字、未定义控制序列、未定义引用、横纵溢出及越出纸页的文字块均为零。全部1492个英文稳定目标保留；中文1525个目标无重复或悬空引用。保留5条字体警告（中文斜体回退正体及不超过1pt的数学字号替代）。见 `audits/MECHANICAL.json`。

R2历史暂停及424页验证分别保存在 `PAUSED.md`、`audits/R2-REPLAY.json` 和 `audits/R2-FINAL_SOURCE_SNAPSHOT.json`。用户已于2026-10-22恢复项目。现行441页的最终视觉与源码包验证完成后将在本页及R3审计明确记录。
