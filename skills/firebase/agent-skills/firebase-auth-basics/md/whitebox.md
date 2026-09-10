# firebase-auth-basics (`firebase/agent-skills/firebase-auth-basics`)

## whitebox

- 前置确认: Firebase 项目已创建、CLI 已登录 (npx -y firebase-tools@latest)。
- 开通登录方式: 在 firebase.json 写入 auth 配置块 (如 emailPassword / googleSignIn / anonymous), 执行 deploy --only auth 部署到后端 (CLI 仅支持这三种, 其余提供商去控制台手动开启)。
- 客户端接入: 按 Web / Flutter / Android 对应的参考文档集成 SDK, 用户登录后拿到 ID Token 和 Refresh Token。
- 数据加固: 在 Firestore / Storage 安全规则中用 request.auth 限制访问, 凭登录状态保护数据。

- 声明式配置 + 部署生效: 登录提供商写进 firebase.json 的 auth 块, 由 Firebase CLI 推送到 Firebase 后端, 后端据此自动生成所需 OAuth 客户端; 域名白名单只写裸域名 (localhost 而非 http://localhost:9090), 否则弹窗报 unauthorized-domain。
- 双令牌身份机制: 登录后发短效 ID Token (JWT, 1 小时) 用于向 Firebase 服务或自有后端证明身份, 配长效 Refresh Token 换新; 所有提供商的用户统一由唯一 uid 标识。
- 参考文档分层: 各平台接入细节不在主文件里, 分散在 references/ 下 (client_sdk_web / flutter_setup / client_sdk_android / security_rules), 执行到对应步骤时读取, 依赖各平台 Firebase 客户端 SDK。
