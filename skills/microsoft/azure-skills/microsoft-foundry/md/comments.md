# microsoft-foundry (`microsoft/azure-skills/microsoft-foundry`)

## comments

- user: 第一次用的新手, category: 坑, comment: 第一句就说清是新建还是改现有 agent。我没说,它默认走了从零搭建的快速流程,差点覆盖我的旧代码。
- user: 后端老兵, category: 妙用, comment: 我把线上 trace 喂给它攒成回归数据集,之后每次改 prompt 前先跑一遍评测,坏改动当场现形,不用等用户来骂。
- user: 运维老哥, category: 注意, comment: 部署报容量不足别急着重试,先让它查配额和各区域余量,该换区域就换,盲目重试纯属白烧时间。
- user: 全栈独立开发, category: 坑, comment: 我手贱把 endpoint、镜像地址手动抄进 .foundry/agent-metadata.yaml,两处不一致排查半天。azd 环境变量才是事实来源。
- user: 算法工程师, category: 妙用, comment: 微调前的 grader 校准别跳过。我先用几十条人工标注对齐评分标准,训完的评估才可信,不然分数虚高。
- user: AI 产品经理, category: 注意, comment: 让它优化提示词,它是先跑评测再改,不是拍脑袋改文案。提前备几条典型问答当测试集,前后对比才有依据。
