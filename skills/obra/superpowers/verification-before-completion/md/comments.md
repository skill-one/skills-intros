# verification-before-completion (`obra/superpowers/verification-before-completion`)

## comments

- user: 后端老兵, category: 妙用, comment: AI 子代理说"已修复"不算数。我验收前先 git diff 看实际改动,抓过两次它根本没碰那个文件。
- user: 第一次用的新手, category: 坑, comment: 改完代码自己读一遍就说"应该能过",CI 直接红了。现在必须先跑测试,看到 0 failures 才回话。
- user: 运维老哥, category: 注意, comment: lint 全绿≠构建通过,我 lint 过了就部署,结果编译挂。测试、构建、部署各有各的验证命令,别拿 A 的证据撑 B。
- user: 测试工程师, category: 妙用, comment: 回归测试我会先故意撤掉修复跑一次,必须见它失败,再恢复验证通过。靠这招抓出一个永远通过的摆设测试。
- user: 接活的自由职业者, category: 坑, comment: 深夜赶工最容易"就这次不跑了",第二天客户打开页面就报错。现在把验证命令写进交付清单,累了照着执行。
- user: 刚带团队的技术组长, category: 启发, comment: 汇报从"搞定了"改成带证据:"34/34 通过,exit 0"。组里为到底完没完的扯皮明显少了。
