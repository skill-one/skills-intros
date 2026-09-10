# deprecation-and-migration (`addyosmani/agent-skills/deprecation-and-migration`)

## comments

- user: 后端老兵, category: 坑, comment: 同一次发版里改列名又上新代码, 灰度期新旧共存, 旧代码查不到列, 报错且回滚救不回数据. 现在五步走: 加新列→双写→回填→切读→最后单独发版才 drop.
- user: 运维老哥, category: 坑, comment: 回填一条 UPDATE 跑全表→直接锁表→支付回调积压半小时. 现在分批五千行加节流, 建大索引用 CONCURRENTLY 不阻塞写, 热表迁移线上无感.
- user: 接手祖传项目的新手, category: 妙用, comment: 拿四个信号给交接模块做体检: 半年没提交却有人调用、没负责人、测试红着没人修、文档指向不存在的系统. 体检完只剩两条路: 派人接手或排期迁移, 不再悬着.
- user: 带团队的技术负责人, category: 启发, comment: 以前发完弃用公告就完事, 半年没人迁还怪用户. 明白"谁弃用谁负责迁移"后重做: 配迁移指南加校验脚本, 逐个消费方迁, 迁移率从一成拉到全量.
- user: 独立开发者, category: 注意, comment: 给老接口定过硬下线日期, 却没给迁移工具, 到期用户炸锅被迫延期. 现在默认公告式弃用让用户自选节奏, 只有安全问题才设硬期限, 且必配脚本和文档.
- user: 维护开放API的全栈, category: 妙用, comment: 旧接口签名不动, 用 adapter 转发到新实现, 再按 feature flag 逐个用户切流. 出问题只关 flag 秒回退, 不用整次回滚发版, 下游 20 个调用方零感知.
