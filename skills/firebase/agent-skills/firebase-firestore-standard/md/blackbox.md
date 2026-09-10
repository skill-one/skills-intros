# firebase-firestore-standard (`firebase/agent-skills/firebase-firestore-standard`)

## blackbox

**function**: 帮你从零开通 Google 云端数据库 Firestore 并安全地用起来: 建库、写数据保护规则、在网页代码里存取数据、排查查询报错。

- input: 「我刚注册了 Firebase 项目, 帮我开通一个 Firestore 数据库存 App 数据」, output: 数据库开通完成, 项目里能直接存数据了, 并附上接下来要做的一两步操作说明
- input: 一段需求描述, 如「用户只能看和改自己的笔记, 不能碰别人的」, output: 一份可直接部署的安全规则代码, 贴上去别人的数据就动不了
- input: 「网页里怎么把用户填的留言保存起来, 还能显示所有留言?」, output: 可直接复制运行的网页 JavaScript 代码: 保存留言 + 读取留言列表
- input: 一段报错文本, 如「查询报错: The query requires an index」, output: 指出缺了哪种索引, 并给出一条可直接执行的创建索引命令
