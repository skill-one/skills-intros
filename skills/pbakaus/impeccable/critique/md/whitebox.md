# critique (`pbakaus/impeccable/critique`)

## whitebox

- 前置准备: 调用 /impeccable 技能载入设计原则与反模式清单, 按协议收集设计上下文 (界面要达成什么)
- 并行双评估: 独立运行 LLM 设计评审 (A) 与自动化检测器扫描 (B), 两者互不可见对方输出以避免偏置
- 综合报告: 融合两路发现 (一致点、检测器漏检/误报), 产出 Nielsen 10 项启发式评分表 (/40)、AI 味判定、P0-P3 优先级问题、角色红旗测试
- 定向提问: 仅针对已发现的具体问题问 2~4 题 (优先方向/设计意图/处理范围), 不问泛泛问题
- 输出行动清单: 按用户选择排出命令优先级 (如 /clarify → /layout → /polish), 说明各命令聚焦哪些发现

- 双盲隔离: 两路评估优先派发给独立子代理 (如 Claude Code 的 Agent 工具); 浏览器操作强制新建标签页并改标题标注 [LLM]/[Human], 防止页面状态互相污染
- 确定性检测链: CLI 用 `npx impeccable --json` 扫 25 种模式 (需含标记的 HTML/JSX 等文件; URL 场景因需 Puppeteer 跳过 CLI; 200+ 文件用 --fast 纯正则跳过 jsdom); 页面场景用 `npx impeccable live` 起服务注入 detect.js, 再经 read_console_messages 读 `[impeccable]` 前缀日志取结果
- 量化与人格测试: 8 项认知负荷清单 (>2 项失败标为中等, >4 项为严重)、决策点可见选项 >4 即标记、Nielsen 启发式 0-4 分制 (总分 20-32 为真实界面常态); 报告必须指出检测器抓到 LLM 漏检的问题及误报
