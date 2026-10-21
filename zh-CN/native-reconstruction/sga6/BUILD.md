# SGA 6 原生中文工作稿：已暂停

用户已要求收尾并暂停, 不自动继续. 指定英文底稿全文已有中文首译; R2补回了法文原本中大量被英文压缩或误写的材料. **原书恢复尚未完成, 独立数学校订未通过全卷认证**. 准确未完页码和出版附属材料见 `PAUSED.md`、`ORIGINAL-RECONCILIATION.md` 及逐页审计.

交付入口为 `main.tex`、`build/SGA6-zh-CN.pdf`（424页）和 `SGA6-zh-CN-source.zip`. 原有中文资料、法文参考件和其他作者目录均未修改. 原第XI讲未写成、未出版, 没有补造.

在本目录执行 `./build.sh`, 以禁止shell escape的XeLaTeX编译两遍. 本次环境为TeX Live2025、LaTeX2e2024-11-01. 标准依赖包括fontspec、amsmath/mathtools、mathrsfs、tikz-cd、enumitem、longtable/booktabs、hyperref/hyperxmp、microtype. ctex、xeCJK、zhnumber的固定2022官方依赖与LPPL源文件置于 `dependencies/`. 需安装Noto Serif/Sans/Mono CJK SC与Latin Modern Roman字体; 未捆绑字体. 不需要原扫描PDF或联网即可编译.

排版按本书LNM225黑黄封面、窄开本比例、简洁讲次与原数学编号适配中文; 新增原丛书题名页和版权页均为原生TeX. 所有正文、数学、交换图为原生LaTeX/TikZ, 没有扫描页或图像数学覆盖. 不同讲次的原书记号分别保留, 没有强行套用全套统一模板.

本轮最终合卷两遍成功, 424页. 缺字、未定义控制序列、未定义引用、横向溢出均为0; 第XIII讲仍有一处0.83272pt纵向溢出, 所有424页的文字块均未越出纸页. 中文斜体回退正体和最多1pt字号替代提示仍保留. 全部1492个英文稳定目标均在; 中文1525个目标无重复或悬空链接. 机械证据在 `audits/MECHANICAL.json`.

最终PDF实际查看第1、3、5、25、48、100、232、374、424页; 其余有各讲工作单元的有界样页检查. 不是全页视觉校对. 第25页附录推论脚注标记有孤行排字现象, 在暂停检查点保留. 第II讲未完成48页法文核对、1页符号待辨; 196条出版目录均未开始, 均没有计为完成.

源码包由 `package-source.py` 生成. 独立解包编译记录与最终编译输入逐字节一致性证据见 `audits/REPLAY.json`; 最终产物哈希见 `audits/FINAL_ARTIFACTS.json`. 历史394页版的验证只适用于提交 `c5e9de07be3d275c0ea8f12865793f2c56abb0c6`, 不能套用于本版.
