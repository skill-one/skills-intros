# connector-googlemail (`caffeinelabs/skills/connector-googlemail`)

## comments

- user: 第一次接 Google 登录的新手, category: 坑, comment: 一开始用 getProfile 拿邮箱地址, 结果 403 说 scope 不足。改成 OAuth.getUserEmail, 只申请 openid email 就通了。
- user: 后端老兵, category: 注意, comment: 回调地址必须和 Google 后台登记的一字不差, 测试域名和正式域名要分别注册, 我漏登记一个就报 redirect_uri_mismatch。
- user: 也接过 X 登录的独立开发者, category: 妙用, comment: 接过 X 的登录, 那边 refresh_token 会轮换得存新的; Google 不轮换, 刷新后只更新 access_token, 逻辑一下简单了一半。
- user: 运维老哥, category: 坑, comment: 试过没关 is_replicated, 一次发信每个节点都带着 token 出站, cycles 翻了好几倍。务必显式设 false, 安全又省钱。
- user: 前端出身第一次玩 canister, category: 注意, comment: 装完就点连接, 一直报 Gmail is not configured, 排查半天才发现要先让管理员在设置页填好 Client ID 和 Secret。
- user: 做站内通知功能的 solo 产品人, category: 妙用, comment: 我的场景只是发通知, 就只申请 openid email + gmail.send, 授权页只有两项用户秒点同意; readonly 等真要读信再加。
