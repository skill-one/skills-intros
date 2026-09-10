# caveman-stats (`juliusbrussee/caveman/caveman-stats`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我先让模型"帮我查用量", 白白多烧一轮; 其实直接敲 /caveman-stats 就行, 数字由钩子秒回, 不占对话。
- user: 后端老兵, category: 妙用, comment: 长重构中途跑一次, 看到 Net 为负它直说并建议关掉 caveman——照做即可, 这行比"省了多少"的毛数诚实得多。
- user: 运维老哥, category: 注意, comment: 规则开销默认按 1250 tokens/轮估算, 和你的环境不符就设 CAVEMAN_RULE_OVERHEAD_TOKENS 改掉, 否则 Net 全偏。
- user: 精打细算的独立开发者, category: 注意, comment: 数字只读当前会话日志, 新开会话就归零; 想对比就在同类任务、同一进度点各跑一次, 别拿不同任务互比。
- user: 长会话写作者, category: 坑, comment: 会话才开三四轮就跑, 估算抖得没法看; 攒到十几轮再看才稳, 前期那个 Net 别当真。
- user: 管账的产品经理, category: 启发, comment: 它让我明白"省了多少"是毛数, 扣掉每轮固定规则开销才知道真省假省; 现在我只认 Net 那行再决定开关。
