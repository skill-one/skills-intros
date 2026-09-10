# requesting-code-review (`obra/superpowers/requesting-code-review`)

## comments

- user: 独立开发者, category: 妙用, comment: 卡了两天的问题,我试了指南里「卡住时」的用法,顺手发起评审,agent 指出我需求理解就错了,十分钟解围。
- user: 第一次用的新手, category: 坑, comment: 我把需求写成「实现登录」,评审只查了代码风格,漏掉业务逻辑错误;改贴原始需求文档后,一次揪出三个问题。
- user: 后端老兵, category: 注意, comment: BASE_SHA 选错等于白审:任务跨三个提交,我只填了 HEAD~1,评审只看到最后一个。发起前先确认提交范围。
- user: Tech lead, category: 启发, comment: 评审说我的并发写法有 bug,我拿压测报告有理有据地推回,它撤回了。别盲从评审,拿证据反驳反而更快。
- user: 副业写码的产品经理, category: 坑, comment: 改动小就跳过评审,结果一个「简单」改动把缓存 key 改串了,上线才炸。它明说了:再小也别跳过。
- user: 带实习生的组长, category: 注意, comment: Important 的问题我拖到下个任务再修,错误沿依赖链传染,返工量翻倍。Critical 立刻修,Important 修完再走。
