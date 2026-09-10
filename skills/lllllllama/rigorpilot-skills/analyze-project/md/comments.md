# analyze-project (`lllllllama/rigorpilot-skills/analyze-project`)

## comments

- user: 组里新来的博士新生, category: 坑, comment: 我第一句就让它"跑一下训练看报错", 它只读代码不执行命令, 白等一轮。要跑脚本排错得用别的执行类技能, 它只管看懂代码。
- user: 复现论文的研究生, category: 妙用, comment: 接手没文档的老仓库, 我先要一份 SUMMARY.md 摸清模型结构和训练/推理入口, 再决定动哪里, 比自己盲翻代码省半天。
- user: 帮忙审学生代码的师兄, category: 注意, comment: 它标记的可疑实现只是启发式线索, 不是实锤 bug。我直接拿去当评审结论, 被作者当场证伪, 人工核验这步别省。
- user: 白天写业务晚上复现论文的工程师, category: 妙用, comment: 把 RISKS.md 当接手检查单用: 列的三条疑似数据泄漏里真有一条。读码阶段的报告直接喂给下一步复现, 衔接很顺。
- user: 第一次跑复现项目的新手, category: 注意, comment: 它不装环境、不下权重, 只管读代码。先把环境配好、checkpoint 备齐再叫它分析, 要不然分析完还得自己补一轮。
- user: 带三四个学生的研究组长, category: 启发, comment: 以前我让学生上来就改代码, 现在要求先交只读分析再动手。"先看懂再改"这个流程, 比它省下的时间本身更值钱。
