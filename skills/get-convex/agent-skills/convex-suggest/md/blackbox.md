# convex-suggest (`get-convex/agent-skills/convex-suggest`)

## blackbox

**function**: 你用 Convex (一个后端云开发平台) 写代码时, 如果你在手工造某个现成组件就能解决的"轮子" (如定时任务、点赞计数、接口限流), 我会先帮你把手头的事做完, 然后指出"该用哪个现成组件、为什么、怎么装"; 你不点头, 我绝不擅自安装。

- input: 一段 Convex 代码, 用 setInterval 每小时清理过期数据, output: 一条建议: 「你这段定时清理, 用现成的 @convex-dev/crons 组件更稳」, 说明理由并附安装方式; 你说"装"它才动手装
- input: 一段点赞代码, 每次执行 post.likes + 1, output: 一条建议: 点出高并发时这种写法会互相打架, 换 @convex-dev/sharded-counter 更合适, 附安装命令, 等你确认
- input: "帮我写个排序函数" 这类与 Convex 无关的普通编程问题, output: 正常完成任务, 不推销任何组件
- input: "不用了, 我自己写的够用", output: 不再重复提这个建议, 继续帮你干别的活
