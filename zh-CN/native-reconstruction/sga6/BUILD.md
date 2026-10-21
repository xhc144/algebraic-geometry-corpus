# SGA 6 简体中文原生重建工作稿

交付为**覆盖指定英文底稿全卷的首译工作稿**, 不是原书完整校订版. 原书逐段完整性核对与删节恢复仍未完成, 详见 `ORIGINAL-RECONCILIATION.md`、`PROGRESS.json` 及 `audits/`. 原书第十一讲未写成、未出版, 不作为漏译或已译正文计数. 所有原始资料与既有中译均保持不变.

## 文件与构建

- 主文件: `main.tex`; 各讲、附录和书末: `chapters/`.
- 编译产物: `build/SGA6-zh-CN.pdf`, 394 页.
- 独立源码包: `SGA6-zh-CN-source.zip`.
- 逐段来源范围: `COVERAGE.tsv`; 底本与 ZIP 校验: `audits/SOURCES.json`.

在本目录运行:

```sh
./build.sh
```

脚本以禁用 shell escape 的 XeLaTeX 连续编译两遍. 标准 TeX Live 需提供 amsmath、mathtools、mathrsfs、tikz-cd、enumitem、longtable、booktabs、hyperref、hyperxmp、microtype、fontspec. 中文依赖 ctex/xeCJK/zhnumber 已置于 `dependencies/`, 来自官方 ctex-kit 的固定 2022 标签并保留源文件及 LPPL 声明. 不需要原始 PDF 或联网才能构建本稿.

系统字体需有 Noto Serif CJK SC、Noto Sans CJK SC、Noto Sans Mono CJK SC 与 Latin Modern Roman. 字体不捆绑. 本次使用 TeX Live 2025, LaTeX2e 2024-11-01. `audit-project.py` 使用 Python3; PDF 边界检查还使用 PyMuPDF, 与编译本身无关.

## 原书样式与原生内容

封面采用 LNM225 原书的黑黄分区、编号和题名层级, 全部用 TikZ 矢量元素重建; 未复制藏书贴纸. 书页为 170×248mm 的窄开本, 保留简洁讲次、题名、作者和原有数学编号, 中文用宋体正文. 没有扫描页覆盖、图像数学或通用讲义模板. 交换图均为原生 TeX/TikZ. 原书目录列原页码, 其中英文误列的第四讲起始页222已依法文纠正为274.

## 本次实际验证

- 合卷连续两遍 XeLaTeX 编译成功, 394 页.
- 从源码 ZIP 解压至独立 `/tmp` 目录, 连续两遍编译也成功, 394 页; 原生 TeX 文件逐字节相同, 两份 PDF 的全部页面提取文本 SHA-256 一致. 见 `audits/REPLAY.json`.
- 英文的全部1492个稳定锚点均保留; 中文含1496个锚点（4个原文恢复新增）, 无重复锚点或悬空链接. PDF有2321个链接注释, 内部页目标均有效.
- 缺字、未定义控制序列、未定义 LaTeX 引用、纵向溢出均为0. 有一处1.98pt横向正文宽度溢出, 未越过纸页边界; 保留真实日志, 未抑制警告. 另有中文斜体回退正体与最多1pt字号替代提示.
- 全394页文字块边界检查未发现超出纸页. 最终PDF实际查看13个样页, 包括封面、译稿说明、目录、公式/证明、恢复的V4.11–4.14、VI/VII/VIII及索引. 另有逐讲独立样稿检查. 抽查范围见 `audits/RENDER_PLAN.json`; 未宣称逐页视觉校对.

这些结果只说明上述构建与机械项目, 不证明数学正确、翻译完美或原书完整. 第V等讲仍有已知原书删节待恢复, 第III等讲仍有来源疑点. 此稿不可标为 SGA6 原书完整重建完成.
