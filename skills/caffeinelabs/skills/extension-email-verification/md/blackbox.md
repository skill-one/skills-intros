# extension-email-verification (`caffeinelabs/skills/extension-email-verification`)

## blackbox

**function**: 给用户发送一封含「点击验证」链接的邮件，对方点开后邮箱即被确认为真实有效，你可以随时查询任意邮箱是否已通过验证。

- input: 用户注册时填写的邮箱地址（如 zhang@example.com）和一封欢迎邮件的内容, output: 该邮箱收到一封邮件，内含一个「点击此处验证邮箱」的链接
- input: 用户点击了邮件里的验证链接, output: 系统确认这是本人操作，该邮箱被标记为「已验证」，用户看到验证成功
- input: 一个查询：某个邮箱（如 zhang@example.com）验证过了吗？, output: 一个明确的答复：是（已验证）或 否（未验证）
