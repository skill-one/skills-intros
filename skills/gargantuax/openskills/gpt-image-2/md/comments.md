# gpt-image-2 (`gargantuax/openskills/gpt-image-2`)

## comments

- user: 后端老兵, category: 妙用, comment: 发正式请求前先跑 --dry-run, 不花钱就能看到最终请求体。我靠它提前抓到 size 写错和参数组合冲突, 省了一堆重试。
- user: 第一次用的新手, category: 坑, comment: 我想边流式预览边出 3 张图, 直接报错。后来才明白公共 Images 路由 stream=true 和 n>1 不能同时开, 只能二选一。
- user: 运维老哥, category: 注意, comment: 配置优先级是 CLI > 环境变量 > .env。我在 CI 里环境变量 OPENAI_BASE_URL 指着测试网关, 一直覆盖 .env 里的正式地址, 排查了半天。
- user: AI 应用开发, category: 妙用, comment: responses 加 --stream --partial-images 2, 再 --save-response 存事件流, 图没出完就能看到局部预览, 用来跟产品对构图方向特别省时间。
- user: 独立设计师, category: 坑, comment: 想出透明底 logo, 结果直接被校验拦下。尺寸也不是随便填的, 换成 1536x1024 这类受支持的值才过。不支持的组合在发送前就会被拒。
- user: 自建网关用户, category: 注意, comment: responses 默认文本模型是 gpt-5.4, 我的自建网关没部署它, 一直报模型不存在; --model 换成网关里有的文本模型才通, 别只盯着图片模型调。
