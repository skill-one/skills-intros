# baoyu-translate (`jimliu/baoyu-skills/baoyu-translate`)

## whitebox

- 加载偏好: 按优先级找 EXTEND.md (项目 → XDG → 家目录), 找不到则阻塞式首次问答生成; 同时合并三层术语表 (EXTEND 内联/外部文件 + 内置 EN→ZH + CLI)
- 物化源文本: 文件原样使用, URL/内联文本先存为 translate/{slug}.md; 建输出目录 {源目录}/{文件名}-{目标语言}/, 所有中间文件都落在这里
- 评估篇幅: ≥4000 词时先全文抽术语建会话表, 用脚本按 Markdown 块边界切块, 每块并行派一个子代理翻译, 完成后按序合并为草稿
- 按模式翻译: quick 直接译; normal 先分析再译; refined 追加 批评→修订→润色 三步, 每步落盘编号文件 (01-analysis ~ 05-revision)
- 写最终 translation.md, 扫一遍图片内嵌文字语言是否与新译文一致并提醒用户 (只列清单, 不自动改图), 输出摘要

- 跨块一致性靠'共享上下文'而非事后对齐: 分析出的风格、术语表、比喻映射、难点统一内联进 02-prompt.md, 每个子代理读同一份再各自翻译自己的块
- 结构感知切分: 长文由 scripts/main.ts 只在 Markdown 块边界 (标题/段落/列表/代码块/表格) 切分, 单块超限退化为按行、再按词; 外部依赖仅 bun (缺失则 npx -y bun)
- refined 模式的阶梯校验: 04-critique 只诊断不改正 → 05-revision 逐条落实 → 最终润色为 translation.md; 全程不调外部翻译/校对 API, 翻译与审校均由主代理和子代理 (Agent 工具) 自身完成
