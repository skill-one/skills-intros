# firecrawl-research-index (`firecrawl/skills/firecrawl-research-index`)

## blackbox

**function**: 你描述一个研究问题, 我帮你找出能回答它的学术论文 (覆盖生物医学临床文献和 arXiv 计算机/物理/数学预印本), 交给你一份按相关度排序的论文清单。

- input: 「最近有哪些 CRISPR 治疗镰状细胞病的临床试验论文?」, output: 一份论文清单: 每篇含标题、作者、发表出处、日期和摘要, 相关度高的排前面
- input: 「最早提出扩散模型的是哪篇论文? 有哪些类似方法?」, output: 开创性论文 + 一批同门/竞品方法的论文, 合成一份完整的相关工作家族清单
- input: 「xx 论文里实际和哪些模型做了对比? 分数是多少?」, output: 从该论文正文中摘出的具体对比对象和报告的数字, 而不是只给摘要
