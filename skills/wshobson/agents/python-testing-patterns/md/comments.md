# python-testing-patterns (`wshobson/agents/python-testing-patterns`)

## comments

- user: 后端老兵, category: 妙用, comment: 测重试逻辑不用真等超时：mock 的 side_effect 传个列表，前两次抛异常最后一次成功，再断言 call_count，几秒验证完整套重试。
- user: 测试开发实习生, category: 坑, comment: 我把被测函数本身 mock 掉了，测试全绿，一上线接口就炸。该 mock 的是它调的外部依赖（网络、数据库），被测的那段代码要真跑。
- user: CI/CD 运维老哥, category: 妙用, comment: CI 里加 --cov-fail-under=80，覆盖率一掉流水线直接红，没人能偷偷合代码；本地用 -m "not slow" 跳过慢测试秒出结果。
- user: 独立开发者, category: 妙用, comment: token 过期、会员到期这种时间逻辑，以前得改系统时间测；freezegun 把时间钉死还能 move_to 往前拨，过期场景一分钟写完。
- user: 第一次写测试的新手, category: 坑, comment: 文件和函数没按 test_ 前缀命名，pytest 收集到 0 条，我以为装坏了；改完名立刻能跑。函数也别叫 test_1，挂了根本查不到测的哪个功能。
- user: 测试组老组长, category: 启发, comment: 为凑覆盖率补了一堆简单函数测试到 90%，核心分支照样漏。改用「模块_场景_预期结果」命名用例后，逼自己先想清楚每个测试到底验证什么行为。
