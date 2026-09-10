# convex-test (`get-convex/agent-skills/convex-test`)

## comments

- user: 踩过库的全栈新手, category: 坑, comment: 我以为要连自己的 dev 环境才能跑，结果测试数据写进了真实库。后来才懂 convexTest(schema) 自带内存后端，不用配任何连接。
- user: 十年后端老兵, category: 妙用, comment: withIdentity 能直接伪造用户身份，一条测试同时验证「本人能删、别人不能删」，不用真的登两个号来回切。
- user: 独立开发者, category: 妙用, comment: 改定时任务最怕上线才发现问题。现在测试里排好任务，调 finishInProgressScheduledFunctions 把它跑完再断言，心里有底。
- user: 前端转全栈, category: 坑, comment: clone 来的测试直接跑报找不到模块——先 npm i -D convex-test vitest，再按模板建好 vitest 配置文件就通了。
- user: 测试工程师, category: 注意, comment: 测试里用了真实时间和外部请求，偶尔莫名失败。换 fake timers 并 mock 掉外部调用后，才稳定到秒级跑完。
- user: 维护老项目的人, category: 启发, comment: 我只写了正常流程，未登录、参数非法这些分支还靠手测。补上 error path 断言后，重构才敢放心。
