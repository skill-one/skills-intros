# argent-create-flow (`software-mansion/argent/argent-create-flow`)

## whitebox

- 分诊选型: 先读参考文档; QA 用例/验收标准场景先加载 argent-qa-flows, 再定 flow 类型 — e2e 以 launch: 起头, fragment 声明 executionPrerequisite
- 实时录制: 首次启动/操作前开启录制器, 一次录一步并即时验证; await-ui-element 等检查在对应状态出现时录制, 不事后重建
- 打磨: 把录制步骤转成语义目标 (严格 id > 稳定文本/无障碍标签), 每个屏幕变化补身份检查 + await idle, 不改变步骤原意
- 端到端回放: 最终 YAML 无中断完整跑一遍; QA 流程要求连续两遍通过
- 交付报告: 文件路径、回放命令、结果、前置条件/副作用、坐标与原始手势例外

- 录制不可回溯 + 显式绑设备: 录制器必须先于首步启动, 已完成的路径无法补录; 回放从不自动绑定 iPhone — 须显式传 udid (CLI --device), 仅 kind "device" 且 connected 的物理机可跑; 真机上 UI 树就是 describe 树, pinch/rotate 必失败 (硬件契约依赖 argent-ios-device-interact)
- 稳定性门禁: 选择器只允许固定于应用代码、跨账号/数据/时间/数量/顺序/locale 不变的值 (禁止 gate 在 Today/计数/时间戳上); 屏外元素用 scroll-to, 重复元素用 within/after/next 作用域消歧; 原始坐标警告必须立即过 coordinate fallback gate; 屏幕变化靠目标身份检查 + await idle 证明 (静止 ≠ 身份, idle 可能带警告通过)
- 修复收敛规则: 回放失败先定位首个分歧点, 只修最小合理单元 → audit → 全量回放; 两轮仍失败即停, 绝不为通过而削弱检查; 打磨期唯一允许的未录制插入是 snapshot:、导航 idle、Chromium 打包 launch:; 本地脚本仅当用户明示要求且经 flow-add-script 录制
