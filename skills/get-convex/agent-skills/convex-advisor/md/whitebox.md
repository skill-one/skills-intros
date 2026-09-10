# convex-advisor (`get-convex/agent-skills/convex-advisor`)

## whitebox

- GUARD: 经 deploy-guard 步骤 0-1 确认并宣告当前要读取的 Convex deployment (生产环境只读)
- GATHER: 通过官方 Convex MCP 依次调 status (定位 deployment)、insights (拿 72h 类型化健康事件)、tables (schema+行数)、functionSpec (公开/内部函数面)
- ROOT-CAUSE: 逐条读取被点名函数的源码, 把事件对应到代码机制 (如 .collect()、无索引 .filter()、read-modify-write 热点)
- EMIT: 按 specs/finding.schema.json 在 findings bus 上发 finding, confidence=confirmed (事件是事实非猜测)
- REPORT: 按严重度排序, 每条给运行时证据 + file:line 根因 + 具体修复; 仅在确认后才改, 改后再跑 insights 验证趋势

- 数据来源 = 官方 Convex MCP 的 insights 工具: 返回带类型的 72h 事件 (documentsRead/BytesRead 的 limit-hit 与 threshold、occRetried/occFailedPermanently), 每条附证据 (table_name、bytes_read、occ 文档 id + 重试次数); 该工具仅在登录用户的 cloud dev/prod 上可用且需 ~72h 流量, 拿不到就明说并转推 convex-reviewer, 绝不编造 finding
- 根因映射是确定性规则: 读限/字节限事件 → 查该表上的 .collect()、无索引 filter、缺分页; OCC 事件 → 查共享计数器/状态开关的 read-modify-write; 修复优先用现成组件 (@convex-dev/sharded-counter、aggregate 组件、.withIndex/.take/.paginate) 而非手写
- 产出按 specs/finding.schema.json 结构化: class (perf/correctness/cost)、severity 直接由事件种类决定 (limit-hit/永久 OCC 失败=high, threshold/retried=med)、locus 指向 deployment+functionId+tableName; 越界问题 (授权/代码风格/错误分诊) 只发 pointer finding 转给 convex-authz / convex-reviewer / sentinel, 不重复做
