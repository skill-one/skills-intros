# convex-auth (`get-convex/agent-skills/convex-auth`)

## blackbox

**function**: 给一个 Convex 应用 (用 Convex 做后端的项目) 加上用户登录功能: 装好后用户就能注册、登录, 而且登录状态能稳定保持。

- input: 一个还没有登录功能的 Convex 项目, output: 同一个项目, 多了登录页面: 新用户能用指纹/面容 (passkey) 注册, 老用户能登录进来
- input: 「我想要 Google 一键登录」这样的需求描述, output: 项目里出现 Google 登录按钮, 点它能走完 OAuth 流程并成功登录
- input: 一个「每次刷新都变回未登录」的应用, output: 修好的版本: 刷新、关掉浏览器再打开, 登录状态都还在
