# baoyu-danger-x-to-markdown (`jimliu/baoyu-skills/baoyu-danger-x-to-markdown`)

## blackbox

**function**: 把 X (Twitter) 的推文、推文串或长文章一键转存为 markdown 文件保存到本地, 方便存档和贴进笔记软件。

- input: 一条推文链接, 如 https://x.com/用户名/status/123456, output: 一个 .md 文件: 包含推文原文、作者、时间、封面图等信息, 可直接归档或导入笔记软件
- input: 一条长推文串 (thread) 的链接, output: 一个按顺序收齐整条串每条推文的 .md 文件
- input: 一篇带图片和视频的推文链接, 并选择「连媒体一起保存」, output: .md 文件 + 本地保存好的图片/视频文件, 文内链接自动指向本地文件
- input: 一篇 X 长文 (Article) 的链接, output: 提取完整正文后的 .md 文件
