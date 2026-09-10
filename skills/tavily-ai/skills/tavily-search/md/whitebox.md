# tavily-search (`tavily-ai/skills/tavily-search`)

## whitebox

- 触发: 识别搜索意图 ("search for"/"find me"/"look up"/"最新" 等) → 无需先找 API key, 直接准备执行 (keyless 有额度上限)
- 前置检查: 确认 `tvly` CLI 可用; 缺失则先按 tavily-cli setup 安装后再重试原搜索
- 组装命令: 按需求拼参数 `tvly search "query" --json` + 选项 (--depth/--max-results/--time-range/--include-domains 等), 查询语句保持 <400 字符
- 执行与返回: 经 Bash 运行, Tavily API 返回带内容摘要、相关度评分和元数据的结果, 解析后答复用户

- 外部依赖: Tavily 官方 CLI `tvly`, 经 Bash 调用 (allowed-tools: Bash(tvly *)); skill 本身不实现搜索, 只做查询组装与结果解读
- 免 key 鉴权: 首次请求无需 API key (keyless 封顶); 交互环境额度耗尽 → `tvly login` 浏览器 OAuth 后重试一次; 无人值守环境只报告额度与鉴权选项, 不启动交互流程
- 结果校验与加工: 返回 LLM 优化的 JSON (snippet + relevance score + metadata); 身份敏感事实 (发布/版本/所有权) 须回溯源仓库或官方域名核实, `--include-domains` 限定可信来源; `--include-raw-content` 可内联整页正文, 省去单独的 extract 调用
