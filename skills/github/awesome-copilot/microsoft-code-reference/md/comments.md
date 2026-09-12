# microsoft-code-reference (`github/awesome-copilot/microsoft-code-reference`)

## comments

- user: 写 C# 十年的后端老兵, category: 妙用, comment: AI 生成的方法名越顺口越要查。它给我写了 BlobClient.UploadFile(), 搜了发现根本没这方法, 实际是 UploadAsync。现在 AI 写完我先搜一遍再跑。
- user: 第一次用的新手, category: 坑, comment: 照旧博客抄了 CloudBlobClient, 满屏报错。搜类名才知道那是 v11 旧包, v12 早换成 BlobServiceClient 了。搜索结果里直接标注了新旧版本。
- user: Python 数据工程师, category: 妙用, comment: 让 AI 写示例常是拼凑的。用代码搜索限定 language: python, 拿到官方完整可跑的示例, 连认证初始化的上下文都带, 改改参数就能用。
- user: 运维老哥, category: 注意, comment: 我们环境连不上微软文档的 MCP 接口, 我以为没戏了, 结果还能走 npx @microsoft/learn-cli 命令行查, 免安装。前提是机器能访问 learn.microsoft.com。
- user: 前端转 .NET 的半路出家人, category: 注意, comment: 一开始只搜 Upload, 出来一堆无关结果; 带上命名空间 Azure.Storage.Blobs 才精准命中。方法有多个重载时别靠猜, 一定 fetch 整页看全参数。
- user: 云端开发, category: 坑, comment: 上传 Blob 报 403 我先怀疑代码, 折腾两小时。后来按流程搜 DefaultAzureCredential troubleshooting, 才发现是没跑 az login 且没配 RBAC 角色。
