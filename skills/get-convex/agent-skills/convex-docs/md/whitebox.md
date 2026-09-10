# convex-docs (`get-convex/agent-skills/convex-docs`)

## whitebox

- 先钉住版本: 用 node 读取本项目实际安装的 convex 版本号及各 @convex-dev/* 组件版本
- 按新鲜度层级取文档: 优先用已接入的 docs 工具, 否则抓取 docs.convex.dev 对应页的 markdown 版本, 最后才退到普通网页搜索 (视为未验证)
- 对拿不准的导出/API, 核对 node_modules 里已装包的 .d.ts 与 package.json exports (该版本的真值)
- 把查到的新鲜事实 (签名/参数) 按出处引用并套用, 具体代码写法交回 convex-expert 完成
- 若出现版本不匹配的构建报错: 重新钉版本、重取当前 API, 而不是猜另一种拼写

- 版本钉定 (PIN): 通过 Node.js 执行 `node -p "require('./node_modules/convex/package.json').version"` 或读 package.json, 确保引用的文档与实际安装版本一致 — 版本错位是写错 Convex 代码的头号来源
- 分层取真 (freshness hierarchy): 最省优先 — (a) 已接入的 docs 检索工具 (返回按版本限定、重排的答案) → (b) 把文档页以 markdown 形式抓取 (比 HTML 省 token) → (c) 普通网页搜索兜底但视为未验证
- 类型真值校验 (VERIFY): node_modules 里已安装包自身的 exports 与 .d.ts 类型声明是本版本的最终权威, 优先级高于任何文档页
