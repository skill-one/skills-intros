# playwright-generate-test (`github/awesome-copilot/playwright-generate-test`)

## whitebox

- 1. 接收用户给的场景; 没有场景就先追问, 拿到才动工
- 2. 通过 Playwright MCP 提供的浏览器工具, 按步骤逐条实际执行场景, 禁止跳过直接写代码
- 3. 全部步骤跑完后, 依据完整消息历史生成 @playwright/test 的 TypeScript 测试
- 4. 把测试文件保存到 tests 目录
- 5. 执行该测试文件, 失败就修改重跑, 循环直到通过

- 真机驱动而非凭空生成: 核心约束是 '不许提前/只凭场景写代码', 必须先用 Playwright MCP 工具在真实浏览器里一步步操作, 保证测试贴合真实页面行为
- 消息历史作为代码依据: 生成的测试不是基于场景文本, 而是基于 MCP 执行步骤后的完整对话记录, 即 '先做后写'
- 闭环校验: 生成后立即执行测试并迭代修复, 以 '测试通过' 为最终交付标准; 依赖的外部工具为 Playwright MCP (浏览器操作) 与 @playwright/test (测试框架)
