# 构建与检查

本工程仅包含本卷的新增中文译稿，不替换英文或法文底本，也不修改已有中文译本。
中文书名页取法文档案首页的居中分组；正文沿用报告标题与命题的下划线层级、左侧公式编号和朴素页眉。不是通用讲义模板。

依赖：XeLaTeX、latexmk、ctex、AMS、mathtools、TikZ（cd、arrows.meta）、enumitem、ulem、fancyhdr、hyperref，
以及系统字体 Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC、Latin Modern Mono。
不随源包分发字体，不需网络或付费服务。

在本目录执行（独立源码包同样适用）：

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

`main-II.tex` 可独立构建报告 II。`main.tex` 汇编已保存的中文组件；实际覆盖以 `PROGRESS.json` 和 `qa/coverage.json` 为准。
缺少的报告段落不以英文或占位符充作译文。
跨卷引用及未译部分的引用保留印刷编号，不为其虚构超链接目标；`qa/cross-references.json` 列出各类目标。

编译成功、数学符号机械比对、逐段翻译完整性、人工数学校订、逐页视觉检查是不同项目，必须分别记录。

在原仓库内可另执行 `python3 tools/audit.py`，以锁定的英文读者 TeX 作逐组件核验。
独立源码包不复制英文、原刊 PDF 或字体；因此运行源文对比脚本时须另有仓库底本，编译中文正文则不需要它们。

本轮实测内核为 TeX Live 2025/dev（LaTeX 2024-11-01 patch2），使用 CTeX2.5.10、xeCJK3.9.0、zhnumber3.0。
初始系统缺少中文宏包，最新 CTAN 版又要求更新内核，故在临时 TEXMF 中从 CTeX 官方仓库的
`ctex-v2.5.10` 标签生成兼容宏包（提交 `13a22565bdd14d750b604c2f1ed0fa1938cb6cd4`）。
实际验证命令在上述 `latexmk` 前加 `TEXMFHOME=/tmp/sga7-texmf-2024 XDG_CACHE_HOME=/tmp/sga7-cache`；
这两个路径是本轮环境配置，不是中文工程的文件依赖。在正常安装相应宏包的系统中无需这两个环境变量。
