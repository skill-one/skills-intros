# sanity-best-practices (`sanity-io/agent-toolkit/sanity-best-practices`)

## whitebox

- 收到任务后, 先在 skill 内置的 Quick Reference 索引中匹配最贴合的那 1~2 个主题/框架指南 (如 groq、nextjs、schema)
- 只加载对应的 references/*.md 参考文件 (如 references/groq.md), 其余不读
- 以参考文件中的正确/错误代码示例、决策矩阵为准, 对照用户代码执行具体任务 (schema 设计、GROQ 查询、框架集成等)
- 任务跨多个关注点时, 才按需补充加载额外的参考文件, 否则不扩展

- 按主题选择性加载: skill 本质是一份主题索引 + 参考文件库, 按任务定向读取 1~2 个文件, 相当于对 Sanity 官方最佳实践文档的精准检索, 而非全量上下文
- 示例驱动校准: 参考文件内置 incorrect/correct 对照代码与决策矩阵, 所有 schema、GROQ、集成的输出都以这些示例为对齐标准
- 全局规则兜底 (依赖外部库处也在此): 无论任务是什么都遵守——普通文档的 _id 由 Sanity 生成、关系用 reference 字段 + GROQ 解析、视频禁止用 file 资产做生产播放, 必须走 Media Library (defineVideoField + @mux/mux-player-react 经 Mux 转码自适应播放) 或外接 Mux/YouTube/Vimeo 只存嵌入地址
