# image-to-video (`prime-skills/runcomfy-agent-skills/image-to-video`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我拿照片配音想让人开口，结果 Wan 2.7 根本不看图，纯按文字生成人脸。照片要动走 HappyHorse；对口型 = 文字造人 + 你的音频。
- user: 短视频编导, category: 注意, comment: 音频多长 duration 就填多少。我 8 秒配音却选了 15 秒，后 7 秒全是无声空镜，白烧一次额度。
- user: 出海产品运营, category: 妙用, comment: 本地化批产：prompt 和 seed 锁死不动，只换 audio_url，英日西三版口型不同、画面一致，落地页视频一晚出齐。
- user: 人像摄影师, category: 坑, comment: HappyHorse 输出画幅 = 输入图，不自动裁切。想要 16:9 横版，先在本地把图裁好再传；另外原图超 10MB 直接被拒。
- user: 后端老兵, category: 坑, comment: 我把 69 当限流连着重试，其实 69 是上游故障该停下；75（超时/429）才值得重试，77 是没登录。CI 里别 login，直接设 RUNCOMFY_TOKEN。
- user: 电商详情页设计师, category: 启发, comment: 以前总把照片内容写进 prompt，动效很平。现在只写要动的："缓慢 dolly in，rim light 渐亮"，一镜一动作，长镜头拆成 5 秒段再剪，稳多了。
