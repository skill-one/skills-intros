# implement-specs (`warpdotdev/common-skills/implement-specs`)

## whitebox

- 校验前置条件: specs/<工单>/ 下已存在 PRODUCT.md 与 TECH.md, 且规格已评审通过
- 通读规格: 以 PRODUCT.md 为行为事实来源、TECH.md 为架构事实来源, 先理解行为/约束/风险/验证计划再写代码
- (大型功能时) 提供可选辅助文档: PROJECT_LOG.md 记进度、DECISIONS.md 记决策, 避免重复探索
- 拆解实现步骤并编码: 行为对齐 PRODUCT.md, 架构与顺序对齐 TECH.md, 同步补测试与验证产物
- 实现若推翻原设计, 立即回写对应规格; 收尾前按当前规格逐项验证 (测试通过) 后才算完成

- 双规格锚定解析: PRODUCT.md 只管用户可见行为 (UX/边界/成功标准), TECH.md 只管架构/模块边界/实现顺序; 所有改动以这两份为唯一对齐基准
- 规格-代码同 PR 共演进: 规格修订、代码、测试进同一个 PR, 且决策变化时立即改规格而非攒到最后; PR 描述的是实际交付的功能, 评审始终锚定真实实现
- 无外部工具/库/模型 API 依赖: 全流程只基于 markdown 规格文件、git PR 工作流, 以及仓库自带的测试惯例 (单测 + 重要用户流的集成/E2E 测试)
