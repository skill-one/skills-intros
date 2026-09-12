# tavily-cli (`tavily-ai/skills/tavily-cli`)

## whitebox

- 环境就绪: `tvly` 未装则用 curl 安装脚本 (或 uv/pip) 安装, 再 `tvly init --skip-auth` 装内置技能并跑一次真实 keyless 搜索验证
- 按升级阶梯选命令: 无 URL → `search`; 有 URL → `extract`; 大站定位子页 → `map`; 整站批量抓取 → `crawl`; 多源综合 → `research`
- 执行: 一般加 `--json` 运行, 结果直接是 LLM 优化的 JSON; map/crawl/research 需先认证, search/extract 可免 key 但受速率上限
- 遇限流/需认证时: `tvly login` 走浏览器 OAuth, 然后原命令重试一次
- 交付: 用 `-o` 把 JSON 存文件, 或 crawl 用 `--output-dir` 每页落一个 Markdown

- 单一入口 = shell 子进程: 所有能力都通过 `Bash(tvly *)` 调 `tvly` CLI 子命令完成, skill 本身不含独立逻辑, 只是选命令和传参
- 输入输出全 JSON 化: `--json` 输出为 LLM 优化的结构化数据, `-o` 落盘保存, crawl 额外支持按页面拆分 Markdown; 失败靠退出码反馈 (0 成功 / 1 安装失败 / 2 输入错 / 3 认证错 / 4 API 错)
- 外部依赖: Tavily 后端 API (经 `tavily-cli` 二进制, curl 脚本/uv/pip 安装); 认证走浏览器 OAuth (localhost 回调, 远程需端口转发) 或 `TAVILY_API_KEY` 环境变量
