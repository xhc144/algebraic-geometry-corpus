# 构建与检查

需要 XeLaTeX、book、CTeX/xeCJK、Latin Modern、AMS、mathrsfs、mathtools、TikZ/tikz-cd、adjustbox、enumitem、multicol、hyperref，以及 Noto Serif CJK SC / Noto Sans CJK SC / Noto Sans Mono CJK SC 系统字体。通常使用包含中文支持的完整 TeX Live 即可；不附带字体文件。

在本目录执行：

```sh
python tools/refresh_checkpoint.py
mkdir -p build
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

`chapters-current.tex` 只纳入真实存在的中文稿。缺失篇章和剩余源段落没有用英文正文、占位符或摘要补足。单篇的部分译稿在源段落边界处停止，完整性只按 `coverage/` 记录判断。

本环境原有 TeX Live 2025/dev 缺少中文支持。曾尝试 CTAN 2026 的新 CTeX，但它要求更新的 LaTeX 内核，未采用。实际本地构建使用 Debian 官方 `texlive-lang-chinese_2024.20250309-1_all.deb` 和 `texlive-lang-cjk_2024.20250309-1_all.deb`，解包至 `/tmp/sga3-tex-deps/debian/`，通过 `TEXINPUTS=/tmp/sga3-tex-deps/debian/usr/share/texlive/texmf-dist/tex//:` 搜索，不改变系统安装。标准完整 TeX Live 不需要这一临时路径。preamble 中移除了本分工完全未调用的 `stmaryrd` 依赖；未替换任何数学符号。

须分别检查编译错误、缺字、重复标签、未定义引用、溢出、原生图形和渲染页面。源宏 `SGARefLink` 对缺失目标会退化为普通文字，故“日志无 undefined”不能证明链接完整；需同时查看静态引用审计，区分前半部外部引用、尚未翻译的后续目标及底本原有错链。原有纸本页码与公式编号不应改为本稿页码。

任何完整性、数学正确性或逐页检查声明都必须有相应实证。未完成、未检查或失败的项目必须明记。
