# openapi-spec-generation (`wshobson/agents/openapi-spec-generation`)

## comments

- user: 后端老兵, category: 妙用, comment: 把重复出现的 User/Order 结构用 $ref 抽到 components 复用, 改一处全局同步, spec 文件直接短了一半。
- user: 前端转全栈, category: 坑, comment: 接口字段可能为 null 却没标 nullable, 生成的客户端按必填处理, 上线遇到空值直接崩。现在字段一律显式标可空性。
- user: 第一次用的新手, category: 注意, comment: 上手前先定好是先写 spec 还是先有代码, 我两边混着写, 最后 spec 和实现对不上, 推倒重来一遍。
- user: 技术负责人, category: 启发, comment: 需求评审直接带着 spec 过, 前后端看同一份契约文件, 口头对需求扯皮少了一大半, 变更也有据可查。
- user: 运维老哥, category: 坑, comment: server url 写死了测试环境地址, 上生产忘改查了半天。改用 server variables 按环境切换才稳定。
- user: SDK 使用者, category: 注意, comment: 生成客户端 SDK 前务必给字段补 examples, 不然注释全空, 接手的人只能翻源码猜字段含义。
