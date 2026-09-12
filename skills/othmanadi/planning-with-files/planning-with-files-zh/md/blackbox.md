# planning-with-files-zh (`othmanadi/planning-with-files/planning-with-files-zh`)

## blackbox

**function**: 把复杂的多步骤任务变成一份会自己更新的书面计划：干到哪一步、查到了什么、踩过什么坑，都记在你的项目文件里，中断重启也能从断点无缝接着干。

- input: 一个多步骤任务，比如「帮我把老项目迁移到新框架」, output: 项目目录里出现三个文件：task_plan.md（分阶段的计划，完成一项勾一项）、progress.md（干过的活和测试结果）、findings.md（过程中查到的结论），每完成一步自动更新
- input: 任务做了一半被中断，新开会话只说一句「继续」, output: 不需要你复述背景，直接从上次的断点接着做，已完成的阶段不重做，之前发现的坑不再踩
- input: 一个需要反复查资料的任务，比如「调研三种数据库哪个适合我们」, output: 每查到一条结论就记进 findings.md，最后给你一份带依据的对比总结；中途上下文再长、会话再久，结论也不会丢
