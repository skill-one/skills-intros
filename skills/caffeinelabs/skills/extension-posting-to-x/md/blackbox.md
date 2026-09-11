# extension-posting-to-x (`caffeinelabs/skills/extension-posting-to-x`)

## blackbox

**function**: 给你的应用加上「连接 X (Twitter) 并发推文」的能力——每个用户授权自己的 X 账号后, 就能在你的应用里直接发推。

- input: 一句需求, 如「我想让我的应用能发推文」, output: 能发推的应用: 新用户看到「连接 X 账号」按钮, 授权后输入文字点发送, 推文就出现在他的 X 主页上
- input: 来自 X 开发者后台的 Client ID (一串公开字符), output: 配置完成的应用: 管理员设置一次, 之后所有用户都能走「登录 → 授权 → 发推」流程
- input: 具体发推场景, 如「用户完成订单后自动发一条感谢推」, output: 按场景自动发推的应用: 事件一触发, 推文自动从该用户的 X 账号发出
