# square-post (`binance/binance-skills-hub/square-post`)

## blackbox

**function**: 把你给的文字、图片或视频直接发布到币安广场，发完返回帖子链接（只发新帖，不管改帖删帖）。

- input: 一段文字，如「BTC 突破历史新高 $BTC」, output: 这条动态已出现在币安广场，返回帖子 ID 和链接
- input: 一段配文 + 最多 4 张图片文件（如 K 线截图）, output: 图文动态发布成功，返回帖子链接
- input: 长文正文 + 标题 + 一张封面图, output: 以带封面的文章形式发布到广场，返回文章链接
- input: 一个视频文件 + 可选配文, output: 视频发布成功（封面自动从视频截取），返回帖子链接
