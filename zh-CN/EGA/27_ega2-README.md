# 《代数几何学原理 II》简体中文版

本包是 Alexander Grothendieck 与 Jean Dieudonné 的 *Éléments de géométrie algébrique II* 的独立、非官方中国大陆简体中文工作版。译文覆盖卷首、§§1–8（至 §8.14.14）、参考文献、符号与术语索引、目录，以及原卷《勘误与补遗（第一表）》至印刷页 222。

主阅读文件为 `ega2-zh-hans-cn.pdf`。可编辑源文件归档为 `ega2-zh-hans-cn-source.zip`；解压后在 `02_reader` 目录运行四遍 LuaLaTeX，即可重建阅读版：

```text
lualatex --interaction=nonstopmode --halt-on-error --file-line-error main.tex
```

译文保留原有公式、编号、标签、交叉引用、图式、引文与原页锚点。经结构与公式回放、四遍串行构建、字体与字形检查、文本提取、链接解析和逐页视觉检查。当前状态为“生产者完成并通过机械与视觉 QA”，不冒充原作者、IHÉS、NUMDAM 或任何机构的官方版本，也不冒充独立中文审校认证。

NUMDAM 权威扫描、法文及英文见证文件均不在本包内。它们只用于来源核对；本包不对 EGA 原文作新的开放许可或公共领域声明。源文中经来源守护者确认的数学错误，只在中文阅读层以可逆注记校正；尚未裁定的疑点继续按印刷原文呈现并保留在勘误候选记录中。
