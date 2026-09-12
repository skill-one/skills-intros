# javascript-testing-patterns (`wshobson/agents/javascript-testing-patterns`)

## comments

- user: 后端老兵, category: 妙用, comment: 把仓库层改成构造函数注入后, 测试里直接塞个假实现, 不连数据库秒级跑完. 重构老服务前先干这个最值。
- user: 前端新人, category: 坑, comment: beforeEach 忘了加 vi.clearAllMocks(), 上个用例的调用次数累计到下个用例, 断言莫名全挂, 查了一下午才定位。
- user: 测试工程师, category: 注意, comment: 配置自带 80% 覆盖率红线, 老项目接入 CI 直接全挂. 先删 coverageThreshold 跑通, 再逐步拉回 80%。
- user: 全栈独立开发, category: 妙用, comment: faker 工厂只传我关心的字段, 其余随机生成, 造数从十几行缩到一行, 还顺带覆盖了各种意外数据的组合。
- user: 技术组长, category: 启发, comment: "测行为不测实现"这条让我重审存量用例: 一半在断言内部调用, 一重构就红. 改成断言返回结果后才敢动代码。
- user: 转行自学者, category: 注意, comment: 集成测试和 React 组件测试在主文档只有一句带过, 完整代码在 references 文件里, 别翻半天以为没写。
