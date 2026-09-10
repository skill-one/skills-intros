# skill-vetter (`useai-pro/openclaw-skills-security/skill-vetter`)

## comments

- user: 第一次用的新手, category: 坑, comment: 第一次只把简介那几行贴给它审,它说没法查正文。后来学乖了:给完整的 SKILL.md 原文,权限声明写在开头 frontmatter 里,这部分才是重点,别漏。
- user: 运维老哥, category: 妙用, comment: 我给它派了个指南没明说的活:已装技能每次版本更新后重新审一遍。真抓到过一次,小版本升级后悄悄多了 network 权限,当场拦下没装。
- user: 安全工程师, category: 注意, comment: 别只盯着最终结论,我每次额外追问一句『这技能是否同时要 network 和 shell』。这组合能借命令把数据发出去,是我最在意的一条红线。
- user: 接活的独立开发者, category: 妙用, comment: 自己写的技能先丢给它过一遍再发团队仓库,省得同事装到带 curl 示例的文档被标红,来回沟通一轮直接省掉。
- user: 小团队负责人, category: 启发, comment: 现在团队装技能前都先让它出报告贴进审批单。大家从『看下载量装』变成了『看权限和红旗装』,这个习惯比工具本身值钱。
- user: 不懂安全的前端, category: 注意, comment: WARNING 不等于不能用,它分级的:Critical 直接别装;Warning 按报告建议先放沙箱试跑。我一开始见黄灯就全拉黑,误杀了不少好技能。
