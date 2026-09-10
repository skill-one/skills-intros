# security-requirement-extraction (`wshobson/agents/security-requirement-extraction`)

## comments

- user: 第一次写安全需求的后端新人, category: 坑, comment: 我写「系统必须安全」被评审打回:无法验收。改成「登录失败 5 次锁定 15 分钟,可脚本验证」当场过。空话需求等于没写。
- user: 安全团队负责人, category: 妙用, comment: 我让每条需求都挂上对应威胁编号再拿去要预算,老板质疑时直接翻溯源表指着那条攻击路径说事,一次过审。
- user: B 端产品经理, category: 注意, comment: 它是从你给的威胁分析和业务背景里提炼,不是凭空造需求。我先没给上下文,输出全是套话;补了「支付场景含用户隐私数据」才落地。
- user: 测试工程师, category: 妙用, comment: 每条需求自带验收标准,比如「AES-256 加密且密钥轮换」,我直接转成测试用例,开发没法含糊一句「做了安全」糊弄过去。
- user: 合规专员, category: 注意, comment: 合规映射要趁早。我测评前一个月才补,返工一轮;现在需求一产出就同步对到框架条款,审计时条条有出处。
- user: 创业公司 CTO, category: 启发, comment: 三层结构(业务→安全需求→技术措施)让我发现安全能像普通功能一样拆需求、排优先级进迭代,而不是上线前喊口号。
