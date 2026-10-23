# 构建与核验

解压源码包，在其根目录执行：

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

需要TeX Live的XeLaTeX、ctex/xeCJK/zhnumber、amsmath/amsfonts/amsthm、mathrsfs、mathtools、stmaryrd、TikZ/tikz-cd、adjustbox、enumitem、multicol、etoolbox、hyperref，以及Noto Serif/Sans/Mono CJK SC字体。字体不随包分发。

本执行环境缺少的免费标准TeX包已恢复到 `/tmp/sga3-texmf-2024`，在此环境构建需前置 `TEXMFHOME=/tmp/sga3-texmf-2024 TEXMFVAR=/tmp/sga3-tex-var XDG_CACHE_HOME=/tmp/sga3-cache`；普通完整TeX Live安装不需要这些临时路径。没有付费API或购买额度。

最终主构建777页；缺字、Overfull、undefined reference、重复PDF目标警告均为零。保留5处Underfull及stmary粗体/CJK小型大写字体替代提示，已区别于缺字。精确日志与独立解压重编结果见audit记录。`scripts/verify_pdf.py`核查实际PDF目标、页面边界、图像对象和逐页文本哈希；`render_contact_sheets.py`只生成审查图片，不参与书稿排版。
