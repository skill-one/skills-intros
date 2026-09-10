# modern-web-guidance (`googlechrome/modern-web-guidance/modern-web-guidance`)

## whitebox

- 1. 触发时先执行 `npx -y modern-web-guidance@latest search "<动作导向的查询>"`, 在本地指南库中检索, 返回带 id/分类/相似度的 JSON 列表
- 2. 若搜索结果模糊、无匹配或相似度过低, 降级执行 `list` 命令浏览全部指南
- 3. 选定相关 id 后执行 `retrieve "<id>"` (可逗号分隔传多个 id) 取回完整 Markdown 指南; 若输出被截断, 改为重定向到文件再读取
- 4. 按指南内容实现或修改代码
- 5. 交付前做合规校验: 相关现代模式与必要 fallback 是否正确应用、是否完全满足用户需求

- 语义匹配: search 接收动作式查询 (描述要实现什么), 返回按 similarity 打分的结果, 每条含 id/category/featuresUsed/tokenCount, 用于挑选要取回的指南
- 外部依赖: 全流程依赖 npm 包 `modern-web-guidance@latest`, 经 `npx`/`pnpx` 运行 (Windows 需 `npx.cmd`; 沙箱环境可能需 `NPM_CONFIG_CACHE=/tmp/npm-cache` 或 `--offline`), 首次执行需外网下载; `--skill-version` 标志校验 SKILL.md 是否过期 (过期则向 stderr 输出警告)
- 浏览器兼容策略: 指南默认假设特性已 Baseline Widely available (可无 fallback 使用); 未达该标准的特性必须按指南写 fallback; 若用户定义自定义策略 (如 "Baseline YYYY"), 以特性 "Baseline since" 日期 ≤ YYYY 判定是否可省略 fallback
