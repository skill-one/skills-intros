# better-auth-best-practices (`better-auth/skills/better-auth-best-practices`)

## blackbox

**function**: 帮你在 TypeScript 网页项目里搭好用户登录系统 (Better Auth): 邮箱密码注册、Google 等第三方登录、会话保持、两步验证等，交付能直接粘贴运行的配置代码和要执行的命令。

- input: 「我的 Next.js 项目想加邮箱 + 密码注册登录，用 PostgreSQL」, output: 一段可直接粘贴的 auth.ts 配置 + 前端登录/注册调用代码 + 需要设置的 2 个环境变量 + 要在终端跑的几条命令（装包、建数据表）
- input: 你的 auth.ts 配置文件 + 一句「部署后用户刷新页面就掉登录状态」, output: 指出问题所在的修改后配置代码，以及需要补上/改正的环境变量
- input: 「想加 Google 登录和两步验证」, output: 服务端和前端的接入代码，外加一句提醒：加完插件要重跑一次数据库同步命令
