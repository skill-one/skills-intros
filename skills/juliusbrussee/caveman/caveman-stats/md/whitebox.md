# caveman-stats (`juliusbrussee/caveman/caveman-stats`)

## whitebox

- 用户输入 /caveman-stats 触发。
- hooks/caveman-mode-tracker.js 读入技能, 由 hooks/caveman-stats.js 交付。
- hook 从 session log (会话日志) 读取本会话真实 token 用量。
- hook 计算预估节省; 若存在节省估算且轮数已知, 再算规则开销 (每轮开销 × 轮数) 和净节省 (节省 − 开销)。
- hook 返回 decision: "block", 格式化好的统计数据作为 reason 直接呈现给用户, 模型全程不做任何事。

- Hook 驱动、零模型参与: 统计全部在 hook 层完成, 靠 decision: "block" 把结果作为拦截理由直接注入, 模型无需行动。
- 数据来源是 session log 里的真实用量, 非模型自报。
- 开销核算: 规则开销默认 1,250 input tokens/turn, 可用环境变量 CAVEMAN_RULE_OVERHEAD_TOKENS 覆盖, 乘以轮数; 净节省为负时明说并建议对该工作负载关闭 caveman, 不用毛节省掩盖净亏损 (见 docs/HONEST-NUMBERS.md)。
