# extension-core-infrastructure (`caffeinelabs/skills/extension-core-infrastructure`)

## whitebox

- 应用入口用 QueryClientProvider + InternetIdentityProvider 包裹 App (该扩展随项目自动引入, 无需手动接入)
- 页面加载时 AuthClient 从 IndexedDB 恢复已存会话, 期间 isInitializing=true, 恢复成功后 isAuthenticated=true
- 用户点击登录按钮触发 login(), 打开 Internet Identity 弹窗完成认证 (可选普通 II / Google / Microsoft / 公司 SSO)
- 登录成功获得 identity, 组件按 isAuthenticated 门控渲染已登录界面
- useActor() 以当前 identity 创建类型化后端 actor, 组件直接调用后端方法取数

- 登录变体统一经 Internet Identity 收口: login({provider:"google"/"microsoft"}) 由 II 内置 OAuth 直连, 无需自备 API key; login({ssoDomain}) 通过 https://<域名>/.well-known/ii-openid-configuration 发现企业 OIDC 提供方 (Okta/Entra 等); login() 只能在真实 click 事件内调用, form onSubmit/键盘事件/await 之后均会报错, 因此 SSO 输入区刻意用 div 而非 form
- 认证状态机驱动 UI: hook 内部维护 loginStatus 与 isAuthenticated / isInitializing / isLoggingIn / isLoginSuccess 等字段; 关键规则是 isLoginSuccess 仅在弹窗交互式登录后为 true, 页面刷新恢复会话不算, 所以 UI 门控一律只用 isAuthenticated; clear() 登出并清空存储
- Actor 生命周期绑定 identity: useActor(createActor) 基于 @icp-sdk/core 创建类型化后端 actor (来自 declarations/backend); identity 变化 (登录/登出/会话恢复) 时自动用新 identity 重建 actor, 并失效+重取依赖查询 (依赖 @tanstack/react-query 的 QueryClientProvider); 依赖外部包: @icp-sdk/auth, @icp-sdk/core, @tanstack/react-query, @caffeineai/core-infrastructure, @caffeineai/object-storage
