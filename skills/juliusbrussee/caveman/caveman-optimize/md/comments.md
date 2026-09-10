# caveman-optimize (`juliusbrussee/caveman/caveman-optimize`)

## comments

- user: 前端第一次接优化, category: 坑, comment: 我偷懒想直接拿 .caveman/proposals 里的旧提案选条目，结果那只是历史存档不作数。必须登录后跑 caveman opportunities list 取最新报告。
- user: 第一次用的新手, category: 注意, comment: CLI 没登录或报告里没有 report_only_observations，它就整体停住，不会退回网关或项目密钥入口。开跑前先确认 caveman 登录态。
- user: SRE 老哥, category: 妙用, comment: 它不替你排序，逼我逐条读原文再自己选。照报告去仓库找具体调用点，才发现真凶是工具输出过大，省掉一轮盲改。
- user: 平台组运维, category: 坑, comment: 老文档里的 context-window-bloat、tool-catalog-utilization、verbose-tool-output 已废弃，别按旧标题排优先级；遇到 unlabeled-traffic 应转交 caveman-discover。
- user: 后端老兵, category: 注意, comment: 先备好固定测试数据和统一的质量检查再谈候选改法，缺一样它直接停。单测通过不等于优化成立，基线和候选必须同输入对比。
- user: 技术负责人, category: 启发, comment: 报告模板里 $0 那行点醒我：以前把省的 token 换算成钱往上汇报，没同口径计费其实是脑补。现在只报实测的字节和调用数。
