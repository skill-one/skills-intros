# higgsfield-youtube-thumbnail (`higgsfield-ai/skills/higgsfield-youtube-thumbnail`)

## blackbox

**function**: 你给我视频的主题/标题, 再附上人脸或 logo 照片(可选), 我就产出能吸引点击的视频封面图——支持 YouTube 横版、Shorts 竖版、Instagram 方版, 生成后还能按你说的只改某一处细节。

- input: 一句视频主题, 如「我在废品站花 100 元淘到宝贝」+ 一张自己的正面照, output: 一张 4K 横版 YouTube 封面图: 你的脸清晰放大在画面里, 带着切题的表情(如震惊), 场景呼应视频内容, 默认画面干净无文字
- input: 视频主题 + 品牌 logo 图片, output: 封面图里 logo 的形状、颜色、文字样式和原版一模一样, 不变形不跑色
- input: 「做一个 Shorts 封面, 主题是……」, output: 一张 9:16 竖版封面图, 人脸自动安排在画面上方适合手机竖屏观看的位置
- input: 已生成的封面图 + 「把表情改成大笑, 其他都别动」, output: 一张新封面: 只有表情变成大笑, 背景姿势灯光构图全都保持原样
