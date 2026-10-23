# SGA 7-II 恢复交接（2026-10-23）

专属目录为 `zh-CN/native-reconstruction/sga7-ii/`。按用户“这可以继续了”的恢复指令，从最新 main `dbb4b7440031f51a3545d6ed172a987846e4db53` 建立独立分支 `translation/sga7-ii-resume-20261022`。暂停记录及 183 组件、288 页交付校验后才开始增量审校；已有译文未重翻。远端最终提交 SHA 以任务回复和 Git 历史为准，避免提交内自引用。父线程负责合入 main。交付前再 fetch，核实 main 已更新到 `26c13d63be7da31dd3b802bde179c4f1e004b234`，新增提交均未改动本卷目录；保留已发布分支历史，不重写提交。

当前正文覆盖第 X–XXII 讲全部 183 个指定英文组件（21,346 行源文）和另有来源记录的法文引言；保留原定义、陈述、完整证明、例、练习、原注、书目、编号及人名原文。原书封面和标题样式分别适配。183 组件已完成独立源译语义对读，具体范围和最终哈希见 `review/semantic-coverage.json`。这不等于全书逐行法文对校或数学专家出版审定。

本轮实质修订三处：

- XVIII 6.1 固定点 Bertini 步骤追加明确标识的现代译校补证，经独立逐句复核；由吹起产生的截面取得泛纤维有理点，结合光滑性得到几何整性。保留原作者证明和空缺 EGA V 引文；现代补证不冒充找回历史引文。证据见 `review/resume-bertini-independent.json`、`review/resume-bertini-edit.json`。
- 先前六处待核 EGA 引文全部实际查读法文原件，另读 IV 19.4.8，确认 XVIII 2.1.4 的字面引文从 IV 19.4.9 订正为 IV 19.4.8，保留原读法及理由。
- XVIII 4.2.13 按 SGA 法文印刷第 275 页恢复四处理想平方/秩二上标内的逗号转录错误，独立复核通过；精确差异及来源见 `review/resume-ega-*.json`。

现有 41 个组件的正文数学/结构差异逐项冻结在 `review/registered-formula-emendations.json`，机械重比对通过。86 则新增中文编校注与原作者注分开；审计仅移除明确新增编校注，不作全局公式忽略。原英文、法文底本与既有中文译本始终只读。

最终 PDF 为 289 页，两遍 XeLaTeX 编译通过；0 缺字、0 溢出、0 未定义引用、0 LaTeX/宏包警告。六处 underfull 提示保留并实际查看。PDF 含 14 个原生 TikZ 图、130 个 TikZ-cd 图，实际图像对象为 0；没有扫描页覆盖或图片数学。PDF SHA-256 为 `d6405cff2c664ae73c53e6c18c90461cc865adad8b7eb04b4358140826107035`。

本轮 290 页中间稿全套布局联系表已实际检查并抽查高清页面；消除孤行后，最终 289 页中 280 页正文与已检版本逐像素相同（比较区不含页脚页码，且已核对所有正文/脚注文字均在区内），其余 9 页全部高清复查。准确范围见 `review/resume-visual-*.json`、`review/resume-final-render-comparison.json` 及 `review/revised-visual-review.json`。这项布局检查不替代数学审校。

Leitfaden 原图仍未找到：已有两份本库法文扫描与 Springer 官方前置页，本轮又实际查看 Google Books 的 Springer 授权重印预览 PR6–PR9，均未见原图。保留此前 IAS 主 PDF HTTP 403 记录且未重试；另一独立公开镜像一次直接读取也返回 403，未绕过。不能确认不同电子重印扫描是否独立，不根据文字猜画。见 `review/resume-leitfaden-search.json`。历史 EGA V 引文定位、其他已标识记号/边界问题及尚未逐一核验的外部文献仍明确留档。

历史交付 `20839ff94e5e437f456bcba76dc11b56fbf89e45`（285 页）和 `c0ffeb3b934efdbda57ed6cda11ecec850c648d4`（288 页）完整保留；本次恢复首个远端检查点为 `46469a3`。旧执行器断连均经无害检查确认恢复，未重启翻译。全程未强推、未改凭据/权限/可见性，未修改根索引、协调目录或其他作者目录。

`build.sh` 可脱离原仓库、无联网下载、无 shell escape 编译，依赖固定在源码包中；`build_inputs.py` 冻结实际 191 个输入并检查编译期间无变动。`audit.py` 重比对需要英文原件。本轮源码 ZIP 已实际解压到新的空目录，核验 255 个文件后独立编译通过；191 个实际编译输入与主交付逐字节相同，289 页文字逐页一致。最终包只追加审校状态等元数据，再核对所有编译输入与受测集合相同。证据以 `review/standalone-zip-build.json` 为准，逐文件清单为 `SOURCE_ARCHIVE_MANIFEST.json`，交付哈希为 `DELIVERY_SHA256SUMS.txt`。`build/` 为忽略缓存，不能作为交付正文。
