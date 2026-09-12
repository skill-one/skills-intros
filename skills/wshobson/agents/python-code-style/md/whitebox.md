# python-code-style (`wshobson/agents/python-code-style`)

## whitebox

- 判断任务是否落在技能范围内: 写新代码、审查代码风格、配置 linter、写 docstring、定团队规范或项目文档
- 读取用户的代码或 pyproject.toml, 按技能规则体检: 命名 (PEP 8)、导入顺序、行宽 120、类型注解、docstring 完整性
- 套用技能内的现成模式生成产物: ruff/mypy 的 pyproject.toml 配置块、符合规范的代码改写、Google 风格 docstring、README/CHANGELOG 骨架
- 附上可执行的验证命令, 让用户本地跑 ruff check --fix / ruff format / mypy 自检
- 交付时附最佳实践清单 (10 条), 建议接入 CI 让检查在每次提交时自动执行

- 规则库驱动, 不依赖任何模型 API: 所有判断来自 skill.md 内置的硬性规范 — ruff 选用的 lint 规则集 (E/W/F/I/B/C4/UP/SIM)、命名约定 (PascalCase 类 / snake_case 函数 / SCREAMING_SNAKE_CASE 常量)、导入三分组 (标准库 → 第三方 → 本地, 只用绝对导入)
- 配置一次、工具自动执行: 用 ruff 一个工具替代 flake8+isort+black 做格式化和 lint, 用 mypy strict (或 pyright strict) 做类型检查, 全部收敛到 pyproject.toml; 行宽统一 120, 目标版本 py312
- 文档即代码: docstring 统一 Google 风格 (Args/Returns/Raises/Example 段落), 项目文档按固定 README 结构 + Keep a Changelog 格式生成
