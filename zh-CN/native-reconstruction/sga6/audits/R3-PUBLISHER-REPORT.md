# R3 出版附属材料恢复与前置页独立比对

## 范围与来源

本工作单元仅新增 `publisher-inside-cover.tex`、`publisher-back-cover.tex`、`chapters/publisher-catalog.tex`、`chapters/publisher-physics-catalog.tex` 和本组 `audits/R3-PUBLISHER*` 文件. 没有改动 main、preamble、已有 publisher-frontmatter 或 chapters/frontmatter; 没有 Git/index 操作.

原件: `SGA/SGA-6-Theorie-des-intersections.pdf`, SHA-256 `73fbbad41340c12eccdcfcf6c3a1656953fe3d712aa8e391678458ccd17b4baa`.

- 物理 2: 英文出版社说明及 8 条《物理学讲义》广告. 已打开整页和下部放大图, 逐条核对作者、题名、罗马前置页数、正文页数、年份、历史 DM 价格. 第 6 条红色图章覆盖但底下文字仍可读, 原为 V, 340 页, 1970, DM 24,—.
- 物理 717–719: 《数学讲义》第 38–225 卷, 共 188 条. 三页图像均实际打开核对; 不是以 OCR 完成声明. 中文采用原生流式双栏, 为容纳中文而增加页数, 不塞入不可分页的大 minipage.
- 物理 720: 原为纯黄色封底, 左下两个黑色 ISBN. 已看原页, 以原生 TikZ 色面及文字重建; 不加原件没有的宣传文案和装饰黑条.

全部 196 条编号台账见 `R3-PUBLISHER-COVERAGE.tsv`. 实际保存了第 25、50、75、100、125、150、175 条时的 TeX 内容及 SHA-256 检查点. 这些是中间稿, 不代表最终文件的排版修订或地名修订; 最终以 chapters 中两份目录正文为准.

## 原件损坏及确证恢复见证

物理 2 的 Nottingham 图书馆贴纸确实遮住上部中央, 约原页宽的 16%–63%、上部 1%–40%. 最初仅保留可见残句并标记遮挡. 在主线程授权的一轮有界公开检索后, 已找到同年代、同版面、可逐字比对的官方原版见证, 因此该损坏现已通过见证恢复; 没有继续把它作为未译占位内容.

选用 **LNM 228 (1971), Conference on Applications of Numerical Analysis** 的原封二: [Springer 官方 Front Matter PDF](https://link.springer.com/content/pdf/bfm:978-3-540-36976-9/1), PDF 第 1 页, 原页无编号. PDF SHA-256: `5e3f9eb2caa60dde9b0b22165b03749bff292b33201c704f11c9fdefb21eeba8`; 717621 字节. 已下载至 `/tmp/sga6-publisher/LNM228-frontmatter.pdf`, 实际打开渲染图, 对照 SGA6 原物理 2 的全部可见字句、段落断行及垂直顺序. 第 4 类仅为会议报告, 没有新增条件; 有 100 页下限, 无重打补偿条款; 下部所有完整说明、地址、8 条物理书目也相同. 逐段对照与拒用见证记录见 `R3-PUBLISHER-WITNESS.json`.

没有直接采用看似相同的通用说明: LNM108 (1969) 无 100 页下限并有重打补偿条款; LNM235 (1971)、LNM246 (1972) 的会议报告类别另有 a/b 两行条件, 与源件相应处的垂直空间不符. LNM246 曾作为初步候选, 在细看版面后被撤销, 最终没有把这些额外条件带入本稿. 本稿完整恢复说明, 并在正文简短声明借用 LNM228 见证; 原扫描从未替换.

此前只读检索另一个仓库 `/workspace/qiuzhen-2027-reference-library` 的原文 PDF 名录 (排除翻译、版本、检查点及教师讲义后 52 项), 无可识别的同年代 LNM 原扫描. 还只读查验了本仓库 SGA 主目录及 `extra/SGA-archive` 的首尾页: archive 的 12 份 PDF 首尾页均实际看图 (两张接触图), 同年代扫描从讨论班题名页开始, 不含所需封二; SGA4h 的封二为较晚版本, 不作同版见证. 公开检索只用免费官方前置页, 无付费、账号或凭据.

## 值得复核的原目录印刷事实

下列内容照图像保存, 没有按 OCR 或现代数据库静默改成另一值:

- 第 53 卷题名中的数学式为 $\Gamma_4=0$, 已以原生数学录入并单独放大看图.
- 第 73 卷原目录署名确为 J. F. Cerf; 本任务保留原目录署名, 不据书目常识改人名.
- 第 77 卷原目录正文页数 123, 不是 OCR 的 128.
- 第 78 卷前置页数 XVI.
- 第 131 卷价格 DM 22,—, 不是 OCR 的 DM 29.
- 第 173 卷编号是 173, 不是 OCR 的 178.
- 第 179、180 卷前置页数均 IV; 第 195 卷为 III, 255 页.
- 第 208 卷为 VIII, 133 页; 第 224 卷为 XXII, 447 页; 第 225 卷为 XII, 700 页.

## 原前置页物理 5–14 的独立比对

只读比较了现有 `chapters/frontmatter.tex` 与原件物理 5–14; 实际打开标题页、前言、引言三页、目录两页及空白扫描页. 物理 6、8、12 仅有纸背透印/无正文, 不算遗漏. 物理 5 的题名、主持人、六位合作者, 物理 7 的前言实质条款, 物理 9–11 的引言主体和物理 13–14 的目录项目/页码基本齐全. 未重新翻译这些已有的正常中文.

逐页记录及可直接应用的最小修订见 `R3-PUBLISHER-FRONTMATTER.tsv`. 发现一条明确漏引文: 原印 VII (物理 9) 引言首段, 在“凝聚层的对偶理论”之后, 漏掉 `cf. R. Hartshorne, Residues and Duality, Lecture Notes in Mathematics n° 20, Springer`. 应补为“参见 R. Hartshorne,《留数与对偶》,《数学讲义》第 20 卷, Springer”. 本工作单元未修改 frontmatter.

另有一处有实质影响的限定语需主线程裁定: 原印 VIII (物理 10) 的 `ne figure pas encore dans la littérature (sans exclure le travail de Borel-Serre ni le présent séminaire)` 意为“尚未见于文献 (Borel--Serre 的工作和本讨论班也不例外)”. 现有“除 Borel--Serre 的工作及本讨论班外, 这种证明尚未见于文献”将包含两项的限定语反译为排除两项. 这不是缺段, 但直接改变引言历史陈述, 因此单独报告, 未越权修改.

## 验证边界

出版社书目覆盖、原件损坏范围、数学正文独立校订是不同事项. 本报告不宣称正文已通过数学校订, 贴纸下文字现据明确披露的同版见证恢复, 不声称从受损原件直接读出. 独立编译和最终样页检查记录另见 `R3-PUBLISHER-VALIDATION.json`; 主文件集成与最终全卷构建由主线程负责.

最终出版社材料样稿 `R3-PUBLISHER-preview.pdf` 为 6 页: 封二说明和 8 条物理目录同页, 188 条数学目录四页双栏, 最后一页黄色封底. 恢复 LNM228 见证及两处目录术语修订后第 5、6 遍独立编译均 exit 0, 六页实际逐页看图; hbox/vbox 溢出、缺字、未定义控制序列均 0. 这是出版社单元的独立样稿, 不是全卷最终 PDF.
