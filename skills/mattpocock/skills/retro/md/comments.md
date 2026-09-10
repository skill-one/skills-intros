# retro (`mattpocock/skills/retro`)

## comments

- user: 前端独立开发, category: 启发, comment: 我原来把所有代码规范塞进 AGENTS.md,让 agent 干活时每次都读。复盘后才明白规范该交给审查阶段执行,搬走后干活阶段的上下文明显轻了。
- user: 第一次用的新手, category: 注意, comment: 以为是复盘项目进度那种 retro,其实它只管「怎么让 AI 下次干得更好」,不动代码。会话很顺利没踩坑时,结论会很空——专挑翻车的那次用。
- user: 后端老兵, category: 妙用, comment: 把昨天翻车那次会话指给它,它发现 agent 找一个隐藏依赖翻了半小时,最后只在 AGENTS.md 加了一行导航指针,下次一找就中。
- user: 运维老哥, category: 坑, comment: 没指定会话,它默认复盘当前这个刚开头的会话,建议全是套话。错误做法:上来就喊 retro → 后果:白跑一轮。先说清要复盘哪个会话。
- user: 创业团队 tech lead, category: 妙用, comment: 它专挑「从不改变行为的指令」开刀,把全局 AGENTS.md 里近一半没用的话删了。这文件每次运行都进上下文,省的是每一次的开销。
- user: 自由职业全栈, category: 注意, comment: 它建议加的 lint、类型检查这类自动检查,要自己动手装好配置才生效;而且所有改进只作用于以后的会话,当前这堆报错还得让它先修。
