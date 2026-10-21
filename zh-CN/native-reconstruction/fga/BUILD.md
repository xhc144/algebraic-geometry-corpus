# FGA 原生重建与编译

这是部分中文工作稿，不是全书完成版。当前正文为前言、报告 I 引言及 §§1–2；末式为 (2.7)。原文有的全部陈述与一段证明均保留。其余内容列于 PROGRESS.json。

本书保留上游 `book` 文档类、A4/oneside/fleqn、原有标题与页眉层级，以及 Baskervaldx 拉丁字体、Esstix/RSFS 数学字母。中文用 Noto Serif CJK SC；XeLaTeX 直接使用相同 Baskervaldx 的 OpenType 轮廓，避免字体替代。没有跨书统一模板，没有页图叠加。

需要 XeLaTeX、BibTeX、ctex/xeCJK、biblatex（bibtex 后端）、Baskervaldx、Esstix、mathalfa、titlesec、csquotes、cleveref 等上游依赖，以及 Noto Serif/Sans/Mono CJK SC。TeX Live 2022 环境须使用兼容的 biblatex/ctex 版本；依赖来源及散列在 source/TEX_DEPENDENCIES_*.json。字体不随源码包捆绑。

```sh
python tools/build.py
```

脚本串行执行 XeLaTeX、BibTeX、XeLaTeX、XeLaTeX，禁用 shell escape，并保留实际日志于被忽略的 build/。只报告经过实际检查的结果。中文 PDF 在 outputs/FGA-zh-working.pdf。

source/en-latex/ 包含恢复后的完整英文原生工程，九个正文输入已补齐。它不是中文翻译进度。source/generated-xml/ 来自原作者公开 build 分支，构建提交明确对应其 main，且其全部 127 个 .tree blob 与本库一一相同。SOURCE_LOCK.json 给出固定提交和散列。需要重新生成英文正文时可运行 tools/recover_inputs.py；不下载、不执行仓库旧 shell 脚本，不碰中文作者文件。

英文工程的 BibTeX 标点错误、书目跳转标签仅在本工作目录修复。中文与英文的数学内容差异、法文页码和校记逐条记录于 SOURCE_NOTES.json；其余数学节点通过结构核验。源错误的保留项不冒充已解决。独立数学审校尚未完成。

outputs/FGA-zh-working-standalone.tex 是同一中文稿的单文件版本，内嵌书目数据；仍需上述公开 TeX/字体依赖和 BibTeX。outputs/FGA-zh-working-source.zip 是对应的原生项目源码包，不含扫描页、字体或凭据。
