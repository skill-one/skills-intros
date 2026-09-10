# architecture-patterns (`wshobson/agents/architecture-patterns`)

## whitebox

- 接收任务: 确认要架构的服务边界或模块 (新服务设计 / 单体拆分 / 依赖循环排查等场景)
- 选型: 按场景匹配 Clean Architecture / 六边形架构 / DDD, 确定分层与依赖方向 (只准向内)
- 产出: 输出分层结构 + 层间抽象接口 (ports) + 测试边界
- 按需加深: 主文档不够时再读 references/details.md 或 advanced-patterns.md
- 自检: 验证用例测试能用内存适配器脱离真实数据库跑通, 并按故障清单逐条核对

- 依赖校验规则: use_cases 只准 import domain (实体+接口), 禁止 import adapters/infrastructure; 域实体不得出现 SQLAlchemy/Pydantic 注解, 否则拆出独立 ORM 模型并用 repository 的 _to_entity() 映射
- 端口-适配器转换: 数据库等外部设施全部藏在 IRepository 抽象后面, 测试注入 In-Memory 实现, 因此单测无需数据库、Docker 或网络; 控制器只做 解析请求→调用用例→映射响应 三件事
- 校验前移: 值对象 (Email/Money) 在构造时 (__post_init__/constructor) 即校验不变量; 上下文间引用走防腐层 (ACL) 防止模型互相污染; 参考资料为本地 references/ 文件, 无外部模型 API 依赖
