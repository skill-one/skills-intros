# vercel-cli-with-tokens (`vercel-labs/agent-skills/vercel-cli-with-tokens`)

## blackbox

**function**: 把你的网页项目一键部署到 Vercel (一个网站托管平台), 并帮你管理部署网址、环境变量和自定义域名 — 无需手动登录网站操作。

- input: 一个写好的网页项目文件夹 + 一把 Vercel 访问令牌 (token, 相当于平台钥匙), output: 部署完成, 返回一个可访问的网址 (如 https://my-app.vercel.app), 点击即可打开网站
- input: 「上线到正式环境」或「先给我一个预览版看看」, output: 对应环境的部署链接: 正式版面向所有访客生效; 预览版仅用于内部查看, 不影响线上
- input: 一对环境变量, 如 DATABASE_URL=postgres://..., output: 变量已写入项目的配置中, 并附上当前全部变量清单供核对
- input: 一个部署网址 + 「构建失败了, 帮我看看为什么」, output: 该次部署的构建日志和失败原因分析, 如缺依赖、缺环境变量、框架配置错误
