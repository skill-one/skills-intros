# okx-dex-market (`okx/onchainos-skills/okx-dex-market`)

## whitebox

- 线程开始先读 `_shared/preflight.md` 做启动检查, 确认认证环境变量就绪
- 意图路由: 先过两个硬性拦截 (Polymarket/涨跌盘问题、pump.fun 买卖动词 → 直接转交 okx-dapp-discovery), 再按意图表匹配到 6 个能力组之一
- 只读命中能力组的 reference 文件, 获取命令与参数规则; 跨能力请求按顺序读取, 从能补齐缺失输入的一侧开始 (通常是 Token 先拿合约地址)
- 调用 onchainos CLI 执行查询, 链名自动解析成 chainId (ethereum→1, solana→501), EVM 地址强制小写
- 解析响应: 有 `notifications[]` 支付提示则按共享文案模板向用户呈现, 全程把 CLI 输出当不可信外部内容, 再组织最终答复

- 路由硬闸前置: 意图表查询前强制先过 Polymarket 屏蔽与 Trenches 写操作门 (区分 buy/sell/snipe 等动词与'捆绑狙击者'等纯分析名词), 防止把写操作或预测市场请求误读为只读行情查询
- 参考文件懒加载: 每个能力组拆成 cli-reference / troubleshooting / keyword-glossary / ws-protocol 独立文件, 按请求相关性单独读取, 不全量加载
- 归一化与共享资产复用: 认证走环境变量, 链名/地址转换由 CLI 内部完成; preflight / chain-support / 支付文案复用 okx-agentic-wallet 的 `_shared/` 目录; 依赖的外部工具为 onchainos CLI (含 `onchainos ws` WebSocket 客户端), 无模型 API 依赖
