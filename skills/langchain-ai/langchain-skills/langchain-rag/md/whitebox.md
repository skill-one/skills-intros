# langchain-rag (`langchain-ai/langchain-skills/langchain-rag`)

## whitebox

- 任务命中「构建 RAG 系统」→ 触发 langchain-rag skill, 按 skill.md 的三段管线执行: Index → Retrieve → Generate
- Index: 按数据源选 Document Loader (PDF/网页/目录) 载入 → RecursiveCharacterTextSplitter 切块 → OpenAIEmbeddings 向量化 → 存入向量库 (Chroma/FAISS/Pinecone, 按场景选型)
- Retrieve: 用户 query 用同一 embedding 模型向量化, 向量库相似度检索 (或 MMR) 返回 top-k 文档, 可按 metadata 过滤
- Generate: 检索到的文档拼成 context, 连同 query 以 system+user 消息交给 ChatOpenAI (gpt-4.1) 生成回答

- 解析与转换: 各类 Loader 把 PDF/网页/文本统一转为 Document (page_content + metadata); RecursiveCharacterTextSplitter 按分隔符层级 ["\n\n", "\n", " ", ""] 递归切块, chunk_size 1000 + overlap 200 (10~20%) 保边界上下文
- 检索与生成: 索引与查询必须用同一 embedding 模型 (如 text-embedding-3-small), 否则向量不兼容; 检索用相似度或 MMR 平衡相关性与多样性; 依赖 LangChain (Python/TypeScript)、OpenAI API、PyPDFLoader/CheerioWebBaseLoader、Chroma/FAISS/Pinecone
- 校验规则 (fix 清单): chunk_size 控制在 500~1500; 必须持久化到磁盘向量库而非内存; Pinecone 索引维度需与 embedding 维度匹配; FAISS load_local 的 allow_dangerous_deserialization=True 仅限自建可信索引 (pickle 反序列化有代码执行风险)
