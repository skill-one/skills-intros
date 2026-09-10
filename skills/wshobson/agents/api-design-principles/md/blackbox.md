# api-design-principles (`wshobson/agents/api-design-principles`)

## blackbox

**function**: 帮你设计和审查软件之间的接口 (API, 即不同软件互相调用的约定), 让接口好用、规范、不易出错。

- input: 一句话需求, 如: 「我要给手机 App 做登录和查订单的功能」, output: 一份接口设计文档: 每个接口的地址、用途、要传什么参数、会返回什么数据, 开发可直接照着实现
- input: 已有的接口文档或接口列表 (如贴出一段 OpenAPI/Swagger 文件), output: 一份审查报告: 逐条指出设计不合理之处 (命名混乱、缺少分页、错误提示不统一等) 和对应的修改建议
- input: 一个选型问题, 如: 「我们这个系统该用 REST 还是 GraphQL?」, output: 针对你的场景给出明确推荐、理由和注意事项, 而不是两边都说好
