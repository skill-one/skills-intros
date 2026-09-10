# frontend-design (`pbakaus/impeccable/frontend-design`)

## whitebox

- 被触发后读取 skill.md, 第一件事确认: 本技能已废弃 (deprecated), 功能全部迁移至 `impeccable`
- 检查环境中 `/impeccable` 技能是否存在
- 若存在 → 直接改用 `/impeccable` 处理请求, 并告知用户 `frontend-design` 文件夹是废弃残留、可删除
- 若不存在 → 指引用户在终端运行 `npx impeccable skills update` 更新技能
- 全程不做任何实际设计工作, 唯一职责是重定向

- 废弃声明内嵌: skill.md 正文直接写明 deprecated + 新名称, 无需任何解析逻辑, 读取即知
- 存在性探测分支: 以 `/impeccable` 是否存在为唯一判断条件, 二选一输出『直接使用』或『更新指引』, 无第三条路径
- 外部依赖仅一个: `npx impeccable skills update` (npm 提供的命令行工具, 由用户自行执行); 无设计库、无模型 API——因为本技能被明确禁止做设计工作
