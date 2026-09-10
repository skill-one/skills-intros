# convex-docs (`get-convex/agent-skills/convex-docs`)

## blackbox

**function**: 帮你查到与你项目实际安装版本一致的 Convex 最新文档和 API 用法，避免凭过时记忆写出跑不通的代码。

- input: 一个项目的路径 + 一个 Convex 相关问题，如「这个项目用的 @convex-dev/agent 有没有 export scheduleAt？」, output: 基于你实际安装版本的确认结果：该 API 当前的真实签名和正确用法，并注明出处（文档页 + 版本号）
- input: 一条 docs.convex.dev 上的文档页链接, output: 该页内容转成的 markdown 版文本，同样内容但更省篇幅、更易读
- input: 一条构建报错，如「说某个 Convex 导出或 CLI flag 不存在」, output: 你实际装的版本号、该版本里真正存在且写法正确的 API，以及修正后的代码
