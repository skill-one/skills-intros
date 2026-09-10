# ai-video-generation (`101-skills/superpowers/ai-video-generation`)

## comments

- user: 第一次用的新手, category: 坑, comment: 没先跑 belt login 直接照抄示例命令, 一直报未授权。先装 CLI 再登录这步不能跳, 登录后同一条命令立刻就通了。
- user: 全职自媒体博主, category: 注意, comment: 图生视频的 image_url 只认网络链接, 本地图片要先传图床拿到 https 地址, 直接填本地路径跑不动。
- user: 短视频运营, category: 妙用, comment: 我把生成的无声片段先用 foley 补上脚步声和鸟叫, 再用 media-merger 加淡入转场拼成片, 全程没开剪辑软件。
- user: 知识区UP主, category: 妙用, comment: 用文字转语音技能先生成旁白音频, 喂给 omnihuman 让照片开口讲课, 口播视频一条龙, 每期省一次出镜。
- user: 独立开发者, category: 注意, comment: 调 prompt 阶段用 veo-3-1-fast 试错, 定稿才换 veo-3-1 正式版。我一开始全用满血版, 一天烧掉小半月额度。
- user: 探店剪辑师, category: 坑, comment: 跑 Seedance 忘了写 generate_audio: true, 出来是无声的, 重跑又扣一次费。要带声音这个参数必须显式传。
