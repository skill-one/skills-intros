# extension-posting-to-x (`caffeinelabs/skills/extension-posting-to-x`)

## whitebox

- 触发词命中 (tweeting/发推/posting-to-X 等) → 加载本 skill, 强制把 `x-client` mops 包写进依赖与 spec, 明确禁止手写 `ic.http_request` 直连 `api.x.com`。
- 前置挂载 `extension-authorization`: 提供 Internet Identity 登录与 caller/admin 角色基建, 否则所有端点因匿名 caller 被拒。
- `mops add x-client@0.2.3`, 按 canonical 布局生成五个文件: main.mo + 迁移链 + mixins (x-config / x-posting) + lib/x.mo。
- OAuth 2.0 PKCE: `startXOAuth` 生成 x.com 授权 URL 并持久化 code_verifier → 用户在 x.com 同意授权 → `completeXOAuth` 用 code 换 access/refresh token, 按 `caller : Principal` 存入 Map。
- 发推: `tweet` 端点先 `ensureFreshToken` (过期则用 refresh_token 静默续期并回存轮换后的新 token 对), 再经 `TweetsApi.createPosts` 发出, Config 固定 `is_replicated = ?false`。

- null 字段处理: `TweetCreateRequest.init()` 在 Motoko 侧把全部可选字段默认为 null 并在线路上省略 (X 对写入拒绝 `"field": null`、对缺失字段返回 null), 依赖 x-client ≥ 0.2.3 的 init 构造器与 `JSON.toCandid`/`JSON.fromCandid` 往返; 手写 HTTP 正是为了绕过这层保护而被列为禁止反模式。
- 非复制式出站调用: Config 固定 `is_replicated = ?false` (非可选项) — 复制式 outcall 会让子网每个节点并发携带 bearer (token 泄露面 ×N、X 限流按 ~13× 计费、限流响应头不一致破坏共识), 三个理由都指向同一配置。
- 令牌安全边界 + 外部依赖: token 存于 `Map<Principal, XAuth>` 仅按 caller 自查, 只暴露 `isMyXConnected`/`startXOAuth`/`completeXOAuth`/`tweet`/`disconnectMyX` 白名单端点, 无任何返回 token 的接口; Client ID 设置端点由 `caffeineai-authorization` 的 `#admin` 角色把关。外部依赖: mops 包 `x-client ~0.2.3` 与 `caffeineai-authorization ~1.0.0`, 目标 API 为 X API v2 (`/2/tweets` 与 OAuth token 端点); 注意 x-client 只封装 token 之后的调用面, OAuth 握手本身仍需按 X 官方文档用 `ic.http_request` 实现。
