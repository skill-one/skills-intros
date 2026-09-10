# sandbox-stable (`cloudflare/skills/sandbox-stable`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我图新鲜把依赖装成 @next 预览版, 容器镜像还留在稳定版, 一启动就报接口不存在. 记住: 依赖和镜像必须同一条版本线, 半新半旧必炸.
- user: 做 AI 代码助手的全栈, category: 妙用, comment: 开了默认会话后, python 会话记住工作目录和装过的依赖, 用户连着追问不用每次重装环境, 多轮执行明显顺滑, 建议第一步就开.
- user: 后端老兵, category: 注意, comment: exec 是等命令跑完才一次性吐 stdout, 我拿它跑长任务硬等到超时. 长任务换 startProcess, 流式收日志用 execStream, 传大文件走 RPC.
- user: 存量项目维护者, category: 坑, comment: 在稳定包上照 1.0 预览文档抄 process.output(), 类型检查全红. 要么留稳定按 2026 弃用指南清理旧 API, 要么彻底迁 @next, 半套混用最惨.
- user: 兼管安全的技术负责人, category: 注意, comment: 真实密钥别塞沙箱环境变量, 那里只放非密配置; 密钥留 Worker, 进程外呼走 outbound handlers. 我 review 时从里面捞出过同事漏的 key.
- user: 运维老哥, category: 注意, comment: 用预览 URL 上生产, 要提前在自定义域名配好泛解析(如 *.preview.example.com), 我上线当天用户打不开预览链接才补课, 白背一口锅.
