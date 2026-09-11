# extension-email-raw (`caffeinelabs/skills/extension-email-raw`)

## whitebox

- 调用方传入 fromUsername、三组收件人列表 (to/cc/bcc)、subject 和 htmlBody，调用 sendRawEmail
- 底层经由依赖的 extension-email (mo:caffeineai-email/emailClient) 把同一封邮件发送给全部收件人
- 等待并收到 SendResult
- 匹配到 #ok 则正常结束 (示例代码中该分支为空, 无额外动作)

- 单次同文投递: to + cc + bcc 收到的都是完全相同的 htmlBody, 总收件人上限 50, 无逐人个性化——也因此不适合收件人互可见的批量服务邮件
- 结果校验: 返回 SendResult (#ok | #err(Text)), 错误分支用 mo:core/Runtime 的 Runtime.trap(error 文本) 直接中断
- 外部依赖: mops 包 caffeineai-email ~0.2.0 (提供 emailClient), 自身依赖 extension-email 完成实际发送; 需 Caffeine AI plus/pro 订阅
