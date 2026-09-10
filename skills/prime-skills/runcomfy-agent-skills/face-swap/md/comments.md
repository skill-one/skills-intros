# face-swap (`prime-skills/runcomfy-agent-skills/face-swap`)

## comments

- user: 短视频口播博主, category: 坑, comment: 只传 image_url 不给音频, 出来角色全程哑的。Wan 必须配 audio_url, 口型和节奏全跟音频走; 想连声音一起换, 它做不到, 得另找对口型的 avatar 方案。
- user: 独立站卖家, category: 妙用, comment: 第一张放模特脸、后面全放场景图, 一批最多 20 张; 锁死 aspect_ratio 和 resolution, 整批 SKU 出来是同一张脸同一比例, 免了挨张校对。
- user: 动画工作室导演, category: 妙用, comment: 别当换脸工具用: 把自己录的表演视频喂给 Kling Motion Control, 让 IP 形象'演'我, 风格化角色出片比真人换脸还干净。要保留原片动作选它, 纯换脸才用 Wan。
- user: 第一次用的新手, category: 坑, comment: 把本地文件路径直接填进 image_url, 报 exit 65 白折腾半小时——接口只吃 HTTPS 网址。先把图传图床拿到链接再跑, 一次就通。
- user: 品牌视觉设计师, category: 注意, comment: Flux 一次只吃一张图、改一处; 我贪心一句 prompt 同时换脸换发型, 两边都不像, 拆成两次 pass 反而快。没参考图时把新脸用文字描述具体, 效果意外能打。
- user: MCN 内容审核, category: 注意, comment: 工具不替你把关: 换进去的脸要拿到授权, 发布平台可能要求标注'AI 生成', 缺一样随时下架。拿公众人物的脸做恶搞素材, 别怪没人提醒。
