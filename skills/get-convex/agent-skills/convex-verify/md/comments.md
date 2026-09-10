# convex-verify (`get-convex/agent-skills/convex-verify`)

## comments

- user: 第一次用的新手, category: 坑, comment: 没写 vitest.config.ts 直接跑就报 import.meta.glob is not a function。environment 要设 edge-runtime,convex-test 加进 deps.inline,还得装 @edge-runtime/vm,三样缺一不可。
- user: 后端老兵, category: 妙用, comment: 我让它优先用项目自己的 mutation 灌种子数据,等于顺手把入参校验也跑了一遍,比 ctx.db.insert 直插的假数据测得更真,一次顶两次。
- user: 前端转全栈, category: 注意, comment: 模拟多用户时 withIdentity 里的 subject/tokenIdentifier 必须和线上鉴权读的字段一致。我之前用了自造的形状,归属判断永远不匹配,白白排查半天以为代码有 bug。
- user: 赶工期的外包, category: 坑, comment: 急着交付,我想删掉"别人被拒绝"那条断言让测试变绿,被拦下了——后来一查,那个接口真在漏权限。记住:有问题改函数,别改测试,测试改绿了什么也证明不了。
- user: 独立开发者, category: 妙用, comment: 最值钱的是它会断言"别人的行不在我的返回列表里"。我以前只测自己能查到,从没发现列表接口把全站数据吐给了每个登录用户。
- user: 小团队技术负责人, category: 注意, comment: 它只验证你已经写好的那几个具体函数,想从零搭测试框架不是它的活,需求别提错。另外全程进程内跑不用部署,验证一轮挺快,可以当发布前例行检查。
