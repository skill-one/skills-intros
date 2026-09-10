# code-review-and-quality (`addyosmani/agent-skills/code-review-and-quality`)

## comments

- user: 创业公司 Tech Lead, category: 妙用, comment: 按「先查测试, 再看实现」的顺序让它过一遍, 真的抓出了只测正常路径的测试。合并前跑一次, 比上线后救火省心多了。
- user: 第一次用的新手, category: 坑, comment: 我把 AI 一口气生成的八百行整坨丢给它审, 结论很浅。后来拆成百行级小改动分别审, 问题立刻藏不住了。
- user: 后端老兵, category: 注意, comment: 它的放行标准是「确实变好就通过」, 不追求完美。别指望它纠结风格细节, 那类意见会标成 Nit, 改不改你定。
- user: 被 review 吵怕过的前端, category: 妙用, comment: 强制每条意见带 Critical/Nit 标签后, 没人再把建议当强制要求吵了。几条高把握意见, 胜过一长串琐碎清单。
- user: 运维老哥, category: 坑, comment: 我图省事一把梭把依赖全升了, 构建挂了却查不出哪个包干的。改成一次只升一个、单独合并, 出事回滚也干净。
- user: 单兵作战的全栈, category: 启发, comment: 「复杂度被搬家不等于被减少」点醒了我: 重构后读者要装的概念没变少, 就是假重构。现在我先数概念再动手。
