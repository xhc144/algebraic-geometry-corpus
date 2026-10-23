# 构建与验收

在本目录先建立 `build/`，再运行三遍：

```sh
mkdir -p build
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

需要 XeLaTeX、CTeX/xeCJK、amsmath/amsthm、TikZ/TikZ-CD、mathrsfs、enumitem、fancyhdr、geometry、hyperref、zref-abspage/zref-user，以及 Latin Modern、Noto Serif CJK SC / Sans CJK SC / Sans Mono CJK SC 字体。源码不捆绑字体。直接编译不需要 Python、原扫描、OCR、网络或图片文件。

`python3 scripts/build.py` 执行三遍受限编译，冻结全部 TeX 哈希，核对缺字、未解析引用、溢出、字体警告和 PDF 边界，输出目录根部的交付 PDF。它额外需要 PyMuPDF。`python3 scripts/render_review.py` 渲染所有页面及编号接触表，需要 PyMuPDF 和 Pillow；实际打开查看的页须另记，不用“已渲染”冒充“已目视检查”。

本执行环境的 XeTeX 为 TeX Live 2025/dev、LaTeX 2024-11-01，原先缺少 CTeX。当前使用免费的 TeX Live 2024 tlnet-final 中 ctex、xecjk、zhnumber，安装于 `/tmp/fga-texmf`；公开来源、版本与哈希见 `evidence/tex-dependencies.json`。本环境验证调用方式为 `TEXMFHOME=/tmp/fga-texmf XDG_CACHE_HOME=/tmp/fga-cache python3 scripts/build.py`。未修改系统字体、凭据或其他工程。

`python3 scripts/source_navigation.py prepare` 根据已经核对的 canonical 源页注释安装零宽锚点、保留并链接原索引页码、生成339行源页检索表。它先核对覆盖和重复，再写文件；维护源码或移动页界后才需要重跑。`python3 scripts/source_navigation.py audit` 在完成三遍构建后检查实际 PDF：所有339行数字、716个索引链接、339个回正文链接和所有物理页顶部目的地均须一致。正常从源码 ZIP 编译时，已生成的导航文件随包提供，不需要 Python。

`python3 scripts/package_source.py` 生成确定性的源码 ZIP、内部逐文件 SHA-256 清单及外部 `SHA256SUMS`。ZIP 排除 `build/`、预编译 PDF、ZIP 自身和外部校验和；原扫描位于工程外，也不会打包。解包后在 `fga-explained/` 内按上述命令编译即可。独立重建的实际结果见 `evidence/replay-review.json`，不把旧版本的成功套用到修改后的源码。

OCR 仅作历史识别辅助：`python3 scripts/ocr_scan.py --workers 6` 使用本地免费 Tesseract，需要原始扫描；`evidence/ocr-uncorrected/` 明确不是已译内容。源文完整性和独立内容审校、机械编译、输出页面视觉检查、源码包重建是分别记录的验收项目。
