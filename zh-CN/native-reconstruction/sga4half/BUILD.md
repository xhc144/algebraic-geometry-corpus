# 构建与核验

入口为 `main.tex`，引擎为 XeLaTeX。所有正文、公式、交换图均为原生 TeX；没有扫描页叠印、图片公式或外部图片依赖。交换图沿用本书原生 Xy-pic 代码。

## 所需环境

- Python 3（仅构建和审计脚本所需，标准库即可）；XeLaTeX 与 BibTeX。
- TeX Live/MiKTeX 标准包：CTeX、xeCJK、zhnumber、fontspec、AMS、Xy-pic、footmisc、enumerate、lmodern、mathrsfs、stmaryrd、microtype、hyperref、fancyhdr、geometry。
- 系统字体：Latin Modern Roman/Sans/Mono、Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC。字体不随源码打包。

标准环境中，在本目录执行：

```sh
python3 tools/build.py
```

脚本关闭 shell escape，按 XeLaTeX → BibTeX → XeLaTeX → XeLaTeX 顺序构建；如引用仍需收敛，再编译一次。成功后写出 `SGA4half-zh-CN.pdf`、`audit/build-status.json` 和 `audit/final-build.log`。如存在未定义引用或缺字，脚本以非零状态结束；溢出另列诊断，不能据返回码推断没有排版问题。

本次执行环境的基础 TeX 未安装 CTeX、xeCJK、zhnumber、stmaryrd。已从 TeX Live 2025 的公开历史仓库安装到工作区隔离目录，只选入必要宏包，未改动系统或另一挂载仓库。该环境的实际命令是：

```sh
python3 tools/build.py --texmfhome /workspace/texmf-sga4half-selected
```

这条可选路径只描述本次环境，不是工程的硬编码依赖。最终源码 ZIP 在通常已安装上述包和字体的环境中直接使用第一条命令。编译无需联网，无付费 API。

## 数学与来源审计

在原仓库中执行：

```sh
python3 tools/audit.py --english ../../../en/KokunoYumeto-sga-en/release/05_SGA4HALF_EN_COMPLETE_READER.tex
```

此审计按保留的稳定标签、环境、引文、公式和原生图命令核对八讲。法文见证支持的订正、原书自身的疑点、重新换行与原始编号恢复都须结合 `audit/chapter-*-review.md` 阅读；计数相等不能证明文字完整或数学正确。

`SOURCE_LOCK.json` 固定英文 TeX、PDF、源码 ZIP、法文见证的 SHA-256 和来源选择。`audit/native-source-manifest-check.json` 记录 ZIP 内 17 项全部验真。SGA 3/4 散装 TeX 与发布清单不符的情况也已只读核实，未替换任何原件。

实际编译、缺字、引用、溢出、渲染页数及视觉检查的最终状态以 `PROGRESS.json` 与 `audit/` 的记录为准。译文覆盖、原著完整性校勘、数学审校和编译成功是四个不同状态。
