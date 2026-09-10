# convex-verify (`get-convex/agent-skills/convex-verify`)

## whitebox

- ① 锁定目标: 确认要证明的具体 Convex query/mutation 及其行为契约 (谁能访问、返回什么数据); 意图不明则只问一个聚焦的问题。
- ② 环境准备: 确保 convex-test + vitest 为开发依赖, 写好 vitest.config.ts (edge-runtime 环境 + convex-test 内联 + @edge-runtime/vm), 拿到 convexTest(schema) 的 `t` 句柄; 复用项目已有测试设置。
- ③ 播种数据: 优先走应用自身的函数 (让 seed 经历真实的校验/写入路径), 种下「调用者自己的行」+「第二个用户的行」; 公开 API 建不了的夹具才用 t.run(ctx.db.insert)。
- ④ 多身份驱动: 用 t.withIdentity 依次以 (a) 合法 owner (b) 另一个用户 (c) 未认证 三种身份调用同一函数。
- ⑤ 断言并报告: 断言正面结果 (拿到该拿的行/变更) + 负面结果 (他人被拒、未认证被拒、列表只含自己的行), 跑 npx vitest run, 汇报通过与失败项。

- 进程内执行, 免部署: 依赖 convex-test + vitest, 且 vitest.config.ts 必须设 test.environment: 'edge-runtime' 并把 convex-test 加进 server.deps.inline, 否则运行时直接报 import.meta.glob is not a function (已验证过); 另需 @edge-runtime/vm。
- 身份模拟实现权限测试: t.withIdentity({ subject, tokenIdentifier, ... }) 用应用真实的身份形状, 让同一函数被 owner/他人/未认证 三种调用者驱动, 从而可断言鉴权拒绝与 data-scope (他人的行必须缺席)。
- 负面断言为承重墙, 结果外发: 每次验证必须含至少一条「应被拒者被拒」的断言 (rejects.toThrow(/forbidden|not authorized|403/)); 失败的负面断言 = 真实 authz/正确性缺陷, 按 specs/finding.schema.json 发 bus finding (证据为具体失败的探针调用), 修的是函数不是测试 — 绝不为了变绿而弱化断言。
