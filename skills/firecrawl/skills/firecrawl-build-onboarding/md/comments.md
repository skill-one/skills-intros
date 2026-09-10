# firecrawl-build-onboarding (`firecrawl/skills/firecrawl-build-onboarding`)

## comments

- user: 第一次接 API 的实习生, category: 坑, comment: 我在 SSH 远程服务器上跑 init --all --browser,浏览器根本弹不出来没法登录。后来在本地跑完拿到 key,再把 .env 拷到服务器才通。
- user: 自建服务运维老哥, category: 注意, comment: 我们是自建部署,只配了 API key,结果请求全打到官方云上去了。自托管必须同时写 FIRECRAWL_API_URL,不然默认连 hosted API。
- user: 全栈独立开发者, category: 妙用, comment: 本想只配个 key,init 一条命令把 CLI 也装上了。写代码前先在终端用 CLI 把要抓的 URL 试一遍,确认返回格式没问题再搬进代码,调试省一半时间。
- user: 后端老兵, category: 注意, comment: 往老项目里接别急着新建 .env,先看仓库里环境变量怎么管的,跟着既有约定放 key,不然 CI 上读不到,本地能跑线上挂。
- user: 前端转全栈, category: 启发, comment: 它把我接第三方服务的流程固化了:配 key → 选最窄的接口 → 先跑真实冒烟测试再写业务代码。以前总写完一堆代码才发现 key 没配对。
- user: 手上有 key 的懒人, category: 妙用, comment: 手上已有 key 就别重跑 auth 流程,直接把 FIRECRAWL_API_KEY=fc-... 写进 .env 就能用。我当时傻乎乎重跑了一遍登录,其实指南开头就写了这条捷径。
