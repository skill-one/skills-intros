# github-issues (`github/awesome-copilot/github-issues`)

## blackbox

**function**: 帮你管理 GitHub 仓库里的 issue(工作单/任务条目): 提 bug、提功能需求、建任务, 以及打标签、设负责人、关单、查询、标记任务之间谁挡住谁。

- input: 一句话描述 + 仓库地址, 如「在 acme/app 提个 bug: 登录页用 SSO 登录会崩溃」, output: 一个创建好的 issue: 编号 + 网页链接, 标题、类型 (Bug)、复现步骤、期望结果都已按规范写好
- input: 「把 #42 关掉, 打上 high-priority 标签, 指派给 zhang」, output: 更新完成的 #42: 状态已关闭、带 high-priority 标签、负责人是 zhang (附链接)
- input: 「这个仓库还有哪些没修完的 bug?」, output: 一份清单: 所有 open 状态 bug 的编号、标题、标签, 一眼看清剩余工作量
