# test-driven-development (`addyosmani/agent-skills/test-driven-development`)

## blackbox

**function**: 帮你写代码、修 bug、改功能, 并且每次交付都附带能自动运行的测试, 用通过的测试证明改动真的有效、没改坏其他东西。

- input: 一条 bug 描述 + 项目路径, 如「完成任务后 completedAt 时间没有更新, 项目在 ./my-app」, output: 修好的代码 + 一个自动化测试: 它在修复前运行会失败(复现 bug), 修复后运行通过, 最后整个项目的全部测试都通过
- input: 一句新功能需求 + 项目路径, 如「任务创建时标题不能为空, 项目在 ./my-app」, output: 实现该功能的代码 + 对应的自动化测试(如「空标题会被拒绝」「首尾空格会被去掉」), 运行结果全部通过
- input: 一个要改动某处功能的已有项目, 如「把订单排序改成最新的在前」, output: 修改后的代码 + 全量测试运行报告, 显示新行为正确且原有功能没有被改坏
