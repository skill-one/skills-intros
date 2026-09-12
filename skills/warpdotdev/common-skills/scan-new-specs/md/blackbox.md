# scan-new-specs (`warpdotdev/common-skills/scan-new-specs`)

## blackbox

**function**: 本盒子已退役(2026-08-20):不再自动扫描规格、起草功能文档,只负责拒绝执行并把用户引导到仍在服役的替代方案。

- input: 「扫描刚合并的产品规格,帮我自动起草文档」, output: 拒绝执行 + 提示:该流程已退役,因为它会为未上线的功能写出不实的文档;改用 missing_docs (drift-watch 模式)
- input: 「我是工程师,想给我的新功能写一篇文档」, output: 指引你直接调用 write-feature-docs,由它和你交互式地完成文档撰写
- input: 「我想设置一个定时自动补文档缺口的任务」, output: 指引改用 missing_docs 技能做定时任务,并警告:如果用本盒子做定时任务,会重新堆出一堆没人审核的草稿
