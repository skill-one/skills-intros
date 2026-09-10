# nia (`nozomio-labs/nia-skill/nia`)

## blackbox

**function**: 把你指定的代码仓库、文档站、论文等资料收录成可提问的知识库, 之后用大白话问问题, 就能得到带出处、可溯源的答案。

- input: 「vercel/ai」这个 GitHub 仓库 + 提问「流式输出是怎么实现的?」, output: 一段直接回答 + 指向具体代码文件的出处, 能看到是哪个文件哪段代码实现的
- input: 一个文档网址 (如 docs.stripe.com) + 提问「怎么发起退款?」, output: 基于该官方文档的准确回答, 附带原文出处, 不会瞎编
- input: 一篇 arXiv 论文链接 + 提问「这篇论文的核心方法是什么?」, output: 论文内容的中文解答和要点总结, 想看细节还能定位到论文原文位置
