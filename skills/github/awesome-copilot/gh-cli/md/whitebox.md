# gh-cli (`github/awesome-copilot/gh-cli`)

## whitebox

- 解析任务, 定位到 gh 命令域 (auth/repo/issue/pr/release/workflow/search/secret 等)
- 从技能参考中取出对应的子命令、flags 和用法示例
- 校验前置条件: gh 已安装 (v2.85.0) 且已认证 (gh auth login 或 GH_TOKEN)
- 生成可直接执行的命令; 若任务跨多步 (如 fork + sync、create + clone) 则按参考手册串联多条命令

- 命令查表解析: skill.md 本质是一棵命令树 (root → 域 → 子命令 → flags), 靠精确查表匹配任务, 不臆造语法; 边界即手册覆盖范围 (仓库/Issue/PR/Actions/Release/Project/组织/扩展等)
- 认证与凭据机制: 所有操作依赖已认证的 gh; 交互式用 gh auth login (web/token 两种方式), 自动化用 GH_TOKEN 环境变量, git 拉取推送凭据由 gh auth setup-git 托管; 企业版走 --hostname 指定主机
- 输出转换: 多数命令支持 --json + --jq (jq 过滤) 获取结构化结果, 或 --web/--no-browser 转为浏览器 URL; 外部依赖: gh CLI、git、jq
