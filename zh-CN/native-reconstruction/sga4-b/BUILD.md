# 构建与核验

本目录是独立的 XeLaTeX 工程，沿用此 SGA 4 英文底稿自带的 AMS/SMF 类、A4 纸张、3 cm 左右边距、2.8 cm 上下边距、罗马讲号、原页码边注与 Xy-pic。`style/localization.tex` 仅负责中文字体、标题与文字宏适配；未套用其他书籍模板。交换图均为可编辑 Xy-pic 代码，无原版页面覆盖、截图公式或扫描图。

原生 AMS 类默认编号深度为 3，会把本书四级段落的印出条号隐藏。中文适配恢复编号到第 5 级；通过实际 TeX 计数器与源码显式标签逐一核对，348 个有编号标题全部相符，其中包括全部 87 个四级段落。详见 `evidence/HEADING_NUMBER_AUDIT.json`。段落和标签未重编号。最终版另修复五个裸标签的计数继承，将引用绑定到已经印出的条号，并限制编者注脚注格式的作用域，避免污染原著罗马数字脚注；详见 `evidence/LAYOUT_NUMBERING_REPAIRS_20261022.json`。

依赖：XeLaTeX、fontspec、unicode-math、polyglossia、geometry、hyperref、Xy-pic、xeCJK、etoolbox；字体 Linux Libertine O、XITS Math、Latin Modern Math、Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC。字体不随源码包捆绑；原底稿已使用 unicode-math 与 Unicode 数学字形，按本书源码保留，未机械替换数学符号。

在本目录运行 `bash tools/build.sh`。已装常规 TeX Live 和上述字体的机器不需要本任务执行环境的额外路径。任务环境的中文 TeX 宏包由既有只读环境 `/workspace/.onboarding/tex/usr/share/texlive/texmf-dist/tex//` 提供，缺少的开源 Latin/XITS 字体在恢复环境中临时下载至 `/tmp/sga4-resume-fonts`，未写入其他仓库或交付包。

`SGA4-b-zh-CN.tex` 为同步的单文件版本。运行 `python3 tools/flatten.py` 从 `main.tex` 及其实际输入重新生成；正文与本书自带的两个类／定理支持文件均内嵌，单独放入空目录后可用 XeLaTeX 连续编译三遍。编译时会由 `filecontents*` 提取这两个本书支持文件，仍需上述标准宏包与字体。`evidence/FLATTENED_SOURCE.json` 保存输入和生成文件的哈希。

如需复核英文底稿与引用，运行 `python3 tools/prepare.py --source-zip /path/to/00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip`。该步骤只读取 ZIP，不执行其中脚本。源码 ZIP 在同一仓库的标准路径可自动定位。独立排版只需要随附的中文 TeX 和 style 文件，不依赖英文 ZIP。

审计同时保留未经校订的冻结源比较和 89 条明示修订记录（先前三条，本轮新增 86 条），分别依据法文异文、对象类型、次数或上下文定理核实；英法同误的修订不冒称法文异文。`SOURCE_CORRECTIONS.json` 限定唯一上下文，不作全局变量替换。`python3 tools/package.py` 打包当前源码与证据，并更新交付文件的 `SHA256SUMS`；源码包不重复收录 PDF。

已知的册外引用由冻结源标签清单核实后排成原有讲号/条号，不制造不存在的 PDF 内链。`evidence/SOURCE_AND_REFERENCE_AUDIT.json` 列明这些引用和源文件审计；未核实的引用不制造替代目标。原文 `\sisi` 的不启用旧分支可能含历史失效标签，应与实际编译警告区分。

编译通过仅表示 TeX 结构可构建；源文疑点、数学陈述的正确性、译文首审与独立专业校订是不同事项，分别见 `PROGRESS.json`、各章 `STATUS.json` 及证据文件。交付时的实际编译和页面查看范围由最终 QA 记录给出。

`evidence/FINAL_QA.json` 与 `PROGRESS.json` 为当前版本总记录。其余检查文件各自绑定输入或 PDF 哈希：早期 300 页视觉报告和八讲检查点是历史证据，恢复深层段落编号后的当前版为 298 页，前轮视觉报告名为 `NUMBERED_VISUAL_*`；本轮中间检查见 `FINAL_VISUAL_*_20261022.json`，编号修复后的最终检查见 `FINAL_NUMBERED_VISUAL_*_20261023.json`。不得将历史检查范围当作当前文件的复核结果。

最终日志保留一项源字体限制：Latin Modern Math 的 script ell 没有粗体字重，粗体上下文使用其常规字重；没有缺字。另有原版类路径、旧颜色选项、本环境法文断词模式及数学标题在 PDF 书签中去除 TeX 数学标记等非致命提示；正文数学不受书签文本处理影响。最终 QA 分别记录错误、未定义引用、缺字、溢出与这些提示，未将其混为“所有警告清零”。
