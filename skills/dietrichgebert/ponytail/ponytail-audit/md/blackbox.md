# ponytail-audit (`dietrichgebert/ponytail/ponytail-audit`)

## blackbox

**function**: 扫描你的整个代码仓库, 找出所有可以删掉、简化或直接用现成功能替代的"多余工程", 输出一份按节省量从大到小排序的瘦身清单——只给报告, 不动手改代码。

- input: 一个代码仓库的路径 + 「audit this codebase」(审计这个代码库), output: 一份瘦身审计报告: 每行一条发现, 标明该删什么、用什么替代, 按可砍掉量从大到小排列, 末尾汇总「总共可省约 -X 行代码、-Y 个依赖」
- input: 一个装了一堆第三方库的项目, 说「find bloat」(找出赘肉), output: 清单指出哪些库其实和系统自带的功能重复, 并写出可直接替换的具体名称——例如「这个依赖可删, 系统自带的 X 就能干同样的活」
- input: 一个已经写得很精简的代码库, output: 只回一句:「Lean already. Ship.」(够精简了, 直接发布), 不会硬找东西砍
