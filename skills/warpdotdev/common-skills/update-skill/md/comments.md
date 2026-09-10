# update-skill (`warpdotdev/common-skills/update-skill`)

## comments

- user: 第一次给 AI 写技能的新手, category: 坑, comment: 我把 name 写成 "PDF_Processing", 校验直接不过——只允许小写字母、数字和连字符, 改成 pdf-processing 才通过.
- user: 做知识库的运维老哥, category: 妙用, comment: 发现 description 是给 AI 检索用的: 把用户会喊的关键词都塞进去, 之后一句"抠 PDF 表格"就能命中技能, 不用记名字.
- user: 要沉淀团队流程的技术负责人, category: 注意, comment: 它管格式和结构, 不替你编内容——流程细节、代码示例还得自己喂给它, 把它当"格式师傅"而不是代笔.
- user: 写惯内部文档的后端, category: 启发, comment: 要求 description 动词开头、第三人称、写清何时用, 才发现我以前写的全是"帮助用户…"这种谁都搜不到的废话.
- user: 半途接手的维护者, category: 注意, comment: 我把细节全堆进 SKILL.md, 写到 300 行才想起拆——流程留正文, 参考资料搬进 references/, 单文件尽量压在 200 行内.
- user: 开源仓库维护者, category: 妙用, comment: 让它先照 .agents/skills/ 里的现成技能动笔, 结构口吻一次到位; 写完跑 skills-ref validate 兜底, 前后各一步免返工.
