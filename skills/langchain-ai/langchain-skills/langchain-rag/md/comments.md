# langchain-rag (`langchain-ai/langchain-skills/langchain-rag`)

## comments

- user: 第一次用的新手, category: 坑, comment: 用 InMemoryVectorStore 跑通 demo 就直接用了, 重启后索引全没, 重新 embedding 又慢又烧钱. 换 Chroma 设 persist_directory, 建一次库反复用.
- user: 后端老兵, category: 坑, comment: 建库用 3-small, 后来查询图新换了 3-large, 检索结果不对劲还难排查. 索引和查询必须同一个 embedding 模型, 固定住版本才消停.
- user: 安全工程师, category: 注意, comment: 网上拷来的 FAISS 索引别直接加载, 那个危险反序列化开关等于放行加载时执行代码. 我只加载自己建的索引, 外来的一律用源文档重建.
- user: 企业内部工具开发, category: 妙用, comment: 把部门和文档类型写进 metadata, 检索时加 filter 只搜本部门内容, 一套向量库服务全公司, 不用每个团队各建一个.
- user: 客服机器人开发, category: 妙用, comment: 手册重复段落多, 普通检索 k=5 返回五条差不多的话. 换 MMR 搜索后结果相关又各有侧重, 喂给模型后回答不再原地绕圈.
- user: 独立开发者, category: 启发, comment: 把检索包成工具交给 agent, 它自己决定何时查文档, 我不再手写检索和回答的串联流程. 突然明白知识库可以做成按需调用的服务.
