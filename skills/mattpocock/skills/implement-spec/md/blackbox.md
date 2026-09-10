# implement-spec (`mattpocock/skills/implement-spec`)

## blackbox

**function**: 给它一份写清楚需求的设计文档和对应的任务清单, 它交付一个包含全部代码改动、可直接进入人工评审的 Pull Request (代码变更汇总页, 供团队审查合并)。

- input: 一份功能需求文档及拆好的任务清单 (如 docs/specs/user-login.md + issue #12 的 6 个子任务), output: 一个分支上的 PR (代码变更汇总页), 包含全部实现代码, 并标注关闭了需求 issue 和每个子任务
- input: 一份含多个独立子任务的后端改造 spec (如『支付重试机制』设计文档), output: 所有子任务逐个完成并汇入同一个 PR, 每个子任务在 PR 中被对应关闭
- input: 已完成实现的 spec PR (处于草稿状态), output: 经代码审查并修复全部问题后, 转为『待评审』状态的正式 PR, 临时工作分支已清理
