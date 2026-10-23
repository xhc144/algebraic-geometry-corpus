# 卷首材料独立内容审校

2026-10-23。只读核对，未改译文、main 或来源说明。

## 实际对照范围

- 固定 ZIP 源 `source/inputs/INTRO/body.tex` 只有一个输入 `tex/components/00_introduction`。已完整逐段对照该组件与 `chapters/00_introduction-zh.tex`：编者告示三段及日期、导言第1–7节、全部六次自定义脚注、导言末新增长编者注、标准文献缩写四项，以及参考文献八项。源头部来源定位（AaIntro-18fev11.pdf，第1–6页，合卷物理页5–10）保留。
- 已读取固定 ZIP 的主文件 `source/SGA3_English_Full_Volume_Native_Cumulative.tex` 卷首（包括标题及 Reconstruction, provenance, and rights status 的全部三段）与中文 `main.tex` 的卷首输入关系。`main.tex` 没有另写一份编者告示；它通过输入 `chapters/00_introduction-zh` 收录上述告示，并先输入 `audit/upstream-notice-zh`。
- 已完整对照 `audit/upstream-notice-zh.tex` 与固定 ZIP 主文件三段 notice，并读取包内 `RIGHTS_AND_PROVENANCE.md`，区分二者并不相同的文字范围。
- 辅助检查：INTRO 21次引用/目标键、6次自定义脚注调用、8个环境起止命令与源守恒。全文通读才是内容审查依据。

## 需主线程局部修正

以下行号均指 `chapters/00_introduction-zh.tex` 的审查时快照。

|位置|现文|建议|理由|
|---|---|---|---|
|82，导言§1|`高度为1的根性群概形 (radicial group scheme) 与限制 p-Lie 代数`|`高度为1的纯不可分群概形（radicial group scheme）与受限 p-Lie 代数`|源词为 radicial / restricted。现行 terminology.csv 已明确采用“纯不可分的（radicial）”“受限p-Lie代数”；沿用根性/限制会与 VII 及既定术语不一致。|
|124，§4|`当该域不完全时`|`当该域不完美时`|源文 not perfect，说的是完美域，不能与完备性/完全性混同。|
|131，§4|`在不完全底域上工作`|`在不完美底域上工作`|源文 nonperfect base field，同上。|

以下著作题名在源中原有，译文完整保留原题，但只为末尾八项书目补了中文；正文、脚注和§7缩写表仍有八处未按“中文题名〔原题〕”处理。建议只补中文题名，原题、作者、出版社、卷期页码及键均保持。

|行号|现题名|建议中文题名（随后保留原题）|
|---|---|---|
|26|Éléments de Géométrie Algébrique|代数几何基础|
|31|Groupes Algébriques|代数群|
|69，双星脚注|Geometric Invariant Theory|几何不变量理论|
|99，三星脚注|Schémas en groupes réductifs|约化群概形|
|175，Bible条目|Groupes de Lie algébriques|代数 Lie 群|
|178，EGA条目|Éléments de Géométrie Algébrique|代数几何基础|
|180，SGA条目|Séminaire de Géométrie Algébrique du Bois-Marie|Bois-Marie 代数几何研讨班|
|182–183，TDTE条目|Techniques de descente et Théorèmes d'existence en Géométrie Algébrique|代数几何中的下降技术与存在定理|

本次不将“Abel概形”作为确定误译：源 abelian schemes 的含义清楚，项目对人名原文的规则可容此译法；若全书另定“阿贝尔概形”，宜在术语统一时处理。

## 缺段与权利说明结论

INTRO 全文未发现整段遗漏、脚注漏译、书目漏项或条件否定翻转。上述术语问题之外，编者告示、历史说明、导言末几何约化性的编者补注均与源对应。

`audit/upstream-notice-zh.tex` 对固定 ZIP 主文件 notice 的三段为完整译文，未漏掉：I–XXVI及索引的英文读本范围、原生图与无光栅调用、Polo–Gille PDF 的控制地位、当时无公开可编辑源码、OCR仅定位/拟稿、Reinhold CC BY 4.0 仅适用于比对译文、不能由此推出法文版本或累积重建权利、内部检查点及各项待审状态、没有作出版或公共许可声明。开头“译者说明”是中文工程新增且明确标示，正确说明“本累积读本”指英文版，没有冒称中文已完成I–XXVI。

包内 `RIGHTS_AND_PROVENANCE.md` 是另一份短说明，另有“源PDF及私有高分辨率权威裁图不包含在包内”“公开分发须另作权利与出版决定”等原句。当前 notice 没有逐句翻译这份独立 Markdown，但它自称的是英文主文件版本说明的完整译文，故不能把这些差异判成对主文件 notice 的缺译。若目标是将包内所有权利文档也完整汉译，须另收该 Markdown；本次不擅自并入或改变说明范围。

## 源原有事项与限制

编者告示把 VI-B 第5节链接到导言§5，是英文源原有错链，已见 audit/SOURCE_ISSUES.md；中文键忠实保留，不列为译者新增错误。其他历史论断或约化性的数学陈述，本次只核源译对应，没有重新认证其定理适用条件。

未重新对照法文 PDF、未重新证明数学、未编译或检查成品PDF。当前 main 的封面覆盖提示属于不断扩展中的工程元数据，不拿它与英文完整读本范围强行等同，也未改动。
