# SGA 4 中文原生重建：X–XIX

**本轮终核与交付已完成。** 用户于 2026-10-22 明确授权恢复；保留全部既有译文，新增 86 组有据校订，并修复脚注与引用编号。当前 PDF 为 298 页；原生工程、单文件版及独立源码包均已真实编译核验，全部页面已渲染查看。`PAUSE.json` 保留上次暂停记录，当前状态见 `PROGRESS.json` 和 `evidence/RESUME_20261022.json`。

本目录只负责 SGA 4 的后半范围。全书按三卷完整目录共 20 讲（含 V bis），前 `ceil(20/2)=10` 讲到 IX；本任务为 X–XIX，共 10 讲。既有中文译本、法文核对底本、英文原文件均未改动；全局目录由协调者管理。

底稿以已验证 `00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip` 的 SGA 4 原生项目为准。散装发布 TeX 的 SHA-256 不符发布清单；ZIP 内发布 TeX 与清单一致，且两份在换行规范化后逐字相同。ZIP 全部 1,868 项的长度与 SHA-256 均通过。详见 `SOURCE_LOCK.json`。

正文为完整逐段首译与原生数学重建，保留原讲号、陈述、证明、注、脚注、书目与可编辑交换图。当前进度以 `PROGRESS.json` 为准；各章 `STATUS.json` 保留初译及发现问题时的历史检查点，当前源文裁决见 `SOURCE_ISSUES.md`。源文中疑似数学笔误、空白引用、冻结底稿自行推断文字等问题单列记录，不凭编译成功宣称已完成专业校订。

用户在本任务会话中明确确认全文翻译授权。授权依据为用户确认，不从仓库许可证或持有文件推断。成果限于用户指定的既有私有仓库。

当前交付覆盖全部 X–XIX 十讲，并已完成非本章译者的逐段双语对照。主文件为 `main.tex`，同步单文件版为 `SGA4-b-zh-CN.tex`，PDF 为 `SGA4-b-zh-CN.pdf`，完整可编辑源码包为 `SGA4-b-zh-CN-source.zip`。编译、数学记号核对、版面查看与校订边界见 `PROGRESS.json`、`evidence/FINAL_QA.json` 和 `SOURCE_ISSUES.md`。89 条上下文校订（包含本轮新增的 86 条）逐项列在 `evidence/SOURCE_CORRECTIONS.json`；原文件不改动。依赖安装与构建见 `BUILD.md`。
