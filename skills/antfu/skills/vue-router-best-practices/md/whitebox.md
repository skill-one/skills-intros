# vue-router-best-practices (`antfu/skills/vue-router-best-practices`)

## whitebox

- 接收用户提出的 Vue Router 相关问题 (如守卫不触发、组件数据不刷新、内存泄漏)
- 用问题描述中的症状关键词, 与 skill.md 的索引条目做匹配 (如 '同路由参数变化数据不更新' → router-param-change-no-lifecycle)
- 按索引指向, 加载对应的 reference/ 目录下的参考文档
- 依据该文档的最佳实践与陷阱说明, 给出针对性的解答或修复方案

- 症状→文档索引机制: skill.md 本质是一张目录表, 按问题症状 (守卫/路由生命周期/路由配置三类) 组织, 每条指向一个具体参考文档, 定位即检索
- 知识来源为技能内置的 reference/ markdown 文档 (如 router-navigation-guard-next-deprecated.md), 覆盖导航守卫、路由生命周期、路由配置三类主题
- 不依赖任何外部工具、库或模型 API, 全部能力来自 skill.md 及其引用的参考文档, 不做超出文档范围的推断
