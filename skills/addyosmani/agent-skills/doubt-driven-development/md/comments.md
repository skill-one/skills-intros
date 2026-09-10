# doubt-driven-development (`addyosmani/agent-skills/doubt-driven-development`)

## comments

- user: 后端老兵, category: 坑, comment: 我一开始把自己的结论也贴给审查者"帮它理解"，结果它每轮都在附和我。改成只给代码和约束，它才挑出缓存淘汰的竞态。
- user: 第一次用的新手, category: 坑, comment: 我把改个变量名也开一轮审查，半天没产出。教训：只在分支逻辑、跨模块、"这很安全"这类拿不准的决策上用。
- user: 架构师, category: 妙用, comment: 方案阶段就用：三句话设计丢给新审查，它质疑我对消息消费顺序的假设。改设计一张纸，改代码得一个迭代。
- user: 运维老哥, category: 坑, comment: 迁移脚本带反引号和$()，内联传给 CLI 被截断还差点执行了里面的命令。现在写临时文件走管道，只读沙箱跑。
- user: 独立开发者, category: 妙用, comment: 同模型自审两轮都说没问题，换个模型几分钟就指出重试逻辑破坏幂等。同源盲区真存在，这步别省。
- user: 数据工程师, category: 启发, comment: 受它影响，做设计前先逼自己两行写清决策。写不出来就说明只有感觉没有决定——这个习惯比审查本身更值。
