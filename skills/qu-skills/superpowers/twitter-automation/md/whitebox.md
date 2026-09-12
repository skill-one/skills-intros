# twitter-automation (`qu-skills/superpowers/twitter-automation`)

## whitebox

- 接到 Twitter/X 任务 (发帖/点赞/转发/DM/关注等), 匹配到对应的 x/* app ID
- 按该 app 的字段规范构造 JSON 输入 (如 {"text": ...}、{"tweet_id": ...}、{"username": ...})
- 通过 Bash 执行 `belt app run <app-id> --input '<json>'`
- belt CLI 调用 inference.sh 平台, 由平台完成对 X 的实际操作
- 读取命令输出, 向用户确认结果

- App 调度: 固定一组 app ID (x/post-tweet, x/post-create, x/post-like, x/post-retweet, x/post-delete, x/post-get, x/dm-send, x/user-follow, x/user-get), 任务类型决定调用哪个
- 输入即 JSON: 全部参数经 --input 传 JSON; 带媒体发帖用 media_url 字段; 复杂输入可先用 `belt app sample` 生成模板再编辑
- 外部依赖: inference.sh CLI (belt) + 账号授权 (`belt login`); 媒体可由 falai/flux-dev-lora (图片) 或 google/veo-3-1-fast (视频) 生成, 取返回的 URL 传入 x/post-create
