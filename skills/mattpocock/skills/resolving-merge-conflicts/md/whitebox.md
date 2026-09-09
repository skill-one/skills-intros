# resolving-merge-conflicts (`mattpocock/skills/resolving-merge-conflicts`)

## whitebox

- 用 git 历史和冲突文件确认 merge/rebase 的当前状态与冲突范围
- 读冲突双方的 commit message / PR / 原始 issue, 搞清每处改动背后的原始意图
- 逐个冲突块解决: 尽量同时保留双方意图; 不兼容时按 merge 的既定目标选边并记录取舍, 绝不发明新行为, 也绝不 --abort
- 跑项目自带的自动化检查 (通常顺序: 类型检查 → 测试 → 格式化), 修复合并引入的问题
- 全部暂存后 commit 收尾; 若在 rebase, 则持续 continue 直到所有提交重放完成

- 意图考古: 解决冲突前先溯源——commit message、PR、原始 issue 是判断双方意图的一手依据, 裁决靠历史证据而非猜测
- hunk 级裁决规则: 以单个冲突块为单位逐个处理; 冲突不可调和时, 以 merge 的既定目标为准选边并明示 trade-off; 硬约束是只解决、永不 abort
- 校验闭环: 完全依赖目标项目自身的自动化工具链 (typecheck / tests / format, 如 tsc、pytest、prettier 等, 以项目实际配置为准) 做回归验证, 检查结果驱动修复; 核心工具只有 git 本身
