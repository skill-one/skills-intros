# ponytail-help (`dietrichgebert/ponytail/ponytail-help`)

## whitebox

- 触发匹配: 捕获 /ponytail-help 或自然语言触发语 ("ponytail help" / "what ponytail commands" / "how do I use ponytail")
- 展示参考卡: 一次性输出模式表 (Lite/Full/Ultra)、六项技能表、停用/默认模式配置、更新方法
- 副作用自检: 明确不切换模式、不写 flag 文件、不持久化任何状态
- 结束: 一次性 (one-shot) 完成, 无后续流程

- 触发解析: 纯关键词匹配 (斜杠命令 + 自然语言短语), 在宿主 agent (Claude Code / Codex / OpenCode) 内完成, 无需独立解析器
- 静态内容直出: 卡片全部内容固化在 SKILL.md 里, 输出即复读, 零计算、零转换、零校验
- 无外部依赖: 不调用任何外部工具、库或模型 API; 与其他 ponytail 技能不同, 显式禁止写状态文件, 保证零副作用
