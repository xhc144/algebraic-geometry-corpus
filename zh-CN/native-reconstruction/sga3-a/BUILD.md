# 构建与检查

从本目录执行 `latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex`。

需要 XeLaTeX、ctex、xeCJK、zhnumber、amsmath/amsfonts/amsthm、mathrsfs、mathtools、stmaryrd、TikZ/tikz-cd、adjustbox、enumitem、multicol、etoolbox、hyperref 与 Noto Serif/Sans/Mono CJK SC 字体。字体不随包分发。

当前环境缺少部分 TeX 包，免费公开 CTAN 依赖安装于临时目录；真实构建记录与已知源文问题将记录于 audit/。请以 PROGRESS.json 判断覆盖，不能据 PDF 或 ZIP 的存在推断全文已完成。
