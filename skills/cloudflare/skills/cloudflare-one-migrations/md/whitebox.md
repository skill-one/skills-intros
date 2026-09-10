# cloudflare-one-migrations (`cloudflare/skills/cloudflare-one-migrations`)

## whitebox

- 识别源栈 (Zscaler ZIA/ZPA、Palo Alto、传统 VPN/SWG), 先索要结构化导出文件和日志, 拒绝用截图或口头描述代替
- 解析导出, 建立清单: 身份、组、应用、隧道/连接器、DNS/URL/防火墙/DLP 策略、对象与列表、命中计数等
- 逐条产出映射表: 源对象 → Cloudflare One 目标资源, 标注置信度、前置依赖、部分支持/不支持项
- 按依赖顺序建资源 (身份/SCIM → 连接器/隧道 → 列表 → TLS 绕过 → Access/Gateway 策略 → DLP → 日志), 全部加迁移前缀、默认禁用/审计模式, 小范围试点并比对日志
- 验证闸门: Cloudflare 对象数 vs 解析出的源对象数, 不符即停; 每条源规则必须映射成功或明确列入 Not Migrated (含原因和安全影响), 最终输出账目表

- 解析: 以结构化导出为输入, 引用跨文件拆分时先拿对象/服务/组文件解析 ID 再判定规则不可映射——依赖源厂商导出文档 (Zscaler ZIA URL/防火墙/SSL/DLP/位置/GRE 导出清单, ZPA app segments/connectors/policies, Palo Alto 规则+对象+hit counts)
- 转换: 按启发式映射——ZIA/SWG 策略→Gateway 流量策略+列表; ZPA 私有应用→Access 应用+Cloudflare Tunnel+私有 DNS+Access 策略; Palo Alto 保留规则意图而非条数 (一条规则可拆多个资源); 无精确等价物 (CAUTION/warn、App-ID、TLS 例外) 一律标记为决策点而非强行映射。生成精确配置前先实时检索 Cloudflare 文档与 API schema
- 校验: 每阶段跑 Validation Gates——数量核对不符即停; unsupported/partial/needs_identity/needs_posture 等条目启用前逐条人工评审; SCIM 同步后用真实试点用户验证组匹配; 先测 TLS 检查与 Do Not Inspect 再开拦截; 保留显式回滚路径 (按前缀禁用规则、恢复源路由)
