# connector-googlemail (`caffeinelabs/skills/connector-googlemail`)

## blackbox

**function**: 给应用加上「用用户自己的 Gmail 发邮件」的功能: 用户在应用里授权一次 Google 账号, 之后应用就能替他发邮件 (如通知、报表、验证码)。

- input: 需求描述:「做一个待办清单应用, 每天早上把今日任务发到用户自己的 Gmail」, output: 可用的应用: 用户点「连接 Gmail」授权后, 每天在自己的 Gmail 收件箱收到今日任务邮件
- input: 需求描述:「应用里要有个按钮, 把周报表用邮件发给用户」, output: 应用里出现「连接邮箱」和「发送报表」功能, 用户确认后报表邮件以其本人 Gmail 地址发出
- input: 需求描述:「让用户能用 Gmail 把反馈直接发给支持团队邮箱」, output: 用户在应用里完成一次 Google 授权, 即可用自己的 Gmail 地址发出反馈, 无需手动复制粘贴邮件内容
