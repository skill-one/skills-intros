# ponytail-debt (`dietrichgebert/ponytail/ponytail-debt`)

## blackbox

**function**: 扫描你的代码仓库, 把所有标记了「ponytail:」的欠账注释汇总成一份技术债清单, 标明每一处凑合方案的上限和何时该回头升级, 全程只读不改代码。

- input: 一个代码仓库目录, output: 一份按文件分组的欠账清单, 每条包含: 所在文件和行号、当时简化了什么、这个凑合方案的极限在哪、什么情况该回头重做; 缺少升级触发条件的条目会被标上 no-tag 腐烂风险; 结尾附统计「共 N 条, M 条无触发条件」
- input: 代码仓库 + 「每条顺便写上是谁留下的」, output: 同样的清单, 每条多一个责任人名字
- input: 代码仓库 + 「把这份清单存成文件」, output: 在仓库里生成一个 PONYTAIL-DEBT.md 欠账台账文件
- input: 一个没有任何 ponytail: 标记的干净仓库, output: 一句回话: No ponytail: debt. Clean ledger. (没有欠账, 台账干净)
