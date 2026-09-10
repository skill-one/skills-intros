# native-data-fetching (`expo/skills/native-data-fetching`)

## whitebox

- 识别任务类型: 是否属于网络请求/数据获取/缓存/调试范畴 (决定是否启用本技能)
- 按内置决策树选型: 简单请求用 fetch, 复杂应用用 React Query, 简单场景用 SWR, Web 路由级加载 (SDK 55+) 用 Expo Router loaders
- 需要路由级加载时, 读取 references/expo-router-loaders.md 补充细节
- 按模板生成代码: 优先 expo/fetch (不用 axios), 强制检查 response.ok 并抛出类型化错误
- 按需叠加横切层: 认证 (expo-secure-store)、离线 (NetInfo)、环境变量 (EXPO_PUBLIC_ 前缀)

- 决策树路由: 内置分支结构 (加载方式/缓存/认证/错误/离线/环境配置/性能), 将用户问题匹配到唯一实现路径
- 栈选型策略: 复杂应用默认 React Query (带 staleTime/retry 配置模板), 简单需求降级为 SWR; 明确排除 axios, 统一用 fetch
- 外部依赖清单: fetch API, TanStack React Query, SWR, expo-secure-store (令牌存储), @react-native-community/netinfo (网络状态), Expo Router loaders (Web/SDK 55+), EXPO_PUBLIC_ 环境变量 (构建期内联)
