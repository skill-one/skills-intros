# verify-and-stop (`juliusbrussee/caveman/verify-and-stop`)

## comments

- user: 刚接手老项目的开发, category: 坑, comment: 我以为是修 bug 的,结果它只验证不修。想让它顺手改代码,请求里必须明确写上"包含修复",否则验完就停。
- user: 测试工程师, category: 妙用, comment: 代码没变时让它先核对仓库状态,没变就直接复用上次的验证结果,回归验证不用每次从头重跑,省一大半时间。
- user: 项目主管, category: 注意, comment: 报告要求它严格分四种状态:通过、失败、环境不可用、被阻塞。以前混着写"没过",别人总追问是没跑还是跑挂。
- user: 后端老兵, category: 妙用, comment: 只改一行配置,它先跑对应模块的小检查,过了才触发完整门禁,不像以前全量跑十分钟才发现第一步就挂了。
- user: 第一次用的新手, category: 注意, comment: 验收条件一过它立刻收工,想顺手清理警告、补测试?不带。要加活就另开任务,别指望收尾时捎带。
- user: 独立开发者, category: 启发, comment: 它让我把"验证"和"修"彻底分开:验收标准先写死,报告只留命令、结果、遗留风险三样,交付反而更有说服力。
