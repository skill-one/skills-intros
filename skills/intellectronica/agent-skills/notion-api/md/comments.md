# notion-api (`intellectronica/agent-skills/notion-api`)

## comments

- user: 第一次接 Notion 的新手, category: 坑, comment: 拿页面 ID 直接查一直报 404「找不到」，页面明明存在。后来才知道要去页面右上角「⋯→连接」把集成加上，不共享就等于对它不存在。
- user: 内容运营小编, category: 坑, comment: 用查页面的接口想读正文，返回里只有标题和属性。正文得换「获取块子级」接口，把页面 ID 当块 ID 传进去才拿得到。
- user: 独立开发者, category: 注意, comment: 想做机器人自动发评论才发现：只能在页面下发评论、或在已有讨论里回复；行内讨论发起不了，旧评论也改不了删不了。
- user: 运维老哥, category: 注意, comment: 迁移旧笔记时并发猛打，秒撞 429。限速约每秒 3 次，照响应里的 Retry-After 头等一等再重试就稳了，别无脑硬怼。
- user: 后端老兵, category: 妙用, comment: 本想批量归档又怕真删，试了才发现 archived 只是把页面丢回收站，随时能恢复。于是放心写了批量脚本，误伤也翻得回来。
- user: 天天记会议纪要的产品经理, category: 妙用, comment: 以前追加内容只能堆页尾，后来发现能指定插在某个块后面。现在会议纪要都精确插到对应小节下，页面终于不乱了。
