# SGA 6 简体中文原生重建工作稿

这是实际译稿的持久检查点, **不是全书完成版**. 原书第十一讲未写成、未出版, 不作为漏译或已译正文计数. 既有中译及所有源资料未修改. 详细来源哈希见 `audits/SOURCES.json`, 逐讲覆盖、疑点与法文核对见 `audits/`.

## 构建

需要 XeLaTeX, ctex/xeCJK, amsmath, mathtools, mathrsfs, tikz-cd, enumitem, longtable, booktabs, hyperref, hyperxmp, microtype. 中文字体 Noto Serif CJK SC、Noto Sans CJK SC 与 Noto Sans Mono CJK SC; 拉丁字体 Latin Modern Roman. 不捆绑字体. 在本目录执行两遍:

```sh
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error -recorder -output-directory=build -jobname=SGA6-zh-CN main.tex
```

书页按原书 LNM225 的窄开本比例设置, 保留简洁居中讲次、题名、作者和原有编号层级; 中文采用宋体正文. 没有扫描页覆盖、图像数学或共用讲义模板. 数学与交换图均由原生 TeX/TikZ 重建. 原书目录页码单列为原页.

当前编译和逐页审查状态以 `PROGRESS.json` 为准. 编译成功不等于全书内容完整, 英文底本本身有省略与错误; 全书法文逐段核校尚未完成.
