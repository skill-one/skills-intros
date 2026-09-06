---
description: agent 何时应/不应自动触发该 skill
output: TriggerGuide
depends_on: [scenario_intro]
---

基于下面对 skill 的场景分析, 为 AI 编码代理写一份触发时机指南:
- use_when: agent 遇到什么任务时应主动使用该 skill (3~5 条)
- avoid_when: 什么情形下不应使用 (2~3 条)

场景分析: {{ deps.scenario_intro.text }}

skill 名称: {{ skill.name }}
SKILL.md 内容:
{{ skill_md }}
