# architecture-decision-records (`wshobson/agents/architecture-decision-records`)

## comments

- user: 后端老兵, category: 妙用, comment: 评审会当场用 Y-Statement 五句话敲定结论，比会后补写全文快得多。新 ADR 标 Supersedes 旧编号，日后能顺着链子翻到当初的取舍。
- user: 第一次用的新手, category: 坑, comment: 我直接在已 Accepted 的旧 ADR 里改决策，同事照旧文档干活返工了。正确做法：新建一条标 Supersedes，旧文件只改状态。它是档案，不是活文档。
- user: 创业公司全栈, category: 注意, comment: 别一上来就用 MADR 全模板，写两条就没人坚持了。小团队换 Template 2 轻量版（状态+背景+决策+后果），能写下去比格式全重要。
- user: 接手祖传项目的新人, category: 启发, comment: 入职先读完 adr 目录 20 条，「为什么选它」没问人就有答案，连被推翻的决策都有完整记录。以前觉得记录是形式，现在动手前会先想：这选择值得留档吗？
- user: 运维老哥, category: 妙用, comment: 下线旧库时套 Template 4，四阶段迁移写进文档，评审没人反对。adr-tools 的 `adr new -s 3` 自动关联旧记录，README 索引也不用手动改。
- user: Tech Lead, category: 注意, comment: 先过「该不该写」对照表再动笔。我们连改配置都写，两周 40 条没人看，重要决策被淹了。Rejected 的别删，后来重选方案时那页否决理由省了一轮调研。
