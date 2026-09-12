# pinia (`antfu/skills/pinia`)

## whitebox

- 接收 Pinia 相关任务: 定义 store、state/getters/actions、插件、store 组合、测试、SSR/Nuxt 等
- 对照 skill.md 的主题索引表, 判断任务属于哪个模块 (核心 Stores / 插件扩展 / 组合复用 / 最佳实践 / 进阶 SSR·Nuxt·HMR)
- 按需加载对应参考文件 (如 references/core-stores.md) 获取该主题的权威写法
- 依据内建的 Key Recommendations 组织方案: Setup Store 优先、解构用 storeToRefs、SSR 中在函数内调用 store 等
- 输出可直接落地的 store 代码与用法建议

- 索引路由: skill.md 本身是一张主题表, 按任务关键词定位到 references/ 下的分主题文档, 答案以文档为准, 不臆造
- 版本锚定: 知识源自 Pinia 官方仓库 (vuejs/pinia) v3.0.4, 生成于 2026-01-28, 回答与官方 API 对齐
- 规范内建: 关键最佳实践 (storeToRefs 保响应性、@pinia/testing 测试、HMR 支持等) 已硬编码在 skill.md, 无需额外外部工具或模型 API
