# wind-mcp-skill (`wind-information-co-ltd/wind-skills/wind-mcp-skill`)

## comments

- user: 量化研究员, category: 妙用, comment: 价格指标工具的 windcode 支持逗号分隔、单次最多 50 个，百来只股票拆两批就完，别傻傻一只只调。
- user: 第一次用的新手, category: 坑, comment: 我把批量行情全塞给 analytics_data，结果它只返回聚合计算、不给标的列表，还更耗积分；行情老老实实走各领域专项工具。
- user: 券商营业部客户经理, category: 注意, comment: 返回数值的单位以自带元数据为准，千万别自己换算；元数据没标就注明单位未知，我按元/港币瞎换算坑过自己。
- user: 财经内容编辑, category: 坑, comment: 要年报原文别走股票工具，那只会给财务数据；公告、年报得走 financial_docs 的公告接口才拿得到。
- user: 独立开发者, category: 妙用, comment: 批量查多个标的先发一只当探针，探针返回错误就整批停手，既不吃限流也不白烧额度，我是踩过限流才学会的。
- user: 私募投研老手, category: 注意, comment: 要的指标字段一多，单批代码数就得往下减——响应体积随代码数×字段数增长，塞满 50 个容易拉不动。
