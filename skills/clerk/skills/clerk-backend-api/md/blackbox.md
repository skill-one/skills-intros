# clerk-backend-api (`clerk/skills/clerk-backend-api`)

## blackbox

**function**: 我是你的 Clerk 用户管理助手: 你用一句话下指令, 我帮你直接完成查用户、建组织、发邀请、改资料这类后台操作, 并把结果整理给你看。

- input: 「列出最近 7 天注册的所有用户」, output: 一份清晰的名单: 每位用户的 ID + 邮箱, 以及总人数
- input: 「创建一个叫 Acme 的组织, 并邀请 bob@acme.com 当管理员」, output: 组织创建成功的确认信息 + 已向该邮箱发出的邀请详情
- input: 「把 user_abc 的会员等级改成 pro」, output: 更新完成的确认, 显示该用户当前保存的资料状态
- input: 「删除用户 user_abc」, output: 先收到一份「删了就找不回来」的数据清单等你确认, 确认后才返回删除成功的回执
