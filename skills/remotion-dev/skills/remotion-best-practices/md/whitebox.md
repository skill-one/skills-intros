# remotion-best-practices (`remotion-dev/skills/remotion-best-practices`)

## whitebox

- 接到任务先做意图归类: 新建视频 / 项目初始化 / React 标记 / 地图 / 多媒体 / 交互 / 渲染 / Studio / 字幕 / SaaS / 查文档 / 升级
- 按 skill.md 中的路由表, 加载对应子技能的 REFERENCE.md (按需加载, 不预载)
- 若任务是建视频但当前无 Remotion 项目, 先走「新建 Remotion 项目」指南
- 严格按已加载的 REFERENCE.md 执行任务
- 执行中若检测到用户在对话外改过代码 → 不覆盖, 视为有意修改或先确认

- 路由器架构: skill.md 本身不含任何实现知识, 只是一张「任务意图 → REFERENCE.md 文件路径」的分发表, 具体知识延迟加载
- 变更保护机制: 主动检测对话外的代码改动, 假设是有意修改或请求确认, 防止覆盖用户工作
- 外部依赖: Remotion 框架 (基于 React 的视频框架) 及其 CLI (npx remotion render、Remotion Studio)、Lambda/Vercel/Cloudflare 渲染、Mapbox/MapLibre/MapTiler 地图、Mediabunny 多媒体包、React 标记
