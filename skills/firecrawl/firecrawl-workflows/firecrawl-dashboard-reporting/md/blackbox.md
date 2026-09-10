# firecrawl-dashboard-reporting (`firecrawl/firecrawl-workflows/firecrawl-dashboard-reporting`)

## blackbox

**function**: 把你有权访问的后台数据看板 (如 Google Analytics、公司内部运营面板) 上的数字抓取出来, 整理成一份结构化的数据报告。

- input: 两个数据看板的网址 + "拉取上周的 DAU、新用户数、付款转化率", output: 一份仪表盘报告: 每个指标的数值、涨跌变化、统计时间段, 以及数据来自哪个页面
- input: 一个需要登录的公司内部后台网址, output: 会先提示你重新登录; 你登录后, 报告里就能带上该后台的指标卡片和表格数据
- input: "整理成 JSON 给我, 指标只看收入相关", output: 一个 JSON 文件: 含报告时间、日期范围、逐条收入指标和摘要, 可直接喂给其他程序
