# SGA 7-II 交接

2026-10-21，专属目录 `zh-CN/native-reconstruction/sga7-ii/`。

当前实际完成：第 X–XXII 讲全部 183 个组件的简体中文原生 TeX；法文引言补译；原书封面和标题风格适配；全卷独立源译语义对读；明确登记原文订正、边界说明和未决问题；修订后 288 页 PDF 两遍编译通过。0 缺字、0 溢出、0 未定义引用、0 LaTeX/宏包警告；六处 underfull 提示保留并实际查看。

源文与组件 SHA-256 在 `SOURCE_LOCK.json`；逐组件实际审读和最终哈希在 `review/semantic-coverage.json`。新增中文编校注统一使用 `editorialnote` / `EditorialFootnote`，区别于原书或英文底本原有脚注。40 个组件的源译数学/结构差异逐项冻结在 `review/registered-formula-emendations.json`，没有通过全局忽略公式错误来伪造一致性。

全部 288 页已有实际布局联系表检查；最后修正仅改变 PDF 第 71、145、223 页，三页均已高清复查，其余 285 页逐像素相同。`review/revised-visual-review.json`、`final-render-comparison.json` 记录准确范围。渲染脚本已修复旧分页高清图缓存残留问题；旧图被审阅者明确排除，不能当新图证据。

已有推送历史：`f17b435891b4b7548668ead40d71d16df2cdc50f` 为首次全卷译稿，`20839ff94e5e437f456bcba76dc11b56fbf89e45` 为前次 285 页交付，本轮提交已正常 rebase 到更新后的 main；整合前的本地检查点为 `0c9bf86`、`e2ea742`，当前可达提交见 Git 历史。最终修订提交 SHA 以任务回复和 Git 历史为准，避免在同一提交内自引用。未修改根索引或其他作者目录。

执行器多次收到断连通知，但每次无害检查均确认文件系统和 Git 可用；183 个组件与已发布 PDF 保留，未重启翻译。最初中文宏包缺失及最新版 ctex 与旧内核不兼容的问题，已由随包固定依赖解决。一次普通 main 推送因其他作者并行更新被拒绝；已按正常 fetch/rebase 整合更新；全程未强推。

遗留问题均为可定位的原文或审定边界：Leitfaden 原图未见于两份本库法文扫描及 Springer 官方前置页；IAS 主 PDF 的读取返回 403，未绕过。XVIII 固定点 Bertini 论证/空缺 EGA V 引文、XVII 法丛记号、XXII 个别边界断言等在译稿及审校 JSON 中明确注明。部分外部历史文献页码未独立逐一核验。全卷语义对读完成，不等于数学专家出版接受。

`build.sh` 可脱离原仓库编译；`build_inputs.py` 记录并核对实际编译输入；`audit.py` 的重比对需英文原件；`make_source_zip.py` 打包并逐文件验证。`build/` 是忽略缓存，不能作为正文或公开资产。源码 ZIP 独立解压编译状态见 `review/standalone-zip-build.json`，准确交付哈希见 `DELIVERY_SHA256SUMS.txt`。
