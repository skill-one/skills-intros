# google-agents-cli-workflow (`google/agents-cli/google-agents-cli-workflow`)

## comments

- user: 第一次用的新手, category: 坑, comment: 上来手动建项目, 结果少了评测样例和 CI/CD 配置, 只能重跑 scaffold 再搬一遍代码。另外先装 uv, 否则 install 命令直接找不到。
- user: 后端老兵, category: 妙用, comment: CLI 命令报错时, 跑 agents-cli 命令 --help, 输出末尾有 Source: 行直接指向实现源码, 看一眼就定位问题, 不用到处瞎搜。
- user: 算法工程师转 agent, category: 坑, comment: 我给 agent 写 pytest 断言回复必须含某关键词, 输出不稳定天天误报。LLM 行为交给 eval 打分, pytest 只留来测函数本身。
- user: 独立接活的全栈, category: 注意, comment: eval run 不管得分多差退出码都是 0, 我看命令成功就当过了。分数必须自己逐条读; 修到达标一般要 5-10 轮, 别指望一遍过。
- user: 做过三个 agent 项目的外包老手, category: 妙用, comment: 要给 agent 加记忆和风险操作审批, 差点从零手写。先查 samples.md 主题索引, 有现成 recipe 可 clone 照改, 至少省一周。
- user: 两人创业团队 CTO, category: 启发, comment: 它问需求时我嫌烦回了句你看着办, scaffold 完发现方向不对整个重做。现在认真答完问题, spec 存档后改需求都有据可查。
