# security-and-hardening (`addyosmani/agent-skills/security-and-hardening`)

## comments

- user: 后端老兵, category: 妙用, comment: audit 报 critical 它不急着升级版本，先确认漏洞函数是否真被调用。没在运行路径上就不阻塞发版，只登记个复查日期，省了一次破坏性强更。
- user: 第一次做登录的新手, category: 注意, comment: 别指望它直接甩你一段登录代码——涉及鉴权、CORS、文件上传它会先停下来问你方案。提前想好「密码怎么存」再来，一次过。
- user: 运维老哥, category: 坑, comment: 限流单机测试全过，上 3 台负载均衡后阈值变 3 倍，登录爆破根本拦不住。多实例部署一定提前说，它才给 Redis 共享计数版本。
- user: 做 AI 功能的全栈, category: 妙用, comment: 给 RAG 摘要功能做加固，它把模型输出当不可信输入对待，拦下了「摘要结果直接拼进 shell 命令」的写法，要求先校验再执行。
- user: 接私活的独立开发, category: 注意, comment: API key 误提交后我删了代码就当没事，它坚持先去平台吊销重发、再清理历史——key 一进远端就按已泄露处理，别存侥幸。
- user: 被 GDPR 删除请求坑过的后端, category: 启发, comment: 它让我加字段前先问「要不要留、留多久」。现在每张表都有保留期限和真正的删除路径，删除请求不再靠翻备份碰运气。
