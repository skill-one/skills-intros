# clerk-setup (`clerk/skills/clerk-setup`)

## blackbox

**function**: 给你的网站或应用加上「登录/注册」功能：给我一个项目，交还给你时用户已经能注册账号、登录，并能控制哪些页面必须登录才能看。

- input: 一个 Next.js 项目的文件夹路径, output: 同一个项目，配置好登录：多了登录/注册页面，被保护的页面未登录会跳转去登录
- input: 一句话需求「给我的 Vue 应用加上登录」+ 项目路径, output: 接好登录的项目代码，本地跑起来就能用邮箱或 Google 账号注册、登录
- input: 一个已经用旧方案（如 Firebase）做登录的老项目, output: 一份迁移方案（老用户怎么搬过来、会不会掉线）+ 换成新登录后的代码
