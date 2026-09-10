# firecrawl-knowledge-base (`firecrawl/firecrawl-workflows/firecrawl-knowledge-base`)

## comments

- user: 第一次用的新手, category: 坑, comment: 第一次跑没配 API key,直接卡死。先去 firecrawl.dev 拿 key 设好环境变量再启动,一次就过。
- user: RAG 应用开发者, category: 妙用, comment: 先用 quick 深度出 reference 版验来源,质量够了再按 rag 目标重跑,直接拿分块加 manifest.json,省得手写清单。
- user: 后端老兵, category: 注意, comment: 开场就报来源 URL、用途和深度,它一句不问直接开干;只说'帮我整理这个',会被反问两三轮才动工。
- user: 攒训练集的算法工程师, category: 妙用, comment: 没给网址只给主题,它靠搜索攒出官方文档+教程+社区帖混着的一批,做语料比手工全,还能直接出 jsonl。
- user: 内部知识库管理员, category: 注意, comment: 结果全在 .firecrawl/域名/ 路径下分目录,找 index.md 和 sources.json 去那儿,别在根目录翻半天。
- user: 独立开发者, category: 启发, comment: 它默认剔掉导航页脚、保留代码块和原文链接,我才发现以前爬的文档一半是噪音,清洗这步真不该省。
