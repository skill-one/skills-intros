# writing-for-agents (`mattpocock/skills/writing-for-agents`)

## comments

- user: 后端老兵, category: 坑, comment: 我写了一堆「不要 X」「禁止 Y」, agent 反而老往这些动作上凑。改成只写目标行为, 如「提交前只跑相关测试」, 问题才真消失。
- user: 第一次写 skill 的新手, category: 坑, comment: 我一开始把所有规则塞进主文件, agent 反而抓不住重点。把只有个别情况才用的规则拆到单独文件, 指针里写清什么情况才去读。
- user: 开源维护者, category: 注意, comment: description 每轮对话都占预算, 别浪费在自我介绍上, 触发场景写进前几个词。同一情况的两个同义触发词合并成一个, 只留真正不同的分支。
- user: 运维老哥, category: 坑, comment: 我把 package.json 脚本抄进文档, 脚本改名后忘更新, agent 照旧文档跑一直失败。现在文档只写查不到的坑, 查得到的让它自己看。
- user: 技术文档写手, category: 妙用, comment: 我挑了个现成词「跑绿」当暗号, 在 AGENTS.md 和日常提示里反复用。现在一句「先跑绿再交」, agent 就走完整个验证流程, 省一大段描述。
- user: 团队 lead, category: 启发, comment: 我写「仔细检查」毫无效果, 改成「每个被改的文件都要出现在改动清单里」, 可数可核对, 漏项立刻降下来。给同事定验收标准同理。
