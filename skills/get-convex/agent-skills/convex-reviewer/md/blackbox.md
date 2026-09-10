# convex-reviewer (`get-convex/agent-skills/convex-reviewer`)

## blackbox

**function**: 审查 Convex 后端代码 (convex/ 目录里的函数), 找出安全漏洞、性能隐患和写法问题, 给出按严重程度排序的修改建议。

- input: 一个 Convex 函数文件, 如 convex/posts.ts, output: 一份审查报告: 按严重程度 (Critical / Important / Suggestion) 列出问题, 例如「任何人都能删除别人的帖子」「这个查询会全表扫描」, 每条都解释为什么危险并给出修改后的写法
- input: 整个 convex/ 目录的路径, 上线前想整体检查一遍, output: 全量审计报告: 逐个函数标注——哪些没做登录校验、哪些参数没验证、哪些写法会拖慢响应, 最后汇总成一份「上线前必修清单」
- input: 一段准备上线的 Convex mutation 代码 (直接粘贴文本), output: 明确的评估结论 + 问题清单: 标出必须修的隐患 (如信任了客户端传来的用户 ID) 和建议改进项, 每条附具体修复方案
