# happyhorse-1-0 (`prime-skills/runcomfy-agent-skills/happyhorse-1-0`)

## comments

- user: 第一次用的新手, category: 坑, comment: 一开始写成画面描述「女生在窗边喝咖啡」, 出来基本不动。改成按时间写动作——转身、走两步、端杯、喝一口, 立刻就活了。
- user: 带货短视频博主, category: 注意, comment: 默认横版 16:9 还自带水印, 发抖音直接踩坑。要手动传 aspect_ratio 9:16、watermark false, 竖版构图也写进 prompt。
- user: 后期剪辑师, category: 坑, comment: 想拿客户配音对口型, 发现这接口根本不收音频, 是纯文生视频。对口型直接换 Wan 2.7 或 Seedance 2.0 Pro, 别在这耗。
- user: 独立广告导演, category: 坑, comment: 传 duration 30 想一把出长片, 直接 422, 上限 15 秒。后来拆成镜头 1 / 镜头 2 分段生成, 每段重写红外套蓝围巾这种锚点, 人设没崩。
- user: 预算敏感的学生党, category: 妙用, comment: 720P 加 3 秒先跑草稿验构图运镜, 满意再上 1080P 定稿。跑错了赶紧 Ctrl-C, 会自动发取消请求, 不白烧 GPU 费。
- user: 出海广告文案, category: 启发, comment: 固定 seed, 每次只改一句话做 A/B 比稿, 客户选稿快了一倍。控制变量的思路不该只留在写代码里, 写创意同样管用。
