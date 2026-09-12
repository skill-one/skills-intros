# planning-with-files-zh (`othmanadi/planning-with-files/planning-with-files-zh`)

## comments

- user: 后端老兵, category: 妙用, comment: 我把报错表当调试知识库用：错误、尝试次数、解法三列照实记。三个月后同款超时问题，翻表 30 秒就定位到当时加的重试逻辑。
- user: 第一次用的新手, category: 坑, comment: 我原以为它能记住我们上次聊的内容，重启后发现它只会读三个规划文件。想查历史得自己显式跑 session-catchup.py --metadata。
- user: 天天查文献的研究生, category: 妙用, comment: 查文献我严格执行"查两轮就存一次"，网页要点只进 findings.md。上下文被压缩后结论全在，换台电脑接着干也不丢线索。
- user: 运维老哥, category: 注意, comment: 并行跑两个任务前先固定各自的 PLAN_ID，在子进程里 export 没用，改不了宿主环境。我踩过两个会话写同一个计划互相覆盖。
- user: 独立开发者, category: 启发, comment: 用了一周才意识到这些纪律对我也适用：现在自己修 bug 也先记错误表，第二次绝不重复同一个失败操作，省了不少瞎试的时间。
- user: 带外包团队的技术主管, category: 注意, comment: 两个代理协作别让它们都改共享计划，必然打架。我的规矩：一个负责人写 task_plan.md，工作者只在分到的账本文件里汇报。
