# resolving-merge-conflicts (`mattpocock/skills/resolving-merge-conflicts`)

## blackbox

**function**: 当 git 合并或变基卡在冲突报错时,把冲突的代码改到两边都说得通,让这次合并顺利收尾。

- input: 一个卡在合并冲突的仓库目录(终端刷满 CONFLICT 报错,文件里全是 <<<<<<< 标记), output: 所有冲突文件被改好,合并提交完成,仓库恢复干净状态,可以继续正常干活 ✅
- input: 一次进行到一半的 rebase(搬到第 3 个提交就停了,还剩 2 个), output: 冲突逐个解决,剩余提交全部搬完,变基收尾,提交历史按原计划排好
- input: 指定某个冲突文件,如 src/pay.py——两个人改了同一个函数, output: 该文件冲突消除:两边的改动意图都保留;实在不能兼容时,选符合本次合并目的的一方,并明确告诉你牺牲了什么
