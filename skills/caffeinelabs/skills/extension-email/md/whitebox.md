# extension-email (`caffeinelabs/skills/extension-email`)

## whitebox

- 后端 (Motoko canister) 导入预制模块 mo:caffeineai-email/emailClient, 拼装发件人用户名、收件人、主题、HTML 正文
- 调用 sendServiceEmail(...), 这是一个 await 的异步调用
- 模块为 recipients 数组中的每个收件人单独发送一封邮件
- 调用返回 SendResult: 成功为 #ok, 主流程到此结束

- 核心依赖是外部预制模块 mo:caffeineai-email/emailClient.mo, 声明为不可修改 (cannot be modified), 由 mops 包 caffeineai-email (~0.2.0) 提供, 需要 Caffeine AI 的 plus/pro 订阅
- 逐收件人发送: recipients 是数组, 但每个人收到的是独立邮件, 不是群发
- 错误通过 variant 类型 SendResult 透传: #err 携带错误文本 (Text), 由调用方自行处理 — skill 示例中的做法是 Runtime.trap 中止并拼接错误信息
