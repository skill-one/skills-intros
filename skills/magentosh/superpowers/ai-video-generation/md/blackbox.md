# ai-video-generation (`magentosh/superpowers/ai-video-generation`)

## blackbox

**function**: 把一段文字描述或一张图片变成短视频；还能让照片里的人开口说话、给视频加音效、提升画质、拼接多段视频。

- input: 一段文字，如「无人机飞过秋天的森林上空」, output: 一段几秒钟的短视频文件（MP4），可带声音
- input: 一张静态照片的链接, output: 这张照片「动起来」的视频，如风吹树叶、镜头缓缓推移
- input: 一张人像照片 + 一段语音录音, output: 照片里的人开口说话、口型对得上的视频
- input: 一段没有声音的视频 + 一句描述，如「脚步声、鸟叫」, output: 配好环境音效的同一支视频
- input: 一段画质模糊的视频, output: 清晰度提升后的同一支视频
