# convex-authz (`get-convex/agent-skills/convex-authz`)

## whitebox

- 先验地基: 检查 auth.config.ts (带 provider) 和以 subject 为键的 users 表是否同时存在; 缺一则不注入 ctx.auth 类校验 (必空转), 只把暴露的特权函数降级为 internalQuery/internalMutation 并提示先搭 auth
- 确定性扫描: 对 convex/**/*.ts (跳过 _generated 和 .d.ts) 跑 4 条 regex, 找出 身份来自参数 / 缺属主校验 / 公开查询按客户端 id 泄漏 PII / 写入时未验父容器属主 四种形态的全部命中, 记录文件+行号+形态
- 逐点加固: 新增/复用 convex/model/auth.ts 导出 requireIdentity(ctx) 与 requireOwner(ctx, doc), 把客户端身份参数换成 ctx.auth, 每处按 _id 的读改先过 requireOwner, 形态 d 先验父文档属主或 membership 再插入子行
- 双重验证: 运行 npx tsc --noEmit 确认类型通过, 再重跑第 2 步扫描确认 0 残留命中 (已修函数因块内出现 ctx.auth 和属主比较而不再命中)
- 按 4 形态分组输出报告: file:line + 谁能冒充谁/读谁的数据 + 具体 diff (不写散文描述)

- 客观优先的两段式解析: 先用 4 条确定性 regex 产出与模型无关的基线 (词边界匹配 args 块里的 v.id(...) 参数, 配对检查整个函数块内是否出现 ctx.auth / 属主比较), 之后才允许 LLM 判断; 禁止跳过扫描直接靠直觉
- 模板化修补而非自由发挥: 逐字复用 convex-expert.md 的规范修复模式, 不自造平行 helper; 关键陷阱内置 —— identity.subject 与 Id<"users"> 字段直接比较永不命中, 须先按 subject 索引解析出 users 行再用 user._id 比较; 内部函数永不放宽为公开
- 外部依赖极简: 只用本地 grep/regex 与 TypeScript 编译器 (npx tsc --noEmit) 做校验, 不调用任何外部模型 API; typecheck 不过即视为未完成
