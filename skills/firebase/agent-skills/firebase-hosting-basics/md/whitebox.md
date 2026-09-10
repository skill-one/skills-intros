# firebase-hosting-basics (`firebase/agent-skills/firebase-hosting-basics`)

## whitebox

- 任务匹配: 判断需求是否落在技能 description 覆盖范围内 (静态站/SPA 部署、firebase.json 配置、预览频道); SSR/App Hosting、Auth、Firestore 等明确不在范围
- 按需加载参考资料: firebase.json 行为配置查 references/configuration.md, 部署/预览频道/版本回滚查 references/deploying.md
- 写/改 firebase.json: 声明 public 目录、redirects、rewrites、headers、多站点等托管行为
- 本地验证: 运行 `npx -y firebase-tools@latest emulators:start --only hosting`, 在 http://localhost:5000 检查效果
- 部署上线: 通过 CLI 正式部署, 或先推到临时预览频道 (preview channel) 验证后再上线

- 按需路由到 reference 文档而非全量加载: 触发后只读配置或部署对应的 markdown 指南, 减少无关内容
- 负向边界校验: description 内置排除清单 (App Hosting/Next.js SSR、Auth、Firestore 规则、Data Connect、Crashlytics), 不匹配即不承接
- 外部依赖: Firebase CLI (经 npx firebase-tools@latest 调用, 负责模拟器与部署); GitHub Actions 做 CI 自动预览/部署; 动态内容经 rewrites 挂到 Cloud Functions 或 Cloud Run; 线上由 Firebase Hosting 服务提供全球 CDN (SSD 缓存) 与零配置 SSL
