# twitter-automation (`101-skills/superpowers/twitter-automation`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我直接把对方用户名填进 recipient_id 发私信，一直报错。后来先跑 x/user-get 拿到用户 id 再传进去，一次就通。
- user: 自媒体内容创作者, category: 注意, comment: media_url 只认公网能访问的链接，我填本地图片路径，发出去的推文没图。直接用图床或生成服务返回的 URL 最稳。
- user: 运维老哥, category: 注意, comment: app 列表里没有现成的定时发布，我用 crontab 定时跑 belt 命令实现的。另外服务器上先确认 belt login 已生效再挂任务。
- user: 社群运营, category: 妙用, comment: 我现在发完推顺手用 x/post-get 核对内容真发出去了，发现发错就用 x/post-delete 秒删，不用去网页里翻找。
- user: 独立开发者, category: 妙用, comment: falai 生图拿到 URL 直接填进 x/post-create，AI 配图推文一条命令链搞定，图床都不用搭。发视频用 veo 同理。
- user: 后端转 AI 工具党, category: 启发, comment: 复杂输入我不再手拼 JSON，先 belt app sample xxx --save input.json 导出模板再改字段，shell 转义报错基本绝迹。
