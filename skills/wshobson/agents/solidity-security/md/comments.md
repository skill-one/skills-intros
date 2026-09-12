# solidity-security (`wshobson/agents/solidity-security`)

## comments

- user: 转行写合约的后端, category: 妙用, comment: 写完提款函数, 让它照模板写个重入攻击合约来打我自己的合约, 看到攻击被 revert 才敢上. 比肉眼查代码靠谱.
- user: 第一次跑 Hardhat 的新手, category: 坑, comment: 直接把示例测试粘进项目就跑, 报错找不到 hardhat 包. 得先初始化 Hardhat、装好 ethers 和 chai, 合约名也要改成自己项目的.
- user: 准备上主网的创始人, category: 注意, comment: 照它准备好文档和测试, 只算审计前准备, 不等于审计. 主网上线前审计费省不掉, 但把写好的注释文档交给审计方, 沟通快很多.
- user: 写测试的 QA, category: 坑, comment: 我断言只写 to.be.reverted, 结果合约因为别的原因挂了测试也"绿", 假安全感. 后来每条都补上具体报错文案, 才真的测到了目标漏洞.
- user: 黑客松常客, category: 妙用, comment: 审计准备那段每个函数的 @notice/@dev 注释模板, 我套在参赛项目里, 队友和评委看注释就懂逻辑, 答辩省了一半解释成本.
- user: DeFi 协议开发者, category: 启发, comment: CEI 顺序(先检查、先改账本、最后才调用外部合约)以前我随手写, 现在写任何对外转账函数都先过这三步, 这个习惯带动了整个团队.
