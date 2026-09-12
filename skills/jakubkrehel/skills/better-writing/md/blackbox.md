# better-writing (`jakubkrehel/skills/better-writing`)

## blackbox

**function**: 审查并改写产品界面里的文字（按钮、报错提示、空状态等），指出哪里写得不清楚、不一致，并给出可直接替换的新文案。

- input: 一个页面/组件的文件路径，如 src/settings/ProfileForm.tsx, output: 一张文案问题清单表：出现位置、原文、建议改成什么、为什么；结尾给出「放行」或「先改再放行」的结论
- input: 一句话需求，如「删除项目的确认弹窗要写什么」, output: 可直接上线的一套文案：标题「删除这个项目？」+ 按钮「删除项目」「取消」
- input: 一段报错提示，如「Oops! Something went wrong.」, output: 改写后的提示，如「无法保存。请检查网络连接后重试」——说清哪里出了问题、用户该怎么补救
