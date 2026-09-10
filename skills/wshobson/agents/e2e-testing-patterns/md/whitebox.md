# e2e-testing-patterns (`wshobson/agents/e2e-testing-patterns`)

## whitebox

- 识别任务: 对照 "When to Use" 判断是否属于 E2E 自动化、flaky 测试排查、CI/CD 流水线、多浏览器等场景, 不契合则不硬套
- 圈定范围: 按测试金字塔, E2E 只测关键用户旅程 (登录/结账/注册等), 明确排除单元逻辑、API 契约和边缘案例
- 写测试: 模拟用户行为 (点击/输入/断言可见结果), 用 data-testid 或 role/label 定位元素, 用 Page Object 封装页面逻辑, 各测试相互独立且自建自清理数据
- 上层知识不够时, 加载 references/details.md 获取详细模式与完整示例
- 测试失败时用 Playwright 工具链调试: --headed / --debug 运行, 截图/录像回放, test.step 分步报告, page.pause 暂停检查页面状态

- 稳定选择器机制: 只依赖 data-testid / data-cy / role / label 定位, 禁用 CSS 类、nth-child 等脆弱选择器——保证 UI 改版不破坏测试
- 防抖与提速机制: 用正确的等待替代固定超时 (治 flaky), mock 外部 API + 并行执行 + 清理测试数据 (治慢)
- 外部依赖: Playwright 与 Cypress 两个测试框架及其 CLI 调试命令 (npx playwright test --headed / --debug); 无外部模型调用, 详细模式存放在本地文件 references/details.md
