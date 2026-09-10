# archify (`tt-a1i/archify/archify`)

## whitebox

- 分型: 按问题路由到五种类型之一 (architecture/workflow/sequence/dataflow/lifecycle); 若输入是 Mermaid, 只提取其拓扑与语义 (flowchart→workflow, sequenceDiagram→sequence, stateDiagram→lifecycle), 不照搬其样式
- 产出候选: 按对应 schema + 示例的字段形状, 用领域语言新写一份小而带类型的 JSON 规格 (artifact first, 先写候选文件再谈其他; 默认静态, 主路径清晰, ≤12 个主节点)
- 校验: 跑 `node bin/archify.mjs validate <type> <candidate.json> --quality showcase --json`, 按 9 项 artifact 检查、0 报错 0 警告的门槛做定向修复; 校验通过后规格字节冻结, 不再改动
- 交付: 跑 `deliver` 命令做最终验收 —— 将规格快照→渲染→原子提交 HTML, 出具 SHA-256 与字节数凭据; 非零退出码绝不谎报成功
- 取证: 跑 `visual-check` 在真实浏览器中对已交付 HTML 采集尺寸测量与截图证据 (不修改、不重渲染); 确定性凭据、浏览器证据、人工视检三者分开陈述

- 单一数据源: 全部由小份 typed JSON 规格决定, 渲染成内联 SVG 的自包含 HTML; 暗色/亮色主题、缩放/搜索/关系追踪、PNG/JPEG/WebP/SVG/WebM 导出等能力内置于生成物中, 属于阅读器自带功能而非额外开发
- 命令行校验器: 依赖 Node.js 运行 bin/archify.mjs (validate/deliver/visual-check/brands/doctor 等子命令); validate 输出 9 项检查与构图/几何诊断, deliver 做确定性快照+原子提交+哈希凭据; showcase 级验收要求全 9 项通过
- 无模型 API、零安装: 全流程是本地确定性工具链, 不调用任何模型; 无 shell 时降级为手工把架构 SVG 放入 assets/template.html 并用 CSS 语义类, 再按交付契约做视觉审查
