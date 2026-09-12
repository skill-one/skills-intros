# react-native-design (`wshobson/agents/react-native-design`)

## whitebox

- 识别任务是否属于 React Native 开发范畴：样式、React Navigation 导航、Reanimated 3 动画、响应式布局、性能优化
- 以内置 Quick Start 组件模式为骨架，输出 TypeScript + StyleSheet.create 的 React Native 组件代码
- 按需接入手势与动画：用 Reanimated 的 useSharedValue/useAnimatedStyle/withSpring 让按压缩放等交互跑在 UI 线程
- 用 Best Practices 清单收尾自检：SafeArea 适配、FlatList 替代 ScrollView+map、React.memo、Platform.select 平台差异
- 对照 Common Issues 提示潜在坑位：手势冲突用 GestureDetector、动画卡顿移入 worklet、useEffect 清理防内存泄漏

- 代码生成：不依赖外部模型/工具调用，直接按 SKILL.md 内的 Quick Start 模板产出代码——React Native 核心组件 (View/Text/Pressable/Image) + StyleSheet.create 样式 + TypeScript 类型标注
- 动画机制：基于 Reanimated 3（useSharedValue + useAnimatedStyle + withSpring），动画在 UI 线程 worklet 执行以保证 60fps；手势经 Gesture Handler 的 GestureDetector/GestureDetector 处理，冲突时用 simultaneousHandlers
- 校验机制：以 SKILL.md 内 Best Practices 与 Common Issues 两份清单做代码审查基准——真机测试提醒、导航 ParamList 类型定义、自定义字体加载 (expo-font/react-native-asset)、刘海屏 SafeArea 处理
