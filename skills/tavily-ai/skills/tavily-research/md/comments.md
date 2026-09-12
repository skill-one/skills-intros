# tavily-research (`tavily-ai/skills/tavily-research`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我拿"X公司CEO是谁"这种一句话能答的问题跑 research, 白等了一分钟。后来看说明才懂: 快速查证用 tvly search 几秒就回, research 是留给多来源综合分析的。
- user: 无头服务器运维, category: 坑, comment: 在无浏览器的服务器上我加 --no-browser, 以为能跳过登录, 结果它只是打印链接、仍在等本地回调, 卡到超时。无人值守环境直接配 TAVILY_API_KEY 才通。
- user: 赶论文的研究生, category: 妙用, comment: 写文献综述时加了 --citation-format apa, 报告里的引用直接就是 APA 格式, 省掉我手动整理参考文献的半天, 换 mla 也一行参数的事。
- user: 急性子产品经理, category: 注意, comment: 第一次跑到 40 秒我以为卡死, Ctrl+C 杀了, 其实 30-120 秒是正常耗时, 白跑一趟。加 --stream 能实时看到进展, 心里有底不瞎等。
- user: 写行业周报的分析师, category: 妙用, comment: 用 --output-schema 传入自定义 JSON 结构, 出来的报告直接是我要的字段格式, 贴进周报和表格里不用再手动拆解重组。
- user: 兼职接单的自由职业者, category: 妙用, comment: 接竞品调研的活, 我用 --no-wait 一口气发起 3 个题目拿到 request_id, 去干别的, 完事逐个 poll 取报告, 几个任务并行, 不串行干等。
