# 第 IX 篇翻译与校对记录

- 完成范围：本篇底本全部正文 §§0–5，包括所有定义、引理、命题、定理、证明、注、交换图及六条参考文献。标题与作者行由主文件提供。
- 源文件：`/tmp/sga4-09-body-source.tex`，1840 行，来自主任务核验的源 ZIP。原始展开片段为 `source/09/drafts/SGA4_IX_LINES_43_278_English.texfrag` 至 `SGA4_IX_LINES_1607_1883_English.texfrag`。
- 输入 SHA-256：`de86d044c4c8414eba703bd2bd06a58dec799537ff41fb09be6429ff3f1600e1`。
- 输出：`body.tex`，1674 行；SHA-256：`733200b3a5147df2677cbed10791b9bc0dbfed8271d1312d55ef526f851ec93b`（主任务进一步排版修正后应更新）。
- 机械核对：70 个 `etiquette` 标签、1 个 `hypertarget`、88 个引用、159 个环境起止事件、6 个 `bibitem` 均按原顺序保留。美元数学片段 1549/1549，忽略空白后多重集仅有五处自然语言翻译差异：`is bijective`→“是双射”、三处 `presheaf`→“预层”、`if`→“若”。其他显示环境中的英语提示词也已译为中文。
- 编译、跨篇引用及页面检查由主任务整合；本记录不宣称独立编译通过、逐页视觉审阅或数学独立复证。译文完整性与底本自身完整性分开列示。

## 原稿问题与待核项

以下均保留所选英文底本，不擅自增补或改写数学内容：

1. 命题 1.2 证明 (iii) 末句为“The second assertion is a consequence of”，未给出所依结果即进入 (iv)。译文忠实保留这句未完成的引导语；这是真实源文缺损，不是译文占位符。
2. 命题 1.2 (i) 与证明 (i) 以分式 `\frac{\lim(\text{\rm presheaf})}{\ass n\subset p}` 表示预层归纳极限。保留原式而未擅自换成另一个极限宏。
3. 定义 2.3 要求有限多个局部闭子概形给出的分解；命题 2.4 (i) 的陈述遗漏明确的“有限”，其证明仍使用有限分解。未替原稿补字。
4. 命题 2.7 证明中的 `2.4 (iv)` 引用后有未闭合的文字括号。
5. 推论 2.7.2 的群层证明中先后以 `(J,H')` 与 `(H',J)` 记指标对，余核处用单箭头而非双箭头。均保留。
6. §2.7.2.1 原稿说“group schemes”而实际讨论群层；译为“群概形”，保留源意待核。
7. 命题 2.8 证明写复合为 `gh`，而引理图的箭头次序通常应仔细核对。
8. 命题 2.9 原有注释已疑问 IV.2.4 的引用；保留该注释与标签。
9. 命题 2.9 的群层证明中 `s_i` 与 `(s_{i1},...,s_{in_i})` 之间缺少关系符号；未补写等号。
10. 命题 2.14 (ii) 陈述中态射为 `p_i:X'_i→X_i`，但上下文目标应与 X 核对；证明又对局部闭分层直接应用开浸入形式的主定理。不得因编译成功视为数学复核通过。
11. 命题 2.14 证明出现 `t_{ij^{\ast}}`（随后又用 `t_{ij\ast}`），以及 `C_{\bar Z_i}` 缺少与附近一致的 i 下标；保留。
12. 定理 3.3 的证明中“SGA VIII 1”缺少 SGA 卷号；命题 3.6 证明显示 VII 2.2 而链接为 `VII.rem2.1`。
13. 公式 (5.3') 弯箭头标作 `d'`，上下文复合应与乘以 d 核对。
14. 命题 5.5 证明原文为 `F=i`, `G`，未形成 `i_!G`；又称群 g 在 U'' 上变成常值，最后写 `ZZ/r` 而不是前文的 `ZZ/ell`。三处均保留。
15. 命题 5.6 对一般 Y 定义函数时写 `(Y)=Sup(Y_i)`，缺少 varphi；证明中开浸入目标为 X 而非 Y；归纳假设写 `H^q(ZZ,ZZ/ell)`，疑应为 Z。均保留原式。
16. 推论 5.7 证明的显示引用为“7.6”，标签却为 `IX.prop5.6`。保留显示号与链接；未静默修正。
17. 参考文献书名、作者名、期刊名及出版机构原样保留；仅译普通描述与“引作”。原稿的出版信息或拼写未作未经依据的修补。

## 法文参考核对边界

主任务提供的只读法文见证：`/tmp/sga4-original-tome2.pdf`。仅用于检索疑点，尚未对本篇全部内容逐句核对出版扫描本。任何英文缺损和数学疑点的最终处理都须另有明确校订记录。

Root layout pass reflowed the long exact sequence following §4 into four aligned lines to remove a 10.29pt overflow. All mathematical symbols and arrows retain their order; only alignment/line-break tokens changed. U+1D52 in the final bibliography is typeset by a native superscript-o mapping because Nimbus Roman lacks that glyph.
