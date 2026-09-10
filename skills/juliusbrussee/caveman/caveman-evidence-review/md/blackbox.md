# caveman-evidence-review (`juliusbrussee/caveman/caveman-evidence-review`)

## blackbox

**function**: 查你的 Caveman Cloud 数据,出一份「钱花哪了、省了多少、哪个任务在烧钱」的证据报告——只看不动,不改任何东西。

- input: 「我们上个月的大模型调用费都花在哪了?」, output: 一份成本拆解报告:按模型、按任务(workflow)的费用排名,每条结论附上具体的调用记录编号(trace id)和时间区间,可追溯到原始记录。
- input: 「Caveman 到底帮我们省了多少钱?这个数可信吗?」, output: 一份总览报告:把三个数字分开列清——实测支出、已验证的节省(有账本记录)、估算的剩余省钱空间,不混着报,并注明数据统计的时间窗口。
- input: 「这个 workflow 为什么最近又贵又老报错?」, output: 一份对比分析:把出问题的调用记录和正常时期的同类记录放在一起比(模型选择、重试次数、缓存命中、耗时),指出差异所在,并明确标出哪些结论有证据、哪些只是猜测。
