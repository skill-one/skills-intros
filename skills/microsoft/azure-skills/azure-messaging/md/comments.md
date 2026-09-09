# azure-messaging (`microsoft/azure-skills/azure-messaging`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我只说"收不到消息"，它反过来问 SDK 和版本，白跑一轮。后来把报错原文加 SDK 版本一起贴，一步定位到连接串写错。
- user: 运维老哥, category: 注意, comment: 先别急着怀疑自己代码。它第一步会查命名空间健康状态，我有次折腾半天，其实是 Azure 侧故障，先查能省几小时。
- user: Java 后端, category: 妙用, comment: 批量处理太久把消息锁耗丢了，它不只给原因，还给了分批续锁的做法和官方文档链接，照改就好，不用自己翻半天文档。
- user: 数据管道工程师, category: 坑, comment: 下游全是重复事件，我以为是代码 bug。实际是两个服务共用默认消费者组，检查点互踩、offset 反复重置。分组建组后消失。
- user: 后端老兵, category: 启发, comment: 它的排查顺序值得抄：先查资源健康，再按报错对语言指南，最后才查配置。我以前上来就调重试参数，方向常是错的。
- user: Python 自学者, category: 注意, comment: 它本身不带各语言排错手册，那在 azure-diagnostics 技能里。直接说"eventhub python"，它会把对应指南翻出来用。
