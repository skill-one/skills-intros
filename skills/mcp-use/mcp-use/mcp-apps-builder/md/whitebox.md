# mcp-apps-builder (`mcp-use/mcp-use/mcp-apps-builder`)

## whitebox

- 先勘察现场: 读 package.json、服务端入口、views/、skills/、mcp-env.d.ts, 并确认已安装的 mcp-use 版本——版本决定能用哪些 API
- 按任务类型只加载对应的参考文档 (server / views / auth / skills-over-mcp / advanced-features, 迁移看 migration, 收尾看 verification), 不读无关内容
- 新项目用 create-mcp-use-app@latest 脚手架生成; 改造时代码严格对着已安装版本的类型写, 不照抄历史示例或旧版 changelog
- 用最小的真实生命周期验证本次改动的行为, 再按风险比例扩大检查范围
- 报告完成前跑一遍 verification 检查单, 类型/导出/鉴权/交互有改动时, 仅源码构建通过不算数

- 事实锚定: 已安装的 mcp-use 包、导出类型、声明文件和项目现有代码是唯一事实来源; 不确定的细节去声明文件/源码里确认, 禁止臆造导出、配置字段或回调形状
- Schema 契约: 工具参数用 inputSchema 定义, 结构化结果与 View 绑定的工具必须加 outputSchema; 成功结果必须返回与 schema 匹配的 structuredContent (裸业务对象不允许); 每个 View 固定放 views/<name>/view.tsx 并以 view: { name } 绑定。依赖: mcp-use 框架 (服务端 API)、mcp-use/react (View 层 React hooks)、MCP 协议本身
- 状态防腐: 身份与可变工作流状态按请求作用域或外部存储管理, 禁止用模块级全局变量承载跨请求状态; 客户端上报的元数据一律视为未验证
