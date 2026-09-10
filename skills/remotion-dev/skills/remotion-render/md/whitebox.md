# remotion-render (`remotion-dev/skills/remotion-render`)

## whitebox

- 收到导出请求后，先判断输出类型：视频（render）还是单帧图（still）
- 视频走 `npx remotion render`，单帧图走 `npx remotion still`，直接执行 CLI 命令
- 渲染参数按需查阅官方 CLI 文档确认后再使用
- 如需透明背景，参照技能包内的 transparent-videos.md 指南配置渲染
- 输出渲染完成的视频/图片文件

- 外部工具依赖：所有渲染均通过 Remotion CLI 执行（`npx remotion render` / `npx remotion still`），不涉及其他库或模型 API
- 参数解析：CLI 全部选项以官方文档为准（remotion.dev/docs/cli/render.md 与 still.md），不臆造参数
- 透明视频：有专门的 transparent-videos.md 指南，按其流程渲染带透明通道的视频
