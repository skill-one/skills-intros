# slack-gif-creator (`anthropics/skills/slack-gif-creator`)

## blackbox

**function**: 你说一句想要的动画效果, 我直接给你一个能在 Slack 里发出去的动图 (GIF) 文件。

- input: 一句话描述, 如「做一个庆祝的星星动图, 发 Slack 频道用」, output: 一个能在 Slack 里直接发送的动图文件 (.gif)
- input: 一张图片 + 一句要求, 如「让这个表情眨眼」, output: 以这张图为基础做成的循环播放动图 (.gif)
- input: 「我要一个 Slack 自定义表情动图」, output: 一个符合 Slack 表情规格的小尺寸动图 (方形、约 3 秒内循环), 传上去就能用
