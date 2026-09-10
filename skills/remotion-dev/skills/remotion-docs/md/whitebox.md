# remotion-docs (`remotion-dev/skills/remotion-docs`)

## whitebox

- 收到关于 Remotion 概念或 API 的问题, 启动四步工作流
- 用关键词调用 Algolia 搜索 API, 在 Remotion 文档索引中检索相关页面
- 从返回的 hits 中按相关性挑出最匹配的文档 URL
- 给每个 URL 追加 .md 后缀抓取页面, 得到 Markdown 原文
- 基于当前文档内容回答或实现, 而非依赖记忆

- 检索依赖外部 Algolia 搜索 API: POST 请求携带预置的 application-id 与 api-key, 固定索引名 "remotion", 每次最多返回 10 条, 只请求页面层级标题和 URL 两个必要字段
- 省 token 抓取: 任意 remotion.dev/docs 页面 URL 加 .md 后缀即可取回 Markdown 源码, 避免抓取完整 HTML
- 校验方式是流程性的而非解析性的: 明确规定"用当前文档而非记忆中的 API 知识"来实现, 防止凭过时记忆输出错误 API
