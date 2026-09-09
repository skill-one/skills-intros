# azure-cloud-migrate (`microsoft/azure-skills/azure-cloud-migrate`)

## comments

- user: 后端老兵, category: 妙用, comment: 本想跳过评估直接转代码,报告却揪出代码里写死的内部域名(order-service:3001),这在 Container Apps 根本不通,等于提前排了一颗雷。
- user: 第一次用的新手, category: 坑, comment: 以为跑完就自动上 Azure,结果它停在"本地测试还是部署"问我。部署是另一段交给 azure-prepare 的,先知道这个,免得干等。
- user: 运维老哥, category: 注意, comment: 动手前先对场景表:Lambda/Beanstalk/Heroku/Cloud Run 等有专门流程,不在名单里的它会退回通用文档,方案没那么细。
- user: 创业公司 CTO, category: 妙用, comment: 源码目录一根手指都不碰,所有产出进"项目名-azure/"新目录。我把两目录 diff 逐文件审,代码评审体验比想象中省心。
- user: 全栈自由职业者, category: 注意, comment: 评估报告一定先出,别催它直接改代码。我照报告先把便宜的风险修掉,再让转换跑,返工少了一半不止。
- user: Java 团队负责人, category: 启发, comment: 评估完发现一半工作量是环境变量和配置而非代码,我原先的工期估算全错。以后接迁移单,先评估再报价。
