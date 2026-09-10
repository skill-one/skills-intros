# python-testing-patterns (`wshobson/agents/python-testing-patterns`)

## whitebox

- 识别任务类型：对照 skill 的 When to Use 清单，判定是单元测试、集成测试、TDD、mock 外部依赖还是排查失败测试
- 按核心规范写测试：AAA 三段式（Arrange-Act-Assert）组织代码，命名遵循 test_<单元>_<场景>_<预期> 模式
- 细节不够时查参考文档：读取 references/details.md 或 references/advanced-patterns.md 中的进阶模式（异步、monkeypatch、数据库、CI/CD 等）
- 交付可运行的测试代码：附 pytest 运行命令，按需带 pytest-cov 覆盖率参数（如 --cov-fail-under=80）

- 测试结构模板机制：每个测试强制 AAA 三段式 + 描述性命名，测试间相互独立、各自清理状态，共享夹具集中放 conftest.py
- 依赖隔离机制：用 unittest.mock 的 Mock + side_effect 模拟外部依赖（可按序返回多次失败再成功，验证重试逻辑）；用 freezegun 冻结或推进系统时间，确定性测试过期/时间跨度等行为
- 运行与度量机制：pytest 作为执行器，@pytest.mark.slow/integration/skip/xfail 等标记支持选择性运行和条件跳过；pytest-cov 统计覆盖率并可设阈值卡点
