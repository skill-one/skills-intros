# code-simplification (`addyosmani/agent-skills/code-simplification`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我对它说"把代码写短点", 换来一行嵌套三元, 更难读了。后来改说"让新同事更快看懂", 出来的 if/else 才是真简单。
- user: 后端老兵, category: 妙用, comment: 合并前把 PR diff 丢给它, 明确只简化本次改动。它不碰没改过的文件, diff 干净, reviewer 再挑不出可读性毛病。
- user: 测试工程师, category: 注意, comment: 它若说"顺手改下测试就能过", 直接拒——行为已经变了。我的验收线: 测试文件必须零改动全绿。
- user: 创业公司全栈, category: 坑, comment: 一次让它做五处简化, 测试挂了查不出哪处引起。改成一处一验、跑完测试再做下一处, 出错立刻能回退。
- user: 祖传代码维护者, category: 启发, comment: 删"多余"兜底逻辑前, 先让它讲清这段代码为什么存在、谁在调它。有次真挖出隐藏调用方, 差点删错。
- user: 带团队的 Tech Lead, category: 注意, comment: 重构和加功能拆成两个 PR。混在一起, reviewer 分不清哪些动了行为, 出问题也没法单独回退那部分。
