# vercel-cli-with-tokens (`vercel-labs/agent-skills/vercel-cli-with-tokens`)

## whitebox

- 定位凭证: 依次检查环境变量 VERCEL_TOKEN → .env 文件 (原名或任意 vercel 相关变量, vca_ 前缀) → 都没有才向用户索要
- 导出 VERCEL_TOKEN 为环境变量, 并确定目标项目/团队 (环境里的 VERCEL_PROJECT_ID + VERCEL_ORG_ID, 或从项目 URL 提取团队 slug)
- 确认 Vercel CLI 已安装: npm install -g vercel, vercel --version 验证
- 部署: 已有项目 ID 直接 vercel deploy -y --no-wait (默认 preview); 否则先 vercel link (--repo 优先, 依赖 git remote), 再走 git push 或 CLI deploy
- 收尾确认: vercel ls --format json 或 vercel inspect <url> 查状态并拿到部署链接

- 凭证传递靠环境变量: CLI 原生读取 VERCEL_TOKEN, 严禁 --token 标志传参 (避免 token 泄露到 shell 历史和进程列表); 解析用 printenv/grep/sed/cut 等 shell 工具完成
- 无链接部署: VERCEL_ORG_ID 和 VERCEL_PROJECT_ID 必须同时设置 (只设一个报错), CLI 据此直接定位项目、跳过 .vercel/ 目录; 否则 link 生成 .vercel/project.json 或 repo.json (CLI 管理, 只读不写)
- 外部依赖: Vercel CLI (npm 全局安装), git (git push 触发自动部署, 须先征得用户同意); 安全护栏: 默认 preview 不上 prod, -y 避免交互卡死, 不 curl 部署 URL 验证
