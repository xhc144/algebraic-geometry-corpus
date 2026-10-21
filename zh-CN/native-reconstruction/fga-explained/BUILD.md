# 构建

在本目录运行：

```sh
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

先建立 `build/`。需要 XeLaTeX、CTeX/xeCJK、amsmath、amsthm、TikZ/TikZ-CD、mathrsfs、enumitem、fancyhdr、geometry、hyperref，以及 Latin Modern、Noto Serif CJK SC / Sans CJK SC / Sans Mono CJK SC 字体。它们都是标准 TeX 或自由字体依赖；源码包不捆绑字体。不能把缺失字体的替代构建当作验收通过。

本执行环境已有 XeTeX（TeX Live 2025/dev，LaTeX 2024-11-01），但缺少 CTeX。为使验证可实际执行，CTeX、xeCJK、zhnumber 的 TeX Live 2024 tlnet-final 包已安装在临时目录 `/tmp/fga-texmf`，通过 `TEXMFHOME=/tmp/fga-texmf` 调用。最初尝试的 2026 当前 CTeX 与本环境旧 LaTeX 不兼容，未用于最终构建。临时缓存位置为 `XDG_CACHE_HOME=/tmp/fga-cache`，未修改系统路径或其他项目。

本地 OCR 命令：`python3 scripts/ocr_scan.py --workers 6`。只使用 Tesseract 本地免费识别，220 dpi 灰度，英文语言模型。数学和图形须另对照扫描；自动 OCR 不算校订。

编译成功只说明语法和字体依赖可用。未译内容、原书疑似笔误、参考文献交叉引用、实际打开检查的页面、缺字和溢出等状态分别记录，不以一次编译代替内容完整性检查。
