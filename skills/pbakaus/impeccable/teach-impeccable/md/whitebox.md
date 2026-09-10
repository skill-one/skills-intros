# teach-impeccable (`pbakaus/impeccable/teach-impeccable`)

## whitebox

- 收到对 teach-impeccable 的调用
- Skill.md 检测到自身标记为 DEPRECATED（已并入 impeccable skill）
- 直接输出一条重命名提示：请改用 impeccable teach，不执行任何 teach 流程

- 无解析/转换/校验逻辑：整个技能只是一条静态的重定向提示
- 零外部依赖：不调用任何外部工具、库或模型 API，输出内容由 Skill.md 硬编码指定
