# review-loop (`2dmurali/review-loop-skill/review-loop`)

## blackbox

**function**: 我不只把活干完, 还会让一个"挑剔的审稿人"给成果打分挑毛病, 反复修改直到达到质量线 (默认 8/10) 才交付 —— 你拿到的永远是打磨过的版本, 附带逐轮评分和修改记录。

- input: 「帮我实现一个用户登录接口, use review-loop」, output: 可用的代码 + 一份审查日志: 第1轮 6/10 (缺输入校验、没处理超时) → 修改后第2轮 8/10 通过
- input: 一段你已写好的 auth 模块代码, output: 问题清单 (如: SQL 注入、无限流, 指到具体行) + 修复后的代码, 评分达标才算完
- input: 一份技术方案草稿, output: 打磨后的最终版, 每轮都被指出过什么问题、改了哪里, 全程可追溯
