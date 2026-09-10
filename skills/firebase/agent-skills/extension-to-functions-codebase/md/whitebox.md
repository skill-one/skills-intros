# extension-to-functions-codebase (`firebase/agent-skills/extension-to-functions-codebase`)

## whitebox

- 盘点资源: 解析 extension.yaml, 将 params/apis/roles/lifecycleEvents/resources 逐项清点, 同时保留原有 devDependencies 与测试脚本
- 按目标落地: 目标 A 输出 functions/src/ + .env 配置; 目标 B 构建 npm 包 (设置 name, node>=22, peerDependencies, ESM/CJS exports 映射)
- 触发器升级 V1→V2: Firestore→onDocumentWritten, Tasks→onTaskDispatched (移除 EXT_INSTANCE_ID), HTTP→onRequest, 并套用解构兼容 shim ({ change, context } / { snapshot, context })
- 生命周期与初始化转换: onInstall→afterFirstDeploy, onUpdate/onConfigure→afterRedeploy; 全局 SDK 实例改在 onInit() 或懒加载 getter 中创建, 禁止顶层 .value()
- 生成 README (安装说明、export * 片段、.env 参数表、Extension vs Package 对比表) 后交付; 全程不执行 npm publish

- 规则化映射转换: extension.yaml 各段与代码 API 一一对应 (params→defineString/Int/Boolean/Secret, apis→requiresAPI, roles→requiresRole, lifecycleEvents→SDK lifecycle hooks), 纯确定性映射, 无模型参与
- 兼容层三件套: ① 解构 shim 让 V1 处理器签名 (change, context) 适配 V2 触发器; ② cpu: "gcf_gen1" 保持 V1 单并发定价 (V2 默认并发可达 80); ③ 声明式 IAM/API (requiresRole/requiresAPI) 替代手动 gcloud 脚本
- 依赖: firebase-functions v2 子模块 (firestore/tasks/https/params) + firebase-admin ^11/^12, 运行时 Node >=22; 外部 SDK (如 BigQuery) 实例一律 onInit/lazy 初始化
