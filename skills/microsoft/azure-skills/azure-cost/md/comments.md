# azure-cost (`microsoft/azure-skills/azure-cost`)

## comments

- user: 第一次接手 Azure 的新手, category: 坑, comment: 直接让它查就报权限错。得先找管理员分配 Cost Management Reader、Monitoring Reader、Reader 三个角色,缺一个都查不了。先确认角色再开工。
- user: 运维老哥, category: 妙用, comment: 按资源组范围查费用很省事。我们一个项目一个资源组,直接对着资源组查,各项目花多少一目了然,不用再导 Excel 手工分摊。
- user: 创业公司 CTO, category: 妙用, comment: 月初就用 forecast 预估本月账单,看着要超预算就提前砍掉测试环境,比月底拿到账单再补救主动太多。
- user: 管财务对账的同事, category: 注意, comment: 查询范围选错,结果差很多:订阅级只看该订阅的账,要看全公司得用管理组或计费账户级别。我先按订阅查,漏了一大块费用。
- user: 后端老兵, category: 注意, comment: 它只管钱。我拿它排查 VM 卡顿,方向就错了——明确不做诊断、部署、安全审计。性能问题请走别的工具。
- user: 云成本负责人, category: 启发, comment: 以前以为省钱得动架构,跑完才发现大头是没人管的闲置资源。先清孤儿资源(未挂载磁盘、闲置公网 IP),再谈优化,顺序别反。
