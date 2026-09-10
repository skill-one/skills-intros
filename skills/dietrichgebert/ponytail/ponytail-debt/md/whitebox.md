# ponytail-debt (`dietrichgebert/ponytail/ponytail-debt`)

## whitebox

- 扫描: 用 grep -rnE '(#|//) ?ponytail:' 全仓搜索标记, 跳过 node_modules、.git、构建产物
- 解析: 按 'ponytail: <上限>, <升级触发条件>' 约定, 从每条注释里抽出上限和触发条件, 一条命中 = 一行台账
- 补强(可选): 对每行跑 git blame -L<line>,<line> 追加责任人
- 风控: 注释里没写升级路径或触发条件的, 打上 no-trigger 标签——这类最容易烂掉
- 输出: 按文件分组报告 '<file>:<line>, 简化了什么. ceiling: 上限. upgrade: 触发条件.', 末尾统计 '<N> markers, <M> with no trigger.'; 一次性的, 不改任何代码

- 注释前缀门控: 必须命中 '# ponytail:' 或 '// ponytail:' 这类注释格式才算数, 单纯在文字里提到这个约定不会被误收进台账
- 结构化解析而非语义理解: 依赖固定书写约定 'ponytail: <ceiling>, <upgrade path>' 直接切出两个字段, 缺触发条件即标 no-trigger
- 只读不动: 全程只扫描和报告; 要落盘 (如写入 PONYTAIL-DEBT.md) 需用户明确要求; 说 'stop ponytail-debt' 即退出
- 外部依赖极简: 仅 grep 和 git (blame), 无库、无模型 API
