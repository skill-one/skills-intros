# hyperframes-animation (`heygen-com/hyperframes/hyperframes-animation`)

## blackbox

**function**: 把你口述的画面动效变成能直接播放的网页动画, 也能给已有的动画作品做体检、加转场、修节奏。

- input: 一句话描述需求, 如: "开头 logo 弹入, 接着三行文字依次上滑浮现", output: 一个能在浏览器里直接打开播放的动画页面, 按你描述的节奏演出, 拖到任意进度点都显示正确画面
- input: 一个已有动画作品的文件夹路径, output: 一份动画体检报告: 哪段时间画面完全静止、哪些元素出场节奏不齐、哪些元素从头到尾没动过
- input: "两个场景之间加个转场" 这样的需求 + 两段场景文件, output: 场景衔接的过渡代码, 插入作品后两个片段之间自然切换, 不会生硬跳变
