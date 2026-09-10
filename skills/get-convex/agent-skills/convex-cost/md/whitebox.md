# convex-cost (`get-convex/agent-skills/convex-cost`)

## whitebox

- GUARD: 声明目标 deployment, 以只读方式访问 dev/prod (insights 仅云端+用户鉴权可用, 不看 previews)
- GATHER: 经 Convex 官方 MCP 拉取花费证据 — `insights` 的 bytes/documents-read 事件、`tables` 的行数、`functionSpec` 的函数面; 无流量时改按查询写法 (.collect() 全表扫描) 估价
- ATTRIBUTE: 按 '单次读取量 × 调用量' 的乘积给函数排序, 两个因子都展示 (低价高频可胜过高价低频)
- PROJECT: 给出每个主要驱动函数的增长曲线 — 全表 .collect() 随表数据线性增长, 索引 .take(n) 保持平稳; 不报假精确的美元数, 绝对值引用官方定价页
- REPORT: 输出按成本排序的驱动清单 (证据+曲线+最省钱的修法), 并经 confirm-cost 闸门拦截任何计费操作 (先报价、拿到明确 yes 才执行)

- 证据源 = Convex 官方 MCP 三件套: `insights` (bytes/documents-read, 直接的成本信号) + `tables` (行数, 给扫描成本定上限) + `functionSpec` (函数面); insights 仅限云端部署+用户鉴权
- 成本模型是乘积不是单因子: cost = 每次调用的数据读取量 × 调用次数; 复杂度按查询写法定性 — `.collect()` = O(表大小), 索引访问 = O(1) 平稳, 只给曲线形状不编造美元总额
- 修复走总线 (bus): 每个成本驱动以 cost-class finding 发出 (证据 = insight 事件 + 增长预测), 指向 convex-expert / convex-advisor 做实际改动; 本技能自身只读不改代码
