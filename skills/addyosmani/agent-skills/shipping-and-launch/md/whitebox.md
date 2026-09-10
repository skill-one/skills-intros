# shipping-and-launch (`addyosmani/agent-skills/shipping-and-launch`)

## whitebox

- 逐项核验发布前清单 (测试/安全/性能/无障碍/基础设施/文档), 全绿才放行
- 部署到 staging: 跑全量测试 + 关键流程手动冒烟
- 部署到生产但 feature flag 关闭, 确认 health check 返回 200 且错误监控无新增
- 灰度放量: 团队内部 → 5% canary → 25% → 50% → 100%, 每阶段对照阈值表监控 24~48 小时, 全绿才进入下一阶段
- 全量后持续监控 1 周, 确认正常即清理 flag 和死代码

- 清单门禁 + 错误预算闸门: 发布前 checklist 六大维度硬核验, 含依赖漏洞审计 (npm audit / pip-audit 等) 和无障碍检测 (axe-core / Lighthouse); 错误预算余量 <20% 只许慢速发布, 耗尽即冻结功能上线
- Feature flag 解耦部署与发布: 代码先进生产但 flag OFF, 按比例逐步放量; 每个 flag 必须有 owner 和过期时间, CI 中同时测试开/关两种状态, 全量后 2 周内清理
- 阈值化决策与回滚: 对照 green/yellow/red 阈值表 (错误率、P95 延迟、客户端 JS 错误、业务指标) 决定前进/暂停/回滚; 回滚通道提前就位 —— 关 flag (<1 分钟)、git revert (<5 分钟)、数据库迁移回滚如 prisma migrate rollback (<15 分钟), 依赖健康检查端点与错误上报服务实时观测
