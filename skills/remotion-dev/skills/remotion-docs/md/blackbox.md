# remotion-docs (`remotion-dev/skills/remotion-docs`)

## blackbox

**function**: 查询 Remotion(用 React 写代码来生成视频的框架)的最新官方文档, 依据文档给出准确、可抄写的用法和答案, 而不是凭旧记忆瞎猜。

- input: 一个 Remotion API 名称, 如「useVideoConfig」, output: 该 API 的作用、参数、返回值说明 + 官方文档链接
- input: 一个问题, 如「怎么在云端(Lambda)渲染视频?」, output: 基于当前官方文档的回答, 附可直接抄写的代码示例和文档链接
- input: 一个报错或需求, 如「转场动画怎么加?」, output: 指向对应官方文档页的链接 + 按最新文档写出的示例代码
