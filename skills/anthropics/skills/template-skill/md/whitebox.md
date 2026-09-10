# template-skill (`anthropics/skills/template-skill`)

## whitebox

- 触发后读取 skill.md 全文，作为唯一能力来源
- 解析结果：仅含 name: template-skill 与占位符 description，正文无任何指令
- 按规则校验：不存在可推导的执行流程、转换或校验逻辑
- 拒绝虚构，向用户如实报告技能为空模板
- 请求用户提供真实 skill.md，之后才能执行任务

- 解析机制：逐行读取 skill.md，仅找到 YAML 头 (name/description) 与 "# Insert instructions below" 空占位符
- 校验机制：所有输出必须可溯源到 skill.md 原文；因文件为空模板，无内容可推导，故不生成虚构流程
- 外部依赖：无——skill.md 未声明任何外部工具、库或模型 API
