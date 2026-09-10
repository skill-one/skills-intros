# ai-avatar-video (`prime-skills/runcomfy-agent-skills/ai-avatar-video`)

## comments

- user: 出海独立站站长, category: 妙用, comment: 没有真人出镜素材, 我先用配套的生图造一张半身虚拟形象, 再喂给 OmniHuman 配配音. 全程不涉及真人肖像, 肖像授权这块直接绕开了.
- user: 第一次用的新手, category: 坑, comment: 我只有文案没音频, 在 OmniHuman 里到处找填台词的地方, 白折腾半天. 它本质是图+音频驱动, 没音频文件该走 HappyHorse, 把台词引号写进 prompt 即可.
- user: 播客剪辑师, category: 坑, comment: 直接喂带背景音乐的成片音频, 嘴型对得乱七八糟. 后来把人声单独分离出来再喂, 同步立刻稳了. 给它的音频越干净, 效果越好.
- user: 运维老哥, category: 注意, comment: 服务器上别折腾 login, 设 RUNCOMFY_TOKEN 环境变量即可. 退出码 75 是限流/超时可重试, 69 是上游故障, 我第一次全当成自己配错, 白查了半天.
- user: 短视频编导, category: 坑, comment: HappyHorse 的台词没加 says clearly 原样引号, 它自己改词甚至不张嘴; 60 秒文案整段塞进去只念了开头两句. 拆成一两句一段, 逐条生成再剪到一起.
- user: 独立游戏主美, category: 注意, comment: 想让角色嘴型精确卡我录好的配音? HappyHorse 不认外部音频, 每跑一次自己重新生成语音. 这种需求走 Wan 2-7 的 audio_url, 背景画面还能随便写.
