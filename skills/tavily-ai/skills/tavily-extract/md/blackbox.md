# tavily-extract (`tavily-ai/skills/tavily-extract`)

## blackbox

**function**: 给我网页链接, 我把页面正文干净地抓下来给你, 去掉广告、按钮等杂乱内容, 只留能读的文字。

- input: 一个网页链接, 如 https://example.com/news/123, output: 这篇文章的完整正文, 纯净文本/markdown, 没有广告和页面杂物
- input: 多个链接 (一次最多 20 个), output: 每个页面各自的正文内容, 逐一列出; 打不开的链接会单独标明失败
- input: 一个链接 + 一句「我只想知道 XX」, output: 只返回页面里与 XX 相关的段落, 而不是整篇文章
- input: 一个需要加载动画后才能看到内容的网页链接, output: 等待页面加载完成后, 依然抓到完整的正文内容
