# modern-javascript-patterns (`wshobson/agents/modern-javascript-patterns`)

## whitebox

- 接收任务, 匹配触发场景: 重构旧 JS 语法、回调迁移 Promise/async-await、实现函数式模式、性能优化等。
- 以导航层的 15 条最佳实践为依据, 逐条转换代码 (const 默认、箭头函数、解构、async/await、避免突变、可选链等)。
- 导航层信息不够时, 按需读取 references/details.md 获取详细模式文档。
- 涉及常见坑 (this 绑定、Promise 反模式、内存泄漏) 时, 查阅 references/advanced-patterns.md。
- 输出符合 ES6+ 规范、可维护、可测试的代码。

- 两级文档 + 懒加载: skill.md 只存导航层 (触发场景 + 15 条最佳实践), 详细内容放 references/details.md, 仅在导航层不足时才读取, 控制上下文开销。
- 清单驱动转换: 以 15 条最佳实践为规则集, 把旧写法 (var、循环、字符串拼接、Promise 链、直接改数据) 系统性替换为对应 ES6+ 模式 (const、数组方法、模板字符串、async/await、展开运算符)。
- 外部依赖: 仅有两个本地参考文件 (references/details.md、references/advanced-patterns.md); skill.md 未声明任何外部工具、库或模型 API。
