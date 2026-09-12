# microsoft-code-reference (`github/awesome-copilot/microsoft-code-reference`)

## whitebox

- 接收 Microsoft SDK/API 任务 (写代码/查 API/排错), 按约定拼查询串: 类名+方法+命名空间, 如 "BlobClient UploadAsync Azure.Storage.Blobs"
- 调用 microsoft_docs_search 确认方法/类/包真实存在
- 若涉及重载或复杂参数, 调 microsoft_docs_fetch 拉取完整参考页
- 调用 microsoft_code_sample_search 按语言取官方可运行示例
- 以文档+示例为准生成或修正代码

- 数据源: Microsoft Learn MCP Server (https://learn.microsoft.com/api/mcp); 不可用时降级为 mslearn CLI (npx @microsoft/learn-cli, 支持 search / code-search / fetch, --json 取原始输出)
- 校验优先: 不凭记忆写代码, 先查官方文档, 专抓幻觉方法名 (UploadFile vs 实际 Upload)、SDK 版本混用 (v11 CloudBlobClient vs v12 BlobServiceClient)、过时写法
- 分层查询: 简单查询一步 search 即可; 复杂 API 用法走完整三步 (search → fetch 详情 → code-sample)
