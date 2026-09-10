# turborepo (`vercel/turborepo/turborepo`)

## whitebox

- 关键词触发: 用户问题命中 turbo.json、任务流水线、缓存、--filter/--affected、monorepo 结构、boundaries 等主题
- 决策树路由: 按 "配置任务 / 缓存失效 / 过滤包 / 环境变量 / CI / 包结构" 等分支定位到对应参考文档
- 读真实配置: 查用户的 package.json 脚本、turbo.json、tsconfig 确认事实再判断 (如先看 build 产出什么文件, 再谈 outputs 是否缺失)
- 反模式检查: 对照错误写法清单逐条核查 (根脚本绕过 turbo、&& 串联、prebuild 手动建依赖、env/inputs 缺失等)
- 按内置模板输出修正配置: 包任务优先 + 写入代码必须 turbo run + dependsOn/outputs 补全

- 决策树路由: 静态关键词 → 固定分支 → skill 内置 references/* 文档路径, 纯文本匹配, 无检索引擎
- 反模式对照校验: 一份固定的 错误/正确 配置对照库; 关键校验点: ① 命令写法 (写进 package.json/CI 必须 turbo run, 交互终端才可用 turbo 简写) ② 依赖声明 (^build 只有在 package.json 声明了 workspace:* 依赖才生效, 缺声明时 prebuild 不会消失) ③ 缓存哈希输入 (环境变量须列入 env, .env 文件须列入 inputs, 否则变更不触发重建; 严格模式会过滤未声明的 CI 变量)
- 模板转换: 输出内置验证过的配置成品 (标准 build pipeline、Package Configurations 的 extends 覆盖、$TURBO_ROOT$ 路径写法)。外部依赖: 技能本身不调用任何外部工具/库/模型 API, 全部能力来自 skill.md 文本; 它指导的对象是外部工具——turbo CLI、包管理器 workspace 协议、以及各框架 (Next.js/Vite/tsc) 的产物路径约定
