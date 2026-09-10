# caveman-setup (`juliusbrussee/caveman/caveman-setup`)

## whitebox

- 扫描依赖文件 (package.json / pyproject.toml / go.mod 等) 和源码, 按 SDK import、原生 HTTP 域名、base-URL 环境变量三层信号定位所有活跃 LLM 调用点, 逐个列出 file:line; 一个都没有则直接终止并输出 'nothing to wire' 模板, 不编造集成。
- 从包/模块名推导 app slug (小写 [a-z0-9] 开头, 可含 [a-z0-9._-], ≤64 字符), 作为网关路径 /w/<app> 的应用标识, 该应用的全部花费在仪表盘上按它归组。
- 改写每个调用点: base URL 换成 GATEWAY/w/<app>/… (保留 SDK 自身路径), 追加 x-cave-api-key 头; byok 模式再加 x-cave-upstream-key, stored 模式省略该行; 新变量 CAVE_GATEWAY_URL / CAVE_API_KEY 写入仓库已有 env 文件。
- 立即发一个真实最小请求 (max_tokens ≤ 32, 走刚接好的协议路径) 做验证, 成功标准 = HTTP 200 且响应含 usage 块。
- 按固定模板出报告, 只填实际观察到的 HTTP 状态码与 in/out token 数, 明确声明节省为 $0 (record 模式, 只测量不优化)。

- 字节保留集成: 全部改动 = base URL 替换 (host → GATEWAY/w/<app>, 保留 provider 原生路径如 /v1/chat/completions 或 /v1/messages) + 一个认证头; 上游安全由网关强制保证——网关从零重建上游认证头, 客户端原 Authorization/x-api-key 永不转发给 provider, stored 模式下上游密钥来自服务端加密连接。
- 双密钥分离与存放: x-cave-api-key 只认证网关 (stored 模式可直接填进 SDK 的 apiKey 参数位, 因为它不会传更远); x-cave-upstream-key 仅 byok 模式携带应用原有的 provider key; CAVE_API_KEY 只进 env 文件, 若该文件未被 gitignore 则补进 .gitignore。
- 验证即报告纪律: 一次真实计费请求作验收 (走 curl 命中刚接好的协议路径), 失败按逐字模板回报 (网关不可达 / 401 invalid key / 404 route not found / provider 4xx-5xx), 绝不软化或假报成功; 未列出的框架 (google-genai / crewai / pydantic-ai 等) 转去拉取 <docs origin>/docs/integrations/ 同源文档。
- 外部依赖: Caveman 网关 (字节保留的 LLM HTTP 代理, 即被测对象)、curl (发验证请求)、上游 provider LLM API (OpenAI/Anthropic 协议); 技能本身不调用任何模型。
