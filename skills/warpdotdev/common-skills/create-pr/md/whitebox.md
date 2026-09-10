# create-pr (`warpdotdev/common-skills/create-pr`)

## whitebox

- 同步主分支: git fetch 后 merge origin/master 到功能分支, 本地解决冲突
- 运行门禁: ./script/presubmit (cargo fmt + clippy + 全量测试), 纯文档改动可跳过
- 自审变更: 用 git log/diff 对比 base 分支, 核对测试覆盖 (修 bug→回归测试, 算法→单元测试, UI 组件→布局测试, P0 流程→集成测试)
- 关联任务: 用 Linear MCP 找到对应 issue, 把 issue ID 写进 PR 标题 (如 [WARP-1234]) 以自动关联
- 开 PR: gh pr create 按模板 (.github/pull_request_template.md) 创建, 默认 --draft; commit 里附 Co-Authored-By: Warp Agent 署名

- 校验机制: ./script/presubmit 是核心门禁, 串联 cargo fmt (格式化)、cargo clippy (lint, 所有 warning 视为 error) 和全部测试; 文档类改动豁免 fmt/clippy
- 外部工具依赖: git (合并/比对 base 分支)、GitHub CLI gh (pr view/create/edit/ready)、Linear MCP 工具 (查 issue 并通过 PR 标题前缀自动关联); PR 正文遵循仓库模板文件
- 测试覆盖门禁: 按改动类型强制要求——bug 修复需能复现原 bug 的回归测试, 非平凡逻辑需单元测试, View 组件需布局不 panic 的测试, P0 用例需 integration/ 目录下的集成测试; 跳过集成测试前必须先问用户
