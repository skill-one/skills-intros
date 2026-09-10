# dbs (`dontbesilent2025/dbskill/dbs`)

## whitebox

- 定位自身 SKILL.md 目录，先跑 bash 版本检查脚本 check-update.sh（有输出则追加在回复最末尾）。
- 通读当前对话恢复任务信息，按内容路由到三种模式之一：新手教程（模式 A）/ 任务编排（模式 B）/ 空对话引导。
- 编排时运行 python3 脚本 list-official-skills.py，从 Marketplace 发现已安装的正式 Skill 候选（排除 /dbs 自身）。
- 只对比候选 frontmatter，按 5 项标准（任务结果/输入匹配/阶段匹配/边界匹配/可执行性）筛出 2–4 个，再判定走单 Skill 还是 1 主 + ≤2 辅的组合。
- 完整读取入选 Skill 的 SKILL.md（组合另读 composition-contract.md），生成一段用户可直接发送的提示词，输出后立即停止，不执行下游 Skill 的业务流程。

- 候选发现与校验：以 .claude-plugin/marketplace.json 为唯一权威源；脚本失败时回退读 references/official-skill-names.txt 并在本地定位对应 SKILL.md；缺文件、路径断裂、定义冲突的候选一律剔除，仍发现不了就停止而非虚构 Skill。
- 编排硬约束：每轮只处理一个任务、产出一份交付物；组合成员角色必须独立（前置筛选/证据补充/验收约束），最终只输出 1 段提示词，且提示词中写入执行顺序、证据、权限与提前停止条件；本 Skill 自身不代做诊断/研究/制作。
- 外部依赖（均为本地工具，无模型 API、无第三方库）：bash 脚本 check-update.sh（拉取官方 UPDATE.json，24 小时内只发一次网络请求，缓存于 ~/.dbs/update_check_at，超时/失败静默跳过）；python3 脚本 list-official-skills.py（候选发现）。
