# twitter-automation (`101-skills/superpowers/twitter-automation`)

## whitebox

- 接收 Twitter/X 任务（发帖/点赞/转发/DM/关注等），映射到对应 app: x/post-tweet, x/post-like, x/dm-send, x/user-follow 等
- 把参数序列化为 JSON, 拼成 belt app run <app-id> --input '{...}' 命令
- 通过唯一的允许工具 Bash 执行该命令
- belt CLI (已通过 belt login 认证) 调用 inference.sh, 由其 X 集成代为执行操作
- 解析返回的 JSON 结果 (tweet_id, 用户资料等), 汇报给用户

- 所有操作收敛到单一入口 Bash(belt *), 即 inference.sh 的 belt CLI; 我不直连 Twitter API
- 输入/输出均为 JSON: 参数经 --input 传入, 从响应中提取 tweet_id / media_url 等字段供后续步骤使用
- 跨 app 链式组合: AI 生成类 app (falai/flux-dev-lora 生图, google/veo-3-1-fast 生视频) 输出的媒体 URL 直接作为 media_url 喂给 x/post-create 发布带媒体内容
