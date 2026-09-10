# python-testing-patterns (`wshobson/agents/python-testing-patterns`)

## blackbox

**function**: 帮你给 Python 代码做「体检」:生成测试代码、隔离外部服务、诊断测试失败,让你改动代码时有信心不出错。

- input: 一个 Python 源码文件 (如 utils.py), output: 配套的测试文件 (test_utils.py), 运行后全绿通过, 覆盖正常情况和边界情况
- input: 一段会调用 API、数据库或时间相关的代码, 要求测试时不真的连外部服务, output: 用替身对象 (mock, 模拟外部服务的假件) 隔离后的测试, 断网也能随时运行
- input: 一片飘红的测试报错输出, output: 失败原因诊断 + 修好的测试或代码
- input: 一条功能需求描述 (还没写代码), output: 先写好的测试代码 (TDD, 测试先行), 明确成功标准后再动手实现
- input: 「我想知道代码有多少被测过了」, output: 覆盖率报告: 哪些行有测试、哪些行还是裸奔, 一目了然
