# FGA3.VI 中文工作稿审查记录

覆盖：原报告 §§0–4，全部正文、陈述、证明、注及已整合的卷首补注；165 个文字/列表单元。原报告日期 1962-05，原编号参考文献 8 条已补回。

译文叶子 SHA-256：`78736c0b209e56356e0d537addf900bcbde80e159ee94f6715e90c96c4ae11ed`。来源锁、原文及 PDF 哈希、逐项校核见相邻 `fga3-vi-qa.json`。

原生两篇独立 wrapper 已实际编译：29 页，XeLaTeX 禁止 shell escape，BibTeX 成功；保留全部 49 个标签、19 个 proof 环境及全部原数学对象（仅下列法文有据的修正及数学注记汉化）。12 个跨篇标签在此二篇 wrapper 中缺席，须由协调者合卷解析；未改全局书目中的 0.46242pt overfull。代表页已视检，未逐页专业审校。

## 有法文证据的符号修正

- `U\cdot  U=D^0` → `U\cdot  U=G^0`；French physical PDF p187 / printed 236-02, text and scanned page agree G^0.
- `X'_s=S_s^0` → `X'_s=X_s^0`；French physical PDF p190 / printed 236-05, visually inspected.
- `G\sigma ` → `G^\sigma `；French physical PDF p191 / printed 236-06, visually inspected superscript sigma.

## 保留待核的问题

- Unnumbered remark after definitions G^tau, G^sigma, G^rho：English and French interchange the sigma/rho primary-component descriptions relative to their immediately preceding definitions. Preserved as source wording; requires editorial decision.
- Paragraph before Lemma 1.4：Both French/English print that phi_n sends x into G (not G^0), and x ∈ X in the following sentence. Preserved pending review.
- Proof of Theorem 1.1(iii), end：Both French/English print g(y′)=x′ after constructing g′. Preserved; likely missing prime on g.
- Section 0 title, original printed 236-01：Original superscript (1) marker restored. No corresponding footnote text found on physical PDF pp186–187; no text invented.

核对法文实体页 186–208 的开头、结尾、章节结构、原书目，以及卷首实体页 9–13（C-07–C-11）相关补注。英文完整覆盖不等于法文逐字审校完成；本稿为全篇初稿，不标作定稿。未运行仓库脚本，未改任何他人章节、原始源文件、共享前言/书目或 Git 引用。
