# baoyu-post-to-wechat (`jimliu/baoyu-skills/baoyu-post-to-wechat`)

## comments

- user: 第一次发公众号的新手, category: 坑, comment: 我自己先把 md 转成 HTML 再发，图片全挂了。直接丢 md 文件就行，它内部会转换，别多此一举。
- user: 公众号运营, category: 注意, comment: 它只帮你存进草稿箱，不会自动发布，发完要去 mp.weixin.qq.com 手动点。API 方式记得备好封面图，不然中途会停下来找你要。
- user: 有云服务器的后端, category: 妙用, comment: 本机 IP 不在白名单直接报 40164。改用 remote-api 走云服务器出口，排版和上传都在本地，AppSecret 也不出本机。
- user: 兼管两个号的新媒体, category: 妙用, comment: EXTEND.md 里配 accounts 块，两个号各有凭据和浏览器配置，发的时候加 --account 别名就切号，不用反复扫码登录。
- user: 远程跑脚本的运维老哥, category: 注意, comment: 在服务器上跑没有界面，扫码很尴尬。配上 TELEGRAM_BOT_TOKEN 和 CHAT_ID，二维码直接推到手机，扫一下就好。
- user: 自媒体作者, category: 启发, comment: 现在只写纯文本丢给它，标题摘要自动生成，还按日期存成 md 当存档。写作和排版分开后，我反而更愿意日更了。
