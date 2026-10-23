# SGA 3 后半部：原生简体中文逐段校订译稿

本目录完成第 XIII–XXVI 讲，共 14 讲，以及第三卷数学指南和卷末索引的全文初译。完整 SGA 3 按 VI_A/VI_B、VII_A/VII_B 分篇，共 28 讲；前 ceil(28/2)=14 讲止于 XII，由另一分工负责。本目录不修改已有中文译本、其他作者目录或原始文献。

`PROGRESS.json`、`coverage/*.json` 和 `evidence/CHECKPOINT_AUDIT.json` 记录全部 16 个展开单元、52,369 行冻结底本的实际连续覆盖。译文包括定义、陈述、证明、例子、脚注、附录、书目、指南及索引；独立 parts 检查点已各合并一次，不重复计数。**本分工全文翻译覆盖和逐段双语独立忠实性审校均已完成。** 原书数学论证未全部重新证明，底本疑点及外部引文的核验范围另有明确记录。 编译、源覆盖和校读分别记录，不能互相替代。本目录也不包含前半部，不能称为完整中文 SGA 3 合集。

交付文件为 `main.tex`、`preamble.tex`、`chapters/`、编译 PDF `SGA3-b-zh.pdf` 及可独立构建的 `SGA3-b-source.zip`。PDF 与源 ZIP 来自同一不可变源码快照，准确提交及产物哈希见 `evidence/BUILD_STATUS.json`。构建方法见 `BUILD.md`；底本问题、已证实订正及实际校读范围见 `SOURCE_REVIEW.md`。

底本选用 `en/KokunoYumeto-sga-en/release/00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip` 内的原生 SGA 3 工程；ZIP SHA-256 与发布清单相符，内部全部 1,868 项已逐一核验。松散的 `03_SGA3_EN_COMPLETE_READER.tex` 与 Git blob 相符，却不符发布清单，因此保留原件，明确选用可校验的源工程。本分工全部 16 个展开单元在仅移除空白及注释后，均与松散文件中的连续内容相符；这不等于字节一致或法文全文校订。完整身份、成员哈希、主分支审计及边界见 `SOURCE_LOCK.json`、`evidence/LOOSE_NATIVE_RECONCILIATION.json`。

`source-reference/` 是从已核验工程递归展开的英文对照底本，只供审计，不参与中文正文编译，也不计作译文。`chapters/*-zh.tex` 才是中文正文。文本、数学、交换图和 Dynkin 图全部原生排版，没有原页覆盖或图像数学；所有图形依赖均展开在 TeX 中。

版式参照只读法文原书实际封面及讲首页：素面标题、原文人名、居中讲标题、左对齐粗体节标题和原编号；中文采用宋体。分册封面注明“简体中文校订译稿”。指南和索引定位页码保留原书页码，不冒充本译稿页码。

用户已明确确认全文翻译授权；此依据不来自仓库或底本许可证。目的地仅为原有私有仓库。现有中文翻译保持原样。
