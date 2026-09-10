# clerk-testing (`clerk/skills/clerk-testing`)

## comments

- user: 第一次用的新手, category: 坑, comment: 没调 setupClerkTestingToken() 就直接访问登录页，一直被拦，还以为是 Clerk 挂了。记住：进授权页面前必须先调它绕过机器人检测。
- user: 自动化测试老手, category: 妙用, comment: 用 Playwright 的 globalSetup 登录一次存进 storageState，后面几十个用例直接复用会话，流水线快了近一半，再也不用每个用例走一遍登录 UI。
- user: 独立开发者, category: 注意, comment: 没 Clerk 账号也能跑：npx clerk@latest init 会自动生成 pk_test_*/sk_test_* 临时开发密钥并写进 env 文件，不用注册不用去 Dashboard。
- user: CI 运维老哥, category: 坑, comment: 图省事把生产密钥贴进 CI 跑测试，既有安全风险也不该这么用。测试只认 pk_test_*/sk_test_*，我的环境变量名都带 _test 后缀来区分。
- user: Cypress 用户, category: 注意, comment: Cypress 忘了在 support 文件加 addClerkCommands({ Cypress, cy })，clerk 相关命令全报 undefined。换 Playwright 则要在 globalSetup 里准备登录态，两边别搞混。
- user: QA 组长, category: 启发, comment: 「测试授权 = 隔离的会话状态」这个心智模型点醒我了：以前用例互相共享登录态，一挂连片倒。现在每个测试独立授权上下文，挂了只挂一个。
