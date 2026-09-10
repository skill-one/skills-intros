# writing-guidelines (`vercel-labs/agent-skills/writing-guidelines`)

## whitebox

- 接收文件或 pattern 参数; 未指定时先询问用户要审查哪些文件
- 每次审查前通过 WebFetch 拉取最新写作规范 (从源 URL 现拉, 不用缓存)
- 读取指定的待审文件
- 逐条套用拉取到的规范规则检查文件
- 按规范指定的 file:line 精简格式输出发现的问题

- 规范外置: 规则不写死在技能内, 而是从 https://raw.githubusercontent.com/vercel-labs/writing-guidelines/main/command.md 每次现拉, 保证永远是最新版; 依赖 WebFetch 工具和 vercel-labs/writing-guidelines 这个 GitHub 仓库
- 远端驱动: 拉取到的文档同时包含全部规则和输出格式说明, 即审查标准与报告格式都由远端内容决定
- 定位式报告: 输出采用 `file:行号` 精简格式, 只列问题点, 不附长篇解释
