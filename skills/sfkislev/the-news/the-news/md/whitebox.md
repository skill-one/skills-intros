# the-news (`sfkislev/the-news/the-news`)

## whitebox

- 接收请求 → 确定国家 key (固定 20 国列表) 与时间模式: 实时快照 / 历史归档 (at) / 逐日概览 (daily-overviews)
- 构造 GET 请求: https://www.thehear.org/api/country-view/[country], 按模式拼接查询参数
- 接收 JSON 响应: headlines (每家媒体一条头版主标题) + overviews (current/previous/yesterday 三份 AI 概览)
- 综合分析: 以原始头条为事实基准, AI 概览仅作语境参考, 同时考虑各媒体的编辑立场差异
- 输出回答, 可选附上 thehear.org 网页链接供用户人工比对原始来源

- 单一公开 REST 端点, 免认证、无 API key; 时间模式由查询参数决定 — 默认实时快照; `?at=<UTC 时间戳>` 取历史归档; `?call=daily-overviews&from=YYYY-MM-DD&to=YYYY-MM-DD` 取逐日概览区间 (上限 7 天)
- 响应为结构化 JSON: headlines 数组每项含 sourceLabel/headline/subtitle/link/capturedAt; 每国覆盖 12–39 个不同立场媒体源, 一次调用即得该国头版全景
- 双层信息校验规则: 原始头条 = 客观历史产物 (事实来源); 服务端预生成的 AI 概览 (由一个能看到头条及先前概览的 AI 模型产出) 仅为解释层; 历史查询受各国最早归档日期约束
