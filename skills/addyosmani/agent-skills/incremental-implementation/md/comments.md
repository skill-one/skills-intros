# incremental-implementation (`addyosmani/agent-skills/incremental-implementation`)

## comments

- user: 刚回滚过一整天的后端新人, category: 坑, comment: 我一口气写完才测,第一片埋的 bug 让后面几片全错,500 行 diff 查不出祸根。现在每片写完立刻跑测试,错了当场修,就几行的事。
- user: 带 AI 干活的前端, category: 妙用, comment: 我拿这套指挥 AI:每片只让它做一件事,明说「UI 下一片再碰」,写完立刻跑测试和构建。以前它一口气吐 500 行,错哪根本查不动。
- user: 后端老兵, category: 坑, comment: 我把顺手清理旧代码混进功能提交,review 的人分不清哪行是改动哪行是清理,整单打回重做。现在 scope 外的问题只记任务,绝不顺手改。
- user: 一人全栈的独立开发者, category: 注意, comment: 单文件小改动别套这套,我给 20 行的函数也切片加测试,流程比改动本身还重。指南明说:范围已经最小就别用。
- user: 养过两周长分支的移动端, category: 妙用, comment: feature flag(功能开关)让我每片都敢合 main:开关挡住半成品,不再养开两周的长分支,合并地狱没了;出事关掉 flag 就是回滚。
- user: 带过烂抽象的技术负责人, category: 启发, comment: 「三行重复好过一个早熟的抽象」点醒我:以前两处相似我就抽公共层,改一处三处崩。现在先写三份直白的,第三处用到再抽,反而快。
