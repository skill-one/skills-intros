# diagnose-ci-failures (`warpdotdev/common-skills/diagnose-ci-failures`)

## whitebox

- 用 git 获取当前分支, 用 gh pr view 检查是否已有 PR (没有则告知用户, 不会自动建)
- 用 gh pr view --json statusCheckRollup 拉取所有 CI 检查项的状态; 若仍在运行, 只报告已过/已挂/进行中, 建议等跑完再诊断
- 对每个失败的 check, 用其 run ID 执行 gh run view <run-id> --log-failed 抓取失败日志, 提取报错信息、文件路径与行号
- 按类型归类错误: 格式化、lint、编译错误、测试失败、平台特有 (WASM/Linux/macOS/Windows)
- 用 create_plan 生成修复计划文档 (问题概述/现状/逐类修复建议/验证命令), 供用户审阅, 不直接改代码

- 唯一外部依赖是 GitHub CLI (gh), 每次调用都强制设置 GH_PAGER=cat 禁用分页 (gh 不支持全局 --no-pager)
- 确定性流水线: 抓日志 → 分类 → 出计划, 输出永远是计划文档而非代码变更; 验证步骤引用 fmt/clippy/测试等命令让修复可被复核
- 错误归类是后续修复的调度依据: 一次只修一个类别 (如先清完所有 clippy 再跑测试), 并交叉引用 fix-errors skill 获取具体修法
