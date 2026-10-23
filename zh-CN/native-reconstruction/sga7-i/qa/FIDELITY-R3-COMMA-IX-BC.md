# IX-B/C 三处额外上标逗号的限定核查

独立 AI 原刊图像核查，非专业人工校对。仅核查委派的三个片段，未重审其他内容，未修改 TeX/PDF/Git。

原刊：`extra/SGA-archive/sga7-1.pdf`。本次实际渲染并用 `view_image` 打开的物理页为 **453、470、473**，均以 144 dpi 单页图查看；对应书中 folio **448、465、468**（页上报告 IX 内部页码分别130、147、150）。不以旧组件中的扫描页码注释充当本次证据。

结论：三处原刊均为单独的普通上标小圆圈 `o`，**没有前置逗号**。三处共须删除三个逗号；不改变上标 `o` 的次数、下标 `o` 或对象。

## 组件166，公式11.0.1，物理453 / folio448

冻结稿片段：
```tex
\Phi_o=A_o/A_o^{,o}
```
原刊对应的准确 TeX 记法：
```tex
\Phi_o=A_o/A_o^o
```

原刊可见分母的 `A` 带下标 `o` 和单独上标 `o`，两者之间无逗号。上标表示特殊纤维群 `A_o` 的**单位连通分支**，商为连通分支群。删除本处上标内逗号1次；不能删去上标或将其误作另一个特殊纤维下标。

## 组件172，公式12.1.3，物理470 / folio465

委派消息称“12.1.1”的反范畴片段，原刊实际编号为 **12.1.3**；12.1.1是 `f_*\mathcal O_X\simeq\mathcal O_S`。

冻结稿片段：
```tex
P=\underline{\operatorname{Pic}}_{X/S}:
  (\operatorname{Sch})_{/S}^{,o}\longrightarrow(\operatorname{Ab}).
```
原刊对应的准确 TeX 记法：
```tex
P=\underline{\operatorname{Pic}}_{X/S}:
  (\operatorname{Sch})_{/S}^{o}\longrightarrow(\operatorname{Ab}).
```

原刊的 `(Sch)` 带下标 `/S` 和单独上标 `o`，无逗号。这里的 `o` 表示 **反范畴**：Picard 函子对 `S`-概形为反变函子，而非群概形的单位连通分支。删除本处上标内逗号1次；保留反范畴上标。无需替换为新记号 `op`，直接恢复原刊 `o` 即可。

## 组件172，公式12.1.12，物理473 / folio468

冻结稿片段：
```tex
A_o^{,o}\simeq\underline{\operatorname{Pic}}^o_{X_o/k}
```
原刊对应的准确 TeX 记法：
```tex
A_o^o\simeq\underline{\operatorname{Pic}}^o_{X_o/k}
```

原刊左端 `A` 带下标 `o` 和单独上标 `o`，无逗号；右端 Picard 的上标也为普通 `o`。左端表示 Néron 模型特殊纤维的**单位连通分支**，与右端 Picard 概形的单位连通分支同构。删除左端上标内逗号1次，右端不变。

## 次数及边界

这次限定核实的三个目标中：组件166为1处，组件172为2处，共3处。冻结 `expose-IX-b-zh.tex`、`expose-IX-c-zh.tex` 的 `^{,o}` 精确检索亦返回这三处。三项均由本次打开的原刊图像直接确认；属于英文/中文冻结转录额外引入的标点，不是原刊数学疑点，也不是新数学纠正。
