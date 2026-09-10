# convex-migrate (`get-convex/agent-skills/convex-migrate`)

## whitebox

- 第一步: 把新字段设为 optional 并先部署, 让现有数据不被校验拒绝。
- 第二步: 安装 @convex-dev/migrations, 编写回填迁移, 把旧行转换/补齐为新 schema 下的有效数据。
- 第三步: 运行迁移, 核对前后行数并确认所有行均有效。
- 第四步: 回填完成后收紧 validator (字段改为 required), 完成收尾部署。

- 外部依赖: Convex 平台 + @convex-dev/migrations 库, 负责对已部署应用执行批量数据回填/转换。
- 两阶段 validator 策略 (核心安全机制): 先 optional 后 required, 严格禁止在回填完成前收紧校验, 否则旧数据会被校验拒绝、直接弄崩线上应用。
- 验证机制: 迁移前后核对行数, 并确认所有行通过新 schema 校验后才进入收紧阶段。
