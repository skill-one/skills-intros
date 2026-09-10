# talking-head-recut (`heygen-com/hyperframes/talking-head-recut`)

## comments

- user: 第一次剪访谈的新手运营, category: 坑, comment: 以为是加字幕的, 其实加的是设计好的图形卡(标题/数据/引言), 原视频原样播放。要逐句字幕得用隔壁 embedded-captions 技能。
- user: 知识区UP主, category: 妙用, comment: 先改 transcript.json 里的专有名词错字(时间戳别动), 卡片文案就干净了; 嘉宾说到数字的瞬间全屏大数字卡正好压上来, 观众都来截图。
- user: 双平台自媒体博主, category: 妙用, comment: 一条横版访谈直接出 9:16, 上下叠放布局(上人脸下卡片), 抖音小红书通发不用二次裁剪。比例按原视频宽高比自动推荐, 基本不用纠结。
- user: Mac剪辑党, category: 注意, comment: 渲染前记得 export PRODUCER_BROWSER_GPU_MODE=hardware, 不然 render 慢很多; 我 ffmpeg 没装, 先跑 doctor 才发现卡在第一步。
- user: 剪了上百期播客的老剪辑, category: 注意, comment: Whisper 会把末词结束时间标出视频时长, 卡片 endSec 不夹回 metadata 的 duration, 成片尾部会多一段黑屏, 长视频一定检查片尾。
- user: 做个人IP的博主, category: 启发, comment: 原视频不动这点点醒我: 素材糊一点不必重录, 信息全靠上层图形卡扛, 包装完就能发。另外默认没有片尾 logo 卡, 想要收尾要提前说。
