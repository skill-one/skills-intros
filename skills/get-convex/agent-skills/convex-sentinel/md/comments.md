# convex-sentinel (`get-convex/agent-skills/convex-sentinel`)

## comments

- user: 第一次用的新手, category: 坑, comment: 装完等了两天没数据——抓 PROD 错误必须先把应用部署到云端,本地 dev 抓不到。先部署,再看错误表。
- user: 后端老兵, category: 妙用, comment: 本来只想抓 500,结果 OCC(并发写冲突)信号也进了表,发现我们高峰期写冲突比想象多,顺手改了表设计。
- user: 独立开发者, category: 注意, comment: 别指望在错误表里翻原文:脱敏是写入时强制的,像密钥的字段名和值默认全打码。要看细节得回本地复现。
- user: 小团队 CTO, category: 妙用, comment: 没自建报错看板:CLI 直接查最近错误,再挂 prod_error 事件做自己想要的反应。数据全程不出自己部署,过合规很省事。
- user: 运维老哥, category: 注意, comment: 上线第一天接口雪崩,同一报错刷爆错误表。记得设采样和上限控制量,不然存储和成本都难看。
- user: 全栈创业者, category: 启发, comment: 开了自愈任务后,反复出现的报错自动分诊、交给 AI 开修复 PR。我反思:以前每周手动过错误列表,纯属浪费半天。
