# find-skills (`vercel-labs/skills/find-skills`)

## whitebox

- 匹配触发条件: 用户问 "how do I do X" / "find a skill for X" 类问题 → 拆解出领域 + 具体任务
- 先查 skills.sh 排行榜 (按安装量排序), 看是否已有知名 skill 覆盖该领域
- 排行榜没覆盖 → 运行 npx skills find [query] [--owner] 关键词搜索
- 不凭搜索结果直接推荐: 先核验安装量、来源信誉、GitHub stars
- 给出候选 (skill 名/安装量/来源/安装命令/skills.sh 链接), 用户确认后执行 npx skills add <owner/repo@skill> -g -y 安装

- 触发解析: 从用户话术 (how do I X / is there a skill / 想扩展能力) 中提取领域 (React、testing、deploy 等) + 任务 (写测试、审 PR 等), 再对照常见 skill 类别表 (web 开发/测试/DevOps/文档/代码质量/设计/效率) 判断是否大概率存在现成 skill
- 两级查找 + 三重质量闸: 一级是 skills.sh 排行榜 (安装量排名, 优先 vercel-labs、anthropics 等高装量来源), 二级是 CLI 搜索 (支持同义词换词, 如 deploy→deployment/ci-cd); 推荐前必须校验: 安装量 (1K+ 优先, <100 谨慎)、来源信誉 (官方来源可信度高于未知作者)、GitHub stars (<100 星需存疑)
- 外部依赖: 唯一外部工具是 Skills CLI (`npx skills`) —— 开放 agent skills 生态的包管理器, 子命令 find / add / update / init; 安装参数 -g (全局, 用户级) 和 -y (跳过确认); 无匹配时的降级路径: 直接用通用能力帮用户 + 建议用 `npx skills init` 自建 skill
