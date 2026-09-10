# organization-best-practices (`better-auth/skills/organization-best-practices`)

## whitebox

- 触发匹配: 任务落在技能描述范围内 (组织搭建/团队管理/成员角色/访问控制/Better Auth organization 插件) 才接手
- 未初始化则先走 Setup 四步: 服务端挂 organization() 插件 → 客户端挂 organizationClient() → npx auth@latest migrate (或 Drizzle/Prisma generate+push) → 核对 organization/member/invitation 三张表已建
- 按任务选章节: 建组织/setActive 切换组织/成员/邀请/角色权限/团队/hooks/schema 定制, 直接套对应代码模式
- 按上下文出代码: 服务端用 auth.api.*, 客户端用 authClient.organization.*
- 收尾附安全约束: 最后一个 owner 不可移除/退出 (先转移所有权再操作), 邀请默认 48h 过期且仅受邀邮箱可接受

- 双层 API 路由: 同一能力有两套入口 — 服务端 organization() 插件 (auth.api.*) 与客户端 organizationClient() 插件 (authClient.organization.*), 由调用场景决定走哪层; 典型分工: addMember 仅服务端, 客户端加成员必须走邀请系统
- 声明式配置 + 生命周期 hooks: 人数上限/邀请有效期/表名字段改名/附加字段全部是 organization() 的选项, 不写过程代码; 自定义逻辑注入 beforeCreate/afterCreate/beforeDelete 等钩子 (软删除即 beforeDelete 内归档后 throw 实现)
- RBAC 模型与外部依赖: 默认三角色 owner/admin/member + hasPermission 动态校验; 自定义角色需开 dynamicAccessControl (依赖 @better-auth/organization/addons); 表结构靠 npx auth@latest migrate 或 Drizzle/Prisma; 邀请邮件需用户自行提供 sendEmail 实现
