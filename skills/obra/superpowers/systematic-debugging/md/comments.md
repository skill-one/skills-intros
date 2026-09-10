# systematic-debugging (`obra/superpowers/systematic-debugging`)

## comments

- user: 第一次线上值班的新手, category: 坑, comment: 我以为 bug 太简单不用走流程, 直接改了配置, 结果上线又炸. 老实复现、读完整个报错才发现是环境变量没传到子进程. 简单 bug 也有根因.
- user: 后端老兵, category: 妙用, comment: 多组件链路出问题时, 我在每层边界打印进/出的数据和配置, 跑一次就知道断在哪层, 不用层层盲猜. 比挨个试省了我半天.
- user: 运维老哥, category: 注意, comment: 连修 3 次都出新症状就停手, 别打第 4 个补丁. 我在一个服务上连改 4 版全失败, 停下来找人聊架构, 十分钟就定位到是模式本身选错了.
- user: 测试工程师, category: 妙用, comment: 我用第 4 阶段验收别人修复: 先要一个最小失败用例, 修完它变绿才算数. 挡住过一次"看日志像好了"的假修复.
- user: 刚转行做开发的新手, category: 注意, comment: 假设被证伪后千万别叠第二个改动. 我同时改了两处, 分不清哪个起效, 只能全部回滚重来. 一次只动一个变量.
- user: 技术主管, category: 启发, comment: 以前组员报 bug 我先问多久修完, 现在先要复现步骤和报错原文. 团队被逼着先查根因, "修完又坏"的返工明显少了.
