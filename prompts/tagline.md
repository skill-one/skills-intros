---
description: 3 条 20 字以内的宣传短标语
output: Taglines
depends_on: [one_liner]
---

基于下面的一句话简介, 为 skill 生成 3 条中文宣传短标语, 每条 20 个汉字以内,
风格精炼有力, 面向开发者群体。

一句话简介: {{ deps.one_liner.text }}

skill 名称: {{ skill.name }}
SKILL.md 内容:
{{ skill_md }}
