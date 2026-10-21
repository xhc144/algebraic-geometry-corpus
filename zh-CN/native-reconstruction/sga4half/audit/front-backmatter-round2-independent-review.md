# 前后置与恢复书目的第二轮独立审校

本轮按协调者委派，只读核对新恢复的四份局部原书目、引言与勘误。已完整读过各目标文件，并逐项看过实际法文页面图片；没有编辑这些正文或书目文件，没有运行构建或提交。本记录独立于第 VII 讲审校。

## 实际检查范围

法文见证为只读 `SGA/SGA-4-5-Cohomologie-etale.pdf`，SHA-256 `621122873e4ee03558cac6462be6fde54aa58f7705e8f75763b6be5bae3dfa1b`。

| 目标文件及本次完整阅读行数 | 实际看图的法文物理页 | 检查结果 |
|---|---|---|
| `bibliographies/chapter-01-original.tex`，1–24 行 | PDF79、80；印刷74、75 | 全部16项。作者姓名、题名、出版单位、卷/报告号、年份、页码和附注逐项吻合。原书 [2] 的1959及25–58、[5] 的266、[12] 的1–12确如原图，未按现代书目信息擅改。 |
| `bibliographies/chapter-02-original.tex`，1–11 行 | PDF114；印刷109 | 全部4项，包含 Anvers II / Lecture Notes349、Bourbaki279/1964年12月/Benjamin、Lang1959、Weil的Act. Sci. et Ind./Hermann/Paris。无漏条或误读姓名。 |
| `bibliographies/chapter-06-original.tex`，1–16 行 | PDF237；印刷232 | 全部9项。Carlitz页码35–37/MR39,6839；Deligne501–597/349；Deligne–Lusztig103,1(1976),103–161；Kazhdan Harvard预印本；Serre1968；Springer Utrecht预印本；Weil三项。第[6]原图确为“Weil groups”，本地照录，不替换成当前通常题名中的Weyl。第[9]原图本来就无出版数据，目标没有猜补。 |
| `bibliographies/chapter-07-original.tex`，1–11 行 | PDF266；印刷261 | 全部4项。Hodge I的1970/I/425–430；Hodge II的40/1972/1–57；Weil I的43/1974/273–307；Weil II“即将发表”均忠实保存原页历史信息。 |
| `frontmatter/preface.tex`，1–23 行 | PDF3、4；原书引言III–IV | 全部段落完整。面向非专家、各讲定位、Grothendieck原迹公式证明及SGA5按原样出版、模系数推广、闭链类/杯积、对偶性、无支集有限性、感谢Verdier、目录方括号简称说明、Bures-sur-Yvette/1976-09-20/Pierre Deligne全部可在原页找到。没有把日期更新成当前时间，也没有删除历史评价。 |
| `frontmatter/errata.tex`，1–43 行 | PDF317；印刷312 | 全部7项勘误、所有行号、替换方向、谱序列与符号公式均已查。另将两个密集公式区域从原PDF以5倍分辨率实际渲染检查，结论见下。标题少一项系列编号，已报告协调者。 |

书目总数为16+4+9+4=33，未发现丢失条目、错误人名或把协调者明确要求保留的历史误号静默纠正的情况。大小写从原书全大写姓氏恢复通常姓名大小写、法文引文中的“载/第…号/即将发表”等中文化没有改变条目内容。此结论是对原页的忠实性核验，不声称原书历史出版数据都与现代书目相符。

## 勘误逐项核验

1. **XIV p.18 l.14：** 原图“(XIX6) au lieu de (XX6)”，目标方向正确：把XX6改为XIX6。
2. **XVI2.2：** 原图要求 F 局部常值，目标完整。
3. **XVI5.2：** 先约化 F 常值，再用 Galois平展覆盖和Hochschild–Serre；目标保留群G、π*F、`H^p(G,H^q(X′,π*F))⇒H^{p+q}(X,F)`，并正确说随后论证成立。
4. **XVII1.1.8：** 检查了ρ的多重指标k、`(-1)^{A(k)}`、复合F∘(G_j)、K_i指数`k_i ε(i) ε(ψ(i))`，以及A(k)两个求和的全部条件：第一项ε(i)=ε(ψ(i))=−；第二项先对ε(j)=−，再对ψ(a)=ψ(b)=j且a<b，乘积k_a k_b。中文未调换符号或少一个条件。
5. **XVII2.1.3：** 删除第三行/第34页第9行，替换第六七行/第34页第12–13行，数字吻合。5倍原图可辨Hom下标确为小写y、小写x′；中间下标fg′；参数g′*F、f_*F，末项f′_*g′*F、g*f_*F均与目标一致。未凭现代排版习惯把x/y改成大写。
6. **XVIII2.14.4：** XVII6.2.4改为XVII6.2.7.2，方向正确。
7. **XVIII p.99 l.1：** U改为u，3.1.11.1改为3.1.16.1，均与原图一致。

## 报告给协调者的一项小缺漏

法文PDF317页首完整为“Erratum pour SGA4. (tome3, Lecture Notes305).”。中文章题已包含“第三卷”，但本次读取的可见正文没有 Lecture Notes305。已建议协调者在章题或随后一行补入可见“Lecture Notes第305卷”；本轮遵守只读委派，未改正文。

该项是系列出版编号的小缺漏，不影响七项勘误的数学内容。是否已补入，应以协调者后续文件和构建为准；本轮文件快照如下，避免将后续修改误算成本次已读内容。

## 已读快照与审校边界

| 文件 | SHA-256 |
|---|---|
| chapter-01-original.tex | `9d1a36cb1590684f9bba3ca1adc3ebee6d30932f95a9fbdf930a79f903c50e12` |
| chapter-02-original.tex | `40554566afbc1761812a0a7d4f969e795977062247293cb51b9868e24708ab70` |
| chapter-06-original.tex | `9a811eab2951fa52c8ffa60203b57fa02fe0d5141614828680e07b06415352b0` |
| chapter-07-original.tex | `3a1324038553d59b96329414e7cb087c96340e8df3d625fb558fe3cb8f8e147a` |
| preface.tex | `cd004c01e1abf4f32f2605e949ade397fb7fd809bdb0ad6f25d4c4b3150ab63c` |
| errata.tex | `23afc38d0f1b95424283f461eb1ae8a5d46f976449eac4612e374a92f8ab371d` |

没有发现需另外猜补的人名、年份、数字或公式。未检查本轮统一书目数据库的元数据，也未检查根文档如何排入这些局部书目。没有做构建、字体、断行、重复目标或PDF页面验收；由协调者统一处理。
