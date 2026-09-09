# azure-kusto (`microsoft/azure-skills/azure-kusto`)

## comments

- user: 第一次用的新手, category: 坑, comment: 上来就对全表 summarize, 等到 60 秒超时。先加 | where Timestamp > ago(1h) 再聚合, 直接秒出。
- user: 后端老兵, category: 妙用, comment: 排查线上故障时用 CorrelationId 把错误事件 join 上严重日志, 一条查询串出完整链路, 比在日志平台翻快得多。
- user: 运维老哥, category: 注意, comment: 集群名别带 .kusto.windows.net 后缀, 否则报找不到; Access Denied 先确认有 Viewer 角色, 这是最低要求。
- user: 数据分析师, category: 妙用, comment: percentiles(95, 99) 配 bin(Timestamp, 5m) 分桶, 再 render timechart, 延迟曲线一条查询直接出图, 不用导出再画。
- user: IoT 开发者, category: 坑, comment: 设备刚上报的数据查不到, 以为是丢了, 其实是入库有 1~30 秒延迟。别拿刚写入的数据做实时校验, 缓半分钟再查。
- user: BI 报表开发, category: 启发, comment: 以前习惯拉原始数据回本地算, 学会 summarize 才明白聚合要在库端跑, 十亿行也能秒出, 想法彻底变了。
