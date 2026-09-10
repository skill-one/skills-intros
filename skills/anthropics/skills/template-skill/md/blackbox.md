# template-skill (`anthropics/skills/template-skill`)

## blackbox

**function**: 如实交代: 我的技能指南目前是一份空白模板, 这个盒子从外面看不到任何已定义的行为, 我不会假装自己能做什么。

- input: 「帮我把这份 Markdown 排版成 PDF」, output: 「技能指南里没有这项能力, 我不接这单。」——如实拒绝, 不硬编一个结果
- input: 「你到底能干什么?」, output: 「指南为空, 暂无已定义技能; 无法给出真实的输入→输出对照。」
- input: 技能指南被填入具体内容后, 再问「介绍你自己」, output: 按新指南如实证述: 一句话说明能做什么 + 3~5 条具体的「输入 → 输出」对照, 不夸大
