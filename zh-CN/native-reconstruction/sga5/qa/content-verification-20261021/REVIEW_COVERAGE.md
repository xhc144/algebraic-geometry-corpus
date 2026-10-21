# 2026-10-21 有界独立内容复核

本轮检查全部指定源组件的中英忠实度，并对每一项已记录的实质疑点查看法文原页。初始清单64项，完整读者检查新增18项，共82项全部裁定；没有未分配、未阅读或等待裁定的清单项。`adjudication-ledger.json`记录来源、实际法文页、数学依据、精确修订及残余范围。各原始裁定JSON保留更详细的目视见证读法；OCR仅用于定位。

这是独立代理检查，不是专业人工审定，也没有声称独立重证每个定理或逐句校勘整部法文正文。覆盖完整性、局部数学裁定、编译与视觉验收分别记录。

| 已出版报告/组件 | 英文源行或法文页 | 未负责该组件初译的读者 | 复核记录 |
|---|---|---|---|
| I（含附录、参考文献） | 323–2150 | sga5_iiib | I-reader-review.md；I-postapplication.json |
| III（含参考文献） | 2151–4477 | sga5_i | III-IIIBI-reader-review.md；同名postapplication.json |
| III B第一部分 | 4478–5245 | sga5_i | III-IIIBI-reader-review.md；同名postapplication.json |
| III B第二部分及参考文献 | 5246–6947 | sga5_x_xii | IIIBII-reader-review.md；同名postapplication.json |
| V（含谱序列附录） | 6948–8494（含两篇间分隔）；完整V/VI范围6948–9352 | sga5_vii_viii | VVI-reader-review.md；VVI-postapplication.json |
| VI | 8495–9352；完整V/VI范围6948–9352 | sga5_vii_viii | VVI-reader-review.md；VVI-postapplication.json |
| VII（含参考文献） | 9353–11878；完整VII/VIII范围9353–12530 | sga5_v_vi | VIIVIII-XXII-reader-review.md；同名postapplication.json；既有05-independent-review.md全范围对照 |
| VIII | 11879–12530；完整VII/VIII范围9353–12530 | sga5_v_vi | 同上；本轮复查集成修改及法文疑点，复用此前已完成的完整源译对照 |
| X（含参考文献） | 12531–13554；完整X/XII范围12531–14583 | sga5_v_vi | VIIVIII-XXII-reader-review.md；同名postapplication.json |
| XII（含参考文献） | 13555–14583；完整X/XII范围12531–14583 | sga5_v_vi | 同上；本轮完整2053行读者检查 |
| XV（含附录） | 14584–15704 | sga5_iii | XV-front-reader-review.md；同名postapplication.json |
| 术语及符号索引，全部108项 | 15705–15817 | sga5_iii | XV-front-reader-review.md；同名postapplication.json |
| 封面及完整卷首 | 法文物理PDF1–11 | sga5_iii | XV-front-reader-review.md；同名postapplication.json |

精确连续范围以各读者报告及`SOURCE_COVERAGE.tsv`为准；没有按粗略分报告边界把相邻文字排除在检查之外。六份修订后验收合计11+12+23+12+13+11=82项，全部通过。`application-verification.json`进一步用冻结字符位置逆向撤销全部112处已记录替换，恢复九个文件的修订前SHA-256，确认无未记录的正文删改；公式标签、引用命令和环境的有序序列保持不变。两条有误的英文增补编注完整译文移入可见校勘附记，原法文证明没有因编注误判而被改坏。

四处原文不确定性已具体处理：

- **I-01**：法文确引不存在的1.9(b)(ii)。不能唯一恢复其拟指条款或所写无界`D_c(X)`范围中的完整推导；保留引文及公式并链接校注，没有据此宣称定理错误。
- **IIIB-20**：法文确额外要求群在`C,D`上平凡作用。改`C`为`Y`会减弱假设，与后文应用的衔接尚缺足够证据，故保留原假设并注明疑义。
- **XXII-06**：修正XII (6.4.7)的`S′`、颠倒分支及漏写的局部纤维条件，同时明写覆盖在该点上方平展的适用范围。法文完整原式保留在校注。层不分歧不能代替任意选定覆盖平展；任意分歧覆盖下的原论证没有被声称复原。独立检查也确认配套(6.3.2)应为加号。
- **FRONT-01**：后文关于有限性及类群的VII确定应为VIII，已改；导言概述中的(I,VII)是否作者拟指VIII不能唯一裁定，保留原读并明确区分。

其余已知问题或已据法文/类型/后续证明校订，或确认为成立的原文/可解释的历史记号。原法文PDF、英文松散TeX和ZIP均只读且哈希复核通过。未改变其他作者目录、全局索引或无关挂载仓库。
