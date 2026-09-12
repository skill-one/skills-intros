# hyperframes-registry (`heygen-com/hyperframes/hyperframes-registry`)

## blackbox

**function**: 在 HyperFrames 视频合成项目里, 从约 400 个现成的视觉效果模板 (如毛刺、胶片颗粒、数据图表、字幕条) 中帮你搜到、装好并接进视频时间轴, 不用手动写这些特效。

- input: 用一句英文描述想要的效果, 如 "让标题一行一行地出现" (reveal a headline one line at a time), output: 一份按匹配度排序的现成效果清单, 每项带名称和用途说明, 供你挑选
- input: 一句话点单, 如 "装上胶片颗粒滤镜" 或 "把所有字幕样式类目下的都装上", output: 效果文件已装进项目文件夹, 外加一段可直接粘贴进视频页面的代码片段
- input: 项目的 index.html + 安排要求, 如 "把数据图表加到第 2 秒出现, 播 15 秒", output: 修改后的 index.html: 该效果已接上时间轴, 按指定的出现时间、时长和图层前后叠放
