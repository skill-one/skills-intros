# tavily-research (`tavily-ai/skills/tavily-research`)

## whitebox

- 触发: 用户提出深度研究类请求 (报告/对比/综述), 确认 tvly CLI 已认证 (OAuth 登录或 TAVILY_API_KEY), 已认证则不重复检查
- 选档: 按复杂度定 --model — 单主题 → mini, 多角度对比 → pro, 默认 auto 由 API 自选
- 执行: 经 Bash 运行 `tvly research "<query>" [--model pro]`, CLI 向 Tavily 服务端提交请求并阻塞等待 30~120s (可 --stream 实时看进度)
- 产出: 服务端多源收集 + AI 综合成带引用的报告返回; 需机器可读加 --json/--output-schema, 需留档用 -o 存文件

- 外部依赖单一: 只通过 Bash 调用 Tavily CLI (`tvly`, allowed-tools 限 Bash(tvly *)), 需预先认证 (浏览器 OAuth `tvly login` 或注入 TAVILY_API_KEY); 源收集/分析/引用生成全部由 Tavily 服务端 AI 模型完成, 本地仅提交、等待、取回
- 深度-速度档位: --model mini (~30s, 单主题) / pro (~60-120s, 多角度综合) / auto (默认, 按复杂度由 API 选)
- 输出结构化与异步控制: --json 取机器可读输出, --output-schema 用自定义 JSON schema 约束结构, --citation-format 定引用格式 (numbered/mla/apa/chicago); 长任务走异步 — --no-wait 先拿 request_id, 再 `tvly research status/poll <request_id>` 轮询, --stream 实时观测
