# extension-email-marketing (`caffeinelabs/skills/extension-email-marketing`)

## comments

- user: 独立开发者, category: 坑, comment: 我图省事把订阅状态也存进了用户档案,用户退订后两边状态打架。后来只信 subscribers 模块这一处数据源,才根治。
- user: 前端转全栈的新手, category: 注意, comment: 订阅和邮箱验证是两道独立的门:用户订阅了但没点验证邮件,群发时 verified() 为空,报"无已验证订阅者"。先接好验证扩展。
- user: 后端老兵, category: 妙用, comment: addTopic 对重名是幂等的,已存在就直接返回原 ID。我把初始化主题放进启动逻辑,省掉了先查再建的判断代码。
- user: 社群站长兼运营, category: 妙用, comment: substitutions 不只能替换名字:我按订阅者所在城市替换成当地活动信息,一套模板群发,每人看到的内容都"量身定制"。
- user: 负责版本升级的维护者, category: 坑, comment: 升级迁移时我引用了 newsletterTopic 变量,但它是 transient 的,上线后主题丢失、订阅报错。迁移文件里必须把 "Newsletter" 字面量重写一遍。
- user: 合规敏感的产品经理, category: 注意, comment: 营销邮件必须带退订链接:漏了 {{UNSUBSCRIBE_URL}} 时示例代码会自动补在末尾,但位置不可控,建议模板里自己放好,过合规审查也顺。
