# 构建与检查

本工程仅包含本卷的新增中文译稿，不替换英文或法文底本，也不修改已有中文译本。
中文书名页取法文档案首页的居中分组；正文沿用报告标题与命题的下划线层级、左侧公式编号和朴素页眉。不是通用讲义模板。

依赖：XeLaTeX、latexmk、ctex、AMS、mathtools、TikZ（cd、arrows.meta）、enumitem、ulem、fancyhdr、hyperref，
以及系统字体 Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC、Latin Modern Mono。
不随源包分发字体，不需网络或付费服务。

在本目录执行：

```sh
python3 tools/audit.py
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

`main-II.tex` 可独立构建报告 II。`main.tex` 汇编已保存的中文组件；实际覆盖以 `PROGRESS.json` 和 `qa/coverage.json` 为准。
缺少的报告段落不以英文或占位符充作译文。
跨卷引用及未译部分的引用保留印刷编号，不为其虚构超链接目标；`qa/cross-references.json` 列出各类目标。

编译成功、数学符号机械比对、逐段翻译完整性、人工数学校订、逐页视觉检查是不同项目，必须分别记录。
