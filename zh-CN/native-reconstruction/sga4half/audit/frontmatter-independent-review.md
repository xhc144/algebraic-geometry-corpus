# 前置材料独立核对

核对者为第 VII 讲翻译分工，独立于这些前置材料的起草者。只读核查；本次没有改动任何前置材料源码。

## 范围与实际证据

逐段比较了 `frontmatter/reading-guide.tex` 与法文原书 `SGA/SGA-4-5-Cohomologie-etale.pdf` 的 PDF 第 6–8 页（印刷页 1–3）；逐段比较了 `frontmatter/chapter-01-intro.tex` 与原书 PDF 第 9 页（印刷页 4）。不仅查看了 PDF 的文本层，也已实际打开四页渲染图像：

- `/tmp/sga4half-front-original-6.png`
- `/tmp/sga4half-front-original-7.png`
- `/tmp/sga4half-front-original-8.png`
- `/tmp/sga4half-front-original-9.png`

这些图像仅用于内部核验，不是交付正文，也未替代任何原生文字或公式。

另只读查看了 `chapters/chapter-01.tex` 的开头及 `main.tex`，核实原书第 9 页的章题、署名以及补入导言的实际挂接位置。章题和 `P. Deligne 著, J.F. Boutot 整理` 已由章节文件保留，导言在第 1 节之前输入，故 `chapter-01-intro.tex` 没有再重复章题和署名并不构成遗漏。

## 结论

在上述明确范围内，未发现整段遗漏、被概述替代的段落、数学条件误译或必须返修的实质翻译错误。两份文件恢复了英文 release/native 项目未带入的原书前置内容。这个结论限于所核四页，不代表全书源完整性或全书校订已经通过。

### 阅读线索

已逐项核对原书各段的完整覆盖：

1. SGA 4 第 I–VI 讲的一般拓扑理论、晶体上同调与所列入门参考书，第 VII–VIII 讲的相对详细程度。
2. 曲线研究的关键地位，第 IX、X、XI 讲以及 [Arcata] III 的定位。
3. 第 XII–XIII 讲的适当换基定理、Artin 逼近法文献的卷年页码及 §3、多次 dévissage、XIV 的应用、紧支集上同调、原生公式 `\eR^i f_!` 及第 XVII 讲。
4. 光滑态射局部无环性、第 XV–XVI 讲、SGA 7 影响及所需 SGA 2 结果。
5. Poincaré 对偶性、[Arcata] VI 与 XVIII 的比较、[Dualité] §3 以及未给出迹态射形式体系证明的限定。
6. 对偶形式体系、奇点解消与纯性猜想、相对/等特征两种情形、维数 0 或 1 的基概形、[Th. finitude] 和 SGA 5 I、III。
7. 原始 SGA 5 的猜想性、局部项未计算、Frobenius 特殊情形的完整证明、[Rapport] 及另外三处参考定位。
8. `\dZ/\ell^n` 到 `\dZ_\ell` 的过渡、J. P. Jouanolou 与 C. Houzel 的署名、I. Bucur 的两讲、Euler–Poincaré 示性数和对应的迹、经典概形上同调与 Serre 报告。
9. 六条完整局部书目以及 SGA、SGA 4、SGA 5 的说明；书名、人名、年份、页码和 Lecture Notes 卷号均已覆盖。SGA 5 “即将在 Lecture Notes 出版”保留了原书的历史措辞。

“Un fil d’Ariane”译为“阅读线索”，“garde-fou”译为“护栏”均保留了原文比喻，没有改变数学信息。

### 第 I 讲导言

已核对六次报告、Arcata、1974 年 8 月、AMS 暑校名称、英文报告题名 “Inputs of étale cohomology”、第七次报告成为本卷的迹公式报告、说明证明目标及一般性/化约上的取舍、“不可约”情形的强调、不主张独创性的限定，以及拟紧/拟分离两项约定和括号内定义。没有遗漏。

## 非阻断的术语统一建议

- 阅读线索的“多重化约”对应 `multiples dévissages`；本卷其他章节多用“逐层约化”。可考虑统一为“多次逐层约化”，以免读者把“多重”误读成数学上的重数；这不属于已确认的内容错误。
- 阅读线索使用“奇点解消”，第 VII 讲译稿使用“奇点消解”。两种说法都能表达 `résolution des singularités`，建议协调者在最终术语检查中选择一种。

没有因这些措辞建议而擅自修改前置源码。

## 检查边界

本次检查是法文原页到中文源文的内容核对。没有在这份报告中宣称已查看这些材料的最终中文排版页，也没有用原书四页的视觉核验代替全书最终 PDF 的编译、缺字、交叉引用或溢出核验。
