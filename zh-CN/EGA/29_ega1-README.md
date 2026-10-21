# 《代数几何学原理 I》简体中文版

本包是 Alexander Grothendieck 与 Jean Dieudonné 的 *Éléments de géométrie algébrique I* 的独立、非官方中国大陆简体中文工作版。译文覆盖卷首、引言、第 0 章、第 I 章至 I.10.15.7，以及原卷末尾的参考文献、记号索引、术语索引、目录、收稿日期与印刷信息。

主阅读文件为 `ega1-zh-hans-cn.pdf`。可编辑源文件归档为 `ega1-zh-hans-cn-source.zip`。解压后，从 `04_build` 目录设置固定构建纪元并串行运行 LuaLaTeX，即可逐字节重建阅读版：

```powershell
$env:SOURCE_DATE_EPOCH = '1787788800'
$env:FORCE_SOURCE_DATE = '1'
lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=complete ega1-complete.tex
```

在辅助文件收敛后重复同一命令；本次冻结版的最后两次构建逐字节相同。

译文保留原有公式、编号、标签、交叉引用、图式、引文与原页锚点。全卷经过结构与公式回放、固定纪元的确定性构建、字体与字形检查、文本提取、链接解析，以及 214 个最终页面的逐页视觉检查。当前状态为“生产者完成并通过机械与视觉 QA”，不冒充原作者、IHÉS、NUMDAM 或任何机构的官方版本，也不冒充独立中文审校认证。

NUMDAM 权威扫描、法文及英文见证文件均不在本包内。它们只用于来源核对；本包不对 EGA 原文作新的开放许可或公共领域声明。来源疑点以可逆记录保留；未获守护者裁定的疑点继续按印刷原文呈现。
