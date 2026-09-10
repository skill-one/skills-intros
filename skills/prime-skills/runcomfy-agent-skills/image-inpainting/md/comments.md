# image-inpainting (`prime-skills/runcomfy-agent-skills/image-inpainting`)

## comments

- user: 电商美工, category: 坑, comment: 我把蒙版黑白搞反过——白色才是要重绘的区域,黑色保留,结果把商品擦掉留下了背景。先拿小图试一张确认方向,再批量跑。
- user: 第一次用的新手, category: 坑, comment: 没登录直接跑,退出码 77,我以为是模型挂了折腾半天。其实先 runcomfy login 就行,新手记得第一步先登录。
- user: 摄影工作室后期, category: 注意, comment: 去瑕疵我一开始拉到 0.9,痘印周围皮肤纹理全被重画了。小修用 0.3–0.5,整块换背景才上 0.8+,返工少多了。
- user: 自由修图师, category: 妙用, comment: 提示词里要写蒙版外的部分,比如"保留屋顶线和天空渐变"。只描述填什么,接缝处常颜色断层,补上这句边缘就服帖了。
- user: CI 自动化运维, category: 妙用, comment: CI 里用 RUNCOMFY_TOKEN 免交互登录;退出码 75 是超时/限流可重试,我只对 75 自动重跑,其他码直接报警,夜间批量稳了。
- user: 新媒体运营, category: 妙用, comment: 客户随手丢图没蒙版也能删水印:换 Nano Banana 2 Edit,写"右下角的水印,其他保持原样",模型自己定位区域。
