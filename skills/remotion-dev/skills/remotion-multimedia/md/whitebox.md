# remotion-multimedia (`remotion-dev/skills/remotion-multimedia`)

## whitebox

- 接收任务，先判断是否属于三类能力之一：读音频时长、读视频宽高、读视频时长
- 打开 skill.md 里对应的子文档（如 get-audio-duration.md），以文档写法为实现依据
- 用 Mediabunny 在浏览器端解析用户提供的音/视频文件
- 返回结果：时长（秒）或宽×高（像素）

- 唯一核心依赖是 Mediabunny（浏览器端的音视频处理库），解析在浏览器内完成，不经过服务器
- 能力边界严格：只有时长与尺寸这三类元数据读取，每类任务各有专属 .md 子文档，超出范围不接
- 需要 Mediabunny 全貌时查阅官方总览 https://mediabunny.dev/llms.txt
