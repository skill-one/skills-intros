# remotion-render (`remotion-dev/skills/remotion-render`)

## whitebox

- 接到导出需求, 判断产物类型: 视频 or 静帧
- 视频走 `npx remotion render`, 静帧走 `npx remotion still`
- 按需查阅官方 CLI 文档 (render.md / still.md) 确定参数选项
- 特殊需求查专门指南 (如透明视频 → transparent-videos.md)
- 执行命令, 产出成品文件交付

- 执行入口是 npx (Node.js 的命令行运行器), 无需本地装包即可拉起 Remotion CLI (当前 skill 版本 4.0.522)
- 渲染参数不凭记忆硬编码, 以官方 CLI 文档为准按需查询, 保证选项用法准确
- 透明视频等特殊场景不靠猜测, 转入对应子文档获取专门流程
