# 原卷卷首范围与导言原文独立核查

独立AI读图复核，非专业人工逐字认证。本次实际用view_image打开 `/tmp/sga7-frontmatter/original-001.png` 至 `original-006.png` 共6页；原始只读PDF为 `extra/SGA-archive/sga7-1.pdf`。本次只写本记录与 `qa/FRONTMATTER-FRENCH-TRANSCRIPTION.tex`，不改187个已有组件、主文件、扉页或其他译稿，不操作Git。

## 范围清单

| 物理PDF页 | 原页标识 | 内容与边界 |
|---|---|---|
| 1 | 未见原印页码；图像底部1为档案页码 | 原卷扉页。研讨班名称、1967–1969、卷题、SGA 7 I、主持人与合作者。没有出版社版权页或独立前言。 |
| 2 | INTRODUCTION；未见原印罗马页码 | 导言第一页。从“Soient S un schéma…”开始，至局部完全交时φ^i消失及(I.4.5)引文结束。不能把档案底部2当作原卷页码。 |
| 3 | VI | 导言续页。从单值定理起，至“les exposés III à V n’existent pas.”结束。 |
| 4 | VII | 导言末页。从报告VI的形变理论起，至后续SGA 7 II出版说明及Deligne署名、地点日期。左侧边缘有相邻页残影，不属于正文。 |
| 5 | Table des Matières | 全卷总目录，条目为I、II、VI、VII、VIII、IX及原卷起始页1、25、32、133、218、313。没有III–V条目，与导言说明一致。 |
| 6 | SGA 7 / Exposé I | 报告I标题、作者、局部Sommaire及0.Préliminaires正文开始；已属于已有正文范围，不是卷首导言的第四页。 |

结论：物理1–5页内没有标题为Préface、Avant-propos或其他独立前言的内容。只有一篇INTRODUCTION，占物理2–4页。其后署名P.DELIGNE，地点日期为“Bures sur Yvette, mai 1972,”。不应另外虚构、补写或从别处拼入一篇前言。

## 扉页逐项核对

- SÉMINAIRE DE GÉOMÉTRIE ALGÉBRIQUE DU BOIS-MARIE（原图全大写未加重音）。
- 1967–1969。
- GROUPES DE MONODROMIE EN GÉOMÉTRIE ALGÉBRIQUE。
- (SGA 7 I)。
- Dirigé par A. GROTHENDIECK。
- avec la collaboration de M. RAYNAUD et D.S. RIM。

注意扉页的M.Raynaud与目录报告II的Michèle Raynaud不可擅自以同一人名替换；这里只记录原页不同写法。

## 总目录逐项核对

1. Exposé I — Résumé des premiers exposés de A. Grothendieck, rédigé par P. Deligne — 1。
2. Exposé II — Propriétés de finitude du groupe fondamental, par Michèle Raynaud — 25。
3. Exposé VI — Formal deformation theory, by D.S. Rim — 32。
4. Exposé VII — Biextension de faisceaux de groupes, par A. Grothendieck — 133。
5. Exposé VIII — Compléments sur les biextensions. Propriétés générales des biextensions des schémas en groupes, par A. Grothendieck — 218。
6. Exposé IX — Modèles de Néron et monodromie, par A. Grothendieck — 313。

目录第VII项在图中为单数“Biextension”，不静默改成复数；最终中文可按数学术语正常表达。上述页码为原卷页码，若在交付目录中保留，必须明确其为原卷页码，不能冒充新排页码。

## 导言转录及语义核对锚点

导言三页法文及数学完整转录在 `qa/FRONTMATTER-FRENCH-TRANSCRIPTION.tex`。它仅作为原文校读证据，不应input到交付PDF。处理只包括合并行末分词、用UTF-8表示重音及用LaTeX表达数学；没有添加中文或改写论证。物理页2无清晰原罗马页码，因此没有凭VI、VII反推后强标V。

需在随后法中对读中特别核对：

- proper与smooth在首段的区别；第二句只有proper假设。
- ℓ在底上可逆、严格限定henselian trait、相应残留域代数闭包的构造。
- 局部模型为proper且flat、相对维数n、只有一个不光滑点；φ^i在[0,n]之外为零。
- 专门化长正合列的方向、几何特殊纤维上Gal(s̄/s)模作为惯性平凡的Gal(η̄/η)模。
- 低次消失判据在当时“仅在特征0”有效；例中局部完全交给出i≠n时消失。
- 对每个T∈I存在正整数N、M使(T^M−1)^N=0；有限型剩余域条件下对任意ℓ进表示的断言。
- 几何证明当时仅在特征0或H¹情形有效；幂零指数N≤i+1及复数域上的超越理论比较。
- 经分歧后，Néron模型连通特殊纤维是阿贝尔簇被环面扩张；不得把核商方向倒置。
- 报告I–V没有分别写成稿，汇总为报告I；III–V不存在，并非本译本漏译。
- π₁^(p)为除p之外的完备化，pro-(p)-有限表示；特征指数p不可误成普通特征在所有情形都正。
- VI必须考虑对象无穷小自同构，不能直接粗暴地转到同构类函子；相对余切复形的Ext带下划线。
- VII、VIII双扩张理论在IX中解释极化到Néron模型的变化；后续SGA7II由P.Deligne与N.Katz撰写，原文为“将于以后出版”，保持历史口吻。
- 全部引文(I2.1)、(I4.2)、(I.4.5)、(I.1.2)、(I.6)、(IX3.6)、(I5.3)，署名及1972年5月日期均已保留。

## 读图不确定性与限制

未发现无法辨认而需要猜补的实质正文。原页数学小字已按图辨认；φ、Gal群的几何点上横线、π₁上标(p)及下划线Ext是随后译稿核对重点。原图物理页2没有可见罗马页码，保持未标，不推断。转录不是新发现的法国原稿版本，也未核验卷首以外出版信息。

待主线程提供中文译稿后，继续做独立法中逐段对读；当前尚未对未见的译稿作任何通过声明。
