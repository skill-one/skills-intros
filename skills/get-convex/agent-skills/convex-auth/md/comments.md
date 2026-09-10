# convex-auth (`get-convex/agent-skills/convex-auth`)

## comments

- user: 第一次接 Convex 活的外包程序员, category: 坑, comment: 页面不报错但永远显示未登录,查了两天代码才发现是漏写 convex/auth.config.ts——这文件错了不报任何错,只会静默保持未登录。上手先检查它。
- user: CI/CD 运维老哥, category: 坑, comment: 在流水线里跑 npx @convex-dev/auth 向导,直接卡到任务超时——它要等终端交互登录。改用 jose 无头生成密钥再写环境变量,几秒跑完,再没挂过。
- user: 后端老兵, category: 妙用, comment: 多行私钥直接 env set JWT_PRIVATE_KEY "$KEY",CLI 把开头的 ----- 当成未知参数报错。换成 NAME=VALUE 形式一次成功,这个细节省我半小时。
- user: pnpm 前端工程师, category: 注意, comment: pnpm 不提升依赖,装完还得单独 pnpm add jose,否则报找不到 jose。用 shadcn 的话 button/input 要先 npx shadcn add,少一个就是硬编译报错。
- user: 周末做 side project 的独立开发者, category: 妙用, comment: 默认走 passkey,用户不用记密码,我也省掉整个找回密码页,独立开发太省事了。记得 SITE_URL 设成 http://localhost:3000,不然登录回调对不上。
- user: 技术小团队 leader, category: 启发, comment: 我以前觉得代码没报错就算完成。这个技能最后要求真实登录走通一遍才算完——auth 坏了往往不报错,必须跑通闭环。这条我已写进团队验收清单。
