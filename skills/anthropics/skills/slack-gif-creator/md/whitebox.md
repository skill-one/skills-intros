# slack-gif-creator (`anthropics/skills/slack-gif-creator`)

## whitebox

- 初始化 GIFBuilder: 按 Slack 用途定尺寸 (表情 128x128 / 消息 480x480) 和 FPS (10-30)
- 循环生成帧: 用 PIL ImageDraw 逐帧绘制图形, 按动画概念 (缓动/正弦振荡/alpha 混合) 计算每帧状态, add_frame 入队
- 保存: builder.save() 把帧序列合成 GIF, 同时做调色板降色、去重帧、emoji 模式优化
- 校验: core.validators 对照 Slack 约束 (尺寸/FPS/颜色数/时长), is_slack_ready 快速判定是否可上传

- 图形全部代码现场绘制: 基于 Pillow 的 ImageDraw 原语 (ellipse/polygon/line/rectangle) 组合出复杂形状; 明确不用 emoji 字体、无预置素材库
- 动画 = 逐帧重绘: 位移/缩放/旋转/淡入淡出分别用 math.sin 振荡、image.rotate、alpha 混合实现, 缓动曲线由自带 core.easing.interpolate (bounce_out/elastic_out 等) 提供; 用户上传的图片也可用 PIL 读入直接使用或仅作参考
- 体积优化三板斧: 降帧 (低 FPS/短时长)、GIF 调色板量化 (num_colors 48-128)、remove_duplicates 去重; 依赖 pillow + imageio + numpy, 不调用任何外部模型 API
