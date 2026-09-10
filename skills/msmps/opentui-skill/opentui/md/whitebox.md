# opentui (`msmps/opentui-skill/opentui`)

## whitebox

- 接收到 TUI 任务后, 先用 SKILL.md 内置的决策树定位归属: 选框架 (core / react / solid), 并映射到所需概念与组件类别 (如输入 → components/inputs.md)
- 按固定阅读顺序加载参考文件: 必先读所选框架的 REFERENCE.md, 再按任务补读相关文件 (写组件 → api.md; 布局 → layout/REFERENCE.md; 排查问题 → gotchas.md)
- 新建项目时用脚手架 bunx create-tui -t react my-app (注意: 选项必须写在参数前面)
- 编写代码, 全程遵守关键规则: 文本样式用嵌套标签而非 props、退出用 renderer.destroy() 而非 process.exit()
- 若运行报错/布局错乱/输入异常, 按排查索引 (Troubleshooting Index) 定位到对应 gotchas.md 或 testing/REFERENCE.md 复现与回归测试

- 决策树路由机制: SKILL.md 用一组『需求 → 参考文件路径』的决策树 (显示内容/用户输入/布局/动画/测试/平台能力/调试) 做任务分流, 保证只加载与当前任务相关的文档, 而非全量参考
- 分层参考文件结构: 每个框架 (core/react/solid) 固定 5 文件 (REFERENCE.md / api.md / configuration.md / patterns.md / gotchas.md), 横切概念 (layout/keyboard/keymap/animation/testing 等) 为单文件 REFERENCE.md 入口, REFERENCE.md 恒为第一入口
- 外部依赖: OpenTUI 运行时是 Bun (JS 运行时), 原生层用 Zig 构建; 布局基于 Yoga/Flexbox; 可选附加包 @opentui/keymap (分层键位)、@opentui/qrcode、@opentui/ssh (SSH 供服务)、@opentui/three (Three.js WebGPU 渲染); 不依赖任何模型 API
