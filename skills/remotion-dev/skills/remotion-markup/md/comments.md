# remotion-markup (`remotion-dev/skills/remotion-markup`)

## comments

- user: 前端转做视频的老哥, category: 坑, comment: 把网页里现成的 CSS animation 和 Tailwind animate-* 直接搬来, 预览里能动, 一导出全是静止画面。必须用 useCurrentFrame + interpolate 重写, transition 留一行都不行。
- user: 动效设计师, category: 妙用, comment: 标题要淡入停住再淡出: 值直接写 [0,1,1,0], easing 也能传数组一段配一个缓动, 省得拆好几层。缩放记得 output 用 perceptual-scale, 不然开头会窜一下。
- user: 第一次用的新手, category: 注意, comment: 跑 npx remotion studio --no-open 起本地预览, 网址后面拼 /组合ID 能直达那个场景, 边改边看, 别傻等整条视频渲染完再检查。
- user: 后端老兵, category: 启发, comment: 我把 npx remotion still [id] --frame=30 --scale=0.25 当单帧冒烟测试: 改完布局先渲一张小图, 几秒出结果, 和写代码先跑单测一个道理。
- user: 剪辑师出身的内容博主, category: 注意, comment: 按剪辑软件的思路记: from 是素材入场点, durationInFrames 是时长, trimBefore 是掐头。时间全写 2 * fps 别写死 60, 以后换帧率节奏不会乱。
- user: 独立开发者, category: 坑, comment: 别手动 npm install @remotion/media, 版本和主包对不上, 渲染时才报错。用 npx remotion add 会自动装匹配版本。素材放 public/, 代码里一律 staticFile() 引用。
