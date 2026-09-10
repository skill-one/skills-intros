# dispatching-parallel-agents (`obra/superpowers/dispatching-parallel-agents`)

## blackbox

**function**: 把一堆互不相关的问题(如多个各自出错的测试、多个损坏的模块)同时并行解决, 最后给你一份逐项汇总: 每个问题的原因和改动。

- input: "重构后这 3 个测试文件全挂了" + 粘贴各文件的报错信息, output: 修复后的代码, 全部测试通过, 附一份汇总: 每个文件各自修了什么、根因是什么
- input: "登录模块和支付模块各有一个 bug, 互不相关" + 两份报错日志, output: 两个模块各自的修复 + 一份清单, 逐条列出每个 bug 的原因与改动点
- input: 5 条互不相关的故障现象描述(不同子系统、不同文件), output: 一份逐项报告: 每项故障的结论、已做的修复, 以及确认各项改动互不冲突、整体验证通过
