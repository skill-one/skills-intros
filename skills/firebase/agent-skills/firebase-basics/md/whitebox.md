# firebase-basics (`firebase/agent-skills/firebase-basics`)

## whitebox

- 环境自检: 运行 `npx -y firebase-tools@latest --version` 确认 CLI 已装、MCP 服务器已装, 并按宿主 agent 类型 (Cursor/Claude Code 等 7 种) 读取对应 references/ 文档装齐技能组
- 认证: 运行 `firebase-tools login` 走浏览器授权 (远程 shell 等无浏览器环境用 `--no-localhost`), 以命令输出当前用户为成功标志
- 项目定位: 暂停并询问开发者选'现有 Project ID'还是'新建'; 用 `use` 查看当前活跃项目, 若已存在则向用户确认是否为目标项目
- 项目落地: `use <PROJECT_ID>` 切换现有项目, 或 `projects:create <project-id> --display-name` 新建 (ID 校验: 6-30 字符、小写、仅数字/连字符、全局唯一)
- 配置文件分发: 移动端接入时用 `apps:sdkconfig ANDROID/IOS <APP_ID> --project <PROJECT_ID>` 程序化拉取 google-services.json / GoogleService-Info.plist 并写入指定路径, 不引导用户去控制台手动下载

- 版本锚定: 所有 CLI 命令强制前缀 `npx -y firebase-tools@latest`, 明令禁止裸 `firebase` 命令 — 靠 npx (Node 的按需执行包工具) 每次解析 latest, 保证行为与最新版 CLI 一致
- 知识路由: Firebase 相关知识优先查 MCP 工具 `developerknowledge_search_documents` (MCP: 模型可调用的外部工具接口), 其次才回退 Google 搜索或内部知识; 远程 API 操作一律走 Firebase MCP Server 工具, 不手写 API 调用
- 引用分发 + 逐步校验: 主文档只放主流程, 环境搭建与 Web/Android/iOS SDK 接入细节分发到 references/*.md 按条件加载; 每步以命令 stdout 做校验 (`--version` 确认 CLI、login 输出当前用户、`use` 输出 Active Project)
