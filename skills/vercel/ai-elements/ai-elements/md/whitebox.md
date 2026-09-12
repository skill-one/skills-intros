# ai-elements (`vercel/ai-elements/ai-elements`)

## whitebox

- 触发条件: 用户要构建聊天机器人 / AI 助手 UI / 任何 AI 聊天界面
- 环境校验: 确认 Node.js ≥18 + Next.js + AI SDK 项目; 若无 shadcn/ui, CLI 会自动安装
- 安装组件: 按项目 packageManager 选择 npx / pnpm dlx / bunx 执行 ai-elements@latest, 组件源码落入 @/components/ai-elements/
- 组装界面: import Message / MessageContent / MessageResponse 等子组件, 配合 @ai-sdk/react 的 useChat 遍历 messages.parts 按 type 渲染
- 定制收尾: 组件代码归项目所有, 直接改文件即可 (如删 rounded-lg), 装完即用, 无需额外配置

- CLI 代码注入: AI Elements CLI (兼容 shadcn/ui CLI) 把组件源码直接下载进项目 components 目录 —— 不是黑盒依赖库, 代码可读可改, 用法与手写组件一致
- 基于 shadcn/ui + Tailwind: 样式靠 Tailwind class + cn() 合并; 组件尽量继承原生 HTML 属性 (如 Message extends HTMLAttributes<HTMLDivElement>), 传 div 支持的任意 props 即可扩展
- 依赖 AI SDK 数据层: useChat 提供消息流, 按 part.type 分发渲染 (text → MessageResponse); 可选接 Vercel AI Gateway, 用一个 key 访问各家模型 API
