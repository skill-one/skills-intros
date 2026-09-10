# obsidian-bases (`kepano/obsidian-skills/obsidian-bases`)

## blackbox

**function**: 在 Obsidian 里把你的笔记变成可筛选、可排序的数据库视图——你说需求, 我给你一个贴进笔记库就能用的 .base 文件。

- input: 一句话需求: "把所有带 #task 标签的笔记做成表格, 显示状态、优先级和截止日期, 没完成的排前面", output: 一个 .base 文件, 粘贴进 Obsidian 后直接出现任务表格, 自动按条件筛选和排序
- input: 一个打开就报 YAML 错误、显示不出内容的 .base 文件, output: 修好的 .base 文件, 贴回原处即可正常渲染
- input: 现有 .base 文件 + 追加需求: "再加一列, 自动算出每本书预估要读多少分钟", output: 更新后的 .base 文件, 表格里多出一列自动计算的读时估算
