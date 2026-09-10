# pr-to-video (`heygen-com/hyperframes/pr-to-video`)

## blackbox

**function**: 给我一个 GitHub PR(代码改动)的链接, 我还你一支讲清楚"这次改了什么、为什么这样改"的讲解视频, 带配音、代码画面和背景音乐, 直接可播放。

- input: 一个 PR 链接, 如 https://github.com/vercel/next.js/pull/58123, output: 一支 MP4 视频: 开头一句话点明这次改动, 中间逐段展示真实的代码 diff 并配旁白讲解, 结尾是贡献者名单
- input: 简写引用 "acme/sdk#1842"(仓库名 + 编号), output: 同样格式的讲解视频; 改动大生成的视频更长、改动小则更短, 自动匹配内容量
- input: 在已克隆的仓库里说 "把当前这个 PR 做成视频", output: 项目目录下渲染好的 video.mp4 文件, 可指定男声/女声配音和背景音乐
