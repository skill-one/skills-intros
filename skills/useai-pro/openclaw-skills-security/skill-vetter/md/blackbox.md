# skill-vetter (`useai-pro/openclaw-skills-security/skill-vetter`)

## blackbox

**function**: 在你安装任何技能 (skill) 之前, 帮你检查它是否安全, 告诉你能不能装。

- input: 从 ClawHub 或 GitHub 上看中的技能说明文件 (SKILL.md), output: 一份安全审查报告: 给出 SAFE / WARNING / DANGER / BLOCK 四档判定, 列出发现的风险点, 并明确建议「装 / 再查查 / 别装」
- input: 一个技能的名字, 比如「gihub-push」, 以及它的来源, output: 仿冒检测结果: 告诉你它是不是蹭热门技能名的高仿品 (比如把 github 拼错), 以及作者的可靠程度
- input: 一个已安装技能的说明文件, 想定期复查一遍, output: 一份权限体检报告: 它能读哪些文件、要不要联网、有没有悄悄要危险权限, 每项标注是否合理
