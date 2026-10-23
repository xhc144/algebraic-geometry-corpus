# R3：I、IX 上标逗号限定原刊核验

结论：指定的 **7处上标逗号均为英中共有的转录标点错误**，原刊没有这些上标逗号。I的5处应统一为 `\widetilde H^i`（保留波浪号，不改成无波浪号的普通 `H^i`）；IX的2处应为 `f_q^n`。这是恢复原刊记号，不是新数学结论。

本次仅核验上述指定片段，未重新审查正文其他内容，未修改任何TeX/PDF，未执行Git操作。独立AI原刊图像核验，非专业人工认证。

## 实际查看的原刊图页

原刊文件：`/workspace/sga7-i-resume/extra/SGA-archive/sga7-1.pdf`。

- PDF物理页20，书页15，报告I定理4.5证明：150dpi渲染并以view_image打开。五处H均带波浪号、上标只有i，无逗号。
- PDF物理页364，书页359，报告IX定理4.3(b)：130dpi渲染并打开。句末“de la forme”后的Frobenius幂为下标q、上标n，即 `f_q^n`，随后才有正文逗号及 `avec n≥0`。
- PDF物理页365，书页360，报告IX证明(b)、公式4.3.1前：130dpi渲染并打开。正文“est”后的幂同样为 `f_q^n`，随后有正文逗号。
- PDF物理页366，书页361：也实际打开，属于邻页定位查看；不作为上述两处修正的必要证据。

没有把扫描索引注释当作实际图像核验。物理页367–368仅曾渲染，**未打开，不计作实看页**。

## I：组件05，五处

文件：`chapters/expose-I-zh.tex`。本次读取时的行号为618、620、628、632（632行含两处），共5处。

| 行 | 修改前精确片段 | 修改后 | 原刊位置 |
|---|---|---|---|
| 618 | `=\widetilde H^{,i}(\bar V)` | `=\widetilde H^i(\bar V)` | 书页15，(1)中的等式链第一处 |
| 620 | `\widetilde H^{,i}(\bar V_{\bar\eta})` | `\widetilde H^i(\bar V_{\bar\eta})` | 同一等式链箭头之后 |
| 628 | `\widetilde H^{,i}(V')` | `\widetilde H^i(V')` | (2)中的消失等式 |
| 632，第1处 | `\widetilde H^{,i}(\bar V)` | `\widetilde H^i(\bar V)` | “on conclut en notant que”后 |
| 632，第2处 | `\widetilde H^{,i}(V')` | `\widetilde H^i(V')` | 同句“limite inductive des”后 |

第632行完整源片段：

```latex
注意到 $\widetilde H^{,i}(\bar V)$ 是各 $\widetilde H^{,i}(V')$ 的滤过余极限, 即得结论.
```

相应修正：

```latex
注意到 $\widetilde H^i(\bar V)$ 是各 $\widetilde H^i(V')$ 的滤过余极限, 即得结论.
```

冻结英文 `/tmp/sga7-r3-baseline/reader.tex` 组件05同样有5处：812、814、825、829、830行。因此分类为**共有源转录标点错误**，而非中文独有误译。

## IX：组件140，两处

文件：`chapters/expose-IX-zh.tex`，共2处。

第1745行（定理4.3(b)）：

```latex
若 $g$ 在 $\pi_o$ 中的像形如 $f_q^{,n}$，其中 $n\geq0$，则它甚至是整数。}
```

修正为：

```latex
若 $g$ 在 $\pi_o$ 中的像形如 $f_q^n$，其中 $n\geq0$，则它甚至是整数。}
```

第1777行（证明(b)，4.3.1之前）：

```latex
b) 若 $g$ 在 $\pi_o$ 中的像为 $f_q^{,n}$，公式（\SGARefLink{sga7.sga7i.eix.n4-2-10}{4.2.10}）现在变成
```

修正为：

```latex
b) 若 $g$ 在 $\pi_o$ 中的像为 $f_q^n$，公式（\SGARefLink{sga7.sga7i.eix.n4-2-10}{4.2.10}）现在变成
```

冻结英文 `reader.tex` 组件140的20131、20169行也写 `f_q^{,n}`，故同属**共有源转录标点错误**。原刊句读逗号在幂之后的正文层级，不属于指数；仅删除指数内逗号，不删改正文句读。

## 限制与完成情况

指定I五处、IX两处均已原刊图像确认，共7处，无未决数学问题或执行阻塞。本报告只提出精确替换，尚未应用修改。
