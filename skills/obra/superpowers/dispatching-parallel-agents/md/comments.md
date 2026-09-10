# dispatching-parallel-agents (`obra/superpowers/dispatching-parallel-agents`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我一条消息只派了一个 agent,结果它们排队跑,等了三倍时间。多条任务必须塞进同一条消息里一起发,才是真并行。
- user: 后端老兵, category: 妙用, comment: 把报错原文和失败的测试名整段贴进每个 agent 的提示里,再加一句「别动生产代码」,返回的修复基本一次过。
- user: QA 测试工程师, category: 坑, comment: 我把两个互相牵连的 bug 拆给两个 agent,一个改完,另一个的假设全塌了。相关故障先一起查,确认独立再拆。
- user: 全栈独立开发, category: 妙用, comment: 不止修测试:我同时派三个 agent 分别调研候选库、读文档,互不干扰,一上午就拿到三份对比结论。
- user: 创业公司技术负责人, category: 启发, comment: 为了写清每个 agent 的任务,我被迫先自己划清问题边界。这套「拆域、定目标、给约束」后来直接被我拿来给人分工。
- user: 运维老哥, category: 注意, comment: 别全信 agent 汇报的「全绿」,它可能系统性误判。交回来我自己重跑全套测试、抽查改动,真抓到过一次假修复。
