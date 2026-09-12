# backtesting-frameworks (`wshobson/agents/backtesting-frameworks`)

## comments

- user: 第一次写回测的量化新手, category: 坑, comment: 全历史数据调参, 回测年化 30%, 实盘亏 15%。后来切成训练/验证/测试三段, 测试集只跑一次, 才看到真实水平。
- user: 私募量化研究员, category: 妙用, comment: 没用一次性 train/test, 改成滚动窗口 walk-forward 每年重训重测, 贴近实盘定期调参的节奏, 策略衰减能提前几个月暴露。
- user: 数据工程师, category: 注意, comment: 用后复权价格直接回测等于偷看未来 (未来的分红都被算进去了), 必须换成 point-in-time 数据——当时实际能看到的价。
- user: 炒股十五年的老股民, category: 坑, comment: 只拿现存股票回测, 退市股全被漏掉, 收益虚高。补齐退市证券数据后, 年化从 18% 掉到 9%, 吓出一身汗。
- user: 期货交易老手, category: 注意, comment: 回测必加交易成本。我设了双边手续费加 0.1% 滑点, 日内高频策略直接由赚转亏, 早知道能省三个月。
- user: 业余写策略的程序员, category: 启发, comment: 现在动手前先写死参数范围和评估标准。以前测 50 个策略挑最好的那个, 这个「挑」的动作本身就是偏差。
