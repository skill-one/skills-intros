# implement-spec (`mattpocock/skills/implement-spec`)

## comments

- user: 第一次用的新手, category: 坑, comment: 直接丢一份需求文档进去它不动手——这技能默认 spec 已拆成带阻塞关系的 tickets。先把任务图写好再跑, 一次就通。
- user: 后端老兵, category: 妙用, comment: 发现 tickets 文件是个活队列: 跑到一半我改了某票的依赖标注, 空闲的实现者马上去抢刚解锁的活, 等于随时能调优先级。
- user: 带团队的技术负责人, category: 注意, comment: 所有票最后合进同一个 draft PR, 不是一票一 PR; 结尾会自动跑 /code-review, 你环境里没装这个命令会卡在最后一步。
- user: 运维老哥, category: 坑, comment: 中途手动 kill 过一次, 留下一堆残留 worktree 和实现分支。正常跑完它会自动清理, 别中途砍; 真中断了就 git worktree list 查完逐个删。
- user: 独立接活的自由开发者, category: 坑, comment: 两张票都改同一个文件但我没标阻塞, 并行实现后合并直接撞冲突, 多返工一小时。阻塞关系宁多标不漏标, 真会撞车。
- user: 架构师, category: 启发, comment: 子代理之间靠指针指到 spec 和笔记、从不复制内容——我把这习惯带回团队: 让人自己去查文档, 口头转述的口径漂移少多了。
