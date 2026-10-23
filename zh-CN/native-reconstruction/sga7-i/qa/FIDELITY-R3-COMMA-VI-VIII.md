# VI／VIII上标逗号定向原刊核实

结论：指定5处的逗号均非原刊记号。VI是普通上标0（3处）或n（1处）；VIII是普通Pic^0（1处）。英文冻结转录及中文均含这些逗号，属于转录排字残留传播，不是中文独有误译。建议仅删上标花括号中的字面逗号。

本次是独立AI定向原刊页图核实，非专业人工认证。未改TeX、PDF或Git。

## 实际原刊与页码

原刊文件：extra/SGA-archive/sga7-1.pdf。实际160dpi渲染并用view_image打开物理页77、78、79、273、274（1起算）。直接核对印本底部页码，分别为72、73、74、268、269。物理页=印本页+5；未沿用上游组件注释中的旧physical索引。

- VI原刊为英文。物理78／印73上半页，定义3.1(b)续文，The right derived functor of后的函子定义，和where后的显示式，两处均为普通上标0，前面没有逗号。
- 物理79／印74，Lemma 3.2证明首个显示式为普通上标0；Corollary 3.3证明(a)中it suffices to show that后的函子为普通上标n，均无逗号。
- 物理77／印72用于确认定义3.1(b)前文语境，不把它计作四处目标所在页。
- VIII物理273／印268，4.6证明末部先出现到Pic_{Q/k}的态射；物理274／印269第一行明确为Q′=Pic^0_{Q/k}，0前没有逗号。这在4.7标题之前，归4.6证明。

## 精确片段与次数

以下中文行号为核实时真实章节文件行号；英文组件局部行号按冻结BEGIN/END跨度、BEGIN行算1。

1. VI组件27，chapters/expose-VI-a-zh.tex:2807；英文局部172行；原刊物理78／印73。
   改前：\check{\underline H}^{,0}_{A|R}:
   改后：\check{\underline H}^{0}_{A|R}:
2. VI组件27，chapters/expose-VI-a-zh.tex:2813；英文局部178行；原刊物理78／印73。
   改前：[\check{\underline H}^{,0}_{A|R}(F)](B)=
   改后：[\check{\underline H}^{0}_{A|R}(F)](B)=
3. VI组件28，chapters/expose-VI-a-zh.tex:2901；英文局部59行；原刊物理79／印74。
   改前：\longrightarrow[\check{\underline H}^{,0}(F)](B)
   改后：\longrightarrow[\check{\underline H}^{0}(F)](B)
4. VI组件28，chapters/expose-VI-a-zh.tex:2949；英文局部110行；原刊物理79／印74。
   改前：\check{\underline H}^{,n}(G)
   改后：\check{\underline H}^{n}(G)
5. VIII组件110，chapters/expose-VIII-zh.tex:2073；英文局部107行；原刊物理274／印269。
   改前：Q'=\underline{\Pic}^{,0}_{Q/k}.
   改后：Q'=\underline{\Pic}^{0}_{Q/k}.

次数：VI组件27两处、组件28两处，合计4处；VIII组件110一处；总计5处。真实中文章节与冻结英文组件中各命中这5处。不要删除正确薄空格命令^{\,\bullet}中的\,；这与字面上标逗号不同。

VIII修订PDF物理169／印168的视觉异常，对应原刊物理274／印269。本次未重新打开修订PDF；该页视觉证据已记录于FIDELITY-R3-VISUAL-151-200.json。

五处均已有明确原刊支持，无未决目标、无阻塞。只处理指定上标逗号，不声称全文原刊复校。
