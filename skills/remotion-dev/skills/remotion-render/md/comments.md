# remotion-render (`remotion-dev/skills/remotion-render`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我以为发个命令就能凭空生成视频, 结果它是「导出」不是「制作」: 必须先有写好的 Remotion 项目, 没项目就无从渲染。
- user: 短视频博主, category: 妙用, comment: 用 npx remotion still 把成片里最出片的一帧导成图片当封面, 同一个项目正片和封面一起出, 省去开剪辑软件截帧那步。
- user: 前端工程师, category: 注意, comment: 渲染参数(选哪段视频、输出路径、格式)别凭记忆瞎猜, 官方把完整选项列在 docs/cli/render.md, 我照着那页一次就跑通了。
- user: 动画设计师, category: 注意, comment: 想要透明背景的动效素材(比如贴片叠到别的视频上), 默认导出是不透明的, 得按技能里的 transparent-videos 专门指南来渲染。
- user: 后端老兵, category: 妙用, comment: npx 方式不用额外装 CLI, 项目里直接跑就能导出。我把渲染挂到服务器定时任务, 每天自动产出一条数据视频日报。
- user: 视频剪辑老手, category: 启发, comment: 导出变成一条命令后, 我把流程改成了模板化: 每期只换文字和数据再重渲染, 一次命令就是全新一期, 产能翻倍。
