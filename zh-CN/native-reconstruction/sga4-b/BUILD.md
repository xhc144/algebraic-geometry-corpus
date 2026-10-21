# 构建与核验

本目录是独立的 XeLaTeX 工程，沿用此 SGA 4 英文底稿自带的 AMS/SMF 类、A4 纸张、3 cm 左右边距、2.8 cm 上下边距、罗马讲号、原页码边注与 Xy-pic。`style/localization.tex` 仅负责中文字体、标题与文字宏适配；未套用其他书籍模板。交换图均为可编辑 Xy-pic 代码，无原版页面覆盖、截图公式或扫描图。

依赖：XeLaTeX、fontspec、unicode-math、polyglossia、geometry、hyperref、Xy-pic、xeCJK、etoolbox；字体 Linux Libertine O、XITS Math、Latin Modern Math、Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC。字体不随源码包捆绑；原底稿已使用 unicode-math 与 Unicode 数学字形，按本书源码保留，未机械替换数学符号。

在本目录运行 `bash tools/build.sh`。已装常规 TeX Live 和上述字体的机器不需要本任务执行环境的额外路径。任务环境的中文 TeX 宏包由既有只读环境 `/workspace/.onboarding/tex/usr/share/texlive/texmf-dist/tex//` 提供，缺少的开源 Latin/XITS 字体曾临时下载至 `/tmp/sga4-fonts`，未写入其他仓库或交付包。

如需复核英文底稿与引用，运行 `python3 tools/prepare.py --source-zip /path/to/00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip`。该步骤只读取 ZIP，不执行其中脚本。源码 ZIP 在同一仓库的标准路径可自动定位。独立排版只需要随附的中文 TeX 和 style 文件，不依赖英文 ZIP。

已知的册外引用由冻结源标签清单核实后排成原有讲号/条号，不制造不存在的 PDF 内链。`evidence/SOURCE_AND_REFERENCE_AUDIT.json` 列明这些引用和源文件审计；未核实的引用不制造替代目标。原文 `\sisi` 的不启用旧分支可能含历史失效标签，应与实际编译警告区分。

编译通过仅表示 TeX 结构可构建；源文疑点、数学陈述的正确性、译文首审与独立专业校订是不同事项，分别见 `PROGRESS.json`、各章 `STATUS.json` 及证据文件。交付时的实际编译和页面查看范围由最终 QA 记录给出。

最终日志保留一项源字体限制：Latin Modern Math 的 script ell 没有粗体字重，粗体上下文使用其常规字重；没有缺字。另有原版类路径、旧颜色选项和本环境法文断词模式等非致命提示。最终 QA 分别记录错误、未定义引用、缺字、溢出与这些提示，未将其混为“所有警告清零”。
