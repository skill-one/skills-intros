# insforge-cli (`insforge/insforge-skills/insforge-cli`)

## comments

- user: 后端老兵, category: 妙用, comment: CI 脚本里全靠退出码分支:2=没登录、3=没关联项目。配合 --json 拿结构化输出,脚本自动判断该重跑 login 还是 link,不用人盯着。
- user: 运维老哥, category: 坑, comment: 跑 npx @insforge/cli 卡在「Ok to proceed?」不动,我还查了半天网络。其实是少了个 -y,要写 npx -y @insforge/cli,不然在脚本里会永远挂着。
- user: 第一次用的新手, category: 坑, comment: 我先照模板把应用全写完,连的是占位符地址,联调全报错推倒重来。正确顺序:先 login、create 拿到真实 URL 和密钥,再动手写代码。
- user: 独立开发者, category: 启发, comment: 以前遇到平台的问题就跟它死磕一下午。现在先 feedback 把问题报上去,换个变通办法继续干,当天能交付,平台那边还有回应。
- user: 前端转全栈, category: 注意, comment: 差点把 admin key 放进前端环境变量——这是全权管理员钥匙,泄露等于整库裸奔。只能放服务端,谁能看哪些数据交给 RLS 行级策略管。
- user: 沙箱里跑 AI 编程的工程师, category: 注意, comment: 沙箱里浏览器打不开回调,login 会干等。用 --device --json 拿验证链接和码发给用户,他点完授权再跑一次同命令,会接着原来的码继续。
