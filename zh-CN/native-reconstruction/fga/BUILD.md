# FGA 编译

保留本书上游book、A4/oneside/fleqn、标题/页眉层级、Baskervaldx拉丁字体和Esstix/RSFS数学字母；中文用Noto Serif/Sans/Mono CJK SC。没有跨书统一模板或源页覆盖。

需要XeLaTeX、BibTeX、ctex/xeCJK、biblatex（BibTeX后端）、Baskervaldx、Esstix、mathalfa、titlesec、csquotes、cleveref及上述字体。字体不随包捆绑。TeX Live2022须用兼容biblatex/ctex版本；实际环境的公开依赖来源/散列见source/TEX_DEPENDENCIES_*.json。

```sh
python tools/build.py
python tools/package.py
```

本项目新写构建工具串行运行XeLaTeX、BibTeX、XeLaTeX、XeLaTeX，禁用shell escape，日志留在build/。未执行上游shell脚本。中文PDF在outputs/FGA-zh-working.pdf。

单文件TeX内嵌全部正文、前导定义及书目，仍需公开TeX/字体依赖。放入空目录运行：

```sh
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error FGA-zh-working-standalone.tex
bibtex FGA-zh-working-standalone
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error FGA-zh-working-standalone.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error FGA-zh-working-standalone.tex
```

source/en-latex/为恢复九个生成输入后的完整英文比对工程。上游build提交明确对应main，全部127个.tree blob与本库逐一一致；SOURCE_LOCK.json固定提交与散列。tools/recover_inputs.py仅用锁定本地XML/XSLT，禁用网络/外部实体，不碰中文正文。

SOURCE_NOTES.json和source/reviews/区分法文有据修正与来源本身疑误。全书、源码包及单文件独立重建状态见PROGRESS.json。biblatex的BibTeX fallback提示是预期信息。源码包过程XML/映射尚未应用全部校改，以chapters/*.tex为排印源。
