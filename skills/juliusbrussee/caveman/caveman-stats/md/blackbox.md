# caveman-stats (`juliusbrussee/caveman/caveman-stats`)

## blackbox

**function**: 输入一条 /caveman-stats 命令，立刻看到本次会话的真实用量账单：实际消耗了多少 token、精简模式帮你省了多少、扣掉模式本身的开销后净赚还是净亏。📊

- input: 会话进行中，敲一条命令：/caveman-stats, output: 一段即时的数字统计：本次会话实际 token 用量、估算节省量、规则开销、净节省，一目了然
- input: 在已经聊了很多轮的长会话里输入 /caveman-stats, output: 按轮数累计的节省估算，并附上净收益（总节省减去每轮固定开销）
- input: 在净收益为负的任务场景下输入 /caveman-stats, output: 直白标明「净收益为负」，并建议这类任务关掉精简模式——不给你只看毛节省的漂亮数字
