# image-edit (`prime-skills/runcomfy-agent-skills/image-edit`)

## comments

- user: 电商运营, category: 妙用, comment: 20 张 SKU 图一次喂给 Nano Banana,锁 aspect_ratio=1:1、resolution=1K 统一换右下角水印,一次跑完全部一致,省掉了逐张修图的半天。
- user: 第一次用的新手, category: 坑, comment: 第一反应把本地路径 D:/pic.jpg 填进 image_urls,直接失败。模型只抓公网可访问的 HTTPS 图片,先把图传到图床再跑,一次就过。
- user: 自媒体博主, category: 坑, comment: 想拿两张图合成,先试了 Flux Kontext,它只收单张。换 GPT Image 2 Edit 并写明"人物来自图1、光线来自图2",编号引用,一次就对了。
- user: 外包美工, category: 注意, comment: GPT Image 2 Edit 只有 auto 和三种固定尺寸,想自定义 800×1200 不行。不改画幅就留 auto,能保住原图比例。
- user: 摄影后期, category: 妙用, comment: 去电线时给 mask 边缘羽化 1–3px,strength 0.5 跑 Z-Image Inpaint,天空过渡完全看不出修痕;整块背景替换时才拉到 0.9。
- user: 后端老兵, category: 启发, comment: Prompt 先声明"保持××不变"再写改动,这个顺序在我所有修图任务里都成立;复合改动拆成多轮小改,比一条大 prompt 稳得多。
