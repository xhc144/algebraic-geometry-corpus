# 续译检查点

本交付是明确的部分成果，不能标记 assigned scope complete。分配的14篇中，已完整译出导言及 I、II、III、IV；V、VI-A、VI-B、VII-A、VII-B、VIII、IX、X、XI、XII，以及第一卷索引尚未翻译。本轮保存可编译 TeX、原生图、PDF、源码 ZIP 和逐组件审计；后续应从 V 的第00组件继续。

底本固定为仓库 `en/KokunoYumeto-sga-en/release/00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip` 内 `native/SGA3/SGA3_English_current_buildable_source_20260823/source/`。外部哈希、全部1868条外清单、SGA3的919条内部清单均已核验；散装 TeX 的发布清单哈希缺陷仍明确记录，不以本次翻译掩盖或改写源文件。

下一篇原生输入为 `inputs/V/tex/components/00_expose_V_pp251_252_en.tex` 至 `23_expose_V_theorem1041_proof_through_bibliography_en.tex`。源 `inputs/V/body.tex` 充满旧 IfFileExists 的 pending 回退；实际24个组件都存在，不应把这些历史回退标题译作正文或计作完成。逐组件完整翻译到新 `chapters/V/`，保留源图及编号；不要把 V 的路径规则套在 I–IV 图上。V 的主文件原来重定义 SGAThreeNativeInput 来解析图路径，整合时须读原生 master 相应段。完成 V 后才接 VI 的 A/B 两篇；本项目不得触及另一作者的 XIII–XXVI。

构建使用系统 XeLaTeX、latexmk 与临时标准 TeX 包树。当前运行环境缺 ctex/xeCJK/zhnumber/stmaryrd，已从免费 CTAN 安装到 `/tmp/sga3-texmf-2024`（与系统 LaTeX兼容）和 `/tmp/sga3-texmf`。命令环境：`TEXMFHOME=/tmp/sga3-texmf-2024:/tmp/sga3-texmf TEXMFVAR=/tmp/sga3-tex-var XDG_CACHE_HOME=/tmp/sga3-cache`。可移植源码包需要安装 BUILD.md 所列标准依赖和 Noto CJK 字体；未打包字体，也未使用付费服务。

译文覆盖与数学审校严格分开。I 01–08、II 10–14有首轮独立文字对照；I09自检，III–IV译者自检。SOURCE_ISSUES.md有多处高优先级底本疑点，均未伪造修正。脚注、文献标题、人名、公式、标签及交换图保留；仅已记录的源码换行/损坏箭头/书签宏修复改变排版代码。COMPONENT_CHECKS.json仍保留实际差异，不把自然语言公式翻译或已记录修复伪报为字节恒等。

发布分支 `translation/sga3-a-20261021`。首个检查点发布后因对已发布提交作 rebase，普通 push 被 non-fast-forward 拒绝；随后在本目录内保留新版内容并正常合并旧已发布历史，普通 push 成功，从未 force push。继续此已发布分支时应保留已发布历史，正常合并并发 main 更新；不要 force push。协调器负责全局索引，本目录外不做内容改动。
