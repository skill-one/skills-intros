# implement-specs (`warpdotdev/common-skills/implement-specs`)

## blackbox

**function**: 把已经定稿的产品/技术文档变成能跑的功能代码, 并且文档和代码始终对得上、一起交付。

- input: 一个已批准的功能文档目录, 如 specs/APP-1234/(内含 PRODUCT.md 和 TECH.md), output: 按文档实现好的功能代码, 和这两份文档放在同一个 PR (代码审查包) 里提交, 审阅者一次看全
- input: 开发中途一句改动要求: "下单按钮在没选完地址前应是灰色不可点", output: 改好的代码 + 同步更新过的文档 (行为描述与新代码一致), 继续放在同一 PR 里
- input: "这个功能做完了吗, 靠谱吗?", output: 一份验证结论 + 配套测试代码, 逐条对照文档里的验收标准告诉你哪些过了、哪些没过
