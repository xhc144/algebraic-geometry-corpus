# 原书两篇序言的补译记录

## 来源、范围与完成状态

- 来源：主任务提供的只读 Springer SGA 4 第一卷原书扫描 `/tmp/sga4-springer-tome1.pdf`。
- 扫描 SHA-256：`f4f025b21f5fe3c2ef6a94ef525ae510e58b26ecade9712821f8e091df20057b`。
- 完整范围：物理 PDF 第 2–13 页，零基页索引 1–12。第 2–7 页为 `Préface à la deuxième édition`，含 Bures, Novembre 1969 日期与 LEITFADEN 图；第 8–13 页为 `AVANT-PROPOS`，含全部原页脚注及历史增补。
- 输出：`front-prefaces.tex`，原生中文 LaTeX，题名分别为“第二版序言”“前言”；保留 1、2、3、4 及 a–e 等原有分项。正文与图均无扫描页覆盖或图片公式。
- 源扫描 12 页的对应 PNG `page-02.png` 至 `page-13.png` 均已经逐页用图像工具打开、核对；OCR 文本只作辅助，未直接接受错误的数学识别。
- 每个源页边界在源码中均有 `SOURCE physical PDF page N` 注释。中译不强制与法文分页相同。
- 已完整翻译所有源页可见正文，重建导读图，并保留 12 个正文脚注及 1 个原书无正文标记、独立排出的脚注文本。总计 13 个注。
- 不把源扫描页角、复印污点、切边及 PDF 添加的物理页码误作正文。
- 编译与最终中文页面视觉检查由主任务统一进行；本记录的逐页查看是法文源页查看，不宣称已经查看中文成品。

## 数学、脚注和原貌核对

1. 第 4 页扫描的函子为 `f^!`、`Rf_!`，不是 OCR 的 `f”`、`Rf,`；已原生重建。态射为 `f:X→Y`。
2. 历史篇名采用原页可见的 `VI_B`，包括两处正文及导读图；未静默改成现有英文整合稿的 `V bis`。
3. 第 6 页的域为 `F_ell`、`Q_ell`、`F_p`；保留原句给出的两个情形。原页“ou est le corps premier”按可见文字译作“或者是素域”，并未从 OCR 误成的词串造出新数学条件。
4. 第 8 页第一脚注为 `H^i(X,Z_ell)` 和 `q^{i/2}`，不是 OCR 的 H1 或 q/2；已对扫描核验。
5. 第 9 页为系数 `Z/ell^nu Z`，`nu→+infty`，以及 `Z_ell`；原生排版。
6. 第 10 页的同伦不变量为 `pi_i`；第 11 页 Picard 不等式为 `rho≤b_2`；均已据图核定。
7. 原页第 10 页 (***) 指向第 11 页独立脚注 (*)。源码保留两条注，通过稳定锚点连接；“原书下一页”中的“原书”用于明确历史分页，避免误指重新排版后的中文页。
8. 原页第 12–13 页的数字注号为 (2)、(3)、(4)，已局部保留；星号注独立采用原书的星号序列，不改成全书自动编号。
9. 原书第 11 页最后脚注保留“第 (ix) 页”这一原有指向，未未经依据改号。
10. 原书第 5 页 c) 中印作 `XVII 5.5, 2.1`，照录这一显示引用；尚未据后篇替换为推测的更正号。
11. 人名、书名和文献标识保留原文脚本，包括 DELIGNE、GROTHENDIECK、SAINT-DONAT、WEIL、HODGE、MONSKY-WASHNITZER、MANIN、Michael ARTIN、Barry MAZUR、CHAFAREVITCH 等。
12. “固有支集”与后文“紧支集”分别对应两篇序言源页的 `supports propres` 与 `supports compacts`，未抹去历史用词差别。

## 导读图的原生重建

TikZ 保留 I–XIX 各节点及 VI_B，三组左大括号和六组中文说明。箭头为：VI→VI_B、VI→VII、X→XI、X→XV、X→XII、XIV→XVI、XV→XVI、XIV→XVII、XVI→XIX、XVI→XVIII、XVII→XVIII。采用双线箭身模拟原图。没有新增原图未画出的逐篇箭头。

主文件须加载 `tikz` 以及库 `arrows.meta,decorations.pathreplacing`。原生图的大小、排版溢出与链接警告尚须在最终主文件编译后检查。
