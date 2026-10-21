# SGA 3-b 接续记录

根分支 `translation/sga3-b-20261021`；首个已推送提交 `d28abf71e18b8ceac4b59d6916141d7215f6deea`。工作区后续真实译文尚在推进，提交不得越出本目录。

- 已核验底本：SOURCE_LOCK.json。冻结英文逐讲展开文件 source-reference/*.tex，与 /tmp/sga3-audit/units/*.tex 内容相同；不得重译已完成段落。English source-reference 不参与中文编译、不计翻译。
- shared root 文件：main.tex、preamble.tex、chapters-current.tex、PROGRESS.json、tools/、evidence/、指南与索引。共享底层已补 ctex/xeCJK（BUILD.md 说明临时路径）。\TranslationNote 保留原注编号。
- 子任务 xiii_xiv：XIII 已全译；XIV 首轮至1830/3401，已 followup 续1831–3401，然后独占XXIII1–3108。
- 子任务 xv_xvi：XV 在推进至5238；随后需新轮续XVI1–2008，再译XXI尾3045–5057，写parts/XXI-tail-zh.tex及coverage-parts/XXI-tail.json，不能改XXI前缀。
- 子任务 xvii_xviii：XVII在推进至4860；随后XVIII1–1589，再译XXVI尾2664–4641，写parts/XXVI-tail-zh.tex及coverage-parts/XXVI-tail.json，不能改XXVI前缀。
- 子任务 xix_xxi：XIX已全译且法文订正5.13为t≠0；XX在推进至3578；随后只译XXI前缀1–3044，不能开始3045的§6。
- 子任务 xxii_xxiii：仅继续XXII1–7294；XXIII已转给xiii_xiv，不可重复。
- 子任务 xxiv_xxvi：XXIV已全译；只译XXVI前缀1–2663，不能开始2664的§5。
- 根已全译XXV910行、GUIDE126行、TERMINAL_INDEX254行。XXV501行内公式多重集、66行间公式逐序、47targets均与源相符。

尾部分工只在前缀译者完成并停止该文件后，由根将 parts/XXI-tail-zh.tex、parts/XXVI-tail-zh.tex 依序追加到相应chapters文件，合并coverage为全区间；不能把尾部既当独立章节又重复纳入。parts及coverage-parts是实际译文持久检查点，不是占位。

仍需：继续各子任务至完整；逐单位检验math/keys/环境/段落；明确原文疑误与法文订正；稳定源后多遍编译、静态ref审计（SGARefLink会退化为普通文字，日志无undefined不能证明全链接）；处理overflows；渲染实际看页并记录样本，不虚称逐页独立审校；生成同源PDF/源码ZIP；正常fetch/rebase并提交推送，核验只含独占目录。

源覆盖与独立校对分开。所有现行coverage/*.json为具体断点真值，本文仅分工接续，不替代最新元数据。无访问拒绝；不要因已完成译者首轮结束而停止根任务，应followup继续。
