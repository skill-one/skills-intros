# organization-best-practices (`better-auth/skills/organization-best-practices`)

## blackbox

**function**: 帮你在应用里搭建"组织/团队"功能: 建组织、邀成员、设角色权限、分组管理, 直接交付能跑的配置和代码。

- input: 「我想给我的 SaaS 加上组织和团队功能, 用 Better Auth」, output: 可直接粘贴的服务端 + 客户端配置代码, 外加数据库迁移命令和一份验证清单 (确认组织、成员、邀请三张表已生成)
- input: 「怎么邀请成员加入组织, 自动发邀请邮件, 7 天内有效」, output: 邀请邮件的发送配置代码 + 调用邀请接口的示例代码
- input: 「我想加一个 moderator 角色, 只能查看成员和邀请, 不能修改」, output: 创建自定义角色的代码 + 判断某用户是否有权限的检查代码
- input: 「怎么防止误删组织、防止最后一个管理员被移除」, output: 对应的保护配置代码 + 安全转移所有权后再降级/移除的操作代码
