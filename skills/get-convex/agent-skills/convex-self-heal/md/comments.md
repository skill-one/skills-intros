# convex-self-heal (`get-convex/agent-skills/convex-self-heal`)

## comments

- user: 后端老兵, category: 妙用, comment: 半夜报错暴涨没吵我: 一次性网络抖动被它归为 transient 直接重试, 没开垃圾 PR。以前用其他监控工具这点真做不到。
- user: 第一次用的新手, category: 坑, comment: 上来就说'帮我修线上报错', 它直接停下提醒我没装 sentinel。教训: 先装好错误捕获再启动循环, 否则一步都走不动。
- user: 运维老哥, category: 注意, comment: 部署后验证别看 insights 面板, 它只收性能事件; 要去 sentinel 表和 logs 里确认错误签名不再出现。我一开始就盯错了地方。
- user: 独立开发者, category: 妙用, comment: 它开的 PR 自带证据: 类型检查结果、真实数据预演、报错输入修前能复现修后消失。我照着证据评审就敢合, 不用自己搭环境跑。
- user: 创业团队 CTO, category: 注意, comment: 启动前先划授权范围: 默认只自动备校验器、加索引、补归属检查这类安全修复, 其余全留给人; 它从不自动合并, 键一直在人手里。
- user: 前端转全栈, category: 启发, comment: 根因没查清它宁可停也不硬修——说错的修复比挂着的报错更糟。治好了我'先改了再说'的毛病。
