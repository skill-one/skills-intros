# azure-cost-optimization (`microsoft/azure-skills/azure-cost-optimization`)

## blackbox

**function**: 审查你的 Azure 云账单, 找出闲置、浪费和过度配置的资源, 交给你一份「实际花了多少钱、哪里能省、怎么省」的报告。

- input: 「帮我看看这个订阅哪些钱花冤枉了」+ 提供 Azure 订阅 ID, output: 一份成本优化报告 (Markdown 文件): 当月实际花费总额、花钱最多的资源排行榜 (每项带 Azure 门户直达链接)、可立即删除的闲置资源清单, 以及每项建议的预计月节省金额和执行命令
- input: 「我的 Azure Cache for Redis 是 P1 档, 但负载一直很低, 能不能省钱?」, output: Redis 专项分析: 该缓存实际利用率 + 能否降级到更低档位 + 降级后的预计月节省金额, 附降级操作步骤
- input: 「这个月 AKS 集群费用突然翻倍了, 帮我查查原因」, output: 异常排查报告: 定位到是哪个节点池 / 命名空间的用量导致费用暴涨, 并给出后续预算告警的设置建议
