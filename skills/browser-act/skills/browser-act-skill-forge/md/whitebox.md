# browser-act-skill-forge (`browser-act/skills/browser-act-skill-forge`)

## whitebox

- 加载 browser-act 浏览器自动化工具 (Skill tool 调用)，确认 API Key 配置
- 解析需求：明确目标站点与目标数据/操作，拆解为独立能力单元，一次性向用户确认执行计划
- 探索站点：优先用流量观测 (network requests / HAR) 找内部 API 端点，API 不可行则回退 DOM 选择器，记录可复现的完整调用方式
- 生成 Skill 包：把验证过的 JS 封装成 argparse 参数化的 Python 脚本 + SKILL.md，逐脚本端到端回环验证，再做合规自检
- 交付：派发 Sub-Agent 自动化测试 → 安装 Skill → 汇报结果 → 若有执行意图则按 Skill 执行用户的原始任务 (批量任务写批处理脚本)

- 网络抓包优先的探索：靠 browser-act 的 network requests / HAR 录制发现站点前端内部 API；JS 只能在浏览器 eval 环境跑 (仅原生 API，禁止 require/import 外部模块)；用复合 eval、运行时优先等规则压缩浏览器往返次数；DOM 路径须三层选择器验证 (元素断言→结果检查→成功标准)，禁止凭空编写
- 封装与校验：验证过的 JS 片段 → 业务参数抽成 argparse 参数、固定值硬编码进 JS f-string (花括号转义 {{}}) 的 Python 脚本 → 双重回环验证：python 生成 JS 字符串 + eval 注入浏览器比对结果，并模拟错误场景确认返回 {"error": true} 而非崩溃，失败即修不可跳过
- 外部依赖与边界：依赖 browser-act 工具 (浏览器自动化 + 流量观测) 和 Python；测试必须经 Sub-Agent 执行；运行边界 = 用户已登录浏览器内手动可见的数据，不做网络层 JS 拦截、不走第三方采集服务或官方开放平台 API，所有数据留本地
