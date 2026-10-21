# 构建与核验

在本目录运行：

```sh
bash build.sh
```

使用 XeLaTeX 两遍编译，关闭 shell escape。`assemble.py` 要求 183 个中文组件全部存在；缺组件即停止，避免把缺页构建误作完整稿。构建不依赖英文原文件或原 PDF，也不访问网络。

系统要求：XeLaTeX、常规 TeX Live 宏包（amsmath、amssymb、mathtools、fontspec、TikZ、enumitem、geometry、hyperref、fancyhdr 等）、`tar`、Python 3，以及 Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC 字体。本环境已具备这些系统依赖。

`dependencies/` 内固定保存 ctex、xeCJK、zhnumber、ulem 的标准 TeX Live 运行包，构建时只把 `tex/` 树解入 `build/texmf`，不会安装到系统或更改全局配置，不捆绑字体。来源、校验和及 LPPL 信息见 `DEPENDENCIES.json` 及包内原始文件头。初次采用最新版 ctex 时与环境内旧 LaTeX 内核不兼容，现已固定兼容版本；此前分章“缺包失败”记录保留，最终集成构建已经通过。

输出为 `SGA7-II-zh-CN.pdf`，中间文件位于被忽略的 `build/`。原生图形均在相应章节 TeX 内，无须原扫描图。版式相关的中文下划线使用 xeCJKfntef；数学下划线保持数学命令。

在原仓库中运行 `python3 audit.py` 可重新核对冻结英文底本与译文；该审计需要仓库中的英文源，但独立编译不需要。审计不证明原书数学正确性，也不代替逐句专业校订。

`render_review.py` 依赖 PyMuPDF 与 Pillow，仅用于生成布局审查图；编译 PDF 不需要这两个包。`make_source_zip.py` 生成带逐文件 SHA-256 清单的源码包，排除构建缓存、重复 PDF 和 ZIP 自身。
