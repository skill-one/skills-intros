# playwright-generate-test (`github/awesome-copilot/playwright-generate-test`)

## comments

- user: QA 新手第一次写自动化, category: 坑, comment: 只丢一句『测下登录』, 出来的用例没断言像走过场. 把场景写成步骤+预期, 比如『密码错误应提示报错』, 用例立刻完整.
- user: 被拉来补 E2E 的后端老兵, category: 妙用, comment: 它不是看描述硬写, 而是先在浏览器里把流程真点一遍, 选择器都是页面上真实存在的. 我给下单流程补回归用例, 头回跑就绿了.
- user: 独立开发全栈, category: 坑, comment: 第一次本地服务没起, 它卡在页面打不开干耗. 先把应用跑起来、确认 URL 能访问, 场景里再带上测试账号密码.
- user: 测试组长, category: 注意, comment: 产物是 TypeScript 用例, 固定存进 tests 目录. 项目要先装好并初始化 @playwright/test, 不然它最后执行验证那步直接报错.
- user: 前端工程师, category: 妙用, comment: 我把 PRD 验收标准原样粘给它, 每条『用户应该…』各成一个用例. 评审时直接拿生成的测试当验收清单, 产品也能看懂.
- user: 三年测试老手, category: 启发, comment: 失败几次后发现, 锅多半在场景写得糊, 不在工具. 现在写需求就顺手拆成『操作+预期』, 一次生成即过, 它逼我把需求想清楚.
