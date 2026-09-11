# extension-openai (`caffeinelabs/skills/extension-openai`)

## whitebox

- 触发识别: 用户/规格提到 ChatGPT、GPT、LLM、chatbot 或 embeddings 时, 在写任何触及 api.openai.com 的代码之前加载本配方
- 选变体: 按用户/管理员/完全匿名三选一 — 由"谁贴 key、谁付费"决定; 前两者需先加载 extension-authorization (登录与角色基础设施)
- 加依赖: `mops add openai-client@0.2.5` 一步原子更新 mops.toml 和 mops.lock
- 生成代码: canister 状态里存 key (按用户 Map<Principal, Text> 或单个变量) + set/clear/configured 三个端点 + SDK 胶水层
- 校验不变量: Config 上 is_replicated = ?false、无任何返回 key 的 getter、不写日志、匿名调用方拒绝

- 认证模型: OpenAI 只用单一静态 Bearer key (sk-...), 无 OAuth/回调/刷新; key 永不离开 canister, 前端只拿到 "已配置?" 的 Bool — 任何返回 ?Text 的读取端点都视为泄漏点被禁止
- `is_replicated = ?false` 强制写入 Config, 三个理由: 复制型外呼会让子网每个节点各自过一次 TLS 携带 Bearer (泄漏面)、OpenAI 按 N 倍计费 (约 13× cycles), 且 LLM 概率采样响应过不了复制共识
- 类型化绑定替代手写 HTTP: openai-client mops 包 (由 OpenAPI spec 2.3.0 生成的 Motoko 绑定, Chat/Embeddings/Images/Audio 等 8 个模块), JSON.init 构造器把全部可选字段默认置 null — 不再手搓 JSON; 外部依赖: openai-client@~0.2.5、caffeineai-authorization@~1.0.1 (Internet Identity 登录 + caller/角色)、OpenAI REST API
