# organization-best-practices (`better-auth/skills/organization-best-practices`)

## comments

- user: 第一次用的新手, category: 坑, comment: 直接删了测试组织,成员、邀请全被级联清掉才反应过来。现在在 beforeDelete 钩子里先归档再抛错,救回过一次手滑。
- user: 全栈独立开发者, category: 注意, comment: getInvitationURL 只给你链接,不发邮件,我以为调完接口用户就能收到,干等了两天。要么配 sendInvitationEmail,要么自己把链接发出去。
- user: SaaS 后端老兵, category: 妙用, comment: 把套餐塞进组织 metadata,membershipLimit 写成函数去读它——免费版 50 人、企业版 1000 人,一处配置搞定分层。
- user: 前端开发, category: 坑, comment: 用 checkRolePermission 控制按钮显隐就当权限做完了,接口没拦,被人直接调 API 越权。它只管静态 UI,真正拦截要走 hasPermission 接口。
- user: 技术团队 Leader, category: 坑, comment: 想删自建的 moderator 角色一直报错,查了半天发现有成员还挂着它。先用 updateMemberRole 把人换到别的角色,才删得掉。
- user: 小团队技术主管, category: 注意, comment: 邀请默认 48 小时过期,我们用户爱周末集中看邮件,周一来全失效了。上线前把 invitationExpiresIn 调成 7 天,客诉归零。
