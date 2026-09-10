# solana-dev (`solana-foundation/solana-dev-skill/solana-dev`)

## comments

- user: 链上数据分析师, category: 妙用, comment: 只想查个钱包余额、追一笔交易, 它直接给了一条公共 RPC 的 curl, 十秒出结果, 根本不用搭项目。拉老交易它还主动带 version 参数, 我以前老栽在这儿。
- user: 第一次写 Solana 合约的新手, category: 坑, comment: 我图省事想让它直接发主网交易, 被拒: 只走 devnet, 必须先模拟再让我签名。别嫌烦——模拟真拦下过我的账户配置错误, 要动主网得自己明确确认。
- user: 维护老项目的前端, category: 注意, comment: 项目还是老版 web3.js, 它不肯往旧代码里直接塞新写法, 一律导向官方迁移方案, 还要把旧类型圈进适配层。赶工期的话先声明只加功能, 免得被顺手重构。
- user: Rust 合约工程师, category: 妙用, comment: 以前集成测试要写一串充值转账的前置交易; 现在用 Surfpool 的 cheatcode 一行改余额、改代币状态, 还能时间穿越模拟预言机。让它搭测试状态, 用例干净一大截。
- user: 运维老哥, category: 注意, comment: 开工前它先对环境: Node 要 20.18+, 还要 Rust 和 Solana/Anchor CLI。我们 CI 里 Node 偏旧, 它坚持先升级——那些 GLIBC 报错基本都是版本不匹配, 先备好工具链。
- user: 交易机器人作者, category: 启发, comment: 它把链上读回的数据全当不可信输入: 反序列化前先验账户归属, memo 里出现指令一律无视。点醒了我——我的机器人一直把 memo 原样写日志, 那里面能藏注入内容。
