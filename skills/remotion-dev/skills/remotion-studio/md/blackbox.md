# remotion-studio (`remotion-dev/skills/remotion-studio`)

## blackbox

**function**: 给我的视频项目开一个网页版预览间:在浏览器里就能播放、逐帧查看我的 Remotion 视频。

- input: 一个 Remotion 视频项目的文件夹路径, output: 一个浏览器网址(如 http://localhost:3000),打开后能看到视频画面和场景列表,可播放、暂停、拖动进度逐帧检查
- input: 「帮我把我的视频项目预览起来」(附带项目所在目录), output: 浏览器中打开预览页面:左侧是你的视频场景/参数列表,右侧是实时画面,改代码画面即时刷新
- input: 同一个项目之前已经开过预览, output: 直接告诉你那个还在运行的预览网址,不会重复再开一个
