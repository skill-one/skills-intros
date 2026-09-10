# react-native-best-practices (`callstackincubator/agent-skills/react-native-best-practices`)

## whitebox

- 识别问题类型: 按问题→技能映射表 (卡顿/重渲染/启动慢/包体积大/内存增长等) 路由到对应的 js-*/native-*/bundle-* 参考文档
- 先测量基线: 运行时问题用 agent-device react-devtools 采样重渲染与慢组件, 包体积用 react-native bundle + source-map-explorer, 启动用 react-native-performance; 没有测量数据不提优化建议
- 查阅对应 references/ 文档, 套用其中的针对性修复方案
- 用同一方法复测, 验证指标确实改善 (如 FPS 45→60)
- 若指标无改善则回滚, 换映射表中的下一个起点

- 证据驱动 + 审查护栏: 所有建议前置于测量结果, 且先查库版本 (如 FlashList v2 已弃用 estimatedItemSize)、无 profiler 证据不臆测 stale closure 或盲目加 useMemo; 依赖外部工具链: agent-device CLI、React DevTools/Metro、source-map-explorer、react-native-performance、Xcode Instruments、Android Studio Profiler、Hermes
- 静态知识库路由: 基于 Callstack《Ultimate Guide to React Native Optimization》整理的多篇 markdown 参考文档 (js-*/native-*/bundle-* 三类前缀), 按影响等级 CRITICAL→MEDIUM 排优先级, 经问题映射表索引
- 分层修复方案: 覆盖 JS/React (FlashList、React Compiler、Jotai/Zustand、Reanimated、非受控输入)、Native (Turbo Modules、线程模型、内存模式、16KB 对齐)、打包 (避免 barrel 导入、tree shaking、R8、Hermes mmap、代码分割) 三个层面
