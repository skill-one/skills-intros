# vitest (`antfu/skills/vitest`)

## blackbox

**function**: 一个专管「单元测试」的编程助手: 帮你给 JS/TS 代码写测试、修测试报错、配置测试功能 (mock 假数据、覆盖率报告、快照对比等)。

- input: 一个写好的 JS/TS 源码文件 (如 utils.ts), output: 配套的测试文件 (如 utils.test.ts), 里面是针对每个函数的多个测试用例
- input: 一个跑不过/报错的测试文件, 附上报错信息, output: 报错原因说明 + 改好的测试代码
- input: 一句话需求: 「测试时不要真的发网络请求」, output: 用 mock (假数据替代真实请求) 改写后的测试代码, 直接可用
