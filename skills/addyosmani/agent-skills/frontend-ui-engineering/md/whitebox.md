# frontend-ui-engineering (`addyosmani/agent-skills/frontend-ui-engineering`)

## whitebox

- 确认任务属于"构建/修改用户界面", 按组件拆出文件结构 (组件、测试、Storybook、hook、types 同目录共存)。
- 为涉及的状态选最简方案: 在 useState → 提升状态 → Context → URL 参数 → 服务端缓存 → 全局 store 的决策表里挑一档。
- 按项目设计系统实现视觉: 语义色 token、固定间距刻度、正确标题层级, 刻意规避紫色渐变等 "AI 味" 默认样式。
- 补齐工程细节: 键盘可达、ARIA 标注、焦点管理、加载骨架屏/错误/空三态, 移动优先的响应式。
- 按验证清单走查: Tab 遍历、320/768/1024/1440px 四档断点、axe-core 无警告, 通过即交付。

- 容器/展示分离 + 组合优于配置: 数据获取与 loading/error/empty 判断放容器组件, 纯渲染放展示组件; 复杂状态抽成自定义 hook; 技术栈为 React (TSX) + Tailwind, 组件文档可选 Storybook。
- 状态路由决策表: useState (组件内 UI 态) → 提升 (2-3 个兄弟共享) → Context (主题/认证等读多写少) → URL searchParams (筛选/分页, 可分享) → React Query/SWR (服务端数据缓存, 支持乐观更新) → Zustand/Redux (全局复杂状态); prop 钻取超 3 层即重构组件树。
- WCAG 2.1 AA 内建于实现而非后补: 优先原生语义元素 (button 而非 div+role)、图标按钮补 aria-label、对话框打开即移入焦点、骨架屏标注 aria-busy、不全靠颜色传达状态; 验证靠键盘走查 + axe-core 检查 (详见 references/accessibility-checklist.md)。
