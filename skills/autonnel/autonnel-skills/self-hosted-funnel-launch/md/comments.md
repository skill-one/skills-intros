# self-hosted-funnel-launch (`autonnel/autonnel-skills/self-hosted-funnel-launch`)

## comments

- user: 第一次自建的新手, category: 坑, comment: Workers 免费版连改一下午页面,发布十几次就报错,以为部署坏了——其实是 KV 每天只有 1000 次写入,发布一次刷一次缓存。定稿再发布。
- user: 写自动化脚本的 Python 党, category: 坑, comment: 用 urllib 调 MCP 连 health 检查都 403(error code: 1010),以为是 key 错了折腾半天——是 Cloudflare 封 Python-urllib 这个 UA,换 httpx 立通。
- user: 一人独立开发者, category: 妙用, comment: 建页试错全在本地 Docker 跑,后台和 schema 跟 Workers 部署完全一样,迁上去零返工;落地页静态请求免费,只有下单和接口计费。
- user: 投放运营, category: 注意, comment: 广告里别填 /n/ 开头的链接,那是前向跳转,换页就断流;要填落地页自己的 slug。error 页没绑好的话,拒付时买家直接白屏。
- user: 给 agent 写调用层的后端老兵, category: 坑, comment: 缺写权限的调用照样返回 HTTP 200,错误藏在 result.isError 里,我的脚本带着失败结果一路跑完。先判 isError 再读内容,别拿状态码当真相。
- user: 非技术出身的网店店主, category: 启发, comment: 最戳我的是那句:没真实跑过一单的 funnel,失败率是"未知"不是"低"。现在每次上线前我固定走一遍:下单、接受 upsell、拒付一次、退款。
