# argent-react-native-optimization (`software-mansion/argent/argent-react-native-optimization`)

## whitebox

- Phase 1 静态扫描: 项目根目录跑一次 ESLint (RN 性能规则集), 按文件派子代理并行修复机械性问题 (如内联样式、index key)
- Phase 2 语义扫描: 按 checklist 逐项派子代理审查需要判断的领域 — memoization、列表渲染、动画、异步模式、effect 清理、状态卫生、context 架构
- Phase 3 实测剖析: 挂载 profiler 双端采样, 跑关键用户路径, 聚合 React + native 分析交叉定位真实瓶颈, 修最高影响项
- 复测: 对比目标指标 — 改善则保留, 无净收益或权衡不可接受则回滚; 架构级修改每周期只改一个再复测, 机械性修改批量后复测一次
- Phase 4 回归验证: 遍历范围内所有屏幕查崩溃/红屏/运行时日志, 最后重跑 lint 确认没引入新问题

- 先测量后动手: 修前必须定义目标指标+阈值 (禁散弹式优化); 用 profiler 做发现而非仅验证; 设备操作用 argent-create-flow 录制成 flow, 保证每轮复测步骤完全一致
- 剖析工具链 (依赖 argent-react-native-profiler skill): react-profiler-renders 快速扫描出热组件; react-profiler-start → stop → analyze + native-profiler-analyze + profiler-combined-report 做深度测量; react-profiler-component-source / fiber-tree 追溯组件源码与祖先渲染成本 — 若报告 reactCompilerEnabled=true, 需用 fiber-tree 确认缺失 useMemoCache (compiler bail-out) 后才允许提 useCallback/useMemo/React.memo
- 主代理/子代理分工 + 回归防线: Phase 1–2 派子代理并行 (lint 一文件一个, 语义一 checklist 项一个), 但子代理不能碰设备 — profiling 与 E2E 验证只在主代理做; 修复前用 react-profiler 系列重新取证做逻辑推演, 提交前用 debugger-evaluate 验证, 回归靠 debugger-log-registry 查日志 + 截图查红/黄屏 (未连接则按其 guidance 先重连)
